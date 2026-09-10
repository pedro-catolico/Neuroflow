import os
import glob
import re
import json

prompts_dir = r'art/prompts/illustration-prompts'
files = sorted(glob.glob(os.path.join(prompts_dir, 'NF-[0-9][0-9][0-9].md')))

# Ground truth from Master Plan
MASTER_PLAN = {
    "NF-001": {"titulo": "Primeira Onda", "motivo": "Animal", "modo": "animal contemplativo", "funcao": "serenity & fluid grace", "level": "Level 2", "composicao": "Fluxo lateral", "fluxo": "Ondular", "densidade": "Média", "conceito": "Duas baleias jubarte deslizando em mar calmo, onde as ondas e o ar se fundem em linhas orgânicas fluídas"},
    "NF-002": {"titulo": "Nó de Conexão", "motivo": "Flora", "modo": "natureza protagonista", "funcao": "growth & emergence", "level": "Level 3", "composicao": "Expansão central", "fluxo": "Radial", "densidade": "Média", "conceito": "Flor de lótus desabrochando com hastes e pétalas que se ramificam em redes neurográficas aquáticas"},
    "NF-003": {"titulo": "Respiração Expandida", "motivo": "Human Female", "modo": "protagonista humano", "funcao": "presence & mindfulness", "level": "Level 4", "composicao": "Expansão central (invertida — densa nas bordas, leve no centro)", "fluxo": "Centrípeto", "densidade": "Alta nas bordas, espaço em branco no centro", "conceito": "Figura humana feminina em postura de respiração consciente, com linhas fluídas de expiração circulando ao seu redor"},
    "NF-004": {"titulo": "Tecido de Neurônios", "motivo": "Symbolic Composition", "modo": "composição simbólica", "funcao": "wonder & deep focus", "level": "Level 5", "composicao": "Rede distribuída", "fluxo": "Radial (múltiplos focos)", "densidade": "Média-Alta a Alta", "conceito": "Composição simbólica de linhas de pensamento e pontes orgânicas entrelaçadas em arcos fluídos e constelações poéticas"},
    "NF-005": {"titulo": "Fluxo Suave", "motivo": "Landscape", "modo": "ambiente protagonista", "funcao": "quietude & expansão", "level": "Level 1", "composicao": "Fluxo lateral", "fluxo": "Ondular", "densidade": "Baixa", "conceito": "Dunas de areia e horizonte desértico suave sob luz limpa, com linhas esparsas e amplo espaço em branco"},
    "NF-006": {"titulo": "Espiral Aberta", "motivo": "Human Male", "modo": "protagonista humano", "funcao": "introspection & perspective", "level": "Level 3", "composicao": "Espiral orgânica", "fluxo": "Espiral (centrífugo)", "densidade": "Média (aumentando nas bordas)", "conceito": "Figura humana masculina sentada em postura de observação contemplativa do céu estrelado"},
    "NF-007": {"titulo": "Encontro de Correntes", "motivo": "Human Group", "modo": "composição híbrida", "funcao": "connection & harmony", "level": "Level 2", "composicao": "Diagonal dinâmica", "fluxo": "Ondular (duas direções convergindo)", "densidade": "Média-Baixa", "conceito": "Duas pessoas caminhando silenciosamente em terreno plano cujas sombras e vestimentas convergem em fluxo"},
    "NF-008": {"titulo": "Campo de Forças", "motivo": "Object", "modo": "objeto protagonista", "funcao": "balance & tension", "level": "Level 4", "composicao": "Campo denso", "fluxo": "Radial (múltiplos)", "densidade": "Média-Alta", "conceito": "Pêndulo e pedras suspensas em arranjo zen cercados por linhas de atração gravitacional e magnética"},
    "NF-009": {"titulo": "Semente de Luz", "motivo": "Human Female", "modo": "protagonista humano", "funcao": "renewal & hope", "level": "Level 2", "composicao": "Expansão central", "fluxo": "Centrífugo", "densidade": "Baixa no centro, aumentando para as bordas", "conceito": "Figura feminina segurando delicadamente uma semente luminosa da qual emergem ramificações de vida"},
    "NF-010": {"titulo": "Labirinto Orgânico", "motivo": "Architecture", "modo": "ambiente protagonista", "funcao": "refuge & discovery", "level": "Level 3", "composicao": "Campo denso", "fluxo": "Ondular (multiple)", "densidade": "Média", "conceito": "Jardim meditativo com caminhos curvos de pedra e pórtico de madeira integrados à vegetação fluída"},
    "NF-011": {"titulo": "Vórtice Suave", "motivo": "Human Male", "modo": "protagonista humano", "funcao": "stillness & absorption", "level": "Level 3", "composicao": "Espiral orgânica (centrípeta)", "fluxo": "Centrípeto", "densidade": "Baixa-Média no centro, alta nas bordas", "conceito": "Figura humana masculina caminhando lentamente por um corredor de bambus cujos topos se curvam num vórtice"},
    "NF-012": {"titulo": "Raízes e Galhos", "motivo": "Tree", "modo": "natureza protagonista", "funcao": "grounding & stability", "level": "Level 3", "composicao": "Expansão central (árvore invertida)", "fluxo": "Descendente", "densidade": "Alta na base, baixa no topo", "conceito": "Carvalho ancestral cujas raízes subterrâneas e galhos altos estendem-se em ramificações neurográficas"},
    "NF-013": {"titulo": "Ondas Sobrepostas", "motivo": "Water", "modo": "ambiente protagonista", "funcao": "rhythm & tranquility", "level": "Level 2", "composicao": "Fluxo lateral", "fluxo": "Ondular", "densidade": "Baixa-Média", "conceito": "Ondas do mar encontrando formações rochosas costeiras em camadas rítmicas fluídas"},
    "NF-014": {"titulo": "Colisão e Harmonia", "motivo": "Human Group", "modo": "composição híbrida", "funcao": "connection & catharsis", "level": "Level 4", "composicao": "Diagonal dinâmica", "fluxo": "Radial (dois focos opostos)", "densidade": "Alta no centro, diminuindo para as bordas", "conceito": "Duas mãos humanas aproximando-se no momento anterior ao toque, cercadas por ondas fluídas de energia"},
    "NF-015": {"titulo": "Micro-Universo", "motivo": "Symbolic Composition", "modo": "composição simbólica", "funcao": "wonder & intricate focus", "level": "Level 5", "composicao": "Rede distribuída", "fluxo": "Radial (múltiplos focos)", "densidade": "Muito Alta", "conceito": "Estrutura microbiótica e marinha de corais entrelaçados revelando detalhes minuciosos"},
    "NF-016": {"titulo": "Silêncio", "motivo": "Animal", "modo": "animal contemplativo", "funcao": "solitude & peace", "level": "Level 1", "composicao": "Bordas ativas (centro vazio)", "fluxo": "Centrípeto", "densidade": "Muito baixa", "conceito": "Garça solitária alçando vôo sereno sobre um lago calmo ao amanhecer"},
    "NF-017": {"titulo": "Transição", "motivo": "Landscape", "modo": "ambiente protagonista", "funcao": "transformation & passage", "level": "Level 3", "composicao": "Diagonal dinâmica", "fluxo": "Lateral + transformação", "densidade": "Baixa → Alta (esquerda para direita)", "conceito": "Cordilheira de montanhas ao amanhecer transformando-se de relevo suave em vales arborizados"},
    "NF-018": {"titulo": "Célula em Expansão", "motivo": "Human Female", "modo": "protagonista humano", "funcao": "refuge & protection", "level": "Level 3", "composicao": "Expansão central", "fluxo": "Centrífugo", "densidade": "Média no centro, baixa fora", "conceito": "Figura humana feminina sentada em contemplação acolhida sob uma abóbada natural de trepadeiras e salgueiros que se abrem"},
    "NF-019": {"titulo": "Murmúrio", "motivo": "Flora", "modo": "natureza protagonista", "funcao": "delicate serenity", "level": "Level 4", "composicao": "Campo denso", "fluxo": "Ondular", "densidade": "Média-Alta (linhas finas)", "conceito": "Campo de lavandas e gramíneas altas ondulando suavemente sob a brisa do entardecer"},
    "NF-020": {"titulo": "Correntes Cruzadas", "motivo": "Architecture", "modo": "objeto protagonista", "funcao": "passage & harmony", "level": "Level 3", "composicao": "Campo denso", "fluxo": "Radial (múltiplos)", "densidade": "Média", "conceito": "Ponte de pedra antiga cruzando riacho sinuoso em floresta temperada"},
    "NF-021": {"titulo": "Arquipélago", "motivo": "Animal", "modo": "animal contemplativo", "funcao": "lightness & freedom", "level": "Level 2", "composicao": "Contraste de escala", "fluxo": "Radial (distribuído)", "densidade": "Baixa-Média", "conceito": "Bando de pássaros flutuando em vôo sereno sobre ilhas distantes no oceano"},
    "NF-022": {"titulo": "Grande Espiral", "motivo": "Tree", "modo": "natureza protagonista", "funcao": "grandiosity & connection", "level": "Level 5", "composicao": "Espiral orgânica", "fluxo": "Espiral", "densidade": "Média a Alta", "conceito": "Oliveira milenar ancestral vista em perspectiva ascendente (contra-plongée) cujos galhos e tronco retorcidos formam espiral expansiva"},
    "NF-023": {"titulo": "Tecido Vivo", "motivo": "Flora", "modo": "natureza protagonista", "funcao": "tactile immersion", "level": "Level 3", "composicao": "Campo denso", "fluxo": "Ondular", "densidade": "Média", "conceito": "Folhagem tropical e samambaias sobrepostas cujas nervuras criam uma textura viva"},
    "NF-024": {"titulo": "Ponto de Equilíbrio", "motivo": "Object", "modo": "objeto protagonista", "funcao": "balance & simplicity", "level": "Level 3", "composicao": "Contraste de escala", "fluxo": "Radial", "densidade": "Média", "conceito": "Arranjo Ikebana com vaso cerâmico, galho curvo e flor em broto em composição equilibrada"},
    "NF-025": {"titulo": "Fluxo Ascendente", "motivo": "Human Male", "modo": "protagonista humano", "funcao": "elevation & aspiration", "level": "Level 2", "composicao": "Diagonal dinâmica (vertical)", "fluxo": "Ascendente", "densidade": "Baixa embaixo, aumentando no topo", "conceito": "Figura masculina em pé na praia observando a lua cheia subir sobre o horizonte marinho"},
    "NF-026": {"titulo": "Densa Calma", "motivo": "Symbolic Composition", "modo": "composição simbólica", "funcao": "deep meditation", "level": "Level 4", "composicao": "Campo denso", "fluxo": "Ondular", "densidade": "Alta", "conceito": "Composição simbólica de pétalas e folhas em deriva assimétrica fluida sobre a água"},
    "NF-027": {"titulo": "Nó Expandido", "motivo": "Human Female", "modo": "protagonista humano", "funcao": "release & freedom", "level": "Level 4", "composicao": "Expansão central", "fluxo": "Centrífugo", "densidade": "Baixa no centro, crescente para as bordas", "conceito": "Figura feminina desatando suavemente uma fita fluida em suas mãos"},
    "NF-028": {"titulo": "Dispersão", "motivo": "Animal", "modo": "animal contemplativo", "funcao": "presence & wild grace", "level": "Level 3", "composicao": "Expansão central (desestruturada)", "fluxo": "Centrífugo (irregular)", "densidade": "Alta no centro, baixa nas bordas", "conceito": "Cervo solitário parado em clareira na floresta sob névoa matutina"},
    "NF-029": {"titulo": "Interligações", "motivo": "Symbolic Composition", "modo": "composição simbólica", "funcao": "intellectual stimulation", "level": "Level 4", "composicao": "Rede distribuída", "fluxo": "Radial (múltiplos focos)", "densidade": "Média-Alta", "conceito": "Composição simbólica de constelação de formas orgânicas geométricas fluidas interconectadas"},
    "NF-030": {"titulo": "Pausa", "motivo": "Object", "modo": "objeto protagonista", "funcao": "quietude & solitude", "level": "Level 1", "composicao": "Bordas ativas", "fluxo": "Centrípeto", "densidade": "Muito baixa", "conceito": "Livro aberto repousando sobre mesa de madeira ao lado de janela com vista para jardim"},
    "NF-031": {"titulo": "Território", "motivo": "Flora", "modo": "natureza protagonista", "funcao": "grounding & patience", "level": "Level 3", "composicao": "Campo denso", "fluxo": "Ondular", "densidade": "Média-Alta", "conceito": "Líquens e musgos cobrindo rochas antigas à beira de um lago sereno"},
    "NF-032": {"titulo": "Confluência", "motivo": "Human Group", "modo": "composição híbrida", "funcao": "shared silence & connection", "level": "Level 4", "composicao": "Diagonal dinâmica", "fluxo": "Ondular", "densidade": "Média", "conceito": "Duas pessoas sentadas lado a lado em falésia observando o por do sol no oceano"},
    "NF-033": {"titulo": "Expansão Suave", "motivo": "Human Female", "modo": "protagonista humano", "funcao": "freedom & openness", "level": "Level 2", "composicao": "Expansão central", "fluxo": "Centrífugo", "densidade": "Baixa-Média", "conceito": "Figura feminina de costas abrindo os braços no topo de um morro ao vento"},
    "NF-034": {"titulo": "Profundidade", "motivo": "Tree", "modo": "ambiente protagonista", "funcao": "immersion & mystery", "level": "Level 5", "composicao": "Rede distribuída", "fluxo": "Vertical + ondulante", "densidade": "Alta", "conceito": "Floresta densa de pinheiros com caminho sinuoso no fundo do vale sob luz de névoa"},
    "NF-035": {"titulo": "Ritmo Constante", "motivo": "Architecture", "modo": "objeto protagonista", "funcao": "perseverance & journey", "level": "Level 3", "composicao": "Fluxo lateral", "fluxo": "Ondular", "densidade": "Média", "conceito": "Escadaria de pedra antiga serpenteando por encosta florida e portões de ferro trabalhado"},
    "NF-036": {"titulo": "Limiar", "motivo": "Human Male", "modo": "protagonista humano", "funcao": "transition & choice", "level": "Level 2", "composicao": "Bordas ativas", "fluxo": "Vertical", "densidade": "Baixa-Média", "conceito": "Figura masculina parada no limiar do portal de um templo de madeira observando a chuva cair"},
    "NF-037": {"titulo": "Nebulosa", "motivo": "Tree", "modo": "natureza protagonista", "funcao": "impermanence & wonder", "level": "Level 4", "composicao": "Campo denso", "fluxo": "Radial", "densidade": "Média-Alta", "conceito": "Copa de ipê em flor cujas pétalas flutuam suavemente no ar ao vento"},
    "NF-038": {"titulo": "Pulsação", "motivo": "Animal", "modo": "animal contemplativo", "funcao": "harmony & serenity", "level": "Level 3", "composicao": "Espiral orgânica", "fluxo": "Centrípeto", "densidade": "Média", "conceito": "Par de cisnes deslizando em águas calmas formando círculos de marola ao seu redor"},
    "NF-039": {"titulo": "Transformação", "motivo": "Landscape", "modo": "ambiente protagonista", "funcao": "renewal & vitality", "level": "Level 4", "composicao": "Diagonal dinâmica", "fluxo": "Descendente + ondular", "densidade": "Média-Alta", "conceito": "Cachoeira serena caindo entre pedras e desaguando em poço natural cristalino"},
    "NF-040": {"titulo": "Repouso", "motivo": "Landscape", "modo": "ambiente protagonista", "funcao": "peace & stillness", "level": "Level 2", "composicao": "Fluxo lateral", "fluxo": "Ondular", "densidade": "Baixa-Média", "conceito": "Lago alpino à noite com reflexo suave das estrelas e montanhas nas águas imóveis"},
    "NF-041": {"titulo": "Síntese", "motivo": "Human Female", "modo": "protagonista humano", "funcao": "integration & wholeness", "level": "Level 4", "composicao": "Expansão central", "fluxo": "Radial / centrífugo", "densidade": "Média-Alta", "conceito": "Figura feminina sentada em meditação à margem de um lago sereno cercada por flores de lótus em escala natural"},
    "NF-042": {"titulo": "O Grande Fluxo", "motivo": "Tree", "modo": "natureza protagonista", "funcao": "universality & connection", "level": "Level 5", "composicao": "Espiral orgânica", "fluxo": "Espiral", "densidade": "Alta", "conceito": "Árvore universal majestosa cujas raízes e copa envolvem toda a página em movimento espiral"},
    "NF-043": {"titulo": "Momento", "motivo": "Human Female", "modo": "protagonista humano", "funcao": "pure presence & quietude", "level": "Level 1", "composicao": "Bordas ativas", "fluxo": "Centrípeto / ondulante", "densidade": "Muito baixa", "conceito": "Perfil sereno de rosto feminino com olhos fechados sentindo a brisa suave passar"},
    "NF-044": {"titulo": "Infinito", "motivo": "Flora", "modo": "natureza protagonista", "funcao": "joy & expansion", "level": "Level 3", "composicao": "Campo denso", "fluxo": "Radial (multiple)", "densidade": "Média-Alta", "conceito": "Campo expansivo de girassóis sob o sol da tarde com miolos e pétalas em ritmo contínuo"},
    "NF-045": {"titulo": "Retorno", "motivo": "Architecture", "modo": "objeto protagonista", "funcao": "homecoming & peace", "level": "Level 3", "composicao": "Fluxo lateral", "fluxo": "Ondular", "densidade": "Média", "conceito": "Varanda de casa de campo com cadeira de balanço e trepadeira florida abrindo vista para o por do sol"},
}

results = {}

for f in files:
    nf_id = os.path.basename(f).replace('.md', '')
    with open(f, 'r', encoding='utf-8', errors='replace') as fp:
        content = fp.read()

    mp = MASTER_PLAN.get(nf_id, {})
    
    def extract(pattern, text):
        m = re.search(pattern, text)
        return m.group(1).strip() if m else 'NOT FOUND'

    titulo = extract(r'\*\*Título\*\*\s*\|\s*([^\|\n]+)', content)
    motivo = extract(r'\*\*Motivo Principal\*\*\s*\|\s*([^\|\n]+)', content)
    level = extract(r'\*\*Complexidade\*\*\s*\|\s*([^\|\n]+)', content)
    comp = extract(r'\*\*Composição\*\*\s*\|\s*([^\|\n]+)', content)
    fluxo = extract(r'\*\*Fluxo\*\*\s*\|\s*([^\|\n]+)', content)
    dens = extract(r'\*\*Densidade\*\*\s*\|\s*([^\|\n]+)', content)
    func = extract(r'\*\*Função Contemplativa\*\*\s*\|\s*([^\|\n]+)', content)
    modo = extract(r'\*\*Modo Figurativo\*\*\s*\|\s*([^\|\n]+)', content)
    neuro = extract(r'\*\*Integração Neurográfica\*\*\s*\|\s*([^\|\n]+)', content)
    densfig = extract(r'\*\*Densidade Figurativa\*\*\s*\|\s*([^\|\n]+)', content)
    tonal = extract(r'\*\*Tonal\*\*\s*\|\s*([^\|\n]+)', content)
    exp = extract(r'\*\*Experiência\*\*\s*\|\s*([^\|\n]+)', content)
    conc = extract(r'\*\*Conceito\*\*\s*\|\s*([^\|\n]+)', content)
    arch = extract(r'\*\*PROMPT_ARCHITECTURE_VERSION\*\*\s*\|\s*([^\|\n]+)', content)
    mp_ver = extract(r'\*\*MASTER_PROMPT_VERSION\*\*\s*\|\s*([^\|\n]+)', content)
    sp_ver = extract(r'\*\*STYLE_PROMPT_VERSION\*\*\s*\|\s*([^\|\n]+)', content)
    np_ver = extract(r'\*\*NEGATIVE_PROMPT_VERSION\*\*\s*\|\s*([^\|\n]+)', content)

    # Block checks
    block_a = 'BLOCK A' in content
    block_b = 'BLOCK B' in content
    block_c = 'BLOCK C' in content  
    block_d = 'BLOCK D' in content
    block_e = 'BLOCK E' in content
    block_f = 'BLOCK F' in content
    block_g = 'BLOCK G' in content
    block_h = 'BLOCK H' in content
    has_exec = '## 4. EXECUTABLE SPECIFIC PROMPT' in content
    has_gen_hist = '## 5. GENERATION HISTORY' in content
    has_qa_ref = '## 6. SELECTED GENERATION' in content
    has_notes = '## 7. MODIFICATIONS' in content

    # Special flag checks
    has_fairy = 'fairy' in content.lower()
    has_magical_cocoon = 'magical cocoon' in content.lower()
    has_casulo_fantasy = 'casulo' in content.lower() and ('magic' in content.lower() or 'fantasy' in content.lower() or 'fairy' in content.lower())
    has_casulo_residual = 'casulo' in content.lower()  # flag but need context
    has_sacred_geo = 'sacred geometry' in content.lower() or 'geometria sagrada' in content.lower()
    has_sci_anatomy = any(x in content.lower() for x in ['brain scan', 'anatomical cross-section', 'histolog', 'neuron diagram', 'anatomical brain'])
    has_concentric_mandala = 'concentric mandala' in content.lower() or 'mandala' in content.lower()

    # Divergences
    divs = []
    if mp:
        if titulo != mp['titulo']:
            divs.append(f"TITULO: prompt='{titulo}' master='{mp['titulo']}'")
        if motivo != mp['motivo']:
            divs.append(f"MOTIVO: prompt='{motivo}' master='{mp['motivo']}'")
        if level != mp['level']:
            divs.append(f"LEVEL: prompt='{level}' master='{mp['level']}'")
        if comp != mp['composicao']:
            divs.append(f"COMP: prompt='{comp}' master='{mp['composicao']}'")
        if fluxo != mp['fluxo']:
            divs.append(f"FLUXO: prompt='{fluxo}' master='{mp['fluxo']}'")
        if dens != mp['densidade']:
            divs.append(f"DENS: prompt='{dens}' master='{mp['densidade']}'")
        if func != mp['funcao']:
            divs.append(f"FUNC: prompt='{func}' master='{mp['funcao']}'")
        if modo != mp['modo']:
            divs.append(f"MODO: prompt='{modo}' master='{mp['modo']}'")

    flags = []
    if has_fairy: flags.append('FAIRY_LANGUAGE')
    if has_magical_cocoon: flags.append('MAGICAL_COCOON')
    if has_casulo_fantasy: flags.append('CASULO+FANTASY')
    if has_casulo_residual: flags.append('CASULO_RESIDUAL')
    if has_sacred_geo: flags.append('SACRED_GEOMETRY')
    if has_sci_anatomy: flags.append('SCIENTIFIC_ANATOMY')
    if has_concentric_mandala: flags.append('MANDALA_LANGUAGE')

    results[nf_id] = {
        'titulo': titulo,
        'motivo': motivo,
        'level': level,
        'comp': comp,
        'fluxo': fluxo,
        'dens': dens,
        'func': func,
        'modo': modo,
        'neuro': neuro,
        'densfig': densfig,
        'tonal': tonal,
        'exp': exp,
        'conc': conc,
        'arch': arch,
        'mp_ver': mp_ver,
        'sp_ver': sp_ver,
        'np_ver': np_ver,
        'blocks': {
            'A': block_a, 'B': block_b, 'C': block_c,
            'D': block_d, 'E': block_e, 'F': block_f,
            'G': block_g, 'H': block_h
        },
        'has_exec': has_exec,
        'has_gen_hist': has_gen_hist,
        'has_qa_ref': has_qa_ref,
        'has_notes': has_notes,
        'divergences': divs,
        'flags': flags,
    }

with open('scratch/audit_results.json', 'w', encoding='utf-8') as fp:
    json.dump(results, fp, ensure_ascii=False, indent=2)

print("Audit results saved to scratch/audit_results.json")
print(f"Total prompts audited: {len(results)}")

# Quick summary
total_with_divs = sum(1 for v in results.values() if v['divergences'])
total_with_flags = sum(1 for v in results.values() if v['flags'])
all_blocks_ok = sum(1 for v in results.values() if all(v['blocks'].values()))
has_exec_count = sum(1 for v in results.values() if v['has_exec'])

print(f"Prompts with divergences: {total_with_divs}")
print(f"Prompts with special flags: {total_with_flags}")
print(f"Prompts with all blocks OK: {all_blocks_ok}")
print(f"Prompts with executable prompt: {has_exec_count}")

print("\n--- DIVERGENCES ---")
for nf_id, data in results.items():
    if data['divergences']:
        print(f"{nf_id}: {data['divergences']}")

print("\n--- FLAGS ---")
for nf_id, data in results.items():
    if data['flags']:
        print(f"{nf_id}: {data['flags']}")

print("\n--- BLOCKS STATUS ---")
for nf_id, data in results.items():
    missing = [k for k, v in data['blocks'].items() if not v]
    if missing:
        print(f"{nf_id}: MISSING BLOCKS {missing}")
    
print("\n--- VERSION CHECK ---")
for nf_id, data in results.items():
    issues = []
    if data['arch'] != '0.1': issues.append(f"ARCH={data['arch']}")
    if data['mp_ver'] != '0.2.1': issues.append(f"MP_VER={data['mp_ver']}")
    if data['sp_ver'] != '0.2.1': issues.append(f"SP_VER={data['sp_ver']}")
    if data['np_ver'] != '0.2.1': issues.append(f"NP_VER={data['np_ver']}")
    if issues:
        print(f"{nf_id}: {issues}")
