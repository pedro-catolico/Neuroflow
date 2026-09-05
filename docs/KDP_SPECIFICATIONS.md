# KDP SPECIFICATIONS
## NEUROFLOW — Especificações Amazon KDP

> **AVISO CRÍTICO:** Este documento registra especificações técnicas do Amazon KDP.
> As especificações KDP **mudam periodicamente**. Antes de gerar o PDF final,
> SEMPRE verificar em fonte oficial: https://kdp.amazon.com/en_US/help/topic/G201834180

---

## 1. STATUS GERAL

| Campo | Status |
|-------|--------|
| Última verificação | **NÃO REALIZADA** |
| Fonte de verificação | A verificar em: https://kdp.amazon.com |
| Responsável | Usuário / Agente (fase KDP) |

> **Nota:** Todas as especificações abaixo são baseadas em conhecimento geral e devem ser
> CONFIRMADAS em fonte oficial antes de uso em produção.

---

## 2. TIPO DE PUBLICAÇÃO

| Campo | Valor | Status |
|-------|-------|--------|
| Tipo | Paperback (Print on Demand) | Confirmado |
| Plataforma | Amazon KDP | Confirmado |
| Categoria | Arts & Photography > Drawing > Coloring Books | A verificar |
| BISAC | A definir | A DEFINIR |

---

## 3. FORMATO DO LIVRO

| Campo | Valor Padrão | Status |
|-------|-------------|--------|
| **Trim size** | A DEFINIR | **PENDENTE** |
| **Orientação** | A DEFINIR | **PENDENTE** |
| **Número de páginas** | A DEFINIR | **PENDENTE** |
| **Tipo de papel** | Branco (white) — recomendado para colorir | A verificar |
| **Acabamento da capa** | Fosco (matte) — recomendado | A verificar |
| **Impressão** | Preto e branco (B&W) | Confirmado conceitual |

### Trim Sizes Comuns para Livros de Colorir (Não Confirmadas)
| Tamanho | Polegadas | Cm | Observação |
|---------|-----------|-----|-----------|
| 8.5 x 11 | 8.5" × 11" | 21.6 × 27.9 cm | Tamanho mais popular para colorir |
| 8 x 10 | 8" × 10" | 20.3 × 25.4 cm | Alternativa popular |
| 8.5 x 8.5 | 8.5" × 8.5" | 21.6 × 21.6 cm | Formato quadrado |

> **Decisão pendente:** Usuário deve escolher o trim size antes do início da diagramação.
> A escolha afeta a proporção das imagens geradas.

---

## 4. ESPECIFICAÇÕES TÉCNICAS DO INTERIOR

> **Status:** Baseadas em conhecimento geral — VERIFICAR antes de usar

| Parâmetro | Valor (Geral) | Status |
|-----------|--------------|--------|
| Resolução mínima | 300 DPI | A verificar |
| Resolução recomendada | 300 DPI | A verificar |
| Formato do arquivo | PDF/X-1a ou PDF | A verificar |
| Espaço de cor | Grayscale ou CMYK | A verificar |
| Tamanho máximo | 650 MB | A verificar |
| Bleed | 0.125" (3.175 mm) | A verificar |
| Margens | Variável por trim size | A verificar |
| Margem interna (lombada) | Variável por nº de páginas | A verificar |
| Fontes | Embutidas | A verificar |

---

## 5. MARGENS (ESTIMATIVAS — NÃO CONFIRMADAS)

Para livros de colorir, recomenda-se margens generosas para evitar que a arte fique muito próxima da lombada.

| Posição | Mínimo Geral | Recomendado (Colorir) | Status |
|---------|-------------|----------------------|--------|
| Interior (lombada) | 0.375" | 0.5"+ | A verificar |
| Exterior | 0.25" | 0.375" | A verificar |
| Superior | 0.25" | 0.375" | A verificar |
| Inferior | 0.25" | 0.375" | A verificar |

> **Nota:** Margens da lombada variam com o número de páginas. KDP fornece tabela específica.

---

## 6. ESPECIFICAÇÕES DA CAPA

> **Status:** Baseadas em conhecimento geral — VERIFICAR antes de usar

| Parâmetro | Valor | Status |
|-----------|-------|--------|
| Formato | PDF | A verificar |
| Resolução | 300 DPI mínimo | A verificar |
| Espaço de cor | RGB ou CMYK | A verificar |
| Bleed | 0.125" em todos os lados | A verificar |
| Template | Gerado pela calculadora KDP | A verificar |

> **Importante:** A calculadora de capa do KDP gera um template com as dimensões exatas
> baseadas no trim size e número de páginas. USAR SEMPRE a calculadora oficial.
> URL: https://kdp.amazon.com/cover-calculator

---

## 7. METADADOS

| Campo | Valor | Status |
|-------|-------|--------|
| **Título** | NEUROFLOW | Confirmado |
| **Subtítulo** | A DEFINIR | **PENDENTE** |
| **Autor** | A DEFINIR | **PENDENTE** |
| **Descrição** | A DEFINIR | **PENDENTE** |
| **Palavras-chave (7)** | A DEFINIR | **PENDENTE** |
| **Categoria principal** | A DEFINIR | **PENDENTE** |
| **Categoria secundária** | A DEFINIR | **PENDENTE** |
| **ISBN** | A DEFINIR | **PENDENTE** |
| **Idioma** | Inglês | Confirmado |
| **País de publicação** | A DEFINIR | **PENDENTE** |
| **Preço** | A DEFINIR | **PENDENTE** |

---

## 8. PALAVRAS-CHAVE (ESTRATÉGIA — A PESQUISAR)

O KDP permite até 7 palavras-chave. Devem ser pesquisadas com base em:
- Termos de busca reais dos compradores
- Concorrência e saturação de mercado
- Volume de busca estimado

**Candidatas (a pesquisar e validar):**
- adult coloring book
- mindfulness coloring
- relaxation coloring
- abstract coloring book
- stress relief coloring
- neurographic art
- meditation coloring

> **Status:** PENDENTE — Pesquisar antes da publicação

---

## 9. ROYALTIES

| Plano | Porcentagem | Condição |
|-------|-------------|---------|
| 60% | 60% do preço de lista menos custo de impressão | Padrão para paperback |

> **Custo de impressão:** Varia por número de páginas, trim size e tipo de papel.
> Calcular com a calculadora de royalties KDP antes de definir o preço.
> URL: https://kdp.amazon.com/help/topic/G201834220

---

## 10. CHECKLIST PRÉ-PUBLICAÇÃO

```
CHECKLIST KDP — NEUROFLOW
==========================

FORMATO
[ ] Trim size confirmado com KDP
[ ] Número de páginas calculado
[ ] Margens verificadas
[ ] Bleed incluído em todos os arquivos

INTERIOR PDF
[ ] Resolução ≥ 300 DPI verificada em todas as imagens
[ ] Espaço de cor correto
[ ] Fontes embutidas (se houver texto)
[ ] Arquivo dentro do limite de tamanho (650 MB)
[ ] Preview visual revisado página por página

CAPA PDF
[ ] Template KDP usado (calculadora oficial)
[ ] Resolução adequada
[ ] Texto da capa revisado
[ ] Spine (lombada) correta para o nº de páginas
[ ] Contracapa com código ISBN (se aplicável)

METADADOS
[ ] Título finalizado
[ ] Subtítulo finalizado
[ ] Descrição escrita e revisada
[ ] 7 palavras-chave definidas e pesquisadas
[ ] Categorias selecionadas
[ ] Preço calculado com royalties

CONFORMIDADE
[ ] Conteúdo revisado para direitos autorais
[ ] Sem personagens protegidos
[ ] Sem marcas registradas
[ ] Declaração de originalidade
```

---

## 11. LINKS OFICIAIS

| Recurso | URL |
|---------|-----|
| KDP Help Center | https://kdp.amazon.com/help |
| Guia de Formatação | https://kdp.amazon.com/en_US/help/topic/G201834180 |
| Calculadora de Capa | https://kdp.amazon.com/cover-calculator |
| Calculadora de Royalties | https://kdp.amazon.com/help/topic/G201834220 |
| Diretrizes de Conteúdo | https://kdp.amazon.com/en_US/help/topic/G200672390 |

---

*Documento criado em: 2026-09-03*  
*Versão: 0.1.0 — Foundation*  
*AVISO: Verificar TODAS as especificações em fonte oficial antes de usar em produção*
