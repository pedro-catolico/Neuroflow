# QUALITY CONTROL
## NEUROFLOW — Sistema de Controle de Qualidade Visual

---

## 1. SISTEMA DE AVALIAÇÃO

Cada imagem é avaliada em **13 critérios**, em escala de **1 a 5**.

| Pontuação | Significado |
|-----------|-------------|
| **5** | Excelente — supera as expectativas |
| **4** | Bom — atende plenamente |
| **3** | Aceitável — atende com ressalvas |
| **2** | Insuficiente — precisa de revisão |
| **1** | Inaceitável — rejeitar |

---

## 2. CRITÉRIOS DE AVALIAÇÃO

### Critério 1 — Composição
**O que avaliar:** A organização dos elementos na página. O fluxo visual. O uso do espaço.

| Pontuação | Descrição |
|-----------|-----------|
| 5 | Composição dinâmica, equilibrada e com fluxo claro. Usa toda a página |
| 4 | Boa composição com pequenos desequilíbrios |
| 3 | Composição funcional mas previsível ou com áreas mortas |
| 2 | Composição fraca — desbalanceada, sem fluxo ou com áreas vazias |
| 1 | Composição falha — elementos sem organização |

---

### Critério 2 — Coerência Estética
**O que avaliar:** Fidelidade ao estilo Neuroflow. Organicidade. Ausência de elementos genéricos.

| Pontuação | Descrição |
|-----------|-----------|
| 5 | Totalmente alinhada ao estilo Neuroflow — fluida, orgânica, sofisticada |
| 4 | Majoritariamente alinhada com pequenos desvios aceitáveis |
| 3 | Parcialmente alinhada — alguns elementos contraditórios |
| 2 | Pouco alinhada — linguagem diferente ou genérica |
| 1 | Não representa o estilo Neuroflow |

---

### Critério 3 — Complexidade
**O que avaliar:** Nível de detalhe adequado ao nível declarado. Variedade.

| Pontuação | Descrição |
|-----------|-----------|
| 5 | Complexidade perfeitamente calibrada para o nível declarado |
| 4 | Complexidade adequada com pequenas variações |
| 3 | Complexidade próxima mas com desvios perceptíveis |
| 2 | Complexidade inadequada — muito simples ou muito densa para o nível |
| 1 | Complexidade completamente inadequada |

---

### Critério 4 — Qualidade das Linhas
**O que avaliar:** Fluidez, continuidade, espessura, hierarquia.

| Pontuação | Descrição |
|-----------|-----------|
| 5 | Linhas impecavelmente fluidas com hierarquia clara e texturas ricas |
| 4 | Linhas de boa qualidade com pequenas inconsistências |
| 3 | Linhas funcionais mas sem sofisticação ou com irregularidades |
| 2 | Linhas problemáticas — rígidas, quebradas ou sem hierarquia |
| 1 | Linhas de má qualidade — artefatos, pixels, geometria rígida |

---

### Critério 5 — Distribuição Tonal
**O que avaliar:** Presença de highlights, meios-tons e sombras. Uso correto da escala tonal.

| Pontuação | Descrição |
|-----------|-----------|
| 5 | Escala tonal completa (0–6) bem distribuída. Sem excesso de preto |
| 4 | Boa distribuição tonal com pequenas lacunas |
| 3 | Distribuição aceitável mas desequilibrada (muito clara ou muito escura) |
| 2 | Distribuição problemática — extremos sem meios-tons |
| 1 | Tonalidade inadequada — toda branca, toda preta, ou sem gradação |

---

### Critério 6 — Contraste
**O que avaliar:** Diferenciação entre elementos. Legibilidade em impressão. Profundidade visual.

| Pontuação | Descrição |
|-----------|-----------|
| 5 | Contraste excelente — clara diferenciação e profundidade visual |
| 4 | Bom contraste com pequenas áreas de baixa diferenciação |
| 3 | Contraste funcional mas com zonas planas |
| 2 | Contraste insuficiente — imagem "morta" ou plana |
| 1 | Sem contraste — imagem ilegível em impressão |

---

### Critério 7 — Áreas de Coloração
**O que avaliar:** Variedade de tamanhos. Qualidade das células. Oportunidade de coloração.

| Pontuação | Descrição |
|-----------|-----------|
| 5 | Excelente variedade — grandes, médias e pequenas. Convida à coloração |
| 4 | Boa variedade com algumas áreas muito similares |
| 3 | Variedade aceitável mas previsível |
| 2 | Pouca variedade — predominantemente áreas de um só tamanho |
| 1 | Sem variedade ou áreas inutilizáveis para coloração |

---

### Critério 8 — Ausência de Artefatos
**O que avaliar:** Presença de ruído, pixelização, manchas, distorções, elementos estranhos.

| Pontuação | Descrição |
|-----------|-----------|
| 5 | Completamente limpa — sem artefatos |
| 4 | Artefatos mínimos, imperceptíveis em impressão |
| 3 | Alguns artefatos que podem aparecer em impressão |
| 2 | Artefatos visíveis que comprometem a imagem |
| 1 | Artefatos graves — imagem inutilizável |

---

### Critério 9 — Ausência de Texto
**O que avaliar:** Presença de qualquer texto, letra, número ou caractere na imagem.

| Pontuação | Descrição |
|-----------|-----------|
| 5 | Sem nenhum texto |
| 4 | — |
| 3 | — |
| 2 | Texto presente mas pequeno e periférico |
| 1 | Texto presente — REJEITAR AUTOMATICAMENTE |

> **Nota:** Este critério é BINÁRIO na prática. Qualquer texto é motivo de rejeição imediata.

---

### Critério 10 — Ausência de Watermark
**O que avaliar:** Watermarks, logos, assinaturas, marcas d'água do gerador.

| Pontuação | Descrição |
|-----------|-----------|
| 5 | Sem watermark ou assinatura |
| 1 | Watermark presente — REJEITAR AUTOMATICAMENTE |

> **Nota:** BINÁRIO. Qualquer watermark é rejeição imediata.

---

### Critério 11 — Consistência com Style Bible
**O que avaliar:** Alinhamento com os padrões definidos no STYLE_BIBLE.md.

| Pontuação | Descrição |
|-----------|-----------|
| 5 | Totalmente consistente com a Style Bible em todos os aspectos |
| 4 | Consistente com desvios mínimos aceitáveis |
| 3 | Parcialmente consistente |
| 2 | Pouco consistente — viola múltiplos princípios |
| 1 | Inconsistente — viola os princípios fundamentais |

---

### Critério 12 — Adequação à Impressão
**O que avaliar:** Se a imagem funcionará bem impressa em papel de livro de colorir.

| Pontuação | Descrição |
|-----------|-----------|
| 5 | Excelente para impressão — resolução adequada, contraste correto |
| 4 | Boa para impressão com ajustes menores |
| 3 | Funcional em impressão mas com perdas perceptíveis |
| 2 | Problemática em impressão — perda significativa de qualidade |
| 1 | Inadequada para impressão |

---

### Critério 13 — Experiência de Colorir
**O que avaliar:** A qualidade da experiência que o colorista terá ao usar a imagem.

| Pontuação | Descrição |
|-----------|-----------|
| 5 | Experiência excelente — fluída, variada, meditativa e recompensadora |
| 4 | Boa experiência com pequenas limitações |
| 3 | Experiência aceitável mas sem diferencial |
| 2 | Experiência fraca — previsível, monótona ou frustrante |
| 1 | Experiência ruim — dificulta a coloração |

---

## 3. CRITÉRIOS DE DECISÃO

### APPROVED (Aprovada)
- **Critérios 9 e 10:** Obrigatoriamente 5 (sem texto, sem watermark)
- **Média dos demais critérios:** ≥ 3.5
- **Nenhum critério abaixo de:** 2

### REVIEW (Precisa de revisão)
- **Critérios 9 e 10:** 5 (requisito mantido)
- **Média dos demais critérios:** Entre 2.5 e 3.4
- **Ou:** 1 critério com pontuação 2

### REJECTED (Rejeitada)
- **Critério 9 ou 10:** Qualquer pontuação abaixo de 5 (texto ou watermark)
- **Ou:** Média geral abaixo de 2.5
- **Ou:** Mais de 1 critério com pontuação 1

---

## 4. FORMULÁRIO DE QA

```
FICHA DE QA VISUAL
==================
ID: NF-XXX
Data de avaliação: YYYY-MM-DD
Avaliador: [nome/agente]

CRITÉRIOS (1–5):
01. Composição:           __
02. Coerência estética:   __
03. Complexidade:         __
04. Qualidade das linhas: __
05. Distribuição tonal:   __
06. Contraste:            __
07. Áreas de coloração:   __
08. Ausência de artefatos:__
09. Ausência de texto:    __
10. Ausência de watermark:__
11. Consistência StyleBib:__
12. Adequação à impressão:__
13. Experiência de colorir:__

MÉDIA: ____
DECISÃO: [ ] APPROVED  [ ] REVIEW  [ ] REJECTED

OBSERVAÇÕES:
_____________________________________________
_____________________________________________

AÇÃO RECOMENDADA:
_____________________________________________
```

---

## 5. QA TÉCNICO (PDF E KDP)

### 5.1 Verificação de Arquivo

| Critério | Especificação | Status |
|----------|--------------|--------|
| Resolução | ≥ 300 DPI | A verificar |
| Dimensões | Igual ao trim size | A definir |
| Bleed | Conforme KDP | A verificar |
| Margens | Conforme KDP | A verificar |
| Formato | PDF | A verificar |
| Tamanho | ≤ 650 MB | A verificar |
| Espaço de cor | Grayscale ou CMYK | A verificar |
| Fontes embutidas | Sim | A verificar |

### 5.2 Verificação Visual do PDF

- [ ] Todas as páginas presentes e na ordem correta
- [ ] Sem páginas em branco não intencionais
- [ ] Sem páginas cortadas ou desalinhadas
- [ ] Numeração correta (se houver)
- [ ] Capa e contracapa corretas
- [ ] Margens internas (lombada) adequadas

---

## 6. RELATÓRIOS DE QA

Os relatórios de QA são armazenados em:
```
qa/
├── visual/        ← Fichas de QA visual por imagem
├── technical/     ← Relatórios técnicos (resolução, PDF)
└── reports/       ← Relatórios consolidados por fase
```

---

*Documento criado em: 2026-09-03*  
*Versão: 0.1.0 — Foundation*
