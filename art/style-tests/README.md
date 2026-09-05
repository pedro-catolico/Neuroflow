# STYLE TESTS — ÁREA DE TRABALHO
## NEUROFLOW

---

## Propósito

Esta pasta contém as imagens geradas durante a fase **STYLE TEST** — a primeira produção artística do projeto.

O objetivo do Style Test é:
1. Validar a linguagem visual antes da produção em escala
2. Testar o MASTER_PROMPT e STYLE_PROMPT na prática
3. Avaliar a qualidade do grayscale gerado
4. Identificar ajustes necessários nos prompts
5. Obter aprovação explícita antes de produzir as 45 ilustrações

---

## Processo

```
MASTER_PROMPT + STYLE_PROMPT + Conceito específico
↓
GERAÇÃO (generate_image)
↓
SALVAMENTO aqui (art/style-tests/)
↓
AVALIAÇÃO (Quality Control — docs/QUALITY_CONTROL.md)
↓
FEEDBACK → Refinamento de prompts
↓
NOVA GERAÇÃO (se necessário)
↓
APROVAÇÃO → Avançar para produção
```

---

## Organização

```
art/style-tests/
├── README.md (este arquivo)
├── ST-001/
│   ├── ST-001-v1.png
│   ├── ST-001-v2.png
│   └── ST-001-qa.md
├── ST-002/
│   └── ...
└── style-test-summary.md
```

---

## Critérios de Aprovação do Style Test

O Style Test é aprovado quando:

- [ ] Pelo menos 5 imagens geradas em estilos variados
- [ ] Pelo menos 3 níveis de complexidade testados (Level 1, 3, 5)
- [ ] Avaliação QA Visual aplicada em todas as imagens
- [ ] Média de QA ≥ 3.5 nas imagens aprovadas
- [ ] Nenhuma imagem com texto ou watermark
- [ ] Grayscale adequado para impressão (validado visualmente)
- [ ] Usuário revisou e aprovou a direção visual
- [ ] Prompts refinados incorporados no MASTER_PROMPT

---

*Área criada em: 2026-09-03*
