import os
from build_v2 import GLOBAL_HEAD, NAV, FOOTER, render_s05

ABOUT_HTML = """
  <!-- S06 Compact Hero -->
  <section class="hero-v2" style="min-height: 40vh; padding: 160px 32px 40px;">
    <div class="hero-bg-glow"></div>
    <span class="kicker gsap-fade-up" style="font-family: 'Geist Mono', monospace; font-size: 11px; font-weight: 500; color: var(--accent); letter-spacing: .24em; text-transform: uppercase; margin-bottom: 24px;">ABOUT</span>
    <h1 class="gsap-fade-up" style="font-size: clamp(36px, 5vw, 64px); max-width: 1000px;">We're building the AI agent layer for every business.</h1>
    <p class="gsap-fade-up" style="margin-bottom:0; max-width: 700px;">Every business needs to talk to its customers at all hours. Almost none of them can afford to hire for it. That gap is the whole reason this company exists.</p>
  </section>

  <!-- S25 Beliefs (Bento Grid) -->
  <section class="section-v2" style="padding-top: 40px;">
    <h2 class="section-title-v2 gsap-fade-up" style="margin-bottom: 48px;">Our beliefs</h2>
    
    <div class="bento-grid" style="grid-template-columns: repeat(2, 1fr);">
      
      <div class="bento-card gsap-scale-in" style="justify-content: flex-start; min-height: 200px;">
        <h3 class="bento-title" style="margin-bottom: 12px; font-size: 20px;">AI should do things, not just talk.</h3>
        <p class="bento-desc" style="line-height: 1.6; margin: 0;">Most chatbots are glorified FAQ pages. We build agents that take real action: creating tickets, booking meetings, looking up orders, capturing leads. The difference between a chatbot and an agent is what happens after the conversation.</p>
      </div>

      <div class="bento-card gsap-scale-in" style="justify-content: flex-start; min-height: 200px;">
        <h3 class="bento-title" style="margin-bottom: 12px; font-size: 20px;">One brain is better than ten tools.</h3>
        <p class="bento-desc" style="line-height: 1.6; margin: 0;">Your customer data, your product catalogue, your support docs and your team's knowledge should not live in ten separate places that have never spoken to each other. StepsAI connects all of it into one brain that serves your customers and your team.</p>
      </div>

      <div class="bento-card gsap-scale-in" style="justify-content: flex-start; min-height: 200px;">
        <h3 class="bento-title" style="margin-bottom: 12px; font-size: 20px;">Setup should take minutes, not months.</h3>
        <p class="bento-desc" style="line-height: 1.6; margin: 0;">Enterprise AI should not need an enterprise budget or an enterprise timeline. We optimise for how fast you can get live, and we keep pushing on it.</p>
      </div>

      <div class="bento-card gsap-scale-in" style="justify-content: flex-start; min-height: 200px;">
        <h3 class="bento-title" style="margin-bottom: 12px; font-size: 20px;">Your AI should sound like you.</h3>
        <p class="bento-desc" style="line-height: 1.6; margin: 0;">Not like a generic assistant. Not like a customer service script somebody wrote in 2011. Like your business, with your tone and your rules.</p>
      </div>

      <div class="bento-card gsap-scale-in" style="justify-content: flex-start; min-height: 200px;">
        <h3 class="bento-title" style="margin-bottom: 12px; font-size: 20px;">Channels are surfaces, not silos.</h3>
        <p class="bento-desc" style="line-height: 1.6; margin: 0;">Your customer should not have to explain themselves twice because they moved from your website to WhatsApp. One agent, every channel, the same memory.</p>
      </div>

      <div class="bento-card gsap-scale-in" style="justify-content: flex-start; min-height: 200px;">
        <h3 class="bento-title" style="margin-bottom: 12px; font-size: 20px;">Every business deserves this.</h3>
        <p class="bento-desc" style="line-height: 1.6; margin: 0;">Not just companies with an AI team. A Shopify store, a local clinic, a two-person SaaS. Everyone should be able to put an intelligent agent to work in an afternoon.</p>
      </div>

    </div>
  </section>

  <!-- S37 Team Callout -->
  <section class="section-v2" style="background: var(--bg-surface-2); text-align: center; border-top: 1px solid var(--border-subtle);">
    <h2 class="gsap-fade-up" style="font-family: 'Outfit'; font-size: 32px; margin-bottom: 16px;">The team</h2>
    <p class="gsap-fade-up" style="color: var(--text-secondary); margin-bottom: 32px;">A small team building the agent layer for every business.</p>
    <a href="/team/" class="gsap-fade-up" style="text-decoration:none;"><button class="btn-primary">See our team →</button></a>
  </section>
"""

html = GLOBAL_HEAD.format(title="About") + NAV + ABOUT_HTML + FOOTER
dir_path = os.path.join("about")
os.makedirs(dir_path, exist_ok=True)
with open(os.path.join(dir_path, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)
print("Built /about/")
