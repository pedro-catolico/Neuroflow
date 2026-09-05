# PRODUCTION PIPELINE
## NEUROFLOW — Arquitetura da Pipeline de Produção

---

## 1. VISÃO GERAL

```
IDEAÇÃO
  ↓
DIREÇÃO ARTÍSTICA
  ↓
PLANEJAMENTO
  ↓
PROMPT ENGINEERING
  ↓
GERAÇÃO DE IMAGENS ←──────────────┐
  ↓                               │
ANÁLISE                           │ Ciclo iterativo
  ↓                               │ até aprovação
REFINAMENTO ──────────────────────┘
  ↓
CURADORIA
  ↓
TRATAMENTO GRAYSCALE
  ↓
PADRONIZAÇÃO
  ↓
QA VISUAL
  ↓
DIAGRAMAÇÃO
  ↓
GERAÇÃO DO PDF
  ↓
QA TÉCNICO
  ↓
PREPARAÇÃO KDP
```

---

## 2. CHECKPOINTS

Nenhuma fase avança sem aprovação explícita do checkpoint correspondente.

### CHECKPOINT 01 — Direção Artística
**Condição de entrada:** Foundation completa  
**Entregáveis:**
- Style Bible aprovada
- Art Direction aprovada
- MASTER_PROMPT definido e testado
- NEGATIVE_PROMPT definido e testado
- Illustration Master Plan com 40–50 conceitos aprovados

**Aprovação:** Usuário  
**Próxima fase:** Style Test

---

### CHECKPOINT 02 — Style Test
**Condição de entrada:** Checkpoint 01 aprovado  
**Entregáveis:**
- 5–8 imagens de teste geradas
- Avaliação de grayscale (impressão ou simulação)
- QA Visual aplicado em cada imagem de teste
- Feedback incorporado nos prompts
- MASTER_PROMPT refinado (se necessário)

**Aprovação:** Usuário  
**Próxima fase:** Produção em escala

---

### CHECKPOINT 03 — Primeira Geração (Batch 1)
**Condição de entrada:** Checkpoint 02 aprovado  
**Entregáveis:**
- Primeiro batch de imagens geradas (10–15)
- Avaliadas contra Style Bible
- QA Visual aplicado

**Aprovação:** Usuário  
**Próxima fase:** Continuação da produção

---

### CHECKPOINT 04 — Curadoria Final
**Condição de entrada:** Todas as imagens geradas  
**Entregáveis:**
- 40–50 imagens aprovadas em `art/selected/`
- Imagens rejeitadas documentadas em `art/rejected/`
- Grayscale processado em `art/grayscale/`
- Final art em `art/final/`

**Aprovação:** Usuário  
**Próxima fase:** Diagramação

---

### CHECKPOINT 05 — Layout
**Condição de entrada:** Checkpoint 04 aprovado  
**Entregáveis:**
- Template de diagramação definido
- Trim size confirmado
- Ordem das imagens definida
- Elementos editoriais definidos (capa interna, créditos, etc.)
- Preview de algumas páginas

**Aprovação:** Usuário  
**Próxima fase:** Geração do PDF

---

### CHECKPOINT 06 — PDF Final
**Condição de entrada:** Checkpoint 05 aprovado  
**Entregáveis:**
- Interior PDF gerado
- QA técnico aplicado (resolução, margens, bleed)
- Cover PDF gerado
- Pré-visualização completa do livro

**Aprovação:** Usuário  
**Próxima fase:** Preparação KDP

---

### CHECKPOINT 07 — KDP
**Condição de entrada:** Checkpoint 06 aprovado  
**Entregáveis:**
- Metadados KDP preparados
- Categorias definidas
- Preço definido
- ISBN (se aplicável)
- Arquivos dentro das especificações técnicas KDP

**Aprovação:** Usuário  
**Próxima fase:** Upload e publicação

---

## 3. FASE: GERAÇÃO DE IMAGENS

### 3.1 Ferramenta Principal
`generate_image` — nativa do ambiente Antigravity/Gemini

### 3.2 Processo Iterativo

```
CONCEITO (da Illustration Master List)
  ↓
CONSTRUÇÃO DO PROMPT (MASTER + STYLE + ilustração específica)
  ↓
GERAÇÃO INICIAL
  ↓
ANÁLISE CONTRA STYLE BIBLE
  ↓
IDENTIFICAÇÃO DE REFINAMENTOS
  ↓
PROMPT AJUSTADO
  ↓
NOVA GERAÇÃO
  ↓
(Repetir até satisfação ou limite de iterações)
  ↓
CURADORIA (approved / review / rejected)
```

### 3.3 Regras de Geração

- **Nunca** assumir que a primeira geração é definitiva
- **Sempre** registrar o prompt usado na ficha da ilustração
- **Sempre** registrar o motivo de rejeição
- **Máximo** de 5 iterações por ilustração antes de escalar para revisão
- **Batch processing:** Gerar 5–10 imagens por sessão, avaliar, ajustar prompts, continuar

### 3.4 Nomenclatura

```
Arquivo: NF-XXX.png (onde XXX é o número com zeros à esquerda)
Exemplo: NF-001.png, NF-012.png, NF-050.png
```

---

## 4. FASE: CURADORIA

### 4.1 Status de Curadoria

| Status | Pasta | Significado |
|--------|-------|-------------|
| **GENERATED** | `art/generated/` | Imagem gerada, aguardando avaliação |
| **SELECTED** | `art/selected/` | Aprovada na curadoria inicial |
| **REJECTED** | `art/rejected/` | Rejeitada — mantida para referência |
| **IN_REVIEW** | `art/qa/` | Em QA Visual avançado |
| **FINAL** | `art/final/` | Aprovada em todos os critérios |

### 4.2 Rastreabilidade

Cada imagem deve ter uma entrada no Illustration Master Plan com:
- ID único
- Status atual
- Prompt utilizado
- Data de geração
- Motivo de rejeição (se aplicável)
- Observações

---

## 5. FASE: TRATAMENTO GRAYSCALE

### 5.1 Objetivos

- Garantir escala tonal correta conforme Style Bible
- Ajustar contraste para impressão em papel de livro de colorir
- Padronizar resolução e dimensões
- Exportar em formato adequado para diagramação

### 5.2 Parâmetros Técnicos (A Confirmar com KDP)

| Parâmetro | Valor Provisório | Status |
|-----------|----------------|--------|
| Resolução | 300 DPI mínimo | A confirmar |
| Formato | PNG ou TIFF | A confirmar |
| Espaço de cor | Grayscale | Confirmado |
| Profundidade de bits | 8-bit | A confirmar |
| Dimensões | Igual ao trim size | A definir |

### 5.3 Pipeline de Processamento (Futuro)

```python
# Conceito — scripts em production/scripts/
# 1. Carregar imagem gerada (art/selected/)
# 2. Converter para grayscale se não estiver
# 3. Ajustar níveis (highlight, midtone, shadow)
# 4. Ajustar contraste
# 5. Redimensionar para trim size + bleed
# 6. Validar resolução
# 7. Exportar para art/grayscale/
# 8. Gerar log de processamento
```

---

## 6. FASE: DIAGRAMAÇÃO

### 6.1 Estrutura do Interior

```
[Página de Título]
[Copyright / Créditos]
[Introdução / Instruções] (opcional)
[Ilustrações — ordem a definir]
[Contra-capa interna] (opcional)
```

### 6.2 Template de Página de Ilustração

```
[Imagem — centralizada ou com sangria]
[Número da imagem — discreto] (opcional)
[Verso em branco ou com padrão leve] (a definir)
```

### 6.3 Ferramentas de Diagramação (A Definir)

| Opção | Prós | Contras |
|-------|------|---------|
| Python + ReportLab | Automação total | Curva de aprendizado |
| Python + fpdf2 | Simples, sem dependências pesadas | Menos controle |
| Adobe InDesign | Controle profissional | Custo, não automatizável facilmente |
| Affinity Publisher | Boa relação custo/benefício | Semi-automatizável |

**Status:** A DEFINIR — depende das necessidades de automação após Style Test

---

## 7. FASE: QA TÉCNICO

### 7.1 Critérios KDP

| Critério | Especificação | Fonte | Verificado |
|----------|--------------|-------|-----------|
| Resolução mínima interior | 300 DPI | KDP Help | A verificar |
| Formato de cor interior | CMYK ou Grayscale | KDP Help | A verificar |
| Formato de arquivo | PDF | KDP Help | A verificar |
| Tamanho máximo do arquivo | 650 MB | KDP Help | A verificar |
| Bleed (se aplicável) | 0.125" | KDP Help | A verificar |
| Margens mínimas | 0.25" | KDP Help | A verificar |

> **Nota:** Verificar SEMPRE em fonte oficial antes de gerar o PDF final.

---

## 8. AUTOMAÇÃO

### 8.1 Scripts Planejados

| Script | Propósito | Entrada | Saída | Status |
|--------|-----------|---------|-------|--------|
| `validate_images.py` | Validar resolução e formato | `art/selected/` | Relatório de validação | Planejado |
| `convert_grayscale.py` | Converter e ajustar grayscale | `art/selected/` | `art/grayscale/` | Planejado |
| `generate_previews.py` | Gerar thumbnails de preview | `art/grayscale/` | `output/previews/` | Planejado |
| `compose_pdf.py` | Gerar PDF interior | `art/final/`, template | `output/interior/` | Planejado |
| `qa_report.py` | Gerar relatório de QA | `qa/` | `qa/reports/` | Planejado |

### 8.2 Requisitos de Qualidade para Scripts

- Caminhos relativos (nunca absolutos hardcoded)
- Tratamento de erros com mensagens claras
- Logs de execução
- Configuração centralizada (não hardcode de parâmetros)
- Documentação inline

---

## 9. PASTAS E FLUXO DE ARQUIVOS

```
art/
├── generated/      ← Saída bruta da geração
├── selected/       ← Curadoria inicial (aprovadas)
├── rejected/       ← Rejeitadas (mantidas)
├── grayscale/      ← Após processamento tonal
├── qa/             ← Em QA Visual avançado
└── final/          ← Aprovadas em todos os critérios

output/
├── previews/       ← Thumbnails e previews
├── interior/       ← PDF interior final
├── cover/          ← PDF de capa final
└── release/        ← Pacote KDP completo
```

---

*Documento criado em: 2026-09-03*  
*Versão: 0.1.0 — Foundation*
