# CHANGELOG
## NEUROFLOW — Registro de Decisões e Mudanças Estruturais

---

## [0.1.0] — 2026-09-03 — Foundation

### Estrutura
- Criação da estrutura completa do projeto (Foundation Phase)
- Organização de pastas: `docs/`, `art/`, `content/`, `production/`, `output/`, `qa/`, `archive/`
- Criação do `README.md` e `PROJECT_STATUS.md`

### Documentação
- Criação do `docs/ENVIRONMENT_DISCOVERY.md` — Relatório de descoberta do ambiente Antigravity
- Criação do `docs/PROJECT_BRIEF.md` — Brief oficial do produto
- Criação do `docs/STYLE_BIBLE.md` — Autoridade estética do projeto
- Criação do `docs/ART_DIRECTION.md` — Direção artística operacional
- Criação do `docs/PRODUCTION_PIPELINE.md` — Pipeline de produção com checkpoints
- Criação do `docs/QUALITY_CONTROL.md` — Sistema de QA visual (13 critérios)
- Criação do `docs/KDP_SPECIFICATIONS.md` — Especificações Amazon KDP
- Criação do `docs/WORKFLOW_SKILL_ANALYSIS.md` — Análise de criação de skill própria
- Criação do `docs/CHANGELOG.md` — Este arquivo

### Sistema de Prompts
- Criação do `art/prompts/MASTER_PROMPT.md`
- Criação do `art/prompts/STYLE_PROMPT.md`
- Criação do `art/prompts/NEGATIVE_PROMPT.md`
- Criação do `art/prompts/VARIATION_RULES.md`

### Planejamento de Ilustrações
- Criação do `content/illustration-list/illustrations-master.md` — 45 conceitos planejados

### Referências
- Criação do `art/references/README.md` — Política de referências e propriedade intelectual

### Skills Analisadas
- `baoyu-design` — Relevante para direção visual e protótipos
- `release-skills` — Reservada para versionamento futuro
- `code-review-ai-ai-review` — Reservada para revisão de scripts Python
- `antigravity-guide` — Relevante para compreensão do ambiente
- `agy-customizations` — Relevante para configuração futura
- `workflow-skill-creator` — Reservada para pós-Style Test
- Skills biomédicas (30+) — Descartadas como irrelevantes

### Decisões Tomadas
- Conceito visual: Fluxo Neurográfico
- Técnica: Grayscale artístico
- Plataforma: Amazon KDP
- Convenção de nomes: NF-XXX
- Quantidade: 40–50 ilustrações
- Ferramenta de geração: Gemini/Antigravity (generate_image)
- Checkpoints: 7 definidos

### Decisões Pendentes
- Trim size do livro (PENDENTE)
- Número de páginas (PENDENTE)
- Orientação das páginas (PENDENTE)
- Autor/pseudônimo (PENDENTE)
- Preço de venda (PENDENTE)

---

## [0.1.1] — 2026-09-05 — Foundation Refinement

### Estrutura & Rastreabilidade
- Implementação do documento `docs/CRITICAL_DECISIONS.md` para centralização de decisões editoriais e técnicas com status, dependências e gate pré-Style Test.
- Implementação do sistema de Prompt Tracking em `art/prompts/illustration-prompts/` com `README.md`, `_TEMPLATE.md` e 45 fichas individuais (`NF-001.md` a `NF-045.md`) estruturadas com status `PLANNED / NOT TESTED`.

### Mitigação de Riscos & Automação
- Implementação do documento `docs/RISK_MITIGATION.md` complementando o Risk Register de `docs/PROJECT_BRIEF.md` com triggers, prevenção, contingência, escalonamento e relação com os 7 checkpoints.
- Implementação de `production/scripts/config.yaml` e `production/scripts/validate_images.py` para validação técnica inicial de imagens em `art/selected/` sem alterar os arquivos.
- Atualização do `production/scripts/README.md` documentando a configuração e o validador técnico.

---

## [0.1.2] — 2026-09-05 — Contemplative Figurative Identity Alignment

### Identidade Conceitual
- Registro formal da síntese conceitual de identidade visual: **NEUROFLOW — Contemplativo Figurativo** (Figura reconhecível + Estrutura neurográfica orgânica contínua + Composição contemplativa + Complexidade adulta).
- Atualização cirúrgica em `docs/STYLE_BIBLE.md` incorporando a seção 0 (Conceito Síntese) e ajustando a classificação de representação figurativa.
- Adição de nota de alinhamento em `docs/ART_DIRECTION.md` e `docs/PROJECT_BRIEF.md`.
- Atualização de `art/prompts/NEGATIVE_PROMPT.md` e `art/prompts/VARIATION_RULES.md` eliminando proibições genéricas que conflitavam com representação figurativa contemplativa.
- Registro da decisão conceitual aprovada em `docs/CRITICAL_DECISIONS.md` (sob `DECIDIDO`) e `PROJECT_STATUS.md` sem alterar as pendências editoriais/técnicas.

---

## [0.2.0] — 2026-09-05 — Prompt System: Contemplative Figurative Alignment

### Sistema de Prompts (Alinhamento Operacional)
- Elevação do Prompt System para a versão **0.2.0 — Contemplative Figurative Alignment**.
- Atualização do `art/prompts/MASTER_PROMPT.md` integrando o "Contemplativo Figurativo" (figuras/cenas reconhecíveis + fluxo neurográfico orgânico + espaço contemplativo) como constante estrutural.
- Atualização do `art/prompts/STYLE_PROMPT.md` definindo a hierarquia visual de execução (figura $\rightarrow$ linhas $\rightarrow$ espaço $\rightarrow$ contemplação).
- Reestruturação do `art/prompts/NEGATIVE_PROMPT.md` eliminando proibições genéricas herdadas da abstração pura e focando em restrições de estética infantil, cartoon, fotorrealismo e poluição visual.
- Atualização do `art/prompts/VARIATION_RULES.md` definindo a regra de variação ("variar o conteúdo, preservar a linguagem").
- Preservação integral dos Style Tests históricos (`ST-001`, `ST-002`, `ST-003`), da lista mestre (`illustrations-master.md`) e das decisões editoriais pendentes em `docs/CRITICAL_DECISIONS.md`.

---

## [0.2.0] — 2026-09-06 — Illustration Master Plan: Contemplative Figurative Alignment

### Planejamento de Ilustrações (Revisão Estratégica)
- Elevação do Illustration Master Plan para a versão **v0.2.0 — Contemplative Figurative Collection** em `content/illustration-list/illustrations-master.md`.
- Aplicação estrita da regra de ouro editorial: *"Variar o conteúdo, preservar a linguagem"*. A identidade Neuroflow reside na linguagem visual e não na repetição do sujeito.
- Adição dos 5 novos campos obrigatórios em todos os 45 conceitos: `Motivo Principal`, `Modo Figurativo`, `Função Contemplativa`, `Integração Neurográfica` e `Densidade Figurativa`.
- Detalhamento conceitual completo das ilustrações `NF-031` a `NF-045` (anteriormente agrupadas), eliminando placeholders vagos.
- Criação da **Collection Diversity Matrix** consolidando o mapeamento estrutural e a distribuição de motivos (Human Female 15.5%, Human Male 8.9%, Human Group 6.7%, Animal 11.1%, Flora 11.1%, Tree 11.1%, Landscape 11.1%, Architecture 8.9%, Object 8.9%, Symbolic Composition 8.9%, Water 2.2%).
- Sincronização automática das 45 fichas individuais em `art/prompts/illustration-prompts/NF-001.md` a `NF-045.md` mantendo status `PLANNED / NOT TESTED` e prompt específico pendente.
- Preservação integral dos Style Tests históricos (`ST-001` a `ST-004`), documentos de autoridade e decisões editoriais pendentes.

---

*Formato: [versão] — data — fase*

