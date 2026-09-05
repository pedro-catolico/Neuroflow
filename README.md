# NEUROFLOW
## Adult Coloring Book — Pipeline Editorial

> **NEUROFLOW** é um livro adulto de colorir sofisticado baseado no conceito de **Fluxo Neurográfico**.
> Linhas fluidas, formas orgânicas, composição meditativa — uma experiência de coloração contemplativa para adultos.

---

## O PROJETO

NEUROFLOW não é apenas um livro de colorir. É o primeiro produto de uma **pipeline editorial automatizada** para a criação de livros adultos de colorir destinados à publicação comercial no Amazon KDP.

**Conceito:** Fluxo Neurográfico  
**Público:** Adultos  
**Estilo:** Grayscale artístico — linhas fluidas, orgânicas, meditativas  
**Plataforma:** Amazon KDP — Print on Demand  
**Ilustrações planejadas:** 45

---

## ESTRUTURA DO PROJETO

```
Neuroflow/
│
├── docs/                          ← Toda a documentação
│   ├── PROJECT_BRIEF.md           ← Brief do produto
│   ├── ENVIRONMENT_DISCOVERY.md   ← Relatório do ambiente
│   ├── ART_DIRECTION.md           ← Direção artística
│   ├── STYLE_BIBLE.md             ← Autoridade estética (referência principal)
│   ├── PRODUCTION_PIPELINE.md     ← Pipeline com checkpoints
│   ├── QUALITY_CONTROL.md         ← Sistema de QA (13 critérios)
│   ├── KDP_SPECIFICATIONS.md      ← Especificações Amazon KDP
│   ├── WORKFLOW_SKILL_ANALYSIS.md ← Análise de skill própria
│   └── CHANGELOG.md               ← Registro de mudanças
│
├── art/                           ← Todo o trabalho artístico
│   ├── references/                ← Referências e política de IP
│   ├── style-tests/               ← Fase de testes de estilo
│   ├── prompts/                   ← Sistema de prompts
│   │   ├── MASTER_PROMPT.md       ← Prompt base (USAR SEMPRE)
│   │   ├── STYLE_PROMPT.md        ← Detalhes técnicos de estilo
│   │   ├── NEGATIVE_PROMPT.md     ← O que evitar
│   │   ├── VARIATION_RULES.md     ← Regras de variação
│   │   └── illustration-prompts/  ← Prompts específicos por ilustração
│   ├── generated/                 ← Saída bruta da geração
│   ├── selected/                  ← Aprovadas na curadoria inicial
│   ├── rejected/                  ← Rejeitadas (mantidas para referência)
│   ├── grayscale/                 ← Após processamento tonal
│   ├── qa/                        ← Em avaliação de QA
│   └── final/                     ← Aprovadas em todos os critérios
│
├── content/                       ← Conteúdo editorial
│   ├── concepts/                  ← Exploração de conceitos
│   ├── illustration-list/         ← Master Plan das ilustrações
│   │   └── illustrations-master.md ← 45 conceitos planejados
│   ├── metadata/                  ← Metadados do produto
│   └── cover/                     ← Conceitos de capa
│
├── production/                    ← Infraestrutura de produção
│   ├── scripts/                   ← Scripts de automação (Python)
│   ├── templates/                 ← Templates de diagramação
│   ├── layouts/                   ← Layouts de página
│   ├── assets/                    ← Assets de produção
│   └── builds/                    ← Builds intermediários
│
├── output/                        ← Arquivos exportados (somente)
│   ├── previews/                  ← Thumbnails e previews
│   ├── interior/                  ← PDF interior final
│   ├── cover/                     ← PDF de capa final
│   └── release/                   ← Pacote KDP completo
│
├── qa/                            ← Arquivos de QA
│   ├── visual/                    ← Fichas de QA visual
│   ├── technical/                 ← Relatórios técnicos
│   └── reports/                   ← Relatórios consolidados
│
└── archive/                       ← Arquivos históricos
```

---

## PIPELINE DE PRODUÇÃO

```
IDEAÇÃO → DIREÇÃO ARTÍSTICA → PLANEJAMENTO → PROMPT ENGINEERING
→ GERAÇÃO DE IMAGENS (iterativo) → CURADORIA → TRATAMENTO GRAYSCALE
→ PADRONIZAÇÃO → QA VISUAL → DIAGRAMAÇÃO → GERAÇÃO DO PDF
→ QA TÉCNICO → PREPARAÇÃO KDP
```

### 7 Checkpoints Obrigatórios

| # | Checkpoint | Status |
|---|-----------|--------|
| 01 | Direção Artística | ✅ Em progresso |
| 02 | Style Test | ⬜ Pendente |
| 03 | Primeira Geração | ⬜ Pendente |
| 04 | Curadoria Final | ⬜ Pendente |
| 05 | Layout | ⬜ Pendente |
| 06 | PDF Final | ⬜ Pendente |
| 07 | KDP | ⬜ Pendente |

---

## PROMPTS

O sistema de prompts está em `art/prompts/`:

1. **MASTER_PROMPT.md** — Prompt base. Incluir em TODOS os prompts de geração.
2. **STYLE_PROMPT.md** — Detalhes técnicos de estilo.
3. **NEGATIVE_PROMPT.md** — O que evitar.
4. **VARIATION_RULES.md** — Como criar variações mantendo coerência.
5. `illustration-prompts/` — Prompts específicos por ilustração (a criar).

---

## IMAGENS

Fluxo de imagens:

```
art/generated/ → (curadoria) → art/selected/ → (grayscale) → art/grayscale/
→ (QA visual) → art/qa/ → (aprovação) → art/final/ → (diagramação) → output/interior/
```

Imagens rejeitadas: `art/rejected/` (mantidas para referência, nunca apagadas)

**Convenção de nomes:** `NF-001.png`, `NF-002.png`, ..., `NF-045.png`

---

## SKILLS RELEVANTES

| Skill | Uso no Projeto |
|-------|---------------|
| **baoyu-design** | Direção visual, protótipos HTML, documentos de referência |
| **release-skills** | Versionamento (fase futura) |
| **code-review-ai-ai-review** | Revisão de scripts Python de automação |
| **workflow-skill-creator** | Criação de skill NEUROFLOW PRODUCTION (pós-produção) |

---

## QA VISUAL

Sistema completo em `docs/QUALITY_CONTROL.md` — 13 critérios, escala 1–5.

Critérios de decisão:
- **APPROVED:** Média ≥ 3.5, sem texto, sem watermark
- **REVIEW:** Média 2.5–3.4
- **REJECTED:** Texto ou watermark presentes / Média < 2.5

---

## PRÓXIMA ETAPA

**CHECKPOINT 01 — Direção Artística**

1. Revisar e aprovar `docs/STYLE_BIBLE.md`
2. Revisar e aprovar `docs/ART_DIRECTION.md`
3. Revisar e aprovar `content/illustration-list/illustrations-master.md`
4. Validar `art/prompts/MASTER_PROMPT.md`
5. → Avançar para STYLE TEST

---

## DOCUMENTAÇÃO

| Documento | Propósito |
|-----------|-----------|
| [PROJECT_BRIEF.md](docs/PROJECT_BRIEF.md) | Identidade e objetivos do produto |
| [ENVIRONMENT_DISCOVERY.md](docs/ENVIRONMENT_DISCOVERY.md) | Ambiente e skills disponíveis |
| [ART_DIRECTION.md](docs/ART_DIRECTION.md) | Regras de direção artística |
| [STYLE_BIBLE.md](docs/STYLE_BIBLE.md) | **Autoridade estética** (referência principal) |
| [PRODUCTION_PIPELINE.md](docs/PRODUCTION_PIPELINE.md) | Pipeline e checkpoints |
| [QUALITY_CONTROL.md](docs/QUALITY_CONTROL.md) | Sistema de QA |
| [KDP_SPECIFICATIONS.md](docs/KDP_SPECIFICATIONS.md) | Especificações Amazon KDP |
| [WORKFLOW_SKILL_ANALYSIS.md](docs/WORKFLOW_SKILL_ANALYSIS.md) | Análise de skill própria |
| [CHANGELOG.md](docs/CHANGELOG.md) | Histórico de decisões |

---

*Versão: 0.1.0 — Foundation Phase — 2026-09-03*
