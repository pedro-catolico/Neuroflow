# RISK MITIGATION
## NEUROFLOW

> Este documento complementa o Risk Register de `docs/PROJECT_BRIEF.md`. Ele transforma riscos já identificados ou operacionais em triggers, prevenção, contingência, responsável e escalonamento. Não substitui o sistema de QA de `docs/QUALITY_CONTROL.md` nem cria checkpoints novos.

---

## 1. Objetivo

Cada risco é acompanhado por:

- trigger;
- condição de alerta;
- ação preventiva;
- contingência;
- responsável;
- critério de escalonamento.

As classificações de probabilidade são avaliações operacionais, não dados estatísticos:

| Classificação | Leitura operacional |
|---------------|---------------------|
| **LOW** | Pouco provável no estágio atual, mas com ação de controle definida. |
| **MEDIUM** | Pode ocorrer durante o fluxo normal e exige monitoramento ativo. |
| **HIGH** | Provável sem controle consistente ou com impacto direto em uma fase crítica. |

## 2. Matriz

| ID | Risco | Probabilidade | Impacto | Trigger | Prevenção | Contingência | Escalonamento | Responsável | Status |
|----|-------|---------------|---------|---------|-----------|--------------|---------------|-------------|--------|
| R-001 | Inconsistência visual | HIGH | HIGH | QA visual identifica desvio de linguagem, fluxo, tonalidade ou complexidade entre imagens | Referenciar versões dos prompts e aplicar Style Bible, Art Direction e Variation Rules | Suspender o batch afetado, registrar o desvio e propor revisão de prompt | Propor revisão ao identificar padrão recorrente; parar produção em escala até decisão | Agente + Usuário | Ativo |
| R-002 | Excesso de preto ou tonalidade inadequada | MEDIUM | HIGH | QA aponta áreas pretas excessivas, falta de highlights ou contraste impróprio | Aplicar NEGATIVE_PROMPT e critérios tonais existentes | Marcar a imagem como REVIEW ou REJECTED conforme QA; não corrigir visualmente sem avaliação | Solicitar revisão quando o problema exigir mudança de direção ou prompt base | Agente + Usuário | Ativo |
| R-003 | Artefatos de IA | MEDIUM | HIGH | Distorções, ruído, texto, logos ou elementos estranhos observados na imagem | Usar prompts de autoridade e QA visual | Rejeitar texto/watermark conforme `docs/QUALITY_CONTROL.md`; registrar demais artefatos para refinamento | Parar o fluxo da imagem quando houver critério de rejeição automática | Agente | Ativo |
| R-004 | Falha de printability | MEDIUM | HIGH | Dimensões insuficientes, DPI metadata abaixo do mínimo configurado ou QA visual ruim para impressão | Executar validação técnica sem confundir metadata DPI com avaliação de tamanho de impressão | Manter a imagem fora de `art/final/` e revisar o arquivo de origem ou a decisão de layout | Propor revisão para alertas; parar PDF se requisitos confirmados falharem | Agente + Usuário | Ativo |
| R-005 | Especificações KDP desatualizadas | MEDIUM | HIGH | Início de layout/PDF sem confirmação oficial recente | Consultar a fonte oficial indicada em `docs/KDP_SPECIFICATIONS.md` antes do PDF final | Bloquear a preparação KDP até confirmação documentada | Parar pipeline de PDF/KDP e solicitar decisão ou verificação do usuário | Usuário / Agente na fase KDP | Ativo |
| R-006 | Mudança editorial tardia | MEDIUM | HIGH | Alteração de trim, orientação, versos, paginação ou ferramenta após início da fase dependente | Manter `docs/CRITICAL_DECISIONS.md` atualizado e respeitar os gates existentes | Avaliar impacto, registrar retrabalho e replanejar apenas após decisão explícita | Solicitar decisão do usuário antes de alterar arte, layout ou automação dependente | Usuário | Ativo |
| R-007 | Falha de rastreabilidade | MEDIUM | MEDIUM | Imagem, prompt, QA, versão ou motivo de seleção sem referência | Usar fichas em `art/prompts/illustration-prompts/` e manter referências no Master Plan | Pausar a movimentação do item entre estados até completar o registro | Corrigir autonomamente apenas metadados inequívocos; propor revisão se houver ambiguidade | Agente | Ativo |
| R-008 | Crescimento descontrolado de retrabalho | MEDIUM | MEDIUM | Iterações repetidas sem melhoria ou aproximação do limite de cinco iterações da pipeline | Trabalhar em batches pequenos e registrar causa de rejeição | Interromper a iteração da imagem e consolidar opções de revisão | Propor revisão antes de exceder o limite existente ou mudar prompt base | Agente + Usuário | Ativo |
| R-009 | Problemas de automação | LOW | MEDIUM | Script falha, lê caminho incorreto, produz relatório inválido ou não é reproduzível | Configuração centralizada, caminhos relativos, testes de sintaxe e execução segura | Preservar entradas, registrar log e corrigir o script sem modificar imagens | Corrigir falha técnica isolada; solicitar decisão se alterar política técnica ou fluxo | Agente | Ativo |
| R-010 | Inconsistência entre documentação e estado real | MEDIUM | HIGH | Documento afirma estado incompatível com arquivos, testes ou artefatos existentes | Auditorias de referências e atualização conservadora do status | Registrar a divergência sem reescrever silenciosamente a autoridade | Solicitar revisão do usuário quando a divergência afetar decisão artística, checkpoint ou status aprovado | Agente + Usuário | Ativo |

## 3. Escalonamento

### Corrigir sozinho

O agente pode corrigir referências quebradas, erros mecânicos de rastreabilidade e falhas isoladas de script quando a correção não altera conteúdo artístico, decisão editorial, checkpoint ou autoridade existente. A correção deve ficar registrada no changelog quando for estrutural.

### Propor revisão

O agente deve propor revisão quando um risco exigir interpretação estética, ajuste de prompt de autoridade, replanejamento de batch, conflito documental ou mudança que afete mais de um artefato dependente.

### Parar o pipeline

O agente deve interromper a fase afetada quando houver falha de integridade técnica, critério de rejeição automática de QA, ausência de confirmação KDP necessária para PDF/KDP, ou risco que comprometa uma decisão já aprovada. Parar não equivale a avançar ou a decidir: o motivo deve ser registrado.

### Solicitar decisão do usuário

O usuário deve decidir trim size, orientação, paginação, verso, organização editorial, ferramenta de diagramação, aprovações de checkpoint e qualquer alteração artística ou conceitual. Também deve ser consultado quando uma inconsistência histórica afetar o sentido do projeto.

## 4. Relação com QA

`docs/QUALITY_CONTROL.md` continua sendo a única autoridade do QA visual. Esta matriz apenas define como responder aos riscos que o QA, a validação técnica ou a documentação revelarem. Ela não adiciona critérios, pontuações, aprovações ou fichas paralelas de QA.

## 5. Relação com Checkpoints Existentes

| Checkpoint existente | Riscos mais diretamente relacionados |
|----------------------|--------------------------------------|
| Checkpoint 01 — Direção Artística | R-001, R-002, R-006, R-007, R-010 |
| Checkpoint 02 — Style Test | R-001, R-002, R-003, R-004, R-008, R-010 |
| Checkpoint 03 — Primeira Geração | R-001, R-003, R-007, R-008 |
| Checkpoint 04 — Curadoria Final | R-001, R-002, R-003, R-004, R-007 |
| Checkpoint 05 — Layout | R-004, R-005, R-006, R-009 |
| Checkpoint 06 — PDF Final | R-004, R-005, R-009 |
| Checkpoint 07 — KDP | R-005, R-006, R-009 |

Os checkpoints acima são os definidos em `docs/PRODUCTION_PIPELINE.md`; esta relação não cria checkpoints adicionais.

---

*Criado em: 2026-09-05*  
*Versão: 0.1.1 — Foundation Refinement*
