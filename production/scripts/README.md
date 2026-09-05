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
| `validate_images.py` | Validar resolução, formato e dimensões | Planejado |
| `convert_grayscale.py` | Converter imagens para grayscale com controle tonal | Planejado |
| `generate_previews.py` | Gerar thumbnails para preview | Planejado |
| `compose_pdf.py` | Compor PDF interior | Planejado |
| `qa_report.py` | Gerar relatório consolidado de QA | Planejado |

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

Se scripts Python forem necessários:
1. Verificar se `uv` está disponível: `uv --version`
2. Se não: `pip install uv` ou verificar instalação
3. Criar `pyproject.toml` com dependências
4. Usar `uv run` para execução

Dependências prováveis:
- `Pillow` — manipulação de imagens
- `fpdf2` ou `reportlab` — geração de PDF
- `rich` — output formatado no terminal

---

*Criado em: 2026-09-03*
