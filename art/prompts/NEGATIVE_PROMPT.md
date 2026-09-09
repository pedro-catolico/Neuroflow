# NEGATIVE PROMPT
## NEUROFLOW — Elementos a Evitar na Geração

> Lista definitiva de elementos proibidos em todas as gerações do Neuroflow.
> Incluir em todos os prompts de geração.

---

## NEGATIVE PROMPT (Versão 0.2.1 — Contemplative Figurative Authority Alignment)

```
Negative prompt — avoid all of the following:

Text, branding & identifiers:
text, letters, words, typography, numbers, watermark, signature, artist name, logo, 
trademark, copyright symbol, brand name, title text, caption, label

Childlike, commercial & character design aesthetics (PROHIBITED STYLES):
cartoon, comic book style, comic strip, anime, manga, animation cel, character design, 
fantasy character, video game concept art, mascot, commercial character, cute, kawaii, 
childlike illustration, children's coloring book style, caricature, exaggerated facial expression, 
stickers, emoji, pop art

Photorealism, render artifacts & digital painting:
photorealistic, photograph, 3D render, CGI, octane render, unreal engine, cinematic lighting, 
digital painting with visible brushstrokes, oil painting texture, heavy watercolor wash, 
airbrush shading, smooth tonal gradients, pencil sketch without line art definition

Technical & medical illustration:
medical diagram, anatomical cross-section, scientific brain scan, clinical histology, 
technical schematic, blueprint, data visualization

Geometric rigidity & pattern defects:
rigid geometric mandala, symmetrical mandala ornament, mechanical kaleidoscope, 
perfect compass circles, perfect ruler squares, grid pattern, checkerboard, halftone dots, 
wallpaper tiling, seamless repeating pattern

Pure abstraction & clutter:
pure abstract clutter devoid of motive, unrecognizable messy tangle, chaotic scribble, 
overcrowded elements, microscopic unprintable cells, muddy lines

Line art & tonal defects:
gray lines, faded lines, light gray outlines, reduced opacity lines, grayscale shading, 
tonal wash, large solid black fills (greater than small accents), solid black background, 
dark background, inverted colors, lack of contrast
```

---

## CLARIFICAÇÃO DE ELEMENTOS PERMITIDOS

> [!IMPORTANT]
> **MOTIVOS FIGURATIVOS PLENAMENTE PERMITIDOS (desde que adultos e contemplativos):**
> - Figura humana adulta serena (feminina, masculina, duplas/grupos)
> - Animais adultos em posturas elegantes e naturais
> - Flora, árvores ancestrais, folhagens e ramos
> - Paisagens (montanhas, rios, dunas, costa marinha)
> - Arquitetura orgânica (pontes de pedra, pórticos, templos rústicos, varandas)
> - Objetos contemplativos (Ikebana, vasos, livros abertos)
> - Composições de fluxo e simbólicas
>
> O Negative Prompt **NÃO proíbe figuras, animais, plantas ou ambientes**. Ele proíbe estritamente as interpretações inadequadas (estética cartoon/personagem, infantilização, fotorrealismo, esquemas anatômicos médicos e mandalas mecânicas).

---

## APLICAÇÃO

### Versão Abreviada (para prompts curtos)

```
No text, watermarks, signatures, logos. No cartoon, anime, caricature, character design, mascot, or childlike style. 
No photorealism, 3D render, or medical illustration. No solid black fills, no gray lines, no shading. 
No rigid geometric mandalas or pure abstract clutter. Pure black line art on white.
```

### Versão Completa
Usar o negative prompt completo acima sempre que possível, especialmente na geração dos prompts específicos da coleção.

---

## TRATAMENTO DE VIOLAÇÕES

Se uma imagem gerada contiver qualquer elemento da lista:
1. **Texto ou watermark** → REJEITAR imediatamente (não corrigir)
2. **Estética de personagem / cartoon / anime** → REJEITAR (ajustar prompt)
3. **Fotorrealismo / 3D / Ilustração médica** → REJEITAR (ajustar prompt)
4. **Linhas cinzas / sombreamento** → REJEITAR (exigir linha preta pura)
5. **Mandala mecânica / abstração vazia** → REJEITAR (reforçar integração orgânica)
6. **Excesso de preto (> 5%)** → REVIEW (avaliar ajustabilidade)

---

## NOTAS DE VERSÃO

| Versão | Data | Mudança |
|--------|------|---------|
| 0.1.0 | 2026-09-03 | Versão inicial — Foundation Phase |
| 0.2.0 | 2026-09-05 | Reestruturação para eliminar proibições genéricas de figuras e focar na estética infantil/cartoon (v0.1.2) |
| 0.2.1 | 2026-09-09 | Refinamento rigoroso contra character design e diagramas médicos pós-Checkpoint 01 |

---

*Versão: 0.2.1 — Foundation*

