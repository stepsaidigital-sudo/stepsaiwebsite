import os
from build_v2 import GLOBAL_HEAD, NAV, FOOTER, render_s05

PRICING_HTML = """
  <!-- S06 Compact Hero -->
  <section class="hero-v2" style="min-height: 40vh; padding: 160px 32px 40px;">
    <div class="hero-bg-glow"></div>
    <span class="kicker gsap-fade-up" style="font-family: 'Geist Mono', monospace; font-size: 11px; font-weight: 500; color: var(--accent); letter-spacing: .24em; text-transform: uppercase; margin-bottom: 24px;">PRICING</span>
    <h1 class="gsap-fade-up" style="font-size: clamp(36px, 5vw, 64px);">Pay for conversations, not seats.</h1>
    <p class="gsap-fade-up" style="margin-bottom:0;">Start with a 14-day free trial. Cancel anytime.</p>
  </section>

  <!-- S26 Plan Cards -->
  <section class="section-v2" style="padding-top: 40px;">
    <div class="bento-grid" style="grid-template-columns: repeat(3, 1fr); gap: 24px;">
      
      <!-- Starter -->
      <div class="bento-card gsap-scale-in" style="justify-content: flex-start;">
        <h3 style="font-family: 'Outfit'; font-size: 24px; margin-bottom: 8px;">Starter</h3>
        <p style="color: var(--text-secondary); margin-bottom: 24px;">For new businesses automating their first channel.</p>
        <div style="font-size: 48px; font-weight: 800; font-family: 'Outfit'; margin-bottom: 8px;">$27<span style="font-size:16px; color:var(--text-secondary); font-weight:400;">/mo</span></div>
        <p style="font-family: 'Geist Mono', monospace; font-size: 12px; color: var(--accent); margin-bottom: 32px;">INCLUDES 1,000 CONVERSATIONS</p>
        <ul style="list-style: none; padding: 0; margin: 0 0 40px; color: var(--text-secondary); font-size: 15px; line-height: 2;">
          <li>✓ 1 active channel</li>
          <li>✓ 3 connected apps</li>
          <li>✓ 30-day history</li>
          <li>✓ Standard support</li>
        </ul>
        <a href="/partners/apply/" style="text-decoration:none;"><button class="btn-outline" style="width: 100%;">Start free trial</button></a>
      </div>

      <!-- Growth -->
      <div class="bento-card gsap-scale-in" style="justify-content: flex-start; border-color: var(--accent); box-shadow: var(--shadow-lg); transform: translateY(-8px);">
        <div style="position: absolute; top: 24px; right: 24px; background: var(--accent); color: white; padding: 4px 12px; border-radius: 100px; font-size: 11px; font-weight: 700; letter-spacing: 0.5px;">MOST POPULAR</div>
        <h3 style="font-family: 'Outfit'; font-size: 24px; margin-bottom: 8px; color: var(--accent);">Growth</h3>
        <p style="color: var(--text-secondary); margin-bottom: 24px;">For scaling teams running omnichannel support.</p>
        <div style="font-size: 48px; font-weight: 800; font-family: 'Outfit'; margin-bottom: 8px;">$76<span style="font-size:16px; color:var(--text-secondary); font-weight:400;">/mo</span></div>
        <p style="font-family: 'Geist Mono', monospace; font-size: 12px; color: var(--accent); margin-bottom: 32px;">INCLUDES 5,000 CONVERSATIONS</p>
        <ul style="list-style: none; padding: 0; margin: 0 0 40px; color: var(--text-secondary); font-size: 15px; line-height: 2;">
          <li>✓ Unlimited channels</li>
          <li>✓ Unlimited apps</li>
          <li>✓ 1-year history</li>
          <li>✓ Priority support</li>
        </ul>
        <a href="/partners/apply/" style="text-decoration:none;"><button class="btn-primary" style="width: 100%;">Start free trial</button></a>
      </div>

      <!-- Scale -->
      <div class="bento-card gsap-scale-in" style="justify-content: flex-start; background: #0F172A; color: white;">
        <h3 style="font-family: 'Outfit'; font-size: 24px; margin-bottom: 8px; color: white;">Scale</h3>
        <p style="color: #94A3B8; margin-bottom: 24px;">For high-volume operations needing dedicated limits.</p>
        <div style="font-size: 48px; font-weight: 800; font-family: 'Outfit'; margin-bottom: 8px; color: white;">$207<span style="font-size:16px; color: #94A3B8; font-weight:400;">/mo</span></div>
        <p style="font-family: 'Geist Mono', monospace; font-size: 12px; color: #38BDF8; margin-bottom: 32px;">INCLUDES 25,000 CONVERSATIONS</p>
        <ul style="list-style: none; padding: 0; margin: 0 0 40px; color: #94A3B8; font-size: 15px; line-height: 2;">
          <li>✓ Custom AI guardrails</li>
          <li>✓ Custom SLA</li>
          <li>✓ Infinite history</li>
          <li>✓ Dedicated Slack channel</li>
        </ul>
        <a href="/partners/apply/" style="text-decoration:none;"><button class="btn-outline" style="width: 100%; border-color: rgba(255,255,255,0.2); color: white; background: transparent;">Start free trial</button></a>
      </div>

    </div>
  </section>

  <!-- S27 Every plan includes -->
  <section class="section-v2" style="background: var(--bg-surface-2); padding: 80px 32px; border-top: 1px solid var(--border-subtle); border-bottom: 1px solid var(--border-subtle);">
    <div style="max-width: 1200px; margin: 0 auto; display: flex; flex-wrap: wrap; justify-content: space-between; gap: 24px;">
      <h3 style="font-family: 'Outfit'; font-size: 20px; width: 100%; margin-bottom: 24px;">Every plan includes:</h3>
      <div style="display:flex; align-items:center; gap:8px; font-weight:600;"><span style="color:var(--accent);">✓</span> 14-day free trial</div>
      <div style="display:flex; align-items:center; gap:8px; font-weight:600;"><span style="color:var(--accent);">✓</span> All 4 Agent Types</div>
      <div style="display:flex; align-items:center; gap:8px; font-weight:600;"><span style="color:var(--accent);">✓</span> One Inbox</div>
      <div style="display:flex; align-items:center; gap:8px; font-weight:600;"><span style="color:var(--accent);">✓</span> Human Handoff</div>
    </div>
  </section>

  <!-- S29 Conversation Counting -->
  <section class="section-v2">
    <div class="bento-card gsap-fade-up" style="max-width: 800px; margin: 0 auto; text-align:center;">
      <h2 style="font-family: 'Outfit'; font-size: 32px; margin-bottom: 16px;">How does a conversation count?</h2>
      <p style="color: var(--text-secondary); font-size: 16px; line-height: 1.6; margin-bottom: 24px;">
        A conversation is a 24-hour window with a specific customer. Once they message you (or you message them), 1 conversation is deducted from your quota. You can send 1 message or 100 messages within that 24-hour block—it only costs 1 conversation.
      </p>
      <div style="background: var(--bg-surface-2); padding: 16px; border-radius: 12px; font-family: 'Geist Mono', monospace; font-size: 13px; color: var(--text-primary); text-align:left;">
        Customer: "Where is my order?" <span style="color:var(--text-secondary);">[10:00 AM]</span><br>
        Agent: "It arrives tomorrow." <span style="color:var(--text-secondary);">[10:01 AM]</span><br>
        Customer: "Can you change the address?" <span style="color:var(--text-secondary);">[11:30 AM]</span><br>
        Agent: "Done." <span style="color:var(--text-secondary);">[11:30 AM]</span><br>
        <br>
        <span style="color:var(--accent);">→ TOTAL COST: 1 CONVERSATION</span>
      </div>
    </div>
  </section>

  <!-- S24 FAQ -->
  <section class="section-v2" style="background: var(--bg-surface-2); padding-bottom: 120px;">
    <h2 class="section-title-v2 gsap-fade-up" style="margin-bottom: 48px;">Billing FAQ</h2>
    <div style="max-width: 800px; margin: 0 auto;">
      
      <div class="gsap-fade-up" style="background: var(--bg-surface); padding: 32px; border-radius: 16px; margin-bottom: 16px; border: 1px solid var(--border-subtle);">
        <h3 style="font-family: 'Outfit'; font-size: 20px; margin-bottom: 12px;">What happens if I go over my quota?</h3>
        <p style="color: var(--text-secondary); line-height: 1.5; margin:0;">Your agents don't stop working. We will automatically add a $10 top-up pack which gives you an additional 500 conversations for the remainder of the month.</p>
      </div>

      <div class="gsap-fade-up" style="background: var(--bg-surface); padding: 32px; border-radius: 16px; margin-bottom: 16px; border: 1px solid var(--border-subtle);">
        <h3 style="font-family: 'Outfit'; font-size: 20px; margin-bottom: 12px;">Do you have annual billing?</h3>
        <p style="color: var(--text-secondary); line-height: 1.5; margin:0;">Yes, annual plans are available at checkout and come with a 20% discount.</p>
      </div>

    </div>
  </section>
"""

html = GLOBAL_HEAD.format(title="Pricing") + NAV + PRICING_HTML + FOOTER
dir_path = os.path.join("pricing")
os.makedirs(dir_path, exist_ok=True)
with open(os.path.join(dir_path, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)
print("Built /pricing/")
