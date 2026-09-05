# PROJECT BRIEF
## NEUROFLOW

---

## IDENTIDADE DO PRODUTO

| Campo | Valor |
|-------|-------|
| **Nome** | NEUROFLOW |
| **Conceito** | Fluxo Neurográfico |
| **Categoria** | Adult Coloring Book |
| **Público** | Adultos |
| **Idioma** | Inglês (mercado KDP) |
| **Plataforma** | Amazon KDP — Print on Demand |

---

## POSICIONAMENTO

NEUROFLOW é um livro adulto de colorir sofisticado, contemplativo, artístico e voltado à experiência de concentração, relaxamento e mindfulness.

O produto **não deve parecer infantil**. É uma experiência estética e meditativa para adultos que buscam:
- Concentração e foco
- Relaxamento e redução de estresse
- Expressão criativa
- Experiência contemplativa e artística

---

## CONCEITO VISUAL

A inspiração conceitual é o **fluxo neurográfico** — uma linguagem visual baseada em:

- Linhas fluidas e contínuas
- Formas orgânicas interconectadas
- Estruturas abstratas em movimento
- Ritmo, equilíbrio e continuidade
- Expansão e contração de espaços
- Composição meditativa
- Profundidade visual

**O que NÃO é:**
- Coleção genérica de mandalas
- Padrões geométricos rígidos
- Desenhos infantis ou clipart
- Aparência genérica de IA
- Personagens ou elementos narrativos

---

## ESTILO E TÉCNICA

| Campo | Valor |
|-------|-------|
| **Estilo principal** | Grayscale — linhas e tons |
| **Técnica de geração** | IA (Gemini/Antigravity) com curadoria manual |
| **Adequado para** | Lápis de cor, marcadores, pastel, aquarela |

O grayscale é uma **decisão artística deliberada**, não um filtro aplicado. As imagens possuem:
- Highlights, meios-tons e sombras controladas
- Contraste adequado para impressão
- Áreas de coloração interessantes e variadas
- Profundidade visual

---

## DIMENSÕES E FORMATO

| Campo | Valor |
|-------|-------|
| **Trim size** | STATUS: A DEFINIR |
| **Orientação** | STATUS: A DEFINIR |
| **Páginas estimadas** | STATUS: A DEFINIR |
| **Ilustrações estimadas** | 40–50 |
| **Layout de página** | STATUS: A DEFINIR |
| **Bleed** | STATUS: A DEFINIR |
| **Margens** | STATUS: A DEFINIR |

> **Nota:** As opções mais comuns para livros de colorir no KDP são 8.5" × 11" e 8" × 10". A decisão final depende da análise de concorrência e especificações técnicas do KDP.

---

## COLEÇÃO DE ILUSTRAÇÕES

| Campo | Valor |
|-------|-------|
| **Quantidade estimada** | 40–50 ilustrações |
| **Convenção de nomes** | NF-001, NF-002, NF-003... |
| **Níveis de complexidade** | 5 níveis (Level 1 a Level 5) |
| **Variedade** | Alta — evitar repetição estilística |
| **Organização** | A definir (por seção temática ou por complexidade) |

---

## PIPELINE DE PRODUÇÃO

```
IDEAÇÃO
→ DIREÇÃO ARTÍSTICA
→ PLANEJAMENTO
→ PROMPT ENGINEERING
→ GERAÇÃO DE IMAGENS
→ CURADORIA
→ TRATAMENTO GRAYSCALE
→ PADRONIZAÇÃO
→ QA VISUAL
→ DIAGRAMAÇÃO
→ GERAÇÃO DO PDF
→ QA TÉCNICO
→ PREPARAÇÃO KDP
```

---

## OBJETIVOS DO PRODUTO

1. Oferecer uma experiência meditativa e criativa de alta qualidade
2. Posicionar o produto no segmento premium do mercado de colorir adulto
3. Publicar com sucesso no Amazon KDP via Print on Demand
4. Estabelecer uma infraestrutura reutilizável para futuros produtos similares

---

## PRINCÍPIOS DO PROJETO

1. **Qualidade sobre quantidade** — 40–50 imagens excelentes valem mais que 100 mediocres
2. **Rastreabilidade total** — toda decisão e imagem deve ser documentada
3. **Iteração controlada** — checkpoints antes de avançar nas fases críticas
4. **Propriedade intelectual limpa** — criação original, sem derivações problemáticas
5. **Pipeline reutilizável** — arquitetura modular para futuros livros

---

## DECISÕES TOMADAS

| Decisão | Valor |
|---------|-------|
| Conceito visual | Fluxo Neurográfico |
| Público-alvo | Adultos |
| Técnica visual | Grayscale artístico |
| Plataforma | Amazon KDP |
| Convenção de nomes | NF-XXX |
| Quantidade estimada | 40–50 ilustrações |
| Ferramenta de geração | Gemini/Antigravity (generate_image) |
| Checkpoints | 7 checkpoints definidos |

---

## DECISÕES PENDENTES

| Decisão | Status | Responsável |
|---------|--------|-------------|
| Trim size do livro | A DEFINIR | Usuário (após análise KDP) |
| Orientação das páginas | A DEFINIR | Usuário |
| Número total de páginas | A DEFINIR | Usuário |
| Organização das ilustrações | A DEFINIR | Usuário |
| Preço de venda | A DEFINIR | Usuário |
| Título definitivo da capa | A DEFINIR | Usuário |
| Subtítulo | A DEFINIR | Usuário |
| Autor/Pseudônimo | A DEFINIR | Usuário |
| Série ou produto único | A DEFINIR | Usuário |
| Páginas em branco (verso das ilustrações) | A DEFINIR | Usuário |
| Elementos editoriais (introdução, instruções) | A DEFINIR | Usuário |
| Capa — conceito visual | A DEFINIR | Usuário + Art Director |

---

## RISCOS IDENTIFICADOS

| Risco | Probabilidade | Impacto | Mitigação |
|-------|--------------|---------|-----------|
| Inconsistência visual entre imagens geradas | Alta | Alto | Sistema de prompts rigoroso + curadoria |
| Qualidade insuficiente do grayscale gerado | Média | Alto | Style Test antes da produção em escala |
| Violação de propriedade intelectual | Baixa | Alto | Prompts originais + revisão manual |
| Especificações KDP desatualizadas | Média | Médio | Verificar em fonte oficial antes do PDF |
| Excesso de preto nas imagens | Média | Médio | NEGATIVE_PROMPT rigoroso |

---

## REFERÊNCIAS

- Nenhuma referência externa incorporada até o momento
- Ver `art/references/README.md` para política de referências

---

*Documento criado em: 2026-09-03*  
*Versão: 0.1.0 — Foundation*
