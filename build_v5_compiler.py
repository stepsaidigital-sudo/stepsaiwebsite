import os
import re
from build_v2 import GLOBAL_HEAD, FOOTER, render_s05

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

# Clean copywriter annotations like "SECTION 1 — Hero" -> "Hero"
all_content = re.sub(r'SECTION \d+\s*(?:—|-)\s*', '', all_content, flags=re.IGNORECASE)
all_content = re.sub(r'\*([^\*]+)\*', r'\1', all_content)

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

def get_nav(root_prefix):
    return f"""
  <nav class="nav" id="mainNav">
    <div class="nav-container">
      <a href="{root_prefix}StepsAI_Redesign.html" class="nav-logo-area">
        <div class="nav-logo-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="white"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg></div>
        <div class="nav-logo-text">StepsAI</div>
      </a>
      <div class="nav-tabs">
        <a href="{root_prefix}product/ai-agents/index.html" class="nav-tab">Product</a>
        <a href="{root_prefix}solutions/ecommerce/index.html" class="nav-tab">Solutions</a>
        <a href="{root_prefix}pricing/index.html" class="nav-tab">Pricing</a>
        <a href="{root_prefix}partners/index.html" class="nav-tab">Partner</a>
      </div>
      <div class="nav-right">
        <a href="{root_prefix}partners/apply/index.html"><button class="btn-primary">Start free trial</button></a>
      </div>
    </div>
  </nav>
"""

for p in pages:
    data = parse_page(p)
    if not data or not data["route"]: continue
    if data["route"] in ["", "pricing", "partners", "partners/apply", "about"]: continue
    
    html_content = ""
    if data["h1"]:
        html_content += render_s05(data["kicker"], data["h1"], data["sub"])
    
    for block in data["blocks"]:
        if not block["title"] or "Hero" in block["title"]: continue
        
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
    
    depth = len(data["route"].split('/'))
    root_prefix = "../" * depth if depth > 0 else "./"
    
    head = GLOBAL_HEAD.format(title=data["title"])
    head = head.replace('href="/assets/css/style.css"', f'href="{root_prefix}assets/css/style.css"')
    
    footer = FOOTER
    footer = footer.replace('href="/partners/apply/"', f'href="{root_prefix}partners/apply/index.html"')
    footer = footer.replace('href="/solutions/ecommerce/"', f'href="{root_prefix}solutions/ecommerce/index.html"')
    footer = footer.replace('href="/solutions/real-estate/"', f'href="{root_prefix}solutions/real-estate/index.html"')
    footer = footer.replace('href="/about/"', f'href="{root_prefix}about/index.html"')
    footer = footer.replace('href="/contact/"', f'href="{root_prefix}contact/index.html"')
    
    full_html = head + get_nav(root_prefix) + html_content + footer
    
    dir_path = os.path.join(data["route"])
    os.makedirs(dir_path, exist_ok=True)
    with open(os.path.join(dir_path, "index.html"), "w", encoding="utf-8") as f:
        f.write(full_html)
    
    print(f"Compiled /{data['route']}/ flawlessly.")
