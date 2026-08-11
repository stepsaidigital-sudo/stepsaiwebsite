import os
import re

decks = [
    r"C:\Users\user\Downloads\StepsAI-Copy-Deck-v2.md",
    r"C:\Users\user\Downloads\StepsAI-Copy-Deck-v3.md",
    r"C:\Users\user\Downloads\StepsAI-Copy-Deck-v4-FINAL.md"
]

all_content = ""
for d in decks:
    with open(d, 'r', encoding='utf-8') as f:
        all_content += f.read() + "\n\n"

# Hard clean of copywriter annotations
all_content = re.sub(r'SECTION \d+\s*(?:—|-)\s*', '', all_content, flags=re.IGNORECASE)
# Remove asterisks around text
all_content = re.sub(r'\*([^\*]+)\*', r'\1', all_content)

raw_pages = re.split(r'\n# PAGE \d+\s*(?:—|-)\s*', all_content)
raw_pages = raw_pages[1:]

base_dir = r"C:\Users\user\Downloads\HOME STAEP AI"

shared_css = """
    :root {
      --primary: #2563EB; 
      --bg-color: #FAFAFA;
      --text-main: #0F172A;
      --text-muted: #64748B;
      --border-light: #E2E8F0;
    }
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { background-color: var(--bg-color); color: var(--text-main); font-family: 'Inter', sans-serif; line-height: 1.6; overflow-x: hidden; }
    h1, h2, h3, h4 { font-family: 'Outfit', sans-serif; }
    a { text-decoration: none; color: inherit; }
    
    /* Nav */
    .nav { position: fixed; top: 0; left: 0; width: 100%; z-index: 1000; background: transparent; transition: all 0.3s ease; border-bottom: 1px solid transparent; }
    .nav.scrolled { background: rgba(255,255,255,0.9); backdrop-filter: blur(10px); border-bottom: 1px solid rgba(0,0,0,0.05); box-shadow: 0 4px 20px rgba(0,0,0,0.03); }
    
    .nav-container { max-width: 1300px; margin: 0 auto; padding: 16px 32px; display: flex; align-items: center; justify-content: space-between; }
    .nav-logo-area { display: flex; align-items: center; gap: 10px; font-weight: 800; font-size: 20px; text-decoration: none;}
    .nav-logo-icon { width: 30px; height: 30px; background: var(--primary); border-radius: 8px; color: white; display: flex; align-items: center; justify-content: center; }
    .nav-tabs { display: flex; gap: 28px; position: relative; align-items: center; }
    .nav-tab { color: #334155; font-size: 14px; font-weight: 600; cursor: pointer; transition: color 0.2s; display: flex; align-items: center; gap: 4px; text-decoration: none; padding: 10px 0;}
    .nav-tab:hover { color: var(--text-main); }
    
    .has-dropdown { position: relative; }
    .has-dropdown:hover .dropdown-menu { opacity: 1; visibility: visible; transform: translateY(0); }
    .dropdown-menu { position: absolute; top: 100%; left: -20px; background: white; border: 1px solid var(--border-light); border-radius: 16px; width: 280px; padding: 12px; box-shadow: 0 20px 40px -10px rgba(0,0,0,0.1); opacity: 0; visibility: hidden; transform: translateY(10px); transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1); z-index: 1001; }
    .dropdown-item { display: block; padding: 12px 16px; border-radius: 8px; transition: 0.2s; text-decoration: none; margin-bottom: 4px; }
    .dropdown-item:last-child { margin-bottom: 0; }
    .dropdown-item:hover { background: #F8FAFC; }
    .dropdown-item-title { font-weight: 600; font-size: 14px; color: var(--text-main); margin-bottom: 2px; }
    .dropdown-item-desc { font-weight: 400; font-size: 13px; color: var(--text-muted); }
    
    .nav-right { display: flex; align-items: center; gap: 20px; }
    .nav-login { color: #334155; font-size: 14px; font-weight: 600; text-decoration: none; transition: 0.2s;}
    .nav-login:hover { color: var(--text-main); }
    
    .btn-outline { border: 1px solid var(--border-light); background: white; padding: 8px 16px; border-radius: 8px; font-size: 14px; font-weight: 600; cursor: pointer; transition: 0.2s;}
    .btn-outline:hover { border-color: var(--text-main); }
    .btn-primary { background: var(--primary); color: white; padding: 10px 20px; border-radius: 8px; font-size: 14px; font-weight: 600; border: none; cursor: pointer; transition: 0.2s; box-shadow: 0 4px 12px rgba(37,99,235,0.25); }
    .btn-primary:hover { transform: translateY(-1px); box-shadow: 0 6px 16px rgba(37,99,235,0.35); }
    
    /* Hero with Mockup */
    .page-hero { padding: 160px 24px 100px; background: radial-gradient(circle at 50% 0%, #ffffff 0%, #FAFAFA 100%); border-bottom: 1px solid var(--border-light); position: relative; overflow: hidden; display: flex; align-items: center; justify-content: space-between; max-width: 1400px; margin: 0 auto; gap: 64px; }
    .hero-text { flex: 1; max-width: 650px; }
    .hero-text h1 { font-size: 56px; margin-bottom: 24px; letter-spacing: -2px; line-height: 1.1; }
    .hero-pre { font-size: 12px; font-weight: 700; color: var(--primary); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 20px; display: block; }
    .hero-text p { font-size: 18px; color: var(--text-muted); margin-bottom: 40px; line-height: 1.6; }
    .hero-actions { display: flex; gap: 16px; }
    
    .hero-mockup-area { flex: 1; display: flex; justify-content: center; position: relative; }
    .mockup-widget { width: 340px; height: 500px; background: rgba(248, 250, 252, 0.85); backdrop-filter: blur(24px); border-radius: 24px; box-shadow: 0 30px 60px -15px rgba(0,0,0,0.25); overflow: hidden; display: flex; flex-direction: column; border: 1px solid rgba(255,255,255,1); }
    .mw-header { padding: 16px; background: white; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #F1F5F9; }
    .mw-header-left { display: flex; align-items: center; gap: 12px; }
    .mw-avatar { width: 36px; height: 36px; background: #2563EB; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; }
    .mw-title { font-size: 14px; font-weight: 600; color: #0F172A; }
    .mw-status { font-size: 12px; color: #10B981; display: flex; align-items: center; gap: 4px; }
    .mw-status::before { content: ''; width: 6px; height: 6px; background: #10B981; border-radius: 50%; }
    .mw-body { flex: 1; padding: 20px; overflow-y: auto; display: flex; flex-direction: column; gap: 16px; background: #F8FAFC; }
    .mw-msg { max-width: 85%; padding: 12px 16px; font-size: 14px; line-height: 1.5; }
    .mw-msg.out { background: #2563EB; color: white; border-radius: 16px 16px 0 16px; align-self: flex-end; box-shadow: 0 4px 12px rgba(37,99,235,0.2); }
    .mw-msg.in { background: white; color: #0F172A; border-radius: 16px 16px 16px 0; align-self: flex-start; border: 1px solid #E2E8F0; box-shadow: 0 2px 8px rgba(0,0,0,0.02); }
    .mw-card { background: white; border: 1px solid #E2E8F0; border-radius: 12px; padding: 12px; margin-top: 8px; width: 100%; box-shadow: 0 2px 8px rgba(0,0,0,0.02); }
    .mw-card-title { font-size: 13px; font-weight: 600; margin-bottom: 4px; color: #0F172A; }
    .mw-card-sub { font-size: 12px; color: #64748B; }
    .mw-btn { width: 100%; padding: 8px; margin-top: 8px; background: #F1F5F9; border: none; border-radius: 6px; font-size: 12px; font-weight: 600; color: #2563EB; cursor: pointer; }
    .mw-input { padding: 16px; background: white; border-top: 1px solid #E2E8F0; display: flex; gap: 12px; align-items: center; }
    .mw-input-box { flex: 1; background: #F1F5F9; border-radius: 100px; padding: 10px 16px; font-size: 13px; color: #94A3B8; }
    
    /* Layout */
    .section-block { padding: 120px 24px; max-width: 1200px; margin: 0 auto; }
    .section-title { font-size: 36px; font-weight: 800; letter-spacing: -1px; margin-bottom: 64px; text-align: center; max-width: 700px; margin-left: auto; margin-right: auto; line-height: 1.2; }
    
    /* Grid & Cards */
    .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 32px; }
    .card { background: white; border: 1px solid var(--border-light); border-radius: 20px; padding: 48px; transition: 0.3s; position: relative; overflow: hidden; display: flex; flex-direction: column; justify-content: center; }
    .card:hover { box-shadow: 0 30px 60px -15px rgba(0,0,0,0.05); transform: translateY(-4px); border-color: #cbd5e1; }
    .card h3 { font-size: 24px; margin-bottom: 20px; font-weight: 800; letter-spacing: -0.5px; }
    .card p { color: var(--text-muted); font-size: 16px; margin-bottom: 0; }
    .card .receipt { display: inline-flex; align-items: center; gap: 8px; margin-top: 24px; font-family: monospace; font-size: 12px; color: var(--primary); font-weight: 700; background: #EEF2FF; padding: 12px 16px; border-radius: 8px; }
    
    /* FAQ */
    .faq-container { max-width: 800px; margin: 0 auto; background: white; border-radius: 16px; border: 1px solid var(--border-light); padding: 0 32px; }
    .faq-item { border-bottom: 1px solid var(--border-light); }
    .faq-item:last-child { border-bottom: none; }
    .faq-q { padding: 32px 0; font-size: 18px; font-weight: 600; cursor: pointer; display: flex; justify-content: space-between; align-items: center; }
    .faq-q::after { content: '+'; font-size: 24px; color: var(--text-muted); transition: 0.3s; }
    .faq-a { padding-bottom: 32px; font-size: 16px; color: var(--text-muted); display: none; }
    .faq-item.active .faq-q::after { transform: rotate(45deg); }
    .faq-item.active .faq-a { display: block; }
    
    /* CTA */
    .cta-band { background: #0F172A; color: white; padding: 120px 24px; text-align: center; }
    .cta-band h2 { font-size: 48px; font-weight: 900; margin-bottom: 24px; letter-spacing: -1px; }
    
    /* Footer */
    .footer { background: white; padding: 64px 0 32px; border-top: 1px solid var(--border-light); }
    .footer-container { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr 1fr; gap: 48px; max-width: 1200px; margin: 0 auto; padding: 0 24px; }
    .footer-col h4 { font-size: 14px; font-weight: 700; margin-bottom: 20px; }
    .footer-col ul { display: flex; flex-direction: column; gap: 12px; list-style: none;}
    .footer-col a { color: var(--text-muted); font-size: 14px; transition: 0.2s;}
    .footer-col a:hover { color: var(--primary); }
    
    @media (max-width: 992px) {
        .page-hero { flex-direction: column; text-align: center; padding: 140px 24px 60px; }
        .hero-actions { justify-content: center; }
    }
    @media (max-width: 768px) {
        .page-hero h1 { font-size: 40px; }
        .footer-container { grid-template-columns: 1fr; }
        .nav-tabs, .nav-right { display: none; }
    }
"""

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>StepsAI - {title}</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Outfit:wght@500;600;700;800;900&display=swap" rel="stylesheet">
  <style>{css}</style>
</head>
<body>
  <!-- Nav -->
  <nav class="nav" id="mainNav">
    <div class="nav-container">
      <a href="/" class="nav-logo-area">
        <div class="nav-logo-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="white"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg></div>
        <div class="nav-logo-text">StepsAI</div>
      </a>
      <div class="nav-tabs">
        <div class="nav-tab has-dropdown">
           Product <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-left: 4px;"><polyline points="6 9 12 15 18 9"></polyline></svg>
           <div class="dropdown-menu">
               <a href="/product/ai-agents/" class="dropdown-item">
                   <div class="dropdown-item-title">AI Agents</div>
                   <div class="dropdown-item-desc">Customer-facing agents for sales and support</div>
               </a>
               <a href="/product/copilot/" class="dropdown-item">
                   <div class="dropdown-item-title">Internal Copilot</div>
                   <div class="dropdown-item-desc">Your team's internal knowledge assistant</div>
               </a>
           </div>
        </div>
        <div class="nav-tab has-dropdown">
           Solutions <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-left: 4px;"><polyline points="6 9 12 15 18 9"></polyline></svg>
           <div class="dropdown-menu">
               <a href="/solutions/ecommerce/" class="dropdown-item"><div class="dropdown-item-title">E-Commerce</div></a>
               <a href="/solutions/saas/" class="dropdown-item"><div class="dropdown-item-title">SaaS</div></a>
               <a href="/solutions/healthcare/" class="dropdown-item"><div class="dropdown-item-title">Healthcare</div></a>
               <a href="/solutions/education/" class="dropdown-item"><div class="dropdown-item-title">Education</div></a>
               <a href="/solutions/real-estate/" class="dropdown-item"><div class="dropdown-item-title">Real Estate</div></a>
           </div>
        </div>
        <a href="/pricing/" class="nav-tab">Pricing</a>
        <a href="/partners/" class="nav-tab">Partner</a>
      </div>
      <div class="nav-right">
        <a href="#" class="nav-login">Sign in</a>
        <a href="/pricing/"><button class="btn-primary">Start free trial</button></a>
      </div>
    </div>
  </nav>

  {content}

  <!-- CTA -->
  <section class="cta-band">
    <h2>Somebody is typing right now.</h2>
    <div class="hero-actions" style="margin-top: 32px; justify-content:center;">
      <a href="/pricing/"><button class="btn-primary">Start free trial</button></a>
      <button class="btn-outline" style="background:transparent; color:white; border-color:white;">Book a demo</button>
    </div>
  </section>

  <!-- Footer -->
  <footer class="footer">
    <div class="footer-container">
      <div class="footer-col" style="grid-column: span 2;">
        <div style="font-weight: 800; font-size: 20px; margin-bottom:16px;">StepsAI</div>
        <p style="color:var(--text-muted); font-size:14px; max-width: 250px;">Your AI agent layer for every business. Answer, capture, and close at any hour.</p>
      </div>
      <div class="footer-col">
        <h4>Product</h4>
        <ul><li><a href="/product/ai-agents/">AI Agents</a></li><li><a href="/product/copilot/">Internal Copilot</a></li><li><a href="/pricing/">Pricing</a></li></ul>
      </div>
      <div class="footer-col">
        <h4>Solutions</h4>
        <ul><li><a href="/solutions/ecommerce/">E-Commerce</a></li><li><a href="/solutions/saas/">SaaS</a></li><li><a href="/solutions/real-estate/">Real Estate</a></li></ul>
      </div>
      <div class="footer-col">
        <h4>Company</h4>
        <ul><li><a href="/about/">About</a></li><li><a href="/team/">Team</a></li><li><a href="/contact/">Contact</a></li></ul>
      </div>
    </div>
  </footer>

  <script>
    document.querySelectorAll('.faq-q').forEach(q => {
      q.addEventListener('click', () => {
        const item = q.parentElement;
        const isActive = item.classList.contains('active');
        document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('active'));
        if (!isActive) item.classList.add('active');
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

def extract_hero(section_text, page_title="StepsAI"):
    h1_match = re.search(r'# (.+)', section_text)
    h1 = h1_match.group(1) if h1_match else page_title
    
    parts = section_text.split('\n')
    p_text = ""
    pre_text = page_title.upper()
    for line in parts:
        if line.startswith("> **"):
            pre_text = line.replace("> **", "").replace("**", "").strip()
        if not line.startswith('#') and not line.startswith('>') and not line.startswith('`') and len(line) > 15:
            if p_text == "": p_text = line.strip()
        if line.startswith("> ") and not line.startswith("> **") and not line.startswith("> #"):
            if len(line) > 15 and p_text == "":
                p_text = line.replace("> ", "").strip()
                
    # Customize the Mockup based on the page!
    if "REAL ESTATE" in page_title.upper():
        mockup_q = "Is the 3BHK still available?"
        mockup_a = "It is. Want to see it this weekend?"
        mockup_c = "Booked for Saturday 11 AM."
        mockup_card = "<div class='mw-card-title'>Sat 11:00 AM</div><div class='mw-card-sub'>Site Visit Scheduled</div>"
    elif "E-COMMERCE" in page_title.upper():
        mockup_q = "Where is my order?"
        mockup_a = "Order #2453 is out for delivery. It arrives tomorrow before 6 PM."
        mockup_c = "I'll message you when it arrives."
        mockup_card = "<div class='mw-card-title'>Order #2453</div><div class='mw-card-sub'>Out for Delivery</div>"
    elif "PRICING" in page_title.upper():
        mockup_q = "Does this include the Shopify integration?"
        mockup_a = "Yes, Shopify is included on all plans. Would you like to start the free trial?"
        mockup_c = "Great, setting up your trial now."
        mockup_card = "<div class='mw-card-title'>Free Trial Started</div><div class='mw-card-sub'>14 Days Remaining</div>"
    else:
        mockup_q = f"Can you help me with {page_title}?"
        mockup_a = f"Absolutely. Our {page_title} solutions are designed to handle this."
        mockup_c = "Let me show you how it works."
        mockup_card = f"<div class='mw-card-title'>{page_title} Agent</div><div class='mw-card-sub'>Active</div>"
    
    return f"""
  <div style="background: white;">
  <section class="page-hero">
    <div class="hero-text">
        <span class="hero-pre">{pre_text}</span>
        <h1>{h1}</h1>
        <p>{p_text}</p>
        <div class="hero-actions">
          <a href="/pricing/"><button class="btn-primary">Start free trial</button></a>
          <button class="btn-outline">Book a demo</button>
        </div>
    </div>
    
    <div class="hero-mockup-area">
        <div class="mockup-widget">
          <div class="mw-header">
            <div class="mw-header-left">
              <div class="mw-avatar"><svg width="20" height="20" viewBox="0 0 24 24" fill="white"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg></div>
              <div>
                <div class="mw-title">StepsAI Agent</div>
                <div class="mw-status">Online</div>
              </div>
            </div>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#94A3B8" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 16 16 12 12 8"></polyline><line x1="8" y1="12" x2="16" y2="12"></line></svg>
          </div>
          <div class="mw-body">
            <div class="mw-msg in">{mockup_q}</div>
            <div class="mw-msg out">{mockup_a}</div>
            <div class="mw-msg in">Perfect, thanks</div>
            <div class="mw-msg out">{mockup_c}
              <div class="mw-card">
                 {mockup_card}
                 <button class="mw-btn">View Details</button>
              </div>
            </div>
          </div>
          <div class="mw-input">
             <div class="mw-input-box">Type a message...</div>
             <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#2563EB" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
          </div>
        </div>
    </div>
  </section>
  </div>
    """

def extract_grid(section_text):
    # Try to find header+content blocks
    blocks = re.findall(r'(?:> ### |\*\*|\"|`)([^\n\*\"`]+)(?:\*\*|\"|`|\n)(.+?)(?=\n> ### |\n\*\*|\n\"|\n`|$)', section_text, re.DOTALL)
    
    html = '<section class="section-block"><div class="grid">'
    found_cards = False
    
    if blocks:
        for title, content in blocks:
            if len(title.strip()) < 3: continue
            content = content.replace(">", "").strip()
            # Clean weird lines
            content_lines = [l for l in content.split('\\n') if not l.startswith('---') and len(l) > 2]
            content = " ".join(content_lines)
            
            receipt_match = re.search(r'→\s*`([^`]+)`', content)
            receipt_html = ""
            if receipt_match:
                receipt_html = f'<div class="receipt">✓ {receipt_match.group(1)}</div>'
                content = content.replace(f'→ `{receipt_match.group(1)}`', '')
                content = content.replace(f'→`{receipt_match.group(1)}`', '')
            
            if len(content) > 10:
                html += f'<div class="card"><h3>{title.strip()}</h3><p>{content.strip()}</p>{receipt_html}</div>'
                found_cards = True
    
    # If no blocks found, just split by paragraph and make cards
    if not found_cards:
        paras = re.split(r'\n\n+', section_text)
        for p in paras:
            p = p.replace(">", "").replace("---", "").strip()
            if not p or p.startswith('#'): continue
            receipt_match = re.search(r'→\s*`([^`]+)`', p)
            receipt_html = ""
            if receipt_match:
                receipt_html = f'<br><div class="receipt">✓ {receipt_match.group(1)}</div>'
                p = p.replace(f'→ `{receipt_match.group(1)}`', '')
            if len(p) > 20:
                html += f'<div class="card"><p>{p}</p>{receipt_html}</div>'
                found_cards = True
                
    if not found_cards: return ""
    html += '</div></section>'
    return html
    
def extract_faq(section_text):
    qas = re.findall(r'\*\*([^\*]+)\*\*\n> (.+)', section_text)
    if not qas: return ""
    
    html = '<section class="section-block"><h2 class="section-title">Frequently Asked Questions</h2><div class="faq-container">'
    for q, a in qas:
        html += f'<div class="faq-item"><div class="faq-q">{q.strip()}</div><div class="faq-a">{a.strip()}</div></div>'
    html += '</div></section>'
    return html

count = 0
for raw_page in raw_pages:
    title_match = re.search(r'([^\(]+)\(`([^`]+)`\)', raw_page)
    if not title_match: continue
    page_title = title_match.group(1).strip()
    url = title_match.group(2).strip()
    
    if url == '/': continue
    
    # Sections are often separated by ## 
    sections = re.split(r'\n## ', raw_page)
    page_html = ""
    
    for i, sec in enumerate(sections):
        sec = sec.strip()
        if not sec: continue
        
        # Determine if it's a Hero
        is_hero = False
        if i == 0 or sec.lower().startswith("hero"):
            is_hero = True
        elif "# " in sec and i == 0:
            is_hero = True
            
        if is_hero:
            page_html += extract_hero(sec, page_title)
        elif "FAQ" in sec.split('\n')[0]:
            page_html += extract_faq(sec)
        elif "CTA" in sec.split('\n')[0]:
            pass
        else:
            grid = extract_grid(sec)
            if grid:
                sec_title = sec.split('\n')[0].strip()
                # Remove markdown characters from title
                sec_title = re.sub(r'[\*\#]', '', sec_title).strip()
                if sec_title and len(sec_title) > 3 and "---" not in sec_title:
                    page_html += f'<section class="section-block" style="padding-bottom: 0;"><h2 class="section-title">{sec_title}</h2></section>'
                page_html += grid
            
    clean_path = url.strip('/')
    dir_path = os.path.join(base_dir, clean_path.replace('/', os.sep))
    os.makedirs(dir_path, exist_ok=True)
    
    final_html = html_template.replace('{title}', page_title).replace('{css}', shared_css).replace('{content}', page_html)
    
    with open(os.path.join(dir_path, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(final_html)
    count += 1

print(f"Successfully compiled {count} fully featured landing pages with Interactive Mockups.")
