#!/usr/bin/env python3
"""
Validate technical properties of images selected for the Neuroflow pipeline.

Input: art/selected/ by default, configured in config.yaml.
Output: JSON technical report in qa/technical/ and an execution log in production/logs/.
Usage: python production/scripts/validate_images.py [--dry-run] [--input-dir PATH]

The validator is read-only for image files. It distinguishes pixel dimensions,
DPI metadata, and print-size assessment; missing DPI metadata is a warning, not
a claim that the image is unsuitable for print.
"""

from __future__ import annotations

import argparse
import json
import logging
import math
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

try:
    from PIL import Image, ImageFile, UnidentifiedImageError
except ImportError as error:  # pragma: no cover - depends on local environment
    raise SystemExit(
        "Pillow is required to validate images. Install the project dependency before running this script."
    ) from error


EXIT_VALID = 0
EXIT_VALIDATION_FAILED = 1
EXIT_CONFIGURATION_ERROR = 2
EXIT_UNEXPECTED_ERROR = 3
IGNORED_DOCUMENT_EXTENSIONS = {".md", ".txt", ".gitkeep"}
FORMAT_EXTENSIONS = {
    "PNG": {".png"},
    "JPEG": {".jpg", ".jpeg"},
    "TIFF": {".tif", ".tiff"},
}


class ConfigurationError(ValueError):
    """Raised when the validation configuration cannot be used safely."""


def find_project_root(script_path: Path) -> Path:
    """Find the repository root from the script location without hardcoding it."""
    for candidate in (script_path.parent, *script_path.parents):
        if (candidate / "PROJECT_STATUS.md").is_file() and (candidate / "art").is_dir():
            return candidate
    raise ConfigurationError("Project root could not be located from validate_images.py.")


def load_yaml_config(config_path: Path) -> dict[str, Any]:
    """Load YAML with PyYAML when present, otherwise load JSON-compatible YAML."""
    try:
        import yaml  # type: ignore[import-not-found]
    except ModuleNotFoundError:
        try:
            loaded = json.loads(config_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            raise ConfigurationError(
                "PyYAML is unavailable. config.yaml must use the JSON-compatible YAML subset "
                "or PyYAML must be provided by the environment."
            ) from error
    else:
        try:
            loaded = yaml.safe_load(config_path.read_text(encoding="utf-8"))
        except yaml.YAMLError as error:
            raise ConfigurationError(f"Invalid YAML configuration: {error}") from error

    if not isinstance(loaded, dict):
        raise ConfigurationError("config.yaml must contain a top-level mapping.")
    return loaded


def require_mapping(config: dict[str, Any], key: str) -> dict[str, Any]:
    value = config.get(key)
    if not isinstance(value, dict):
        raise ConfigurationError(f"config.yaml field '{key}' must be a mapping.")
    return value


def require_string_list(config: dict[str, Any], key: str) -> list[str]:
    value = config.get(key)
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise ConfigurationError(f"config.yaml field '{key}' must be a list of strings.")
    return value


def validate_config(config: dict[str, Any]) -> None:
    project = require_mapping(config, "project")
    validation = require_mapping(config, "validation")
    paths = require_mapping(config, "paths")
    reports = require_mapping(config, "reports")

    if not isinstance(project.get("name"), str) or not project["name"].strip():
        raise ConfigurationError("config.yaml field 'project.name' must be a non-empty string.")
    minimum_dpi = validation.get("minimum_dpi")
    if not isinstance(minimum_dpi, (int, float)) or minimum_dpi <= 0:
        raise ConfigurationError("config.yaml field 'validation.minimum_dpi' must be positive.")
    require_string_list(validation, "allowed_formats")
    extensions = require_string_list(validation, "allowed_extensions")
    if any(not extension.startswith(".") for extension in extensions):
        raise ConfigurationError("Each validation.allowed_extensions value must begin with '.'.")
    require_string_list(validation, "allowed_color_modes")
    for key in ("check_dimensions", "check_color_mode", "check_dpi"):
        if not isinstance(validation.get(key), bool):
            raise ConfigurationError(f"config.yaml field 'validation.{key}' must be boolean.")
    for key in ("selected", "technical_qa", "logs"):
        if not isinstance(paths.get(key), str) or not paths[key].strip():
            raise ConfigurationError(f"config.yaml field 'paths.{key}' must be a non-empty string.")
    if not isinstance(reports.get("filename_prefix"), str) or not reports["filename_prefix"].strip():
        raise ConfigurationError("config.yaml field 'reports.filename_prefix' must be a non-empty string.")


def resolve_project_path(project_root: Path, relative_path: str, field_name: str) -> Path:
    """Resolve a project-relative path and reject paths outside the repository."""
    candidate = (project_root / relative_path).resolve()
    try:
        candidate.relative_to(project_root)
    except ValueError as error:
        raise ConfigurationError(f"{field_name} must remain inside the project root: {relative_path}") from error
    return candidate


def relative_to_root(path: Path, project_root: Path) -> str:
    return path.resolve().relative_to(project_root).as_posix()


def normalize_dpi(value: Any) -> tuple[float, float] | None:
    """Normalize Pillow DPI metadata only when both dimensions are usable numbers."""
    if not isinstance(value, (tuple, list)) or len(value) < 2:
        return None
    horizontal, vertical = value[0], value[1]
    if not isinstance(horizontal, (int, float)) or not isinstance(vertical, (int, float)):
        return None
    if not math.isfinite(horizontal) or not math.isfinite(vertical) or horizontal <= 0 or vertical <= 0:
        return None
    return (round(float(horizontal), 2), round(float(vertical), 2))


def build_print_size_assessment(
    width: int,
    height: int,
    dpi: tuple[float, float] | None,
    print_config: dict[str, Any],
) -> dict[str, Any]:
    assessment: dict[str, Any] = {
        "status": print_config.get("status", "pending"),
        "trim_size_inches": print_config.get("trim_size_inches"),
        "orientation": print_config.get("orientation"),
        "bleed_inches": print_config.get("bleed_inches"),
        "margins_inches": print_config.get("margins_inches"),
        "note": print_config.get("note"),
    }
    if dpi is None:
        assessment["size_at_embedded_dpi_inches"] = None
        assessment["conclusion"] = (
            "Not assessed: DPI metadata is absent or unusable. Pixel dimensions remain recorded separately."
        )
    else:
        assessment["size_at_embedded_dpi_inches"] = {
            "width": round(width / dpi[0], 3),
            "height": round(height / dpi[1], 3),
        }
        assessment["conclusion"] = (
            "Pending: no trim size, bleed, or margins are configured, so print suitability is not concluded."
        )
    return assessment


def validate_image(
    path: Path,
    project_root: Path,
    validation: dict[str, Any],
    print_config: dict[str, Any],
) -> dict[str, Any]:
    """Inspect one candidate file without mutating it."""
    result: dict[str, Any] = {
        "path": relative_to_root(path, project_root),
        "extension": path.suffix.lower(),
        "errors": [],
        "warnings": [],
        "checks": {},
    }
    errors: list[str] = result["errors"]
    warnings: list[str] = result["warnings"]
    checks: dict[str, Any] = result["checks"]
    allowed_extensions = {item.lower() for item in validation["allowed_extensions"]}
    allowed_formats = {item.upper() for item in validation["allowed_formats"]}

    if result["extension"] not in allowed_extensions:
        errors.append(
            f"Extension '{result['extension'] or '(none)'}' is not allowed by validation.allowed_extensions."
        )
        checks["extension"] = "FAIL"
    else:
        checks["extension"] = "PASS"

    ImageFile.LOAD_TRUNCATED_IMAGES = False
    try:
        with Image.open(path) as probe:
            probe.verify()
        with Image.open(path) as image:
            image.load()
            image_format = (image.format or "UNKNOWN").upper()
            width, height = image.size
            color_mode = image.mode
            dpi = normalize_dpi(image.info.get("dpi"))
    except (UnidentifiedImageError, OSError, ValueError) as error:
        errors.append(f"Image integrity check failed: {error}")
        checks["integrity"] = "FAIL"
        result["result"] = "FAIL"
        return result

    checks["integrity"] = "PASS"
    result["format"] = image_format
    result["pixel_dimensions"] = {"width": width, "height": height}
    result["color_mode"] = color_mode

    if image_format not in allowed_formats:
        errors.append(f"Format '{image_format}' is not allowed by validation.allowed_formats.")
        checks["format"] = "FAIL"
    else:
        checks["format"] = "PASS"

    expected_extensions = FORMAT_EXTENSIONS.get(image_format)
    if expected_extensions and result["extension"] not in expected_extensions:
        errors.append(
            f"Extension '{result['extension']}' does not match detected format '{image_format}'."
        )
        checks["format_extension_match"] = "FAIL"
    else:
        checks["format_extension_match"] = "PASS"

    if validation["check_dimensions"]:
        if width <= 0 or height <= 0:
            errors.append("Image dimensions must be positive pixel values.")
            checks["dimensions"] = "FAIL"
        else:
            checks["dimensions"] = "PASS"

    if validation["check_color_mode"]:
        allowed_modes = set(validation["allowed_color_modes"])
        if color_mode not in allowed_modes:
            errors.append(f"Color mode '{color_mode}' is not allowed by validation.allowed_color_modes.")
            checks["color_mode"] = "FAIL"
        else:
            checks["color_mode"] = "PASS"

    result["dpi_metadata"] = None if dpi is None else {"horizontal": dpi[0], "vertical": dpi[1]}
    if validation["check_dpi"]:
        if dpi is None:
            checks["dpi_metadata"] = "WARN"
            warnings.append(
                "DPI metadata is absent or unusable. This does not determine physical resolution or print suitability."
            )
        elif min(dpi) < float(validation["minimum_dpi"]):
            checks["dpi_metadata"] = "FAIL"
            errors.append(
                f"DPI metadata {dpi[0]} x {dpi[1]} is below the configured minimum of {validation['minimum_dpi']}."
            )
        else:
            checks["dpi_metadata"] = "PASS"

    result["print_size_assessment"] = build_print_size_assessment(width, height, dpi, print_config)
    result["result"] = "FAIL" if errors else ("WARN" if warnings else "PASS")
    return result


def collect_candidates(source_dir: Path) -> tuple[list[Path], list[str]]:
    """Return files to validate while ignoring known directory documentation."""
    candidates: list[Path] = []
    ignored: list[str] = []
    for path in sorted(source_dir.iterdir(), key=lambda item: item.name.lower()):
        if not path.is_file():
            continue
        if path.suffix.lower() in IGNORED_DOCUMENT_EXTENSIONS:
            ignored.append(path.name)
        else:
            candidates.append(path)
    return candidates, ignored


def summarize(results: list[dict[str, Any]]) -> dict[str, int]:
    return {
        "files_scanned": len(results),
        "passed": sum(result["result"] == "PASS" for result in results),
        "warnings": sum(result["result"] == "WARN" for result in results),
        "failed": sum(result["result"] == "FAIL" for result in results),
    }


def configure_logging(log_path: Path | None) -> logging.Logger:
    logger = logging.getLogger("neuroflow.validate_images")
    logger.handlers.clear()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    if log_path is not None:
        file_handler = logging.FileHandler(log_path, encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger


def write_json(path: Path, payload: dict[str, Any]) -> None:
    """Write a report atomically so an interrupted run cannot leave partial JSON."""
    temporary_path = path.with_suffix(f"{path.suffix}.tmp")
    temporary_path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    temporary_path.replace(path)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate selected Neuroflow images without modifying them.")
    parser.add_argument(
        "--config",
        default="production/scripts/config.yaml",
        help="Project-relative configuration path (default: production/scripts/config.yaml).",
    )
    parser.add_argument(
        "--input-dir",
        help="Project-relative input directory. Defaults to paths.selected from config.yaml.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate and print a summary without writing a report or log.",
    )
    return parser


def run(args: argparse.Namespace) -> int:
    project_root = find_project_root(Path(__file__).resolve())
    config_path = resolve_project_path(project_root, args.config, "--config")
    if not config_path.is_file():
        raise ConfigurationError(f"Configuration file not found: {args.config}")
    config = load_yaml_config(config_path)
    validate_config(config)

    validation = require_mapping(config, "validation")
    paths = require_mapping(config, "paths")
    reports = require_mapping(config, "reports")
    print_config = config.get("print_size_assessment")
    if not isinstance(print_config, dict):
        raise ConfigurationError("config.yaml field 'print_size_assessment' must be a mapping.")

    input_setting = args.input_dir if args.input_dir else paths["selected"]
    source_dir = resolve_project_path(project_root, input_setting, "--input-dir or paths.selected")
    if not source_dir.is_dir():
        raise ConfigurationError(f"Input directory not found: {relative_to_root(source_dir, project_root)}")

    timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    technical_qa_dir = resolve_project_path(project_root, paths["technical_qa"], "paths.technical_qa")
    logs_dir = resolve_project_path(project_root, paths["logs"], "paths.logs")
    report_path: Path | None = None
    log_path: Path | None = None
    if not args.dry_run:
        technical_qa_dir.mkdir(parents=True, exist_ok=True)
        logs_dir.mkdir(parents=True, exist_ok=True)
        report_path = technical_qa_dir / f"{reports['filename_prefix']}-{timestamp}.json"
        log_path = logs_dir / f"{reports['filename_prefix']}-{timestamp}.log"
    logger = configure_logging(log_path)
    logger.info("Validating images in %s", relative_to_root(source_dir, project_root))

    candidates, ignored = collect_candidates(source_dir)
    results = [validate_image(path, project_root, validation, print_config) for path in candidates]
    summary = summarize(results)
    overall_result = "FAIL" if summary["failed"] else ("NO_IMAGES" if not results else "PASS_WITH_WARNINGS" if summary["warnings"] else "PASS")
    report = {
        "report_type": "technical_image_validation",
        "generated_at_utc": datetime.now(UTC).isoformat(),
        "project": config["project"]["name"],
        "config": relative_to_root(config_path, project_root),
        "source_directory": relative_to_root(source_dir, project_root),
        "overall_result": overall_result,
        "summary": summary,
        "ignored_documentation_files": ignored,
        "files": results,
        "limitations": [
            "This validator does not modify images.",
            "DPI metadata and pixel dimensions are recorded separately.",
            "Print-size suitability remains pending until trim size, orientation, bleed, and margins are decided.",
            "Watermarks, text, aesthetics, and other semantic visual issues belong to visual QA.",
        ],
    }
    if report_path is not None:
        write_json(report_path, report)
        logger.info("Technical report written to %s", relative_to_root(report_path, project_root))
    else:
        logger.info("Dry run completed; no report or log was written.")

    print(
        "Validation result: "
        f"{overall_result} | scanned={summary['files_scanned']} "
        f"passed={summary['passed']} warnings={summary['warnings']} failed={summary['failed']}"
    )
    if not results:
        print("No candidate image files were found. This is not a validation failure.")
    return EXIT_VALIDATION_FAILED if summary["failed"] else EXIT_VALID


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return run(args)
    except ConfigurationError as error:
        print(f"Configuration error: {error}", file=sys.stderr)
        return EXIT_CONFIGURATION_ERROR
    except Exception as error:  # pragma: no cover - defensive command-line boundary
        print(f"Unexpected validation error: {error}", file=sys.stderr)
        return EXIT_UNEXPECTED_ERROR


if __name__ == "__main__":
    raise SystemExit(main())
