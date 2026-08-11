import os
import re

nav = """<style>
    .nav-dropdown-wrapper:hover .mega-menu { opacity: 1 !important; visibility: visible !important; transform: translateX(-50%) translateY(0) !important; }
    .sol-menu:hover .mega-menu { transform: translateX(0) translateY(0) !important; }
    .res-menu:hover .mega-menu { transform: translateX(0) translateY(0) !important; }
    </style>
  <nav class="nav" id="mainNav">
    <div class="nav-container">
      <a href="./StepsAI_Redesign.html" class="nav-logo-area">
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
                <a href="./product/ai-agents/index.html">AI Agents</a>
                <a href="./product/copilot/index.html">Internal Copilot</a>
              </div>
              <div class="mega-col">
                <div class="mega-col-title">WHAT IT DOES</div>
                <a href="./features/sales-agent/index.html">Sales Agent</a>
                <a href="./features/lead-agent/index.html">Lead Agent</a>
                <a href="./features/meetings-agent/index.html">Meetings Agent</a>
                <a href="./features/support-agent/index.html">Support Agent</a>
              </div>
              <div class="mega-col">
                <div class="mega-col-title">PLATFORM</div>
                <a href="./features/workflows/index.html">Workflows</a>
                <a href="./features/inbox/index.html">One Inbox</a>
                <a href="./features/analytics/index.html">Analytics</a>
                <a href="./integrations/index.html">Integrations</a>
              </div>
              <div class="mega-col">
                <div class="mega-col-title">CHANNELS</div>
                <a href="./channels/website/index.html">Website</a>
                <a href="./channels/whatsapp/index.html">WhatsApp</a>
                <a href="./channels/instagram/index.html">Instagram</a>
                <a href="./channels/standalone-page/index.html">Standalone Page</a>
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
                <a href="./solutions/ecommerce/index.html">E-Commerce <span class="mega-badge">Flagship</span></a>
                <a href="./solutions/saas/index.html">SaaS</a>
                <a href="./solutions/healthcare/index.html">Healthcare</a>
                <a href="./solutions/education/index.html">Education</a>
                <a href="./solutions/real-estate/index.html">Real Estate</a>
              </div>
              <div class="mega-col">
                <div class="mega-col-title">BY ROLE</div>
                <a href="./use-cases/marketing-growth/index.html">Marketing & Growth</a>
                <a href="./use-cases/sales/index.html">Sales</a>
                <a href="./use-cases/support-cx/index.html">Support & CX</a>
                <a href="./use-cases/operations/index.html">Operations</a>
              </div>
            </div>
          </div>
        </div>

        <a href="./pricing/index.html" class="nav-tab">Pricing</a>
        <a href="./partners/index.html" class="nav-tab">Partner</a>

        <!-- RESOURCES MEGA MENU -->
        <div class="nav-dropdown-wrapper res-menu">
          <a class="nav-tab">Resources <span style="font-size: 10px; margin-left: 4px;">▼</span></a>
          <div class="mega-menu" style="min-width: 300px; left: auto; right: 0; transform: translateX(0) translateY(10px);">
            <div class="mega-grid" style="grid-template-columns: 1fr 1fr;">
              <div class="mega-col">
                <div class="mega-col-title">LEARN</div>
                <a href="./blog/index.html">Blog</a>
                <a href="./resources/ai-guides/index.html">AI Guides</a>
                <a href="./resources/case-studies/index.html">Case Studies</a>
              </div>
              <div class="mega-col">
                <div class="mega-col-title">COMPANY</div>
                <a href="./about/index.html">About</a>
                <a href="./team/index.html">Team • Careers</a>
                <a href="./note/index.html">Note • Contact</a>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <div class="nav-right">
        <a href="./partners/apply/index.html"><button class="btn-primary">Start free trial</button></a>
      </div>
    </div>
  </nav>"""

base_dir = r"c:\Users\user\Downloads\HOME STAEP AI"
for f in ["StepsAI_Redesign.html", "index.html"]:
    path = os.path.join(base_dir, f)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as file:
            c = file.read()
        c = re.sub(r'<nav class="nav" id="mainNav">.*?</nav>', nav, c, flags=re.DOTALL)
        with open(path, 'w', encoding='utf-8') as file:
            file.write(c)

print("Injected mega nav into root files.")
