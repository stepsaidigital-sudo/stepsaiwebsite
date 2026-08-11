import re

file_path = r"c:\Users\user\Downloads\HOME STAEP AI\StepsAI_Redesign.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace Nav CSS
new_nav_css = """
    /* --- ADVANCED NAV CSS --- */
    .nav { position: fixed; top: 0; left: 0; width: 100%; z-index: 1000; background: transparent; transition: all 0.3s ease; border-bottom: 1px solid transparent; }
    .nav.scrolled { background: rgba(255,255,255,0.9); backdrop-filter: blur(10px); border-bottom: 1px solid rgba(0,0,0,0.05); box-shadow: 0 4px 20px rgba(0,0,0,0.03); }
    
    .nav-container { max-width: 1300px; margin: 0 auto; padding: 16px 32px; display: flex; align-items: center; justify-content: space-between; }
    .nav-logo-area { display: flex; align-items: center; gap: 10px; text-decoration: none;}
    .nav-logo-icon { width: 30px; height: 30px; background: #2563EB; border-radius: 8px; color: white; display: flex; align-items: center; justify-content: center; }
    .nav-logo-text { color: #0F172A; font-weight: 800; font-size: 20px; letter-spacing: -0.5px; }
    
    .nav-tabs { display: flex; gap: 28px; position: relative; align-items: center; }
    .nav-tab { color: #334155; font-size: 14px; font-weight: 600; cursor: pointer; transition: color 0.2s; display: flex; align-items: center; gap: 4px; text-decoration: none; padding: 10px 0;}
    .nav-tab:hover { color: #0F172A; }
    
    /* Dropdown CSS */
    .has-dropdown { position: relative; }
    .has-dropdown:hover .dropdown-menu { opacity: 1; visibility: visible; transform: translateY(0); }
    .dropdown-menu { position: absolute; top: 100%; left: -20px; background: white; border: 1px solid #E2E8F0; border-radius: 16px; width: 280px; padding: 12px; box-shadow: 0 20px 40px -10px rgba(0,0,0,0.1); opacity: 0; visibility: hidden; transform: translateY(10px); transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1); z-index: 1001; }
    .dropdown-item { display: block; padding: 12px 16px; border-radius: 8px; transition: 0.2s; text-decoration: none; margin-bottom: 4px; }
    .dropdown-item:last-child { margin-bottom: 0; }
    .dropdown-item:hover { background: #F8FAFC; }
    .dropdown-item-title { font-weight: 600; font-size: 14px; color: #0F172A; margin-bottom: 2px; }
    .dropdown-item-desc { font-weight: 400; font-size: 13px; color: #64748B; }

    .nav-right { display: flex; align-items: center; gap: 20px; }
    .nav-login { color: #334155; font-size: 14px; font-weight: 600; text-decoration: none; transition: 0.2s;}
    .nav-login:hover { color: #0F172A; }
"""

# Replace old nav css from `.nav { position: fixed...` down to `.btn-primary... }`
css_pattern = r'\.nav \{ position: fixed;.*?\.btn-primary \{.*?\}'
content = re.sub(css_pattern, new_nav_css + "\n    .btn-outline { border: 1px solid #E2E8F0; background: white; color: #0F172A; padding: 8px 16px; border-radius: 8px; font-size: 14px; font-weight: 600; cursor: pointer; transition: 0.2s; }\n    .btn-primary { background: #2563EB; color: white; padding: 10px 20px; border-radius: 8px; font-size: 14px; font-weight: 600; border: none; cursor: pointer; box-shadow: 0 4px 12px rgba(37,99,235,0.25); transition: 0.2s; }", content, flags=re.DOTALL)

# HTML Nav block replacement
new_nav_html = """  <!-- NAVIGATION -->
  <nav class="nav" id="mainNav">
    <div class="nav-container">
      <a href="/" class="nav-logo-area">
        <div class="nav-logo-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="white"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg></div>
        <div class="nav-logo-text">StepsAI</div>
      </a>
      <div class="nav-tabs">
        <div class="nav-tab has-dropdown">
           Product <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
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
           Solutions <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
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
  </nav>"""

html_pattern = r'<!-- NAVIGATION -->.*?</nav>'
content = re.sub(html_pattern, new_nav_html, content, flags=re.DOTALL)

# Add JS scroll listener
js_scroll = """
<script>
  window.addEventListener('scroll', () => {
      const nav = document.getElementById('mainNav');
      if (window.scrollY > 20) nav.classList.add('scrolled');
      else nav.classList.remove('scrolled');
  });
</script>
</body>"""
content = content.replace("</body>", js_scroll)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Nav updated in StepsAI_Redesign.html")
