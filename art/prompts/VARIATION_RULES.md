# VARIATION RULES
## NEUROFLOW — Regras para Variação Estilística

> Guia para criar variações mantendo coerência visual na coleção.
> Use ao criar os prompts individuais das ilustrações.

---

## 1. PRINCÍPIO DA VARIAÇÃO CONTROLADA

A coleção deve ser variada mas coesa:
- **Variada:** Cada imagem deve ter identidade própria
- **Coesa:** Todas devem ser reconhecíveis como pertencentes ao Neuroflow

O equilíbrio entre variação e coesão é o principal desafio da coleção.

---

## 2. VARIÁVEIS CONTROLADAS

### 2.1 Composição (VARIAR LIVREMENTE)

| Tipo Compositivo | Descrição |
|-----------------|-----------|
| Expansão central | Fluxo do centro para as bordas |
| Diagonal dinâmica | Fluxo em diagonal |
| Espiral orgânica | Movimento espiral não-mecânico |
| Rede distribuída | Múltiplos nós sem centro dominante |
| Fluxo lateral | Movimento predominantemente horizontal |
| Campo denso | Densidade uniforme com variações |
| Contraste de escala | Grande × pequeno em tensão |

**Meta:** Cada tipo compositivo deve aparecer pelo menos 3–5 vezes na coleção.

---

### 2.2 Fluxo Dominante (VARIAR POR GRUPO)

| Fluxo | Sensação | Meta na Coleção |
|-------|---------|----------------|
| Centrífugo | Expansão, abertura | ~20% |
| Centrípeto | Foco, concentração | ~15% |
| Espiral | Transformação, ritmo | ~20% |
| Ondular | Calma, fluxo | ~20% |
| Radial | Energia, vitalidade | ~15% |
| Descendente | Peso, ancoragem | ~10% |

---

### 2.3 Densidade (VARIAR SISTEMATICAMENTE)

Não deve haver mais de 3 imagens consecutivas de alta ou baixa densidade:

```
Sequência de exemplo:
Alta → Média → Baixa → Alta → Média → Alta → Baixa → Média → ...
```

---

### 2.4 Complexidade (VARIAR POR DISTRIBUIÇÃO PLANEJADA)

Ver distribuição em STYLE_BIBLE.md, Seção 6.2.

Não colocar todas as imagens Level 5 no final — distribua.

---

### 2.5 Zona de Interesse Principal (VARIAR INTENCIONALMENTE)

| Zona | Descrição |
|------|-----------|
| Centro | Interesse focal no centro |
| Terço superior | Interesse no topo |
| Terço inferior | Interesse na base (peso visual) |
| Diagonal A | Canto superior esquerdo → inferior direito |
| Diagonal B | Canto superior direito → inferior esquerdo |
| Bordas ativas | Interesse distribuído nas bordas |
| Distribuído | Sem zona dominante — distribuição uniforme |

---

## 3. CONSTANTES OBRIGATÓRIAS

Estes elementos NÃO variam — são a identidade do Neuroflow:

| Elemento | Regra |
|----------|-------|
| Linguagem de linha | Sempre fluida, orgânica, contínua |
| Ausência de geometria rígida | Sempre |
| Escala tonal | Sempre completa (sem extremos puros dominantes) |
| Ausência de elementos figurativos | Sempre |
| Adequação para coloração adulta | Sempre |
| Identidade contemplativa | Sempre |

---

## 4. SEQUENCIAMENTO NA COLEÇÃO

### 4.1 Regras de Sequência

- Nunca mais de 2 imagens do mesmo nível de complexidade em sequência
- Nunca mais de 2 imagens do mesmo tipo compositivo em sequência
- Alternar imagens de alta e baixa densidade regularmente
- Distribuir Level 1 e Level 5 ao longo de toda a coleção (não agregar)

### 4.2 Estrutura Sugerida por Terços

| Terço | Posição | Característica |
|-------|---------|---------------|
| Abertura | NF-001 a NF-015 | Mix de complexidades, boa variedade, impacto visual imediato |
| Corpo | NF-016 a NF-035 | Maior complexidade, mais detalhes, experiências mais imersivas |
| Fechamento | NF-036 a NF-050 | Variedade alta, alguns dos mais especiais, fechamento memorável |

---

## 5. CONSTRUÇÃO DO PROMPT ESPECÍFICO

### Template

```
[MASTER_PROMPT]

[STYLE_PROMPT]

Specific composition for [NF-XXX]:
[Descrição do tipo compositivo]
[Descrição do fluxo dominante]
[Descrição da zona de interesse]
[Descrição de elementos específicos da ilustração]
[Descrição de texturas específicas se houver]
Complexity level: [1–5]
Density: [low / low-medium / medium / medium-high / high]
```

### Exemplo Aplicado

```
[MASTER_PROMPT + STYLE_PROMPT]

Specific composition for NF-007:
Spiral organic composition — a gentle, irregular spiral emanating from the upper-left 
region of the composition. The spiral opens progressively, becoming looser and more 
complex as it moves toward the lower-right. This is not a geometric spiral — it breathes, 
expands and contracts subtly, creating rhythm.

Lines branch off the main spiral in organic tendrils. Some loop back, creating enclosed 
cells of varying sizes. The center of the spiral has beautiful negative space with a few 
delicate detail lines. The outer regions become progressively denser with cross-hatching 
and micro-detail lines.

Flow: Spiral / centrifugal. Dominant movement from upper-left to lower-right with rotation.
Primary zone of interest: upper-left quadrant through center.
Complexity level: 3 (intermediate).
Density: Medium, rising to medium-high at the edges.
```

---

## 6. ANTI-PADRÕES DE VARIAÇÃO

Evitar estas armadilhas comuns:

| Anti-padrão | Problema | Solução |
|-------------|---------|---------|
| 50 variações da mesma "nebulosa de linhas" | Sem variedade real | Planejar explicitamente tipos compositivos diferentes |
| Todas as imagens com o mesmo centro focal | Monotonia estrutural | Variar zona de interesse |
| Complexidade crescente linear | Previsível | Distribuir aleatoriamente |
| Todas ondulares ou todas espirais | Ausência de variedade de fluxo | Planejar distribuição de fluxos |
| Densidade uniforme | Sem dinâmica | Mapear densidade explicitamente |

---

*Versão: 0.1.0 — Foundation*
