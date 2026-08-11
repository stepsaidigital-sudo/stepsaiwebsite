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

pages = re.split(r'\n# PAGE \d+\s*(?:—|-)\s*', all_content)
pages = pages[1:] 

def parse_page(page_text):
    lines = page_text.strip().split('\n')
    header_line = lines[0]
    
    match = re.search(r'\(`?(/[^`\)]+)`?\)', header_line)
    if not match: return None
    route = match.group(1).strip('/')
    
    title = header_line.split('(')[0].strip()
    
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
    if data["route"] in ["", "pricing", "partners", "partners/apply", "about"]: continue
    
    html_content = ""
    if data["h1"]:
        html_content += render_s05(data["kicker"], data["h1"], data["sub"])
    
    for block in data["blocks"]:
        if not block["title"]: continue
        
        # Determine if this should be an accordion (FAQ) or bento grid
        is_faq = "FAQ" in block["title"].upper()
        
        html_content += f'''
        <section class="section-v2" style="background: var(--bg-surface-2);">
            <h2 class="section-title-v2 gsap-fade-up">{block["title"]}</h2>
        '''
        
        if is_faq:
            html_content += '<div style="max-width: 800px; margin: 0 auto;">'
            q = ""
            a = []
            for c in block["content"]:
                c_clean = c.replace('>', '').strip()
                if c_clean.startswith('**') and '?' in c_clean:
                    # Previous Q/A pair
                    if q:
                        html_content += f'''
                        <div class="gsap-fade-up" style="background: var(--bg-surface); padding: 32px; border-radius: 16px; margin-bottom: 16px; border: 1px solid var(--border-subtle);">
                            <h3 style="font-family: 'Outfit'; font-size: 20px; margin-bottom: 12px;">{q}</h3>
                            <p style="color: var(--text-secondary); line-height: 1.5; margin:0;">{' '.join(a)}</p>
                        </div>'''
                    q = c_clean.replace('**', '').strip()
                    a = []
                elif c_clean:
                    a.append(c_clean)
            if q:
                html_content += f'''
                <div class="gsap-fade-up" style="background: var(--bg-surface); padding: 32px; border-radius: 16px; margin-bottom: 16px; border: 1px solid var(--border-subtle);">
                    <h3 style="font-family: 'Outfit'; font-size: 20px; margin-bottom: 12px;">{q}</h3>
                    <p style="color: var(--text-secondary); line-height: 1.5; margin:0;">{' '.join(a)}</p>
                </div>'''
            html_content += '</div></section>'
            
        else:
            html_content += '<div class="bento-grid">'
            # Group by ### title
            card_title = ""
            card_desc = []
            
            for c in block["content"]:
                c_clean = c.replace('>', '').strip()
                if not c_clean or c_clean.startswith('→') or c_clean.startswith('`['): continue
                
                if c_clean.startswith('### '):
                    if card_title or card_desc:
                        html_content += f'''
                        <div class="bento-card gsap-scale-in">
                            <h3 class="bento-title" style="font-size: 24px; margin-bottom: 16px;">{card_title}</h3>
                            <p class="bento-desc" style="font-size:16px;">{' '.join(card_desc)}</p>
                        </div>'''
                    card_title = c_clean.replace('### ', '')
                    card_desc = []
                else:
                    card_desc.append(c_clean)
                    
            if card_title or card_desc:
                html_content += f'''
                <div class="bento-card gsap-scale-in">
                    <h3 class="bento-title" style="font-size: 24px; margin-bottom: 16px;">{card_title}</h3>
                    <p class="bento-desc" style="font-size:16px;">{' '.join(card_desc)}</p>
                </div>'''
                
            html_content += '</div></section>'
    
    # Path resolution logic so absolute URLs don't break if opened locally.
    # Calculate how many levels deep we are.
    depth = len(data["route"].split('/'))
    root_prefix = "../" * depth if depth > 0 else "./"
    
    # Replace all href="/" with href="root_prefix"
    # Actually it's safer to just let the server handle absolute paths, but if they are opening locally,
    # let's just make sure the nav paths are correct.
    # The user was seeing blank pages probably because of absolute paths on file://.
    
    full_html = GLOBAL_HEAD.format(title=data["title"]) + NAV + html_content + FOOTER
    
    # Very crude relative path fixing for the nav if they open via file://
    # We will replace 'href="/' with 'href="' + root_prefix
    # Except for http:// or https://
    full_html = re.sub(r'href="/([^"]*)"', r'href="' + root_prefix + r'\1index.html"', full_html)
    # Fix root link
    full_html = full_html.replace(f'href="{root_prefix}index.html"', f'href="{root_prefix}StepsAI_Redesign.html"')
    # Clean up double index.html
    full_html = full_html.replace('index.htmlindex.html', 'index.html')
    
    dir_path = os.path.join(data["route"])
    os.makedirs(dir_path, exist_ok=True)
    with open(os.path.join(dir_path, "index.html"), "w", encoding="utf-8") as f:
        f.write(full_html)
    
    print(f"Compiled /{data['route']}/ with relative paths and correct bento parsing")
