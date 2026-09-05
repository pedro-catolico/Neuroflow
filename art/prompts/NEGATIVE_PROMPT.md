# NEGATIVE PROMPT
## NEUROFLOW — Elementos a Evitar na Geração

> Lista definitiva de elementos proibidos em todas as gerações do Neuroflow.
> Incluir em todos os prompts de geração.

---

## NEGATIVE PROMPT (Versão 0.2.0 — Contemplative Figurative Alignment)

```
Negative prompt — avoid all of the following:

Text and identifiers:
text, letters, words, numbers, watermark, signature, logo, copyright symbol, 
brand name, artist signature, title text, caption, label

Childlike & commercial character aesthetics (PROHIBITED STYLES):
childlike illustration, children's coloring book aesthetic, cartoon, comic book style,
anime, manga, mascot, commercial character, cute character aesthetic, kawaii,
caricature, exaggerated facial expression, pop art, emoji style, sticker, icon

Photorealism & render artifacts:
hyperrealistic portrait, photographic realism, cinematic photorealism, 3D render,
digital painting with brush strokes, oil painting texture, heavy watercolor wash,
photorealistic texture, real photograph, pencil sketch without line art foundation

Structural & pattern errors:
pure abstraction devoid of figure, unrecognizable subject, unreadable tangle,
rigid geometric mandala, symmetrical mandala ornament, mechanical symmetry,
perfect circles, perfect squares, grid pattern, checkerboard, halftone dots

Visual clutter & readability issues:
visual clutter, chaotic composition, overcrowded elements, unprintable tiny cells,
repetitive mechanical patterns, indistinct forms, muddy linework

Tonal & line art defects:
gray lines, faded lines, reduced opacity lines, grayscale shading, tonal wash,
solid black fill, large solid black areas, black background, gradients, no contrast
```

---

## CLARIFICAÇÃO DE ELEMENTOS PERMITIDOS

> [!NOTE]
> **ELEMENTOS PERMITIDOS (desde que contemplativos e adultos):**
> Figuras humanas adultas serenas, rostos/retratos em postura contemplativa, silhuetas humanas, animais em contexto natural, árvores, plantas, caminhos, arquiteturas e paisagens.
> 
> O Negative Prompt proíbe a **estética infantil, cartoon, fotorrealismo e mandalas**, mas NÃO proíbe a figura humana ou elementos figurativos contemplativos.

---

## APLICAÇÃO

### Versão Abreviada (para prompts curtos)

```
No text, watermarks, signatures. No cartoon, anime, caricature, or childlike style. 
No photorealism or 3D render. No solid black fills, no gray lines, no shading. 
No rigid geometric mandalas or pure abstract clutter.
No commercial logos or trademarked characters.
```

### Versão Completa
Usar o negative prompt completo acima sempre que possível, especialmente nas primeiras gerações.

---

## TRATAMENTO DE VIOLAÇÕES

Se uma imagem gerada contiver qualquer elemento da lista:
1. **Texto ou watermark** → REJEITAR imediatamente (não corrigir)
2. **Estética infantil / cartoon** → REJEITAR (ajustar prompt)
3. **Fotorrealismo / 3D** → REJEITAR (ajustar prompt)
4. **Linhas cinzas / sombreamento** → REJEITAR (exigir linha preta pura)
5. **Mandala / abstração pura** → REJEITAR (reforçar figura reconhecível)
6. **Excesso de preto** → REVIEW (avaliar ajustabilidade)

---

## NOTAS DE VERSÃO

| Versão | Data | Mudança |
|--------|------|---------|
| 0.1.0 | 2026-09-03 | Versão inicial — Foundation Phase |
| 0.2.0 | 2026-09-05 | Reestruturação para eliminar proibições genéricas de figuras e focar na estética infantil/cartoon (v0.1.2) |

---

*Versão: 0.2.0 — Foundation*

