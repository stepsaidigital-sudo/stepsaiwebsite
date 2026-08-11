import os
import re
from build_v2 import GLOBAL_HEAD, NAV, FOOTER, render_s05

decks = [
    r"C:\Users\user\Downloads\StepsAI-Copy-Deck.md",
    r"C:\Users\user\Downloads\StepsAI-Copy-Deck-v2.md",
    r"C:\Users\user\Downloads\StepsAI-Copy-Deck-v3.md",
    r"C:\Users\user\Downloads\StepsAI-Copy-Deck-v4-FINAL.md"
]

all_content = ""
for d in decks:
    if os.path.exists(d):
        with open(d, 'r', encoding='utf-8') as f:
            all_content += f.read() + "\n\n"

# Split by PAGE
pages = re.split(r'\n# PAGE \d+\s*(?:—|-)\s*', all_content)
pages = pages[1:] # Skip the intro

def parse_page(page_text):
    lines = page_text.strip().split('\n')
    header_line = lines[0]
    
    # Extract route
    match = re.search(r'\(`?(/[^`\)]+)`?\)', header_line)
    if not match: return None
    route = match.group(1).strip('/')
    
    # Very basic parsing
    title = header_line.split('(')[0].strip()
    
    # Find Hero Section
    h1 = ""
    sub = []
    kicker = ""
    in_hero = False
    
    blocks = []
    current_block = {"title": "", "content": []}
    
    for line in lines[1:]:
        line = line.strip()
        if line.startswith('## Hero'):
            in_hero = True
            continue
        if line.startswith('## '):
            in_hero = False
            if current_block["title"] or current_block["content"]:
                blocks.append(current_block)
            current_block = {"title": line.replace('##', '').strip(), "content": []}
            continue
            
        if in_hero:
            if line.startswith('> #'):
                h1 = line.replace('> #', '').strip()
            elif line.startswith('> **'):
                kicker = line.replace('> **', '').replace('**', '').strip()
            elif line.startswith('>') and not '›' in line and not line.startswith('> `'):
                sub.append(line.replace('>', '').strip())
        else:
            if line:
                current_block["content"].append(line)
                
    if current_block["title"] or current_block["content"]:
        blocks.append(current_block)
        
    return {
        "route": route,
        "title": title,
        "h1": h1,
        "sub": " ".join(sub),
        "kicker": kicker,
        "blocks": blocks
    }

for p in pages:
    data = parse_page(p)
    if not data or not data["route"]: continue
    
    # Skip pages we already built manually with high fidelity
    if data["route"] in ["", "pricing", "partners", "partners/apply", "about"]: continue
    
    # Build V2 GSAP HTML
    html_content = ""
    
    # S05 Hero
    if data["h1"]:
        html_content += render_s05(data["kicker"], data["h1"], data["sub"])
    
    # Dynamic Blocks
    for block in data["blocks"]:
        if not block["title"]: continue
        
        html_content += f'''
        <section class="section-v2" style="background: var(--bg-surface-2);">
            <h2 class="section-title-v2 gsap-fade-up">{block["title"]}</h2>
            <div class="bento-grid">
        '''
        
        # Simple extraction of blockquotes or bullets into Bento Cards
        for c in block["content"]:
            c_clean = c.replace('>', '').replace('###', '').replace('**', '').strip()
            if not c_clean or c_clean.startswith('→') or c_clean.startswith('`['): continue
            
            html_content += f'''
            <div class="bento-card gsap-scale-in">
                <p class="bento-desc" style="font-size:16px;">{c_clean}</p>
            </div>
            '''
            
        html_content += '''
            </div>
        </section>
        '''
    
    full_html = GLOBAL_HEAD.format(title=data["title"]) + NAV + html_content + FOOTER
    
    dir_path = os.path.join(data["route"])
    os.makedirs(dir_path, exist_ok=True)
    with open(os.path.join(dir_path, "index.html"), "w", encoding="utf-8") as f:
        f.write(full_html)
    
    print(f"Compiled /{data['route']}/ with real content")
