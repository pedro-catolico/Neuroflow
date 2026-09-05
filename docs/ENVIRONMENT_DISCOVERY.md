# ENVIRONMENT DISCOVERY
## Neuroflow — Relatório de Descoberta do Ambiente

**Data:** 2026-09-03  
**Agente:** Antigravity (Google Deepmind)  
**Fase:** Project Foundation

---

## 1. ESTRUTURA EXISTENTE ENCONTRADA

```
Neuroflow/
├── .agent/
│   └── skills/
│       └── code-review-ai-ai-review/
│           └── SKILL.md
├── .agents/
│   └── skills/
│       ├── baoyu-design/
│       │   └── SKILL.md (+ sistema completo)
│       └── release-skills/
│           └── SKILL.md
├── .claude/
│   └── skills/
│       ├── baoyu-design/      (cópia duplicada)
│       └── release-skills/    (cópia duplicada)
└── skills-lock.json
```

### Observação sobre duplicação
As skills `baoyu-design` e `release-skills` estão presentes tanto em `.agents/skills/` quanto em `.claude/skills/`. Isso é esperado: `.agents/skills/` é o caminho para Antigravity/Codex, e `.claude/skills/` é o caminho para Claude Code. O `skills-lock.json` registra a fonte e o hash dessas instalações.

---

## 2. SKILLS INSTALADAS LOCALMENTE

### 2.1 baoyu-design
- **Localização:** `.agents/skills/baoyu-design/` e `.claude/skills/baoyu-design/`
- **Fonte:** GitHub — JimLiu/baoyu-design
- **Finalidade:** Criação de artefatos de design como HTML auto-contido: mockups, protótipos, landing pages, slides, documentos, animações, objetos 3D, diagramas, flyers.
- **Relevância para Neuroflow:** ALTA
- **Como usar:**
  - Direção visual e exploração estética
  - Criação de documentos de referência visual (Style Bible visual, moodboards)
  - Prototipagem de layouts de página
  - Visualização de composições antes da geração final
  - Criação de apresentações e relatórios do projeto
- **Fase da pipeline:** IDEAÇÃO → DIREÇÃO ARTÍSTICA → PLANEJAMENTO → DIAGRAMAÇÃO
- **Uso:** Diretamente, quando for necessário criar artefatos visuais HTML de referência ou protótipos de layout
- **STATUS:** CONFIRMADO

### 2.2 release-skills
- **Localização:** `.agents/skills/release-skills/` e `.claude/skills/release-skills/`
- **Fonte:** GitHub — JimLiu/baoyu-design (repositório)
- **Finalidade:** Workflow universal de release — detecta arquivos de versão, gera changelogs multilíngues, cria tags annotated, publica GitHub Releases.
- **Relevância para Neuroflow:** BAIXA (fase futura)
- **Como usar:** Versionamento do projeto quando houver releases estruturadas
- **Fase da pipeline:** PREPARAÇÃO KDP (empacotamento final)
- **Uso:** Apenas quando o projeto atingir maturidade suficiente para releases formais
- **STATUS:** CONFIRMADO

### 2.3 code-review-ai-ai-review
- **Localização:** `.agent/skills/code-review-ai-ai-review/`
- **Finalidade:** Revisão de código com análise estática multi-ferramenta (SonarQube, CodeQL, Semgrep) e LLMs. Suporta 30+ linguagens e integração CI/CD.
- **Relevância para Neuroflow:** MÉDIA (fase de scripts)
- **Como usar:** Revisão de scripts Python de automação (processamento de imagens, geração de PDF, QA)
- **Fase da pipeline:** AUTOMAÇÃO → QA TÉCNICO
- **Uso:** Como referência para boas práticas ao escrever scripts de automação
- **STATUS:** CONFIRMADO

---

## 3. SKILLS DO AMBIENTE GLOBAL ANTIGRAVITY

### 3.1 antigravity-guide
- **Localização:** Builtin — Antigravity IDE
- **Finalidade:** Guia e referência completa do ecossistema Antigravity (CLI agy, IDE, SDK Python, slash commands, keybindings, customizações).
- **Relevância para Neuroflow:** MÉDIA
- **Como usar:** Compreender o ambiente de execução, configurar agentes, entender limitações
- **Fase da pipeline:** FOUNDATION (configuração inicial)
- **Uso:** Referência durante configuração e desenvolvimento da pipeline
- **STATUS:** CONFIRMADO

### 3.2 agy-customizations
- **Localização:** Builtin — Antigravity IDE
- **Finalidade:** Sistema de customização do Antigravity — Skills, Rules, Plugins, Hooks, MCP Servers.
- **Relevância para Neuroflow:** ALTA
- **Como usar:**
  - Criar regras específicas do projeto (GEMINI.md ou .agents/rules/)
  - Configurar comportamento dos agentes para tarefas artísticas
  - Potencial criação de skill própria para o Neuroflow
- **Fase da pipeline:** FOUNDATION
- **Uso:** Para estruturar a eventual skill NEUROFLOW PRODUCTION
- **STATUS:** CONFIRMADO
- **Descoberta importante:** Skills podem ser instaladas em:
  - Local (projeto): `.agents/skills/`
  - Global (máquina): `~/.gemini/config/skills/`

### 3.3 workflow-skill-creator
- **Localização:** Plugin science — global
- **Finalidade:** Destila um workflow existente em uma skill reutilizável. Requer workflow já existente como base (não cria do zero).
- **Relevância para Neuroflow:** ALTA (fase futura)
- **Como usar:** Após executar manualmente o workflow de produção uma vez, usar esta skill para formalizar e empacotar como NEUROFLOW PRODUCTION skill
- **Fase da pipeline:** Após STYLE TEST (quando o workflow estiver validado)
- **Uso:** FUTURO — não agora
- **Limitação identificada:** Exige workflow existente como base. NÃO pode criar skill antes de executar o workflow real.
- **STATUS:** CONFIRMADO

---

## 4. SKILLS IRRELEVANTES PARA O NEUROFLOW

As seguintes skills do ambiente global pertencem ao plugin `science` e são voltadas exclusivamente para pesquisa biomédica, bioinformática e ciências da vida:

| Skill | Domínio | Razão da Irrelevância |
|-------|---------|----------------------|
| alphafold-database-fetch-and-analyze | Bioinformática | Estruturas de proteínas |
| alphagenome-single-variant-analysis | Genômica | Variantes genéticas |
| chembl-database | Química | Moléculas bioativas |
| clinical-trials-database | Medicina | Ensaios clínicos |
| clinvar-database | Genômica | Variantes clínicas |
| dbsnp-database | Genômica | SNPs |
| embl-ebi-ols | Ontologia | Termos biomédicos |
| encode-ccres-database | Genômica | Regulação genômica |
| ensembl-database | Genômica | Genes/transcritos |
| foldseek-structural-search | Bioinformática | Estruturas 3D de proteínas |
| gnomad-database | Genômica | Frequência de variantes |
| gtex-database | Genômica | Expressão de genes |
| human-protein-atlas-database | Proteômica | Atlas de proteínas |
| interpro-database | Proteômica | Domínios de proteínas |
| jaspar-database | Genômica | Fatores de transcrição |
| literature-search-arxiv | Literatura | Papers científicos |
| literature-search-biorxiv | Literatura | Preprints de biologia |
| literature-search-europepmc | Literatura | Literatura médica |
| literature-search-openalex | Literatura | Pesquisa acadêmica |
| ncbi-sequence-fetch | Bioinformática | Sequências NCBI |
| openfda-database | Medicina | Dados FDA |
| opentargets-database | Farmacologia | Alvos terapêuticos |
| pdb-database | Bioinformática | Estruturas 3D |
| protein-sequence-msa | Bioinformática | Alinhamento de sequências |
| protein-sequence-similarity-search | Bioinformática | Similaridade de proteínas |
| pubchem-database | Química | Compostos químicos |
| pubmed-database | Literatura | Literatura médica |
| pymol | Bioinformática | Visualização molecular |
| quickgo-database | Ontologia | Gene Ontology |
| reactome-database | Bioinformática | Vias metabólicas |
| string-database | Bioinformática | Interações proteína-proteína |
| ucsc-conservation-and-tfbs | Genômica | Conservação evolutiva |
| unibind-database | Genômica | Sítios de ligação |
| uniprot-database | Proteômica | Banco de proteínas |

**Conclusão:** Nenhuma dessas skills possui qualquer relevância para a produção editorial de um livro adulto de colorir. Não devem ser incorporadas à pipeline do Neuroflow.

Também são irrelevantes:
- **uv** — Gerenciador Python. Potencialmente útil apenas se a pipeline usar Python extensivamente (fase futura)
- **android-cli** — Desenvolvimento Android. Irrelevante.
- **science-skills-common / scienceskillscommon** — Biblioteca compartilhada do plugin science. Irrelevante.

---

## 5. AGENTES ENCONTRADOS

Nenhum agente personalizado foi encontrado nas pastas `.agent/` e `.agents/`. Ambas as pastas contêm apenas a subpasta `skills/`. Não existem arquivos de definição de agentes.

**Conclusão:** O projeto não possui agentes customizados atualmente. A arquitetura de agentes está por ser definida.

---

## 6. CONFIGURAÇÕES ENCONTRADAS

### skills-lock.json
```json
{
  "version": 1,
  "skills": {
    "baoyu-design": {
      "source": "JimLiu/baoyu-design",
      "sourceType": "github",
      "skillPath": "skills/baoyu-design/SKILL.md",
      "computedHash": "e7c6e6815fbd359967c5cac0eae78a23b34e720240348739ce86c678c51b780e"
    },
    "release-skills": {
      "source": "JimLiu/baoyu-design",
      "sourceType": "github",
      "skillPath": ".claude/skills/release-skills/SKILL.md",
      "computedHash": "5409cb532b40552f455827f69938193f6b3f3b7e853565e816eee4fa147ab8c7"
    }
  }
}
```

**Observação:** O arquivo `skills-lock.json` está na raiz do projeto, mas deveria estar em `.agents/` para o Antigravity. Isso é normal — pode ser um artefato da instalação via CLI.

---

## 7. FERRAMENTAS POTENCIALMENTE ÚTEIS

| Ferramenta | Uso Potencial | Fase |
|-----------|---------------|------|
| `generate_image` (nativa AGY) | Geração das ilustrações | GERAÇÃO DE IMAGENS |
| `baoyu-design` | Direção visual, protótipos, documentos | IDEAÇÃO, PLANEJAMENTO, DIAGRAMAÇÃO |
| `code-review-ai-ai-review` | Revisão de scripts Python | AUTOMAÇÃO |
| `release-skills` | Versionamento e empacotamento | PREPARAÇÃO KDP |
| `workflow-skill-creator` | Criação de skill NEUROFLOW PRODUCTION | Pós-Style-Test |
| Python + Pillow/PIL | Processamento de imagens, conversão grayscale | TRATAMENTO GRAYSCALE |
| Python + ReportLab/fpdf2 | Geração de PDF | DIAGRAMAÇÃO |
| Python + uv | Gerenciamento de dependências Python | AUTOMAÇÃO |

---

## 8. LIMITAÇÕES IDENTIFICADAS

1. **Geração de imagens:** A ferramenta `generate_image` do Antigravity usa o modelo Gemini. A qualidade e consistência para ilustrações de livros adultos de colorir precisam ser validadas no Style Test antes da produção em escala.

2. **Consistência visual entre imagens:** Não há garantia de que imagens geradas separadamente manterão estilo visual consistente. O sistema de prompts (MASTER_PROMPT + STYLE_PROMPT) é crítico para mitigar isso.

3. **Sem agentes especializados:** Atualmente não existem agentes customizados. Toda execução será pelo agente principal.

4. **workflow-skill-creator:** Não pode ser usado agora. Exige um workflow já executado como base.

5. **Processamento Python:** Se scripts Python forem necessários, precisarão ser desenvolvidos e testados separadamente. uv não está instalado — verificar quando necessário.

6. **Sem controle de versão ativo:** Não foi detectado repositório Git inicializado. Release-skills depende de Git.

7. **KDP:** Especificações do Amazon KDP devem ser verificadas em fonte oficial antes de comprometer o formato final (trim size, resolução, bleed).

---

## 9. RECOMENDAÇÕES ARQUITETURAIS

### 9.1 Estrutura de Pastas
Manter a estrutura proposta no briefing. É modular, clara e escalável. Adaptações menores foram feitas:
- `art/qa/` adicionada para rastreamento de QA visual por imagem
- Separação clara entre `art/` (trabalho) e `output/` (exportação)

### 9.2 Sistema de Prompts
Centralizar no `MASTER_PROMPT.md` a identidade visual estável. Derivar todos os prompts individuais deste documento. Isso é crítico para consistência.

### 9.3 Rastreabilidade
Todo arquivo gerado deve seguir a convenção `NF-XXX`. Nunca usar nomes gerados automaticamente pelo sistema.

### 9.4 Python
Adiar decisão sobre Python até que haja necessidade real. Quando for necessário, usar `uv` para ambientes reproduzíveis.

### 9.5 Agentes
Por ora, um único agente (o principal) é suficiente. A criação de agentes especializados só faz sentido quando os workflows estiverem bem definidos e testados.

### 9.6 Skill Própria
Ver `docs/WORKFLOW_SKILL_ANALYSIS.md` para análise detalhada.

---

## 10. JUSTIFICATIVAS DE ADAPTAÇÕES ARQUITETURAIS

Nenhuma alteração significativa foi necessária em relação à estrutura proposta. A arquitetura planejada é adequada para os objetivos do projeto.

A única observação é que `art/qa/` foi adicionada implicitamente — imagens em QA precisam de uma área de trabalho separada de `art/final/`.

---

*Documento criado em: 2026-09-03*  
*Próxima revisão: Após Style Test*
