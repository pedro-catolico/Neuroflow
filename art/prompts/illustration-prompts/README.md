# ILLUSTRATION PROMPTS
## NEUROFLOW — Rastreamento de Prompts por Ilustração

Esta pasta contém a ficha rastreável de cada ilustração `NF-XXX`. As fichas registram o conceito aprovado no Illustration Master Plan, as versões de prompt usadas, o histórico de geração, a seleção e a referência de QA. Elas não substituem as autoridades do sistema de prompts.

## Relação com as Autoridades

| Fonte | Papel na ficha individual |
|-------|---------------------------|
| `art/prompts/MASTER_PROMPT.md` | Fonte central da identidade visual; a ficha registra versão e referência, sem copiar o texto integral. |
| `art/prompts/STYLE_PROMPT.md` | Fonte central das especificações técnicas de estilo; a ficha registra versão e referência. |
| `art/prompts/NEGATIVE_PROMPT.md` | Fonte central dos elementos proibidos; a ficha registra versão e referência. |
| `art/prompts/VARIATION_RULES.md` | Regras aplicadas à composição, fluxo, densidade e sequência. |
| `content/illustration-list/illustrations-master.md` | Autoridade do conceito, planejamento e status da ilustração. A ficha não altera o conceito. |

## Regra de Versionamento

- `VERSION` identifica a versão da ficha, não a versão dos prompts centrais.
- `MASTER_PROMPT_VERSION`, `STYLE_PROMPT_VERSION`, `NEGATIVE_PROMPT_VERSION` e `VARIATION_RULES_VERSION` registram exatamente as versões usadas em uma geração.
- Cada nova geração recebe uma linha em `GENERATION HISTORY`; não substituir o histórico anterior.
- Mudanças no conteúdo específico da ficha incrementam sua versão e devem manter referências às versões centrais correspondentes.

## Regra de Rastreabilidade

Antes de uma imagem avançar de estado, a ficha deve permitir identificar seu ID, conceito de origem, versões de prompt, modelo, contagem de gerações, arquivo selecionado e referência de QA. Uma ausência de registro deve ser tratada conforme R-007 em `docs/RISK_MITIGATION.md`.

## Regra de Atualização

1. Criar ou completar a ficha a partir do conceito existente no Master Plan.
2. Construir o `SPECIFIC PROMPT` somente depois da revisão apropriada; não inventar detalhes ausentes do plano.
3. Após gerar, registrar data, modelo, resultado e versão na tabela de histórico.
4. Após curadoria ou QA, registrar somente a referência do artefato de QA já existente.
5. Atualizar o Master Plan apenas quando sua própria informação de status ou referência precisar refletir um fato confirmado.

## Regra de Não Duplicação

Não copiar integralmente `MASTER_PROMPT.md`, `STYLE_PROMPT.md` ou `NEGATIVE_PROMPT.md` para cada ficha. As fichas contêm referências e versões; a fonte de verdade continua nos documentos centrais. O `SPECIFIC PROMPT` contém apenas instruções exclusivas daquela ilustração.

## Estado Inicial

As fichas `NF-001` a `NF-045` foram criadas como registros de planejamento. `PLANNED / NOT TESTED` significa que não houve geração, seleção, QA ou aprovação associada à ficha.
