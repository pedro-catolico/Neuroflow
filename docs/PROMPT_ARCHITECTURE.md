# PROMPT ARCHITECTURE v0.1
## NEUROFLOW — Arquitetura de Prompts e Engenharia de Geração Executável

> **Documento de Autoridade da Engenharia de Prompts**  
> **Objetivo:** Estabelecer a arquitetura oficial e padronizada para converter os 45 conceitos do *Illustration Master Plan* (`content/illustration-list/illustrations-master.md` v0.2.0) em prompts de geração de imagem executáveis, garantindo coerência de linguagem, rastreabilidade total e excelência na experiência de coloração adulta.

---

## 1. PRINCÍPIO DA ARQUITETURA

A arquitetura de prompts do Neuroflow baseia-se na regra editorial fundamental:

$$\text{VARIAR O CONTEÚDO, PRESERVAR A LINGUAGEM.}$$

$$\text{Fórmula Visual Executável} = \text{Motivo Reconhecível} + \text{Estrutura Neurográfica Orgânica} + \text{Composição Contemplativa} + \text{Complexidade Adulta}$$

O objetivo desta arquitetura é permitir que ilustrações com assuntos completamente distintos — como **NF-001** (baleias/animal), **NF-003** (figura feminina/humano), **NF-010** (jardim/arquitetura) e **NF-030** (livro à janela/objeto) — compartilhem a mesma "família visual" inconfundível, enquanto oferecem ao colorista uma experiência meditativa única e não-repetitiva.

---

## 2. ESQUEMA DOS BLOCOS OPERACIONAIS (BLOCO A a H)

Todo prompt executável do Neuroflow é montado a partir de **8 blocos funcionais rigorosamente encadeados**:

```
+-----------------------------------------------------------------------+
|  BLOCO A: IDENTITY CONSTANTS (Master Prompt v0.2.1)                   |
+-----------------------------------------------------------------------+
|  BLOCO B: SUBJECT VARIABLES (Motivo Principal & Modo Figurativo)       |
+-----------------------------------------------------------------------+
|  BLOCO C: STRUCTURAL VARIABLES (Pose, Escala, Enquadramento)          |
+-----------------------------------------------------------------------+
|  BLOCO D: NEUROGRAPHIC INTEGRATION (Integração Orgânica Motivo-Linhas) |
+-----------------------------------------------------------------------+
|  BLOCO E: COMPOSITION VARIABLES (Composição, Fluxo & Espaço Negativo)  |
+-----------------------------------------------------------------------+
|  BLOCO F: DENSITY & COMPLEXITY VARIABLES (Nível 1-5 & Densidade)      |
+-----------------------------------------------------------------------+
|  BLOCO G: COLORING EXPERIENCE (Arquitetura de Células & Impressão KDP)|
+-----------------------------------------------------------------------+
|  BLOCO H: NEGATIVE CONSTRAINTS (Negative Prompt v0.2.1)               |
+-----------------------------------------------------------------------+
```

---

### BLOCO A — IDENTITY CONSTANTS (Constantes de Identidade)
- **Função:** Ancorar a imagem na linguagem visual oficial do Neuroflow.
- **Conteúdo:** Estilo de ilustração neurográfica para livro de colorir adulto, sob a síntese *Contemplativo Figurativo*. Traçado em linha preta pura sobre fundo branco. Ausência de geometria rígida, mandalas mecânicas, fotorrealismo, sombreamento cinza ou estética de personagem comercial.
- **Origem:** `art/prompts/MASTER_PROMPT.md` (v0.2.1).

### BLOCO B — SUBJECT VARIABLES (Variáveis do Motivo)
- **Função:** Especificar o motivo concreto e reconhecível da página.
- **Conteúdo:** Categoria principal (`Human Female`, `Human Male`, `Human Group`, `Animal`, `Flora`, `Tree`, `Landscape`, `Architecture`, `Object`, `Symbolic Composition`, `Water`) e a descrição do sujeito extraída de `illustrations-master.md`.
- **Origem:** `illustrations-master.md` (campo *Motivo Principal* e *Conceito*).

### BLOCO C — STRUCTURAL VARIABLES (Variáveis Estruturais)
- **Função:** Definir o ponto de vista óptico, enquadramento e atitude do sujeito na página.
- **Conteúdo:** Ângulo da câmera (plano geral, plano médio, close-up de perfil, contra-plongée, vista frontal serena), postura (não-teatral, serena, em repouso ou movimento natural) e escala de presença na folha.
- **Origem:** `illustrations-master.md` (campo *Modo Figurativo* e *Densidade Figurativa*).

### BLOCO D — NEUROGRAPHIC INTEGRATION (Integração Neurográfica Orgânica)
- **Função:** Garantir que as linhas e redes neurográficas nasçam *do próprio motivo e do ambiente*, sem parecer uma estampa colada por trás do assunto.
- **Conteúdo:** Descrição precisa de onde brotam as linhas contínuas (ex.: contornos de tecidos, cascas de árvore, nervuras de folhas, marolas d'água, arcos de pedra, rugas do terreno) e como conectam o motivo focal ao espaço em redor.
- **Origem:** `illustrations-master.md` (campo *Integração Neurográfica*).

### BLOCO E — COMPOSITION VARIABLES (Variáveis de Composição e Fluxo)
- **Função:** Determinar a dinâmica do olhar e o respiro meditativo da composição.
- **Conteúdo:** Tipo compositivo (Expansão central, Diagonal dinâmica, Espiral orgânica, Rede distribuída, Fluxo lateral, Campo denso, Contraste de escala, Bordas ativas), fluxo dominante (Centrífugo, Centrípeto, Espiral, Ondular, Radial, Descendente, Vertical) e posicionamento do espaço negativo em branco.
- **Origem:** `illustrations-master.md` (campos *Composição* e *Fluxo*) e `art/prompts/VARIATION_RULES.md`.

### BLOCO F — DENSITY & COMPLEXITY VARIABLES (Densidade e Complexidade)
- **Função:** Calibrar a quantidade de detalhes para o nível técnico planejado.
- **Conteúdo:** Nível de complexidade (Level 1 a Level 5) e densidade de linhas (Baixa, Média-Baixa, Média, Média-Alta, Alta, Muito Alta), definindo a taxa de linhas por área.
- **Origem:** `illustrations-master.md` (campos *Complexidade* e *Densidade*).

### BLOCO G — COLORING EXPERIENCE (Arquitetura de Células de Coloração)
- **Função:** Garantir a usabilidade tátil da página para lápis de cor e marcadores.
- **Conteúdo:** Proporção entre áreas amplas de cor, áreas médias de suporte e microdetalhes finos; estanqueidade de células fechadas confortáveis; restrição de preenchimento preto maciço a no máximo 5% em acentos minúsculos; linha preta 100% pura sem cinzas ou gradientes.
- **Origem:** `docs/STYLE_BIBLE.md` e `art/prompts/STYLE_PROMPT.md` (v0.2.1).

### BLOCO H — NEGATIVE CONSTRAINTS (Filtros de Exclusão)
- **Função:** Bloquear ruídos visuais, estéticas inadequadas e artefatos de geração.
- **Conteúdo:** Bloqueio estrito de texto, assinaturas, logos, fotorrealismo, 3D, character design, cartoon, anime, mangá, mascotes, mandalas geométricas rígidas, ilustrações médicas/anatômicas e sombreamentos em cinza.
- **Origem:** `art/prompts/NEGATIVE_PROMPT.md` (v0.2.1).

---

## 3. TABELA DE CONSTANTES VS. VARIÁVEIS

| Componente | Status | Regra de Aplicação |
|:---|:---:|:---|
| **Estilo da Linha (Line Art)** | **CONSTANTE** | 100% linha preta pura sobre fundo branco puro (zero cinza/gradiente). |
| **Identidade Conceitual** | **CONSTANTE** | Contemplativo Figurativo (motivo reconhecível + fluxo neurográfico). |
| **Proibição de Character Design** | **CONSTANTE** | Sem cartoon, anime, mangá, mascote ou expressões teatrais. |
| **Proibição de Mandalas Mecânicas** | **CONSTANTE** | Sem simetria radial perfeita ou padrões de caleidoscópio. |
| **Respiro em Espaço Negativo** | **CONSTANTE** | Mínimo de 20–30% da folha reservada a branco puro. |
| **Motivo Principal** | **VARIÁVEL** | Determinado exclusivamente por `illustrations-master.md` (11 categorias). |
| **Modo Figurativo / Pose** | **VARIÁVEL** | Varia conforme o conceito (humano, animal, botânico, arquitetura, etc.). |
| **Nível de Complexidade** | **VARIÁVEL** | Calibrado de Level 1 a Level 5 segundo a matriz da coleção. |
| **Tipo Compositivo** | **VARIÁVEL** | Alternado entre as 8 opções compositivas de `VARIATION_RULES.md`. |
| **Fluxo Dominante** | **VARIÁVEL** | Alternado entre as 7 direções de fluxo visual. |
| **Integração Neurográfica** | **VARIÁVEL** | Especificada individualmente segundo a natureza anatômica/física do motivo. |

---

## 4. REGRAS DE PRECEDÊNCIA E ACORDO DE HIERARQUIA

Quando houver potencial atrito entre instruções do prompt:

1. **Regra de Ouro (Precedência Máxima):** As **IDENTITY CONSTANTS** e **NEGATIVE CONSTRAINTS** (Blocos A e H) sobrepõem-se a qualquer instrução do motivo. Se uma descrição do motivo sugerir um elemento proibido (ex.: "olhar expressivo de personagem" ou "padrão radiante perfeito"), a restrição estética anula a interpretação narrativa.
2. **Autoridade do Master Plan:** O motivo principal, a complexidade e a composição de cada ilustração **não podem ser alterados** pela engenharia de prompts. O prompt deve traduzir fielmente o `illustrations-master.md`.
3. **Sem Adição Não-Autorizada:** Detalhes secundários (como elementos de fundo) só podem ser adicionados ao prompt se servirem à *Integração Neurográfica* ou à *Função Contemplativa* da página.

---

## 5. TEMPLATE DE MONTAGEM DO PROMPT EXECUTÁVEL (EM INGLÊS)

Os prompts finais de geração consumidos pelas APIs/ferramentas de IA são estruturados no seguinte formato padronizado em inglês:

```text
[BLOCK A — IDENTITY]
Neurographic flow art illustration for an adult coloring book — Contemplative Figurative identity. Crisp black line art on pure white background.

[BLOCK B & C — SUBJECT & STRUCTURE]
Subject: [SPECIFIC SUBJECT DESCRIPTION from Master Plan]. 
Structure & Framing: [Framing, camera perspective, pose/attitude, and figure-space relationship].

[BLOCK D — NEUROGRAPHIC INTEGRATION]
Neurographic Integration: Continuous, fluid, curving lines emerge organically from [specific contours/textures of the subject], weaving the subject and surrounding atmosphere into an unbroken, harmonious living tapestry.

[BLOCK E — COMPOSITION & FLOW]
Composition & Flow: [Compositional type, e.g., Dynamic diagonal] composition with a dominant [Flow type, e.g., wavy/centrifugal] movement. Balanced focal point at [focal zone] with generous, intentional pure white negative space (minimum 25%).

[BLOCK F & G — DENSITY & COLORING EXPERIENCE]
Complexity & Usability: Complexity Level [1-5] with [Density level] line density. Clear, comfortable enclosed coloring cells designed for adult colorists using colored pencils or markers. Clear line weight hierarchy (bold main contours, medium flow lines, fine interior textures). Zero gray lines, zero grayscale shading, zero gradients, zero solid black filled masses.

[BLOCK H — NEGATIVE CONSTRAINTS]
Negative Constraints: Avoid text, letters, watermark, signature, logo. Avoid character design, cartoon, anime, manga, mascot, cute/kawaii aesthetic, childlike illustration, caricature. Avoid photorealism, 3D render, photographic texture, medical/anatomical diagram. Avoid rigid geometric mandalas, mechanical symmetry, halftone dots, chaotic unreadable clutter.
```

---

## 6. EXEMPLOS CONCEITUAIS COMPLETOS DE PROMPT EXECUTÁVEL

### Exemplo 1: NF-007 — *Encontro de Correntes* (Human Group / Level 2)

```text
Neurographic flow art illustration for an adult coloring book — Contemplative Figurative identity. Crisp black line art on pure white background.

Subject: Two serene adult figures walking side by side in quiet contemplation across a vast open landscape. 
Structure & Framing: Full-body medium-long shot in profile-three-quarter view, showing a dignified, peaceful walking posture.

Neurographic Integration: Continuous, fluid curving lines emerge from the folds of their garments and footfalls, extending into the ground textures and surrounding horizon, seamlessly connecting both figures through parallel flowing currents.

Composition & Flow: Dynamic diagonal composition with a dominant wavy, converging flow. Primary focal area centered on the two walking figures, balanced by spacious pure white negative space in the upper sky region (30% open space).

Complexity & Usability: Complexity Level 2 (Simple) with low-medium line density. Spacious, clean enclosed cells ideal for smooth coloring. Distinct line weight hierarchy: bold outlines for the figures, medium flowing terrain lines, delicate interior fabric lines. Zero gray lines, zero grayscale shading, zero solid black filled masses.

Negative Constraints: Avoid text, letters, watermark, signature, logo. Avoid character design, cartoon, anime, manga, mascot, cute/kawaii aesthetic, childlike illustration, caricature. Avoid photorealism, 3D render, photographic texture, medical/anatomical diagram. Avoid rigid geometric mandalas, mechanical symmetry, halftone dots, chaotic unreadable clutter.
```

---

### Exemplo 2: NF-012 — *Raízes e Galhos* (Tree / Level 3)

```text
Neurographic flow art illustration for an adult coloring book — Contemplative Figurative identity. Crisp black line art on pure white background.

Subject: A majestic, ancient oak tree with deep subterranean roots and high spreading canopy branches. 
Structure & Framing: Centered vertical full-tree view capturing both the root network below and the crown above in grounded grandeur.

Neurographic Integration: The tree's bark texture, root tendrils, and branch divisions naturally become the organic neurographic line network, spreading outward into the surrounding soil and air in continuous curvilinear paths.

Composition & Flow: Central expansion composition with a dominant descending and centrifugal flow. High density at the root base transitioning to airy, spacious branch divisions at the top, leaving luminous negative space around the canopy edges.

Complexity & Usability: Complexity Level 3 (Intermediate) with medium line density. Well-defined, comfortable coloring cells. Bold structural lines for the main trunk and primary roots, fine delicate lines for foliage clusters and bark details. Zero gray lines, zero grayscale shading, zero solid black filled masses.

Negative Constraints: Avoid text, letters, watermark, signature, logo. Avoid character design, cartoon, anime, manga, mascot, cute/kawaii aesthetic, childlike illustration, caricature. Avoid photorealism, 3D render, photographic texture, medical/anatomical diagram. Avoid rigid geometric mandalas, mechanical symmetry, halftone dots, chaotic unreadable clutter.
```

---

### Exemplo 3: NF-030 — *Pausa* (Object / Level 1)

```text
Neurographic flow art illustration for an adult coloring book — Contemplative Figurative identity. Crisp black line art on pure white background.

Subject: An open book resting calmly on a rustic wooden table beside a window overlooking a quiet garden. 
Structure & Framing: Close-up eye-level perspective focused on the open pages and gentle light cast from the window frame.

Neurographic Integration: Delicate curving neurographic lines emerge from the open book pages and table grain, dissolving softly into the window light and background garden silhouettes in gentle, sweeping arcs.

Composition & Flow: Active edges composition with a dominant centripetal flow, bringing deep focus to the open book while leaving the central page area crisp and light. Generous negative space (over 40% pure white area).

Complexity & Usability: Complexity Level 1 (Introductory) with low line density. Wide, inviting coloring spaces perfect for relaxing, effortless coloring sessions. Clean primary outlines with minimal fine accent lines. Zero gray lines, zero grayscale shading, zero solid black filled masses.

Negative Constraints: Avoid text, letters, watermark, signature, logo. Avoid character design, cartoon, anime, manga, mascot, cute/kawaii aesthetic, childlike illustration, caricature. Avoid photorealism, 3D render, photographic texture, medical/anatomical diagram. Avoid rigid geometric mandalas, mechanical symmetry, halftone dots, chaotic unreadable clutter.
```

---

## 7. REGRAS DE VALIDAÇÃO DO PROMPT (CHECKLIST DE ENGENHARIA)

Antes de aprovar o `SPECIFIC PROMPT` de qualquer ficha `NF-XXX.md`, ele deve ser validado contra os seguintes 6 critérios:

```
[ ] 01. PRESERVAÇÃO DO MASTER PLAN: O motivo principal, modo figurativo e nível de complexidade batem 100% com o illustrations-master.md?
[ ] 02. LINHA PRETA PURA: Exige explicitamente linha 100% preta pura sobre fundo branco puro (zero cinza, zero gradiente)?
[ ] 03. INTEGRAÇÃO ORGÂNICA: As linhas neurográficas brotam da física/anatomia do próprio motivo em vez de parecer um carimbo de fundo?
[ ] 04. PROTEÇÃO ANTI-CHARACTER DESIGN: O prompt bloqueia explicitamente cartoon, anime, manga, mascotes e expressões caricatas?
[ ] 05. RESPIRO CONTEMPLATIVO: Reserva pelo menos 20-30% de espaço negativo em branco puro?
[ ] 06. ESTRUTURA DE 6 BLOCOS: Todos os 6 blocos executáveis estão presentes no idioma inglês?
```

---

## 8. EXEMPLOS DE ERROS E ANTI-PADRÕES A EVITAR

| Anti-padrão | O que ocorre no erro | Por que é inaceitável | Como corrigir na arquitetura |
|:---|:---|:---|:---|
| **Prompt de Abstração Pura** | *"Abstract neurographic line pattern with swirling loops and nodes..."* | Elimina o motivo figurativo reconhecível, violando a fórmula Contemplativo Figurativo. | Incluir obrigatoriamente o Bloco B com o motivo do Master Plan (ex.: figura humana, árvore, animal). |
| **Viés de Character Design** | *"Cute female character with expressive big anime eyes and detailed clothing..."* | Infantiliza o livro e viola a estética adulta sóbria. | Usar o Bloco H (Negative Constraints) e descrever o sujeito no Bloco B como *"serene adult figure in quiet posture"*. |
| **Linhas Neurográficas "Carimbadas"** | *"Drawing of a deer with a neurographic mandala background pattern behind it..."* | Trata a neurografia como papel de parede separado do motivo. | Aplicar o Bloco D: as linhas devem brotar dos galhos, do corpo do animal e do solo, unindo figura e espaço. |
| **Contradição de Complexidade** | Pedir Level 1 (Simples), mas incluir *"intricate microscopic line weaving across every inch"*. | Inviabiliza a coloração e frustra o público iniciante. | Alinhar a densidade do Bloco F com o nível do Master Plan (Level 1 = poucas linhas largas; Level 5 = trama densa). |
| **Excesso de Preto / Shading** | *"Shaded line art with dark heavy black gradients and filled shadows..."* | Estraga a folha de colorir e mancha a impressão KDP. | Exigir no Bloco G: *Zero grayscale shading, zero gradients, pure black lines on white background*. |

---

*Documento criado em: 2026-09-09*  
*Versão: 0.1.0 — Prompt Architecture v0.1*  
*Status: APROVADO PARA SUPORTE AO CHECKPOINT 02*
