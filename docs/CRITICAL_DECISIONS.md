# CRITICAL DECISIONS
## NEUROFLOW

> Registro operacional das decisões editoriais e técnicas que precisam de definição antes de uma fase irreversível. Este documento centraliza o acompanhamento; não substitui `docs/PROJECT_BRIEF.md`, `docs/KDP_SPECIFICATIONS.md`, `docs/PRODUCTION_PIPELINE.md` ou a aprovação do usuário.

---

## 1. Status Permitidos

| Status | Significado |
|--------|-------------|
| **DECIDIDO** | Aprovado explicitamente pelo responsável e registrado em uma autoridade do projeto. |
| **PROPOSTO** | Alternativa ou recomendação para avaliação; não é uma decisão aprovada. |
| **PENDENTE** | Requer decisão do responsável antes do prazo indicado. |
| **BLOQUEADO** | Depende de uma decisão anterior ou de confirmação externa. |
| **NÃO APLICÁVEL** | Não se aplica ao escopo ou à fase atual; deve indicar a justificativa. |

## 2. Registro de Decisões Críticas

| Decisão | Status | Opções | Recomendação | Impacto | Deadline | Responsável |
|---------|--------|--------|--------------|---------|----------|-------------|
| Trim size | PENDENTE | 8.5 x 11, 8 x 10, 8.5 x 8.5, ou outro formato KDP confirmado | Avaliar os formatos documentados em `docs/KDP_SPECIFICATIONS.md`; 8.5 x 11 é apenas uma proposta de mercado, não uma decisão | Proporção das imagens, área útil, bleed, margens, layout e capa | Antes do Style Test, conforme `PROJECT_STATUS.md` | Usuário |
| Orientação | PENDENTE | Retrato, paisagem ou quadrado, compatível com o trim size | Resolver junto com o trim size para evitar gerar na proporção errada | Composição, proporção e uso de página | Antes do Style Test, conforme `PROJECT_STATUS.md` | Usuário |
| Número total de páginas | PENDENTE | Cenários a calcular após definir elementos editoriais e tratamento do verso | Não há número final aprovado. Um cenário deve considerar ilustrações, páginas editoriais e possíveis versos em branco; múltiplos de 4 são apenas uma consideração de produção, não um requisito KDP assumido | Lombada, custos, margens internas, capa e PDF | Antes do Layout | Usuário |
| Tratamento do verso das ilustrações | PENDENTE | Verso em branco, padrão leve, conteúdo editorial ou outra solução aprovada | Comparar a experiência de colorir, sangramento de marcadores e impacto na paginação; nenhuma opção está aprovada | Paginação, experiência de uso e número total de páginas | Antes do Layout | Usuário |
| Organização temática das ilustrações | PENDENTE | Grupos temáticos, progressão de complexidade, fluxo visual ou ordem editorial híbrida | Usar os grupos de planejamento atuais apenas como referência; não há organização editorial final aprovada | Ordem do livro, páginas editoriais e experiência do leitor | Antes do Layout | Usuário |
| Ferramenta de diagramação | PENDENTE | Python + ReportLab, Python + fpdf2, Adobe InDesign, Affinity Publisher ou outra solução avaliada | Escolher depois do Style Test, conforme `docs/PRODUCTION_PIPELINE.md`, a partir da necessidade real de automação e controle | Reprodutibilidade, custos, template e geração do PDF | Antes do Layout | Usuário |
| Bleed e margens | BLOQUEADO | Conforme formato escolhido e requisitos KDP oficiais confirmados | Confirmar em fonte oficial somente após trim size, orientação e paginação estarem definidos; não usar valores estimados como decisão final | Área segura, corte, lombada, PDF e conformidade KDP | Antes do Layout e do PDF final | Usuário / Agente na fase KDP |

## 3. Registros por Status

### DECIDIDO

Nenhuma das decisões editoriais listadas acima está decidida neste momento. As decisões já confirmadas de conceito, público, técnica artística e plataforma permanecem em `docs/PROJECT_BRIEF.md`.

### PROPOSTO

- 8.5 x 11 é uma alternativa comum documentada para avaliação, não um formato aprovado.
- Uma contagem total de páginas deve ser calculada por cenário depois das decisões de verso e elementos editoriais; nenhum cenário é final.

### PENDENTE

- Trim size.
- Orientação.
- Número total de páginas.
- Tratamento do verso.
- Organização temática das ilustrações.
- Ferramenta de diagramação.

### BLOQUEADO

- Bleed e margens: dependem do formato, da paginação e da confirmação oficial do KDP.

### NÃO APLICÁVEL

Nenhum registro se enquadra neste status na Foundation atual.

## 4. GATE ANTES DO STYLE TEST

Somente as decisões abaixo precisam estar resolvidas antes de um novo Style Test, pois determinam a proporção da arte a ser testada:

- Trim size.
- Orientação.

Número de páginas, tratamento do verso, organização temática final, ferramenta de diagramação, bleed e margens podem permanecer pendentes até o Layout/KDP, respeitando os checkpoints já definidos em `docs/PRODUCTION_PIPELINE.md`.

## 5. Atualização do Registro

1. O responsável aprova explicitamente uma decisão.
2. Atualizar o status para **DECIDIDO**, registrar a fonte de aprovação e refletir a decisão na autoridade relevante.
3. Não alterar uma autoridade existente apenas por uma recomendação deste documento.
4. Quando uma decisão bloquear outra, manter a dependência explícita em vez de inferir um valor.

---

*Criado em: 2026-09-05*  
*Versão: 0.1.1 — Foundation Refinement*
