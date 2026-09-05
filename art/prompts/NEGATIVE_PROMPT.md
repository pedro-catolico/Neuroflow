# NEGATIVE PROMPT
## NEUROFLOW — Elementos a Evitar na Geração

> Lista definitiva de elementos proibidos em todas as gerações do Neuroflow.
> Incluir em todos os prompts de geração.

---

## NEGATIVE PROMPT (Versão 0.1.0)

```
Negative prompt — avoid all of the following:

Text and identifiers:
text, letters, words, numbers, watermark, signature, logo, copyright symbol, 
brand name, artist signature, title text, caption, label

Inappropriate aesthetics:
cartoon, anime, kawaii, cute, childlike, baby, infantile, clipart,
colorful illustration, character design, mascot, emoji style,
flat design, icon, pictogram, sticker

Prohibited character styles & commercial clutter:
childlike figures, cartoon character, mascot, emoji style,
celebrity likeness, fictional trademarked character, pop art, manga, anime,
pure geometric mandalas, abstract geometric clutter

Quality issues:
blurry, pixelated, low resolution, compression artifacts, 
jpeg artifacts, noisy, grainy texture, distorted lines,
overexposed, washed out, muddy, unclear

Tonal problems:
solid black fill, large black area, black background,
no contrast, flat gray, no highlights, no shadows,
solid white (no detail), muddy midtones

Structural problems:
rigid geometry, perfect circles, perfect squares, mechanical symmetry,
bilateral symmetry, radial symmetry (as primary design element),
grid pattern, checkerboard, halftone dots, screen print texture,
photorealistic texture, photographic element, real photograph

Commercial elements:
advertising element, promotional content, product placement,
price tag, barcode

Style contradictions:
photorealistic portrait, photograph effect, 3D render,
digital painting with brush strokes, oil painting texture,
watercolor wash (as primary style — light texture is acceptable),
pencil sketch without line art foundation
```

---

## APLICAÇÃO

### Versão Abreviada (para prompts curtos)

```
No text, watermarks, signatures. No cartoon, anime, or childlike style. 
No photorealism or 3D render. No solid black areas. 
No perfect geometric shapes or rigid mandalas.
No logos, brands, or trademarked characters.
```

### Versão Completa
Usar o negative prompt completo acima sempre que possível, especialmente nas primeiras gerações.

---

## TRATAMENTO DE VIOLAÇÕES

Se uma imagem gerada contiver qualquer elemento da lista:
1. **Texto ou watermark** → REJEITAR imediatamente (não corrigir)
2. **Estética infantil** → REJEITAR (problema de prompt, ajustar)
3. **Excesso de preto** → REVIEW (pode ser ajustável em processamento)
4. **Geometria rígida** → REVIEW (avaliar se é dominante)
5. **Outros artefatos** → REVIEW (avaliar gravidade)

---

*Versão: 0.1.0 — Foundation*
