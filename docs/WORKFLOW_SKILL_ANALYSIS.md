# WORKFLOW SKILL ANALYSIS
## NEUROFLOW — Análise para Criação de Skill Própria

---

## 1. PERGUNTA CENTRAL

**Precisamos realmente de uma skill própria para o Neuroflow?**

**Resposta:** Não neste momento. A criação prematura de uma skill seria contraproducente.

Esta análise explica o raciocínio.

---

## 2. O QUE A SKILL NEUROFLOW PRODUCTION DEVERIA FAZER?

Se fosse criada, a skill NEUROFLOW PRODUCTION teria como objetivo encapsular o workflow completo de produção de um livro adulto de colorir — da concepção ao PDF final.

**Responsabilidades hipotéticas:**
- Orquestrar o ciclo iterativo de geração de imagens
- Aplicar o MASTER_PROMPT de forma consistente
- Conduzir o QA Visual de forma estruturada
- Gerenciar os status de curadoria
- Automatizar o processamento grayscale
- Compor o PDF interior
- Verificar conformidade KDP

---

## 3. O QUE JÁ PODE SER FEITO PELAS SKILLS EXISTENTES?

| Tarefa | Skill Existente | Limitação |
|--------|----------------|-----------|
| Design visual / protótipos | baoyu-design | Não gera ilustrações finais — cria artefatos HTML |
| Code review dos scripts | code-review-ai-ai-review | Revisão de código, não orquestração |
| Versionamento e release | release-skills | Apenas para releases do projeto em si |
| Criação de skill própria | workflow-skill-creator | **EXIGE workflow existente como base** |

**Conclusão:** Nenhuma skill existente cobre o workflow de produção artística diretamente. Mas isso não significa que precisamos criar uma skill agora.

---

## 4. O QUE REALMENTE JUSTIFICA UMA SKILL?

Uma skill é justificada quando:
1. O workflow está **testado e validado** em execuções reais
2. O workflow é **recorrente** e será executado múltiplas vezes
3. O workflow tem **inputs/outputs claros e estáveis**
4. A skill **economiza tempo real** e **reduz erros**

### Situação Atual do Neuroflow

| Critério | Status |
|----------|--------|
| Workflow testado | ❌ NÃO — ainda não foi executado nenhuma vez |
| Workflow recorrente | ✅ Sim — será repetido para novos livros |
| Inputs/outputs claros | ⚠️ Parcialmente — muitas decisões ainda pendentes |
| Skill economiza tempo | ❓ Desconhecido — dependente do workflow real |

**Conclusão:** Faltam os pré-requisitos básicos para criar uma skill agora.

---

## 5. DIVISÃO DE RESPONSABILIDADES

### O que deve permanecer nos DOCUMENTOS

- Direção artística (ART_DIRECTION.md)
- Style Bible (STYLE_BIBLE.md)
- Critérios de QA (QUALITY_CONTROL.md)
- Especificações KDP (KDP_SPECIFICATIONS.md)
- Illustration Master Plan

**Por quê:** São autoridades de referência que precisam ser consultadas, não executadas automaticamente.

---

### O que deve permanecer nos SCRIPTS

- Conversão e processamento grayscale
- Validação de resolução e formato
- Composição do PDF
- Geração de relatórios de QA técnico
- Organização de arquivos

**Por quê:** São operações sobre arquivos — perfeitas para Python scripts. Não precisam de um agente IA para executar.

---

### O que deve permanecer nos AGENTES

- Geração de imagens (usa generate_image)
- Avaliação visual de imagens (julgamento estético)
- Refinamento de prompts com base em feedback
- Decisões de curadoria (subjetivas)
- Interação com o usuário nos checkpoints

**Por quê:** São tarefas que requerem julgamento, criatividade ou interação que só um agente IA pode fazer bem.

---

### O que poderia ir para uma SKILL (futuramente)

- O processo iterativo de geração → análise → refinamento
- A aplicação consistente do MASTER_PROMPT
- O protocolo de QA visual passo a passo
- O protocolo de curadoria estruturado

**Condição:** Apenas após o Style Test validar o workflow completo uma vez.

---

## 6. COMO EVITAR ACOPLAMENTO EXCESSIVO?

Um risco real na criação de uma skill é criar **acoplamento excessivo** entre:
- A skill e decisões ainda não tomadas (trim size, diagramação)
- A skill e ferramentas específicas que podem mudar
- A skill e um estilo visual ainda em refinamento

**Estratégia para evitar:**
- Criar a skill apenas depois do Checkpoint 02 (Style Test)
- Manter a skill focada no processo, não nos parâmetros específicos
- Parametrizar tudo que é variável (não hardcode de valores KDP, etc.)

---

## 7. PROPOSTA (FUTURA — NÃO IMPLEMENTAR AGORA)

Quando o workflow estiver validado, a skill NEUROFLOW PRODUCTION poderia ter:

```yaml
name: neuroflow-production
description: >-
  Workflow de produção de livros adultos de colorir para o projeto NEUROFLOW.
  Orquestra o ciclo iterativo de geração de imagens, curadoria, QA visual
  e processamento grayscale seguindo a Style Bible e Art Direction do projeto.
```

**Fases que a skill cobriria:**
1. Leitura do conceito da Illustration Master List
2. Construção do prompt (MASTER + STYLE + conceito específico)
3. Geração iterativa com análise
4. QA Visual estruturado (13 critérios)
5. Atualização do status na Master List

**Dependências da skill futura:**
- Documenta baoyu-design (para protótipos visuais de referência)
- Referencia STYLE_BIBLE.md e ART_DIRECTION.md
- Usa scripts Python de processamento (production/scripts/)

**Trigger:** Usar workflow-skill-creator após o primeiro ciclo completo de produção.

---

## 8. RECOMENDAÇÃO FINAL

| Pergunta | Resposta |
|----------|---------|
| Criar agora? | **NÃO** |
| Criar depois do Style Test? | **Possivelmente** |
| Criar depois do 1º livro completo? | **Sim — com alta confiança** |

**A skill NEUROFLOW PRODUCTION deve ser criada APÓS o primeiro livro completo**, quando o workflow estiver totalmente validado. Nesse momento, usar `workflow-skill-creator` para destilá-la a partir da experiência real.

---

*Documento criado em: 2026-09-03*  
*Versão: 0.1.0 — Foundation*
