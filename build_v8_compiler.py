import os
import re

GLOBAL_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>StepsAI - {title}</title>
  <link rel="stylesheet" href="{root_prefix}assets/css/style.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
  <style>
    .gsap-fade-up {{ opacity: 0; transform: translateY(40px); }}
    .gsap-scale-in {{ opacity: 0; transform: scale(0.9); }}
    
    .hero-v2 {{ min-height: 80vh; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 160px 32px 80px; position: relative; overflow: hidden; }}
    .hero-bg-glow {{ position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 80vw; height: 80vw; background: radial-gradient(circle, var(--accent-tint) 0%, rgba(251,252,254,0) 70%); z-index: -1; }}
    .hero-v2 h1 {{ font-size: clamp(48px, 6vw, 80px); line-height: 1.05; letter-spacing: -2px; max-width: 1000px; margin: 24px auto; font-family: 'Outfit', sans-serif; }}
    .hero-v2 p {{ font-size: 20px; color: var(--text-secondary); max-width: 720px; margin: 0 auto 48px; line-height: 1.6; }}
    
    .section-v2 {{ padding: 112px 32px; max-width: 1400px; margin: 0 auto; }}
    .section-title-v2 {{ font-size: clamp(36px, 4vw, 54px); letter-spacing: -1px; margin-bottom: 80px; font-family: 'Outfit', sans-serif; text-align: center;}}
    
    .bento-grid {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px; grid-auto-flow: dense; }}
    .bento-card {{ background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 24px; padding: 48px; position: relative; overflow: hidden; display: flex; flex-direction: column; justify-content: flex-end; transition: transform 0.5s cubic-bezier(.16,1,.3,1), border-color 0.5s, box-shadow 0.5s; box-shadow: var(--shadow); }}
    .bento-card:hover {{ transform: translateY(-8px); border-color: var(--accent); box-shadow: var(--shadow-lg); }}
    .bento-title {{ font-size: 32px; font-weight: 700; margin-bottom: 16px; font-family: 'Outfit', sans-serif; color: var(--text-primary);}}
    .bento-desc {{ color: var(--text-secondary); font-size: 16px; line-height: 1.6; }}
    @media (max-width: 992px) {{ .bento-grid {{ grid-template-columns: 1fr; }} }}
    
    /* Interactive S09 Accordion */
    .industries-accordion {{
      max-width: 1200px; margin: 0 auto;
      display: flex; gap: 16px; height: 500px;
    }}
    .accordion-panel {{
      position: relative;
      flex: 1;
      border-radius: 24px;
      overflow: hidden;
      background-size: cover;
      background-position: center;
      transition: flex 0.6s cubic-bezier(0.16, 1, 0.3, 1);
      cursor: pointer;
    }}
    .accordion-panel::after {{
      content: '';
      position: absolute; inset: 0;
      background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0) 100%);
      transition: opacity 0.4s;
    }}
    .accordion-panel:hover {{ flex: 3; }}
    .accordion-content {{
      position: absolute; bottom: 0; left: 0; width: 100%;
      padding: 32px; color: white; z-index: 2;
      display: flex; flex-direction: column; justify-content: flex-end;
    }}
    .accordion-title {{ font-family: 'Outfit', sans-serif; font-size: 28px; font-weight: 700; margin: 0; white-space: nowrap; }}
    .accordion-desc {{
      font-size: 16px; color: rgba(255,255,255,0.8);
      margin-top: 12px; line-height: 1.5;
      opacity: 0; transform: translateY(10px);
      transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .accordion-panel:hover .accordion-desc {{ opacity: 1; transform: translateY(0); transition-delay: 0.1s; }}
    
    .mockup-container {{
      position: relative; max-width: 1000px; margin: 0 auto;
      border-radius: 24px; overflow: hidden;
      box-shadow: 0 40px 80px -20px rgba(0,0,0,0.2);
      border: 1px solid var(--border-subtle);
    }}
    .mockup-container img {{ width: 100%; height: auto; display: block; }}
  </style>
</head>
<body>
"""

def render_s05(kicker, h1, p):
    return f"""
    <section class="hero-v2">
        <div class="hero-bg-glow"></div>
        <div class="gsap-fade-up" style="color:var(--accent); font-weight:700; font-size:14px; letter-spacing:1px; margin-bottom:24px; text-transform:uppercase;">{kicker}</div>
        <h1 class="gsap-fade-up">{h1}</h1>
        <p class="gsap-fade-up">{p}</p>
        <div class="gsap-fade-up" style="display:flex; gap:16px; justify-content:center;">
            <button class="btn-primary">Start free trial</button>
            <button class="btn-outline">Book a demo</button>
        </div>
    </section>
    """

CUSTOM_HOME_HERO = """
  <!-- S04 Landing Hero (Modified for V2 GSAP) -->
  <section class="hero-v2" style="padding: 180px 32px 100px;">
    <div class="hero-bg-glow"></div>
    <span class="kicker gsap-fade-up" style="font-family: 'Geist Mono', monospace; font-size: 11px; font-weight: 500; color: var(--accent); letter-spacing: .24em; text-transform: uppercase; margin-bottom: 24px;">AI AGENT FOR SALES & SUPPORT</span>
    <h1 class="gsap-fade-up" style="font-size: clamp(48px, 7vw, 96px); max-width: 1100px;">It answers.<br>Then it acts.</h1>
    <p class="gsap-fade-up" style="font-size: 24px; max-width: 800px;">StepsAI answers customer questions on WhatsApp, Instagram and your website. Then it books the meeting, saves the lead, or updates the order. Nobody on your team has to be awake for it.</p>
    <div class="hero-actions gsap-fade-up" style="display:flex; gap:16px;">
      <a href="./partners/apply/index.html"><button class="btn-primary" style="padding: 16px 32px; font-size: 18px;">Start free trial</button></a>
      <button class="btn-outline" style="padding: 16px 32px; font-size: 18px;">Book a demo</button>
    </div>
  </section>

  <!-- Real Mockup Showcase (Injecting Life) -->
  <section class="section-v2" style="padding-top:0;">
    <div class="mockup-container gsap-scale-in">
      <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1600&q=80" alt="StepsAI Dashboard Mockup" style="opacity: 0.9;">
    </div>
  </section>
"""

CUSTOM_HOME_ACCORDION = """
  <!-- S09 Interactive Industries Accordion -->
  <section class="section-v2" style="background: var(--bg-surface-2);">
    <div style="text-align: center; margin-bottom: 64px;">
      <span style="font-family: 'Geist Mono', monospace; font-size: 12px; color: var(--text-secondary); letter-spacing: .2em; text-transform: uppercase;">BUILT AROUND YOUR BUSINESS</span>
      <h2 style="font-family: 'Outfit'; font-size: 48px; margin-top: 16px; color: var(--text-primary);">Made for the way your customers buy.</h2>
    </div>
    
    <div class="industries-accordion gsap-fade-up">
      <!-- Healthcare -->
      <a href="./solutions/healthcare/index.html" class="accordion-panel" style="background-image: url('https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=800&q=80'); text-decoration:none;">
        <div class="accordion-content">
          <h3 class="accordion-title">Healthcare & Wellness</h3>
          <p class="accordion-desc">Shows which doctor is free. Books the appointment inside the conversation. Sends the reminder so the slot isn't wasted.</p>
        </div>
      </a>
      <!-- Real Estate -->
      <a href="./solutions/real-estate/index.html" class="accordion-panel" style="background-image: url('https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=800&q=80'); text-decoration:none;">
        <div class="accordion-content">
          <h3 class="accordion-title">Real Estate</h3>
          <p class="accordion-desc">Qualifies the buyer before anyone picks up the phone. Books the site visit while they're still looking.</p>
        </div>
      </a>
      <!-- Ecommerce -->
      <a href="./solutions/ecommerce/index.html" class="accordion-panel" style="background-image: url('https://images.unsplash.com/photo-1607082348824-0a96f2a4b9da?w=800&q=80'); text-decoration:none;">
        <div class="accordion-content">
          <h3 class="accordion-title">Ecommerce</h3>
          <p class="accordion-desc">Checks live stock before it promises anything. Recovers the cart before the customer forgets.</p>
        </div>
      </a>
      <!-- SaaS -->
      <a href="./solutions/saas/index.html" class="accordion-panel" style="background-image: url('https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&q=80'); text-decoration:none;">
        <div class="accordion-content">
          <h3 class="accordion-title">SaaS & Tech</h3>
          <p class="accordion-desc">Answers integration questions from your own docs. Compares plans without pushing the expensive one.</p>
        </div>
      </a>
    </div>
  </section>
"""


FOOTER = """
  <!-- S03 CTA Band -->
  <section class="cta-band">
    <h2>Somebody is typing right now.</h2>
    <div style="display:flex; justify-content:center; gap:16px;">
      <a href="{root_prefix}partners/apply/index.html"><button class="btn-primary">Start free trial</button></a>
      <button class="btn-outline">Book a demo</button>
    </div>
  </section>
  <!-- S02 Footer -->
  <footer class="footer">
    <div class="footer-container">
      <div class="footer-col" style="grid-column: span 2;">
        <div style="font-weight: 800; font-size: 20px; margin-bottom:16px;">StepsAI</div>
        <p style="color:var(--text-secondary); font-size:14px; max-width: 250px;">Your AI agent layer for every business. Answer, capture, and close at any hour.</p>
      </div>
      <div class="footer-col">
        <h4>Product</h4>
        <ul><li><a href="{root_prefix}product/ai-agents/index.html">AI Agents</a></li><li><a href="{root_prefix}pricing/index.html">Pricing</a></li></ul>
      </div>
      <div class="footer-col">
        <h4>Solutions</h4>
        <ul><li><a href="{root_prefix}solutions/ecommerce/index.html">E-Commerce</a></li><li><a href="{root_prefix}solutions/real-estate/index.html">Real Estate</a></li></ul>
      </div>
      <div class="footer-col">
        <h4>Company</h4>
        <ul><li><a href="{root_prefix}about/index.html">About</a></li><li><a href="{root_prefix}contact/index.html">Contact</a></li></ul>
      </div>
    </div>
  </footer>
  <script>
    gsap.registerPlugin(ScrollTrigger);
    gsap.to(".gsap-fade-up", { y: 0, opacity: 1, duration: 1, stagger: 0.15, ease: "power3.out" });
    gsap.utils.toArray('.gsap-scale-in').forEach(element => {
      gsap.to(element, {
        scrollTrigger: { trigger: element, start: "top 85%", toggleActions: "play none none reverse" },
        scale: 1, opacity: 1, duration: 0.8, ease: "power3.out"
      });
    });
    window.addEventListener('scroll', () => {
      const nav = document.getElementById('mainNav');
      if (window.scrollY > 20) nav.classList.add('scrolled');
      else nav.classList.remove('scrolled');
    });
  </script>
</body>
</html>
"""

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

# Clean annotations
all_content = re.sub(r'SECTION \d+\s*(?:—|-)\s*', '', all_content, flags=re.IGNORECASE)

pages = re.split(r'\n# PAGE \d+\s*(?:—|-)\s*', all_content)
pages = pages[1:] 

def parse_page(page_text):
    lines = page_text.strip().split('\n')
    header_line = lines[0]
    
    match = re.search(r'\(`?(/[^`\)]*)`?\)', header_line)
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
            if line.startswith('> #'): h1 = line.replace('> #', '').strip()
            elif line.startswith('> **'): kicker = line.replace('> **', '').replace('**', '').strip()
            elif line.startswith('>') and not '›' in line and not line.startswith('> `'): sub.append(line.replace('>', '').strip())
        else:
            if line:
                current_block["content"].append(line)
                
    if current_block["title"] or current_block["content"]:
        blocks.append(current_block)
        
    return {"route": route, "title": title, "h1": h1, "sub": " ".join(sub), "kicker": kicker, "blocks": blocks}

def get_nav(root_prefix):
    # CSS for hover mega menus
    mega_css = """
    <style>
    .nav-dropdown-wrapper:hover .mega-menu { opacity: 1 !important; visibility: visible !important; transform: translateX(-50%) translateY(0) !important; }
    .sol-menu:hover .mega-menu { transform: translateX(0) translateY(0) !important; }
    .res-menu:hover .mega-menu { transform: translateX(0) translateY(0) !important; }
    </style>
    """
    return mega_css + f"""
  <nav class="nav" id="mainNav">
    <div class="nav-container">
      <a href="{root_prefix}index.html" class="nav-logo-area">
        <div class="nav-logo-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="white"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg></div>
        <div class="nav-logo-text">StepsAI</div>
      </a>
      
      <div class="nav-tabs">
        <!-- PRODUCT MEGA MENU -->
        <div class="nav-dropdown-wrapper">
          <a class="nav-tab">Product <span style="font-size: 10px; margin-left: 4px;">▼</span></a>
          <div class="mega-menu">
            <div class="mega-grid">
              <div class="mega-col">
                <div class="mega-col-title">PRODUCTS</div>
                <a href="{root_prefix}product/ai-agents/index.html">AI Agents</a>
                <a href="{root_prefix}product/copilot/index.html">Internal Copilot</a>
              </div>
              <div class="mega-col">
                <div class="mega-col-title">WHAT IT DOES</div>
                <a href="{root_prefix}features/sales-agent/index.html">Sales Agent</a>
                <a href="{root_prefix}features/lead-agent/index.html">Lead Agent</a>
                <a href="{root_prefix}features/meetings-agent/index.html">Meetings Agent</a>
                <a href="{root_prefix}features/support-agent/index.html">Support Agent</a>
              </div>
              <div class="mega-col">
                <div class="mega-col-title">PLATFORM</div>
                <a href="{root_prefix}features/workflows/index.html">Workflows</a>
                <a href="{root_prefix}features/inbox/index.html">One Inbox</a>
                <a href="{root_prefix}features/analytics/index.html">Analytics</a>
                <a href="{root_prefix}integrations/index.html">Integrations</a>
              </div>
              <div class="mega-col">
                <div class="mega-col-title">CHANNELS</div>
                <a href="{root_prefix}channels/website/index.html">Website</a>
                <a href="{root_prefix}channels/whatsapp/index.html">WhatsApp</a>
                <a href="{root_prefix}channels/instagram/index.html">Instagram</a>
                <a href="{root_prefix}channels/standalone-page/index.html">Standalone Page</a>
              </div>
            </div>
          </div>
        </div>

        <!-- SOLUTIONS MEGA MENU -->
        <div class="nav-dropdown-wrapper sol-menu">
          <a class="nav-tab">Solutions <span style="font-size: 10px; margin-left: 4px;">▼</span></a>
          <div class="mega-menu" style="min-width: 400px; left: 0; transform: translateX(0) translateY(10px);">
            <div class="mega-grid" style="grid-template-columns: 1fr 1fr;">
              <div class="mega-col">
                <div class="mega-col-title">BY INDUSTRY</div>
                <a href="{root_prefix}solutions/ecommerce/index.html">E-Commerce <span class="mega-badge">Flagship</span></a>
                <a href="{root_prefix}solutions/saas/index.html">SaaS</a>
                <a href="{root_prefix}solutions/healthcare/index.html">Healthcare</a>
                <a href="{root_prefix}solutions/education/index.html">Education</a>
                <a href="{root_prefix}solutions/real-estate/index.html">Real Estate</a>
              </div>
              <div class="mega-col">
                <div class="mega-col-title">BY ROLE</div>
                <a href="{root_prefix}use-cases/marketing-growth/index.html">Marketing & Growth</a>
                <a href="{root_prefix}use-cases/sales/index.html">Sales</a>
                <a href="{root_prefix}use-cases/support-cx/index.html">Support & CX</a>
                <a href="{root_prefix}use-cases/operations/index.html">Operations</a>
              </div>
            </div>
          </div>
        </div>

        <a href="{root_prefix}pricing/index.html" class="nav-tab">Pricing</a>
        <a href="{root_prefix}partners/index.html" class="nav-tab">Partner</a>

        <!-- RESOURCES MEGA MENU -->
        <div class="nav-dropdown-wrapper res-menu">
          <a class="nav-tab">Resources <span style="font-size: 10px; margin-left: 4px;">▼</span></a>
          <div class="mega-menu" style="min-width: 300px; left: auto; right: 0; transform: translateX(0) translateY(10px);">
            <div class="mega-grid" style="grid-template-columns: 1fr 1fr;">
              <div class="mega-col">
                <div class="mega-col-title">LEARN</div>
                <a href="{root_prefix}blog/index.html">Blog</a>
                <a href="{root_prefix}resources/ai-guides/index.html">AI Guides</a>
                <a href="{root_prefix}resources/case-studies/index.html">Case Studies</a>
              </div>
              <div class="mega-col">
                <div class="mega-col-title">COMPANY</div>
                <a href="{root_prefix}about/index.html">About</a>
                <a href="{root_prefix}team/index.html">Team • Careers</a>
                <a href="{root_prefix}note/index.html">Note • Contact</a>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <div class="nav-right">
        <a href="{root_prefix}partners/apply/index.html"><button class="btn-primary">Start free trial</button></a>
      </div>
    </div>
  </nav>
"""

def parse_markdown_line(line):
    # Parse bold
    line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line)
    # Parse images (the core requirement for CRM workforce diagrams etc)
    line = re.sub(r'!\[([^\]]*)\]\(([^\)]+)\)', r'<img src="\2" alt="\1" style="width: 100%; border-radius: 12px; margin: 16px 0; border: 1px solid var(--border-subtle); display: block;" />', line)
    return line

for p in pages:
    data = parse_page(p)
    if not data: continue
    
    # REMOVED THE EXCLUSION LINE! We now compile EVERYTHING!
    
    html_content = ""
    if data["route"] == "" and data["h1"]:
        # INJECT CUSTOM HERO FOR HOME PAGE
        html_content += CUSTOM_HOME_HERO
    elif data["h1"]:
        html_content += render_s05(data["kicker"], data["h1"], data["sub"])
    
    for block in data["blocks"]:
        if not block["title"] or "Hero" in block["title"]: continue
        
        if data["route"] == "" and "Industries" in block["title"]:
            # INJECT CUSTOM ACCORDION FOR HOME PAGE SECTION 3
            html_content += CUSTOM_HOME_ACCORDION
            continue
            
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
                    a.append(parse_markdown_line(c_clean))
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
                    card_desc.append(parse_markdown_line(c_clean))
                    
            if card_title or card_desc:
                html_content += f'''
                <div class="bento-card gsap-scale-in">
                    <h3 class="bento-title" style="font-size: 24px; margin-bottom: 16px;">{card_title}</h3>
                    <p class="bento-desc" style="font-size:16px;">{' '.join(card_desc)}</p>
                </div>'''
                
            html_content += '</div></section>'
    
    depth = len(data["route"].split('/')) if data["route"] else 0
    root_prefix = "../" * depth if depth > 0 else "./"
    
    head = GLOBAL_HEAD.format(title=data["title"], root_prefix=root_prefix)
    footer = FOOTER.replace("{root_prefix}", root_prefix)
    
    full_html = head + get_nav(root_prefix) + html_content + footer
    
    if data["route"] == "":
        dir_path = ""
    else:
        dir_path = os.path.join(data["route"])
        os.makedirs(dir_path, exist_ok=True)
        
    with open(os.path.join(dir_path, "index.html"), "w", encoding="utf-8") as f:
        f.write(full_html)
    
print(f"V8 ALL-PAGES Compiler finished.")
