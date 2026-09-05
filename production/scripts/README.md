# SCRIPTS DE AUTOMAÇÃO
## NEUROFLOW — production/scripts/

---

## Propósito

Esta pasta contém scripts de automação para a pipeline de produção do Neuroflow.

Cada script deve ser criado somente quando houver **necessidade real e definida**.

---

## Scripts Planejados

| Script | Propósito | Status |
|--------|-----------|--------|
| `validate_images.py` | Validar integridade, formato, extensão, dimensões em pixels, DPI metadata e modo de cor de `art/selected/` | Implementado — Foundation |
| `convert_grayscale.py` | Converter imagens para grayscale com controle tonal | Planejado |
| `generate_previews.py` | Gerar thumbnails para preview | Planejado |
| `compose_pdf.py` | Compor PDF interior | Planejado |
| `qa_report.py` | Gerar relatório consolidado de QA | Planejado |

---

## Configuração e Uso

`config.yaml` centraliza os formatos aceitos, DPI mínimo, verificações técnicas e caminhos relativos. O arquivo usa o subconjunto JSON-compatível de YAML 1.2 para continuar executável no ambiente atual sem adicionar dependências. Se PyYAML estiver disponível no futuro, o script também aceita YAML convencional.

```powershell
python production/scripts/validate_images.py
python production/scripts/validate_images.py --dry-run
```

- Entrada padrão: `art/selected/`
- Relatório técnico: `qa/technical/`
- Log de execução: `production/logs/`
- `--dry-run` valida sem criar relatório ou log.

O validador nunca modifica imagens. Ele registra dimensões em pixels, DPI metadata e avaliação de tamanho de impressão como informações separadas. Ausência de DPI metadata gera alerta, não uma conclusão sobre a adequação física para impressão. Watermarks, texto e julgamentos visuais continuam exclusivamente no QA visual.

---

## Requisitos de Qualidade

Todo script deve:
- Usar **caminhos relativos** (nunca absolutos hardcoded)
- Ter **tratamento de erros** com mensagens claras
- Gerar **logs** de execução
- Ter **configuração centralizada** (sem hardcode de parâmetros)
- Ter **documentação inline** (docstrings)
- Ser **reproduzível** (mesmo input → mesmo output)
- Ter **saída em arquivo** (não stdout para dados)

---

## Estrutura de Script (Template)

```python
#!/usr/bin/env python3
"""
Script: nome_do_script.py
Propósito: [descrição clara]
Entrada: [o que consome]
Saída: [o que produz]
Uso: python nome_do_script.py [argumentos]

Neuroflow — Adult Coloring Book Pipeline
"""

import argparse
import logging
import sys
from pathlib import Path

# Configuração
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s — %(levelname)s — %(message)s'
)
log = logging.getLogger(__name__)

# Caminhos relativos à raiz do projeto
PROJECT_ROOT = Path(__file__).parent.parent.parent
ART_DIR = PROJECT_ROOT / "art"
OUTPUT_DIR = PROJECT_ROOT / "output"

def main():
    parser = argparse.ArgumentParser(description='[Descrição]')
    # ... argumentos
    args = parser.parse_args()
    
    try:
        # ... lógica
        pass
    except Exception as e:
        log.error(f"Erro: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
```

---

## Nota sobre Python e UV

Para a Foundation atual, não foi criado `pyproject.toml` nem instalada dependência adicional. O ambiente disponível já possui:

- `Pillow` — leitura e validação técnica de imagens

Dependências prováveis para etapas futuras:
- `fpdf2` ou `reportlab` — geração de PDF
- `rich` — output formatado no terminal

Antes de adicionar qualquer dependência futura, verificar o ambiente e a necessidade concreta do estágio correspondente.

---

*Criado em: 2026-09-03*
