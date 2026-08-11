import os
import shutil
from build_v2 import GLOBAL_HEAD, NAV, FOOTER, render_s05

HOME_CSS = """
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
    .accordion-panel:hover {{
      flex: 3;
    }}
    .accordion-content {{
      position: absolute; bottom: 0; left: 0; width: 100%;
      padding: 32px; color: white; z-index: 2;
      display: flex; flex-direction: column; justify-content: flex-end;
    }}
    .accordion-title {{
      font-family: 'Outfit', sans-serif;
      font-size: 28px; font-weight: 700; margin: 0;
      white-space: nowrap;
    }}
    .accordion-desc {{
      font-size: 16px; color: rgba(255,255,255,0.8);
      margin-top: 12px; line-height: 1.5;
      opacity: 0; transform: translateY(10px);
      transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .accordion-panel:hover .accordion-desc {{
      opacity: 1; transform: translateY(0);
      transition-delay: 0.1s;
    }}
    
    /* Mockup Showcase */
    .mockup-container {{
      position: relative; max-width: 1000px; margin: 0 auto;
      border-radius: 24px; overflow: hidden;
      box-shadow: 0 40px 80px -20px rgba(0,0,0,0.2);
      border: 1px solid var(--border-subtle);
    }}
    .mockup-container img {{
      width: 100%; height: auto; display: block;
    }}
"""

# Modify the global head to inject the home css
head_split = GLOBAL_HEAD.split('</style>')
HOME_HEAD = head_split[0] + HOME_CSS + '</style>' + head_split[1]

HOME_HTML = """
  <!-- S04 Landing Hero (Modified for V2 GSAP) -->
  <section class="hero-v2" style="padding: 180px 32px 100px;">
    <div class="hero-bg-glow"></div>
    <span class="kicker gsap-fade-up" style="font-family: 'Geist Mono', monospace; font-size: 11px; font-weight: 500; color: var(--accent); letter-spacing: .24em; text-transform: uppercase; margin-bottom: 24px;">AI AGENT FOR SALES & SUPPORT</span>
    <h1 class="gsap-fade-up" style="font-size: clamp(48px, 7vw, 96px); max-width: 1100px;">It answers.<br>Then it acts.</h1>
    <p class="gsap-fade-up" style="font-size: 24px; max-width: 800px;">StepsAI answers customer questions on WhatsApp, Instagram and your website. Then it books the meeting, saves the lead, or updates the order. Nobody on your team has to be awake for it.</p>
    <div class="hero-actions gsap-fade-up" style="display:flex; gap:16px;">
      <a href="/partners/apply/"><button class="btn-primary" style="padding: 16px 32px; font-size: 18px;">Start free trial</button></a>
      <button class="btn-outline" style="padding: 16px 32px; font-size: 18px;">Book a demo</button>
    </div>
  </section>

  <!-- Real Mockup Showcase (Injecting Life) -->
  <section class="section-v2" style="padding-top:0;">
    <div class="mockup-container gsap-scale-in">
      <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1600&q=80" alt="StepsAI Dashboard Mockup" style="opacity: 0.9;">
    </div>
  </section>

  <!-- S09 Interactive Industries Accordion -->
  <section class="section-v2" style="background: var(--bg-surface-2);">
    <div style="text-align: center; margin-bottom: 64px;">
      <span style="font-family: 'Geist Mono', monospace; font-size: 12px; color: var(--text-secondary); letter-spacing: .2em; text-transform: uppercase;">BUILT AROUND YOUR BUSINESS</span>
      <h2 style="font-family: 'Outfit'; font-size: 48px; margin-top: 16px; color: var(--text-primary);">Made for the way your customers buy.</h2>
    </div>
    
    <div class="industries-accordion gsap-fade-up">
      <!-- Healthcare -->
      <a href="/solutions/healthcare/" class="accordion-panel" style="background-image: url('https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=800&q=80'); text-decoration:none;">
        <div class="accordion-content">
          <h3 class="accordion-title">Healthcare & Wellness</h3>
          <p class="accordion-desc">Shows which doctor is free. Books the appointment inside the conversation. Sends the reminder so the slot isn't wasted.</p>
        </div>
      </a>
      <!-- Real Estate -->
      <a href="/solutions/real-estate/" class="accordion-panel" style="background-image: url('https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=800&q=80'); text-decoration:none;">
        <div class="accordion-content">
          <h3 class="accordion-title">Real Estate</h3>
          <p class="accordion-desc">Qualifies the buyer before anyone picks up the phone. Books the site visit while they're still looking.</p>
        </div>
      </a>
      <!-- Ecommerce -->
      <a href="/solutions/ecommerce/" class="accordion-panel" style="background-image: url('https://images.unsplash.com/photo-1607082348824-0a96f2a4b9da?w=800&q=80'); text-decoration:none;">
        <div class="accordion-content">
          <h3 class="accordion-title">Ecommerce</h3>
          <p class="accordion-desc">Checks live stock before it promises anything. Recovers the cart before the customer forgets.</p>
        </div>
      </a>
      <!-- SaaS -->
      <a href="/solutions/saas/" class="accordion-panel" style="background-image: url('https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&q=80'); text-decoration:none;">
        <div class="accordion-content">
          <h3 class="accordion-title">SaaS & Tech</h3>
          <p class="accordion-desc">Answers integration questions from your own docs. Compares plans without pushing the expensive one.</p>
        </div>
      </a>
    </div>
  </section>

  <!-- S08 Four Agents (V2 GSAP Bento) -->
  <section class="section-v2">
    <h2 class="section-title-v2 gsap-fade-up">Four jobs. One agent that knows your business.</h2>
    <div class="bento-grid">
      <div class="bento-card gsap-scale-in">
        <h3 class="bento-title">Sales Agent</h3>
        <p class="bento-desc">Recommends products, checks what's in stock, and closes the sale.</p>
      </div>
      <div class="bento-card gsap-scale-in">
        <h3 class="bento-title">Lead Agent</h3>
        <p class="bento-desc">Asks the right questions, then saves the lead straight to your CRM.</p>
      </div>
      <div class="bento-card gsap-scale-in">
        <h3 class="bento-title">Meetings Agent</h3>
        <p class="bento-desc">Offers times that are actually free, and books them.</p>
      </div>
      <div class="bento-card gsap-scale-in">
        <h3 class="bento-title">Support Agent</h3>
        <p class="bento-desc">Tracks orders, answers questions, and sorts out problems.</p>
      </div>
    </div>
  </section>
"""

html = HOME_HEAD.format(title="Home") + NAV + HOME_HTML + FOOTER

# Write to both index.html and StepsAI_Redesign.html
with open(os.path.join("index.html"), "w", encoding="utf-8") as f:
    f.write(html)
with open(os.path.join("StepsAI_Redesign.html"), "w", encoding="utf-8") as f:
    f.write(html)
    
print("Built /index.html and StepsAI_Redesign.html")
