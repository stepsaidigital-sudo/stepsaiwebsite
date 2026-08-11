import os
import re

with open('build_v10_compiler.py', 'r', encoding='utf-8') as f:
    code = f.read()

# We need to add CUSTOM_FOUR_AGENTS and intercept it in the loop
CUSTOM_FOUR_AGENTS = """
  <section class="section-v2" style="padding-top: 160px; max-width: 1200px;">
    <div style="text-align: center; margin-bottom: 80px;">
      <span class="gsap-fade-up" style="font-family: 'Geist Mono', monospace; font-size: 12px; color: var(--accent); letter-spacing: .2em; text-transform: uppercase;">FOUR AGENTS, ONE BRAIN</span>
      <h2 class="gsap-fade-up" style="font-family: 'Outfit'; font-size: clamp(40px, 5vw, 56px); margin: 16px 0 24px; color: var(--text-primary);">Four jobs. One memory.</h2>
      <p class="gsap-fade-up" style="font-size: 20px; color: var(--text-secondary); max-width: 700px; margin: 0 auto; line-height: 1.6;">Your support agent knows what your sales agent promised yesterday. That sounds obvious until you have used four separate tools that all forgot.</p>
    </div>

    <div class="bento-grid gsap-fade-up" style="grid-template-columns: repeat(2, 1fr); gap: 32px;">
      
      <!-- Sales Agent -->
      <div class="bento-card" style="padding: 40px; background: #fbfbfd; border: 1px solid var(--border-subtle); display: flex; flex-direction: column; justify-content: space-between; min-height: 400px; border-radius: 32px;">
        <div>
          <h3 style="font-family: 'Outfit'; font-size: 28px; margin-bottom: 16px; color: var(--text-primary);">Sales Agent</h3>
          <p style="color: var(--text-secondary); font-size: 16px; line-height: 1.5;">Checks what is actually in stock before it promises anything, then closes.</p>
        </div>
        <div class="micro-mockup" style="background: #EFEAE2; border-radius: 16px; padding: 16px; margin-top: 32px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 1px solid rgba(0,0,0,0.05);">
          <div class="chat-bubble in" style="color: #111;">Do you have this in large?</div>
          <div class="chat-bubble out" style="color: #111; margin-top: 8px;">Yes, two left! Added to cart.</div>
          <div class="receipt-pill" style="opacity: 1; transform: scale(1); margin: 12px auto 0; box-shadow: none; border: 1px solid rgba(11,158,88,0.2);"><span class="check">✓</span> <span>SHOPIFY</span></div>
        </div>
      </div>

      <!-- Lead Agent -->
      <div class="bento-card" style="padding: 40px; background: #fbfbfd; border: 1px solid var(--border-subtle); display: flex; flex-direction: column; justify-content: space-between; min-height: 400px; border-radius: 32px;">
        <div>
          <h3 style="font-family: 'Outfit'; font-size: 28px; margin-bottom: 16px; color: var(--text-primary);">Lead Agent</h3>
          <p style="color: var(--text-secondary); font-size: 16px; line-height: 1.5;">Finds out budget and timeline the way a good salesperson would, then writes it into your CRM.</p>
        </div>
        <div class="micro-mockup" style="background: #fff; border-radius: 16px; padding: 16px; margin-top: 32px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 1px solid var(--border-subtle);">
          <div style="font-family: 'Inter'; font-size: 12px; color: var(--text-tertiary); margin-bottom: 12px; text-transform: uppercase; letter-spacing: 1px;">HubSpot CRM</div>
          <div style="background: #f4f5f7; border-radius: 8px; padding: 12px; border-left: 3px solid #ff7a59;">
            <div style="font-weight: 600; color: #111; font-size: 14px;">New Lead: Sarah Jenkins</div>
            <div style="color: var(--text-secondary); font-size: 12px; margin-top: 4px;">Budget: $5k-$10k · Timeline: Q3</div>
          </div>
          <div class="receipt-pill" style="opacity: 1; transform: scale(1); margin: 12px auto 0; box-shadow: none; border: 1px solid rgba(11,158,88,0.2);"><span class="check">✓</span> <span>HUBSPOT</span></div>
        </div>
      </div>

      <!-- Meetings Agent -->
      <div class="bento-card" style="padding: 40px; background: #fbfbfd; border: 1px solid var(--border-subtle); display: flex; flex-direction: column; justify-content: space-between; min-height: 400px; border-radius: 32px;">
        <div>
          <h3 style="font-family: 'Outfit'; font-size: 28px; margin-bottom: 16px; color: var(--text-primary);">Meetings Agent</h3>
          <p style="color: var(--text-secondary); font-size: 16px; line-height: 1.5;">Offers times that are genuinely free, and puts the meeting in your calendar.</p>
        </div>
        <div class="micro-mockup" style="background: #fff; border-radius: 16px; padding: 16px; margin-top: 32px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 1px solid var(--border-subtle);">
          <div class="chat-bubble in ig-in" style="color: #111;">I want to book a site visit.</div>
          <div class="chat-bubble out ig-out" style="margin-top: 8px;">Saturday 11 AM works perfectly!</div>
          <div class="receipt-pill" style="opacity: 1; transform: scale(1); margin: 12px auto 0; box-shadow: none; border: 1px solid rgba(11,158,88,0.2);"><span class="check">✓</span> <span>CALENDAR</span></div>
        </div>
      </div>

      <!-- Support Agent -->
      <div class="bento-card" style="padding: 40px; background: #fbfbfd; border: 1px solid var(--border-subtle); display: flex; flex-direction: column; justify-content: space-between; min-height: 400px; border-radius: 32px;">
        <div>
          <h3 style="font-family: 'Outfit'; font-size: 28px; margin-bottom: 16px; color: var(--text-primary);">Support Agent</h3>
          <p style="color: var(--text-secondary); font-size: 16px; line-height: 1.5;">Tracks the order, explains the return policy, and only wakes you if something is actually wrong.</p>
        </div>
        <div class="micro-mockup" style="background: #fff; border-radius: 16px; padding: 16px; margin-top: 32px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 1px solid var(--border-subtle);">
          <div class="chat-bubble in ig-in" style="color: #111; border-radius: 4px;">Where is my order?</div>
          <div class="chat-bubble out ig-in" style="color: #111; margin-top: 8px; border-radius: 4px; border: 1px solid #efefef;">It is out for delivery today at 6PM!</div>
          <div class="receipt-pill" style="opacity: 1; transform: scale(1); margin: 12px auto 0; box-shadow: none; border: 1px solid rgba(11,158,88,0.2);"><span class="check">✓</span> <span>ZENDESK</span></div>
        </div>
      </div>

    </div>
  </section>
"""

# Modify the route exclusion to include "" (Home) so it builds the home page too
code = code.replace('if data["route"] not in ["pricing", "about", "partners"]:', 'if data["route"] not in ["pricing", "about", "partners", ""]:')

# Add the CUSTOM_FOUR_AGENTS variable
code = code.replace('CUSTOM_PRICING_HTML = """', CUSTOM_FOUR_AGENTS + '\n\nCUSTOM_PRICING_HTML = """')

# Inject into the loop
inject_logic = """
    for block in data["blocks"]:
        if not block["title"] or "Hero" in block["title"]: continue
        
        if data["route"] == "" and "Industries" in block["title"]:
            html_content += CUSTOM_HOME_ACCORDION
            continue
            
        if data["route"] == "" and "Four Agents" in block["title"]:
            html_content += CUSTOM_FOUR_AGENTS
            continue
"""

# I need to rewrite the loop part for the home page since the previous v10 compiler stripped the home page loop logic out to just handle the 3 pages.
# Let's completely rewrite the compiler script to be safe.
"""

new_code = """import os
import re

GLOBAL_HEAD = \"\"\"<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>StepsAI - {title}</title>
  <link rel="stylesheet" href="{root_prefix}assets/css/style.css">
  <link href="https://fonts.googleapis.com/css2?family=Geist+Mono:wght@400;500;700&family=Inter:wght@400;500;600&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
  <style>
    .gsap-fade-up {{ opacity: 0; transform: translateY(40px); }}
    .gsap-scale-in {{ opacity: 0; transform: scale(0.9); }}
    
    .hero-v2 {{ min-height: 80vh; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 160px 32px 80px; position: relative; overflow: hidden; }}
    .hero-v2.split-hero {{ flex-direction: row; text-align: left; max-width: 1300px; margin: 0 auto; gap: 64px; }}
    @media (max-width: 1000px) {{ .hero-v2.split-hero {{ flex-direction: column; text-align: center; }} }}
    
    .hero-bg-glow {{ position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 80vw; height: 80vw; background: radial-gradient(circle, var(--accent-tint) 0%, rgba(251,252,254,0) 70%); z-index: -1; }}
    .hero-v2 h1 {{ font-size: clamp(48px, 6vw, 80px); line-height: 1.05; letter-spacing: -2px; font-family: 'Outfit', sans-serif; }}
    .hero-v2 p {{ font-size: 20px; color: var(--text-secondary); max-width: 720px; line-height: 1.6; }}
    
    .section-v2 {{ padding: 112px 32px; max-width: 1400px; margin: 0 auto; }}
    .section-title-v2 {{ font-size: clamp(36px, 4vw, 54px); letter-spacing: -1px; margin-bottom: 80px; font-family: 'Outfit', sans-serif; text-align: center;}}
    
    .bento-grid {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px; grid-auto-flow: dense; }}
    .bento-card {{ background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 24px; padding: 48px; position: relative; overflow: hidden; display: flex; flex-direction: column; transition: transform 0.5s cubic-bezier(.16,1,.3,1), border-color 0.5s, box-shadow 0.5s; box-shadow: var(--shadow); }}
    .bento-card:hover {{ transform: translateY(-8px); border-color: var(--accent); box-shadow: var(--shadow-lg); }}
    .bento-title {{ font-size: 32px; font-weight: 700; margin-bottom: 16px; font-family: 'Outfit', sans-serif; color: var(--text-primary);}}
    .bento-desc {{ color: var(--text-secondary); font-size: 16px; line-height: 1.6; }}
    @media (max-width: 992px) {{ .bento-grid {{ grid-template-columns: 1fr; }} }}
    
    .industries-accordion {{ max-width: 1200px; margin: 0 auto; display: flex; gap: 16px; height: 500px; }}
    .accordion-panel {{ position: relative; flex: 1; border-radius: 24px; overflow: hidden; background-size: cover; background-position: center; transition: flex 0.6s cubic-bezier(0.16, 1, 0.3, 1); cursor: pointer; }}
    .accordion-panel::after {{ content: ''; position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0) 100%); transition: opacity 0.4s; }}
    .accordion-panel:hover {{ flex: 3; }}
    .accordion-content {{ position: absolute; bottom: 0; left: 0; width: 100%; padding: 32px; color: white; z-index: 2; display: flex; flex-direction: column; justify-content: flex-end; }}
    .accordion-title {{ font-family: 'Outfit', sans-serif; font-size: 28px; font-weight: 700; margin: 0; white-space: nowrap; }}
    .accordion-desc {{ font-size: 16px; color: rgba(255,255,255,0.8); margin-top: 12px; line-height: 1.5; opacity: 0; transform: translateY(10px); transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); }}
    .accordion-panel:hover .accordion-desc {{ opacity: 1; transform: translateY(0); transition-delay: 0.1s; }}
    
    .step-line-container {{ position: fixed; top: 0; left: 40px; width: 6px; height: 100%; z-index: 0; pointer-events: none; }}
    .step-line {{ width: 2px; height: 100%; background: var(--line); position: absolute; left: 2px; }}
    .step-line-progress {{ width: 2px; height: 0%; background: var(--accent); position: absolute; left: 2px; transition: height 0.1s linear; }}
    
    .phone-mockup {{ width: 340px; height: 640px; background: #fff; border-radius: 48px; box-shadow: 0 32px 80px rgba(0,0,0,0.15), inset 0 0 0 10px #e0e4e8, inset 0 0 0 12px #f4f5f7; position: relative; overflow: hidden; display: flex; flex-direction: column; flex-shrink:0; }}
    .phone-notch {{ position: absolute; top: 10px; left: 50%; transform: translateX(-50%); width: 120px; height: 28px; background: #e0e4e8; border-radius: 14px; z-index: 10; }}
    .mockup-screen {{ position: absolute; inset: 12px; border-radius: 36px; overflow: hidden; display: flex; flex-direction: column; background:#fff; z-index:1; opacity:0; }}
    .mockup-header {{ height: 80px; padding: 40px 16px 12px; display: flex; align-items: center; gap: 12px; font-family: 'Inter', sans-serif; }}
    .mockup-header.whatsapp {{ background: #008069; color: white; }}
    .mockup-header.instagram {{ background: #fff; color: #111; border-bottom: 1px solid #efefef; }}
    .mockup-body {{ flex: 1; padding: 16px; display: flex; flex-direction: column; gap: 12px; background: #EFEAE2; font-family: 'Inter', sans-serif; }}
    .mockup-body.instagram {{ background: #fff; }}
    .chat-bubble {{ max-width: 85%; padding: 12px 14px; border-radius: 12px; font-size: 14px; line-height: 1.4; position: relative; }}
    .chat-bubble.in {{ align-self: flex-start; background: #fff; border-top-left-radius: 4px; box-shadow: 0 1px 2px rgba(0,0,0,0.05); color:#111; }}
    .chat-bubble.out {{ align-self: flex-end; background: #D9FDD3; border-top-right-radius: 4px; box-shadow: 0 1px 2px rgba(0,0,0,0.05); color:#111; }}
    .chat-bubble.ig-in {{ background: #efefef; border-radius: 18px; color:#111; }}
    .chat-bubble.ig-out {{ background: linear-gradient(135deg, #4F5BD5, #962FBF); color: white; border-radius: 18px; }}
    .chat-time {{ font-size: 10px; color: rgba(0,0,0,0.4); float: right; margin: 8px 0 -4px 8px; }}
    .chat-time.out {{ color: rgba(0,0,0,0.5); }}
    .receipt-pill {{ display: inline-flex; align-items: center; justify-content:center; gap: 8px; background: #E9F8F0; border-radius: 8px; padding: 8px 16px; font-family: 'Geist Mono', monospace; font-size: 11px; font-weight: 500; color: #0C1322; letter-spacing: 0.12em; text-transform: uppercase; margin-top: 16px; align-self:center; opacity: 0; transform: scale(0.94); box-shadow:0 4px 12px rgba(11,158,88,0.15); }}
    .receipt-pill .check {{ color: #0B9E58; font-size: 14px; font-weight: 800; }}
    .receipt-pill span {{ color: #46536B; }}
    
    .micro-mockup {{ transition: 0.3s; transform: translateY(10px); }}
    .bento-card:hover .micro-mockup {{ transform: translateY(0); box-shadow: 0 20px 40px rgba(0,0,0,0.08) !important; }}
    
    .typing {{ display:flex; gap:4px; padding:16px 20px; align-items:center; }}
    .dot {{ width:6px; height:6px; background:rgba(0,0,0,0.3); border-radius:50%; animation: type 1.4s infinite ease-in-out both; }}
    .dot:nth-child(1) {{ animation-delay: -0.32s; }}
    .dot:nth-child(2) {{ animation-delay: -0.16s; }}
    @keyframes type {{ 0%, 80%, 100% {{ transform: scale(0); }} 40% {{ transform: scale(1); }} }}
  </style>
</head>
<body>
  <div class="step-line-container">
    <div class="step-line"></div>
    <div class="step-line-progress" id="stepLineProgress"></div>
  </div>
\"\"\"

CUSTOM_HOME_HERO = \"\"\"
  <!-- S01 Landing Hero - Animated Mockup -->
  <section class="hero-v2 split-hero">
    <div class="hero-bg-glow"></div>
    <div style="flex:1;">
      <span class="kicker gsap-fade-up" style="font-family: 'Geist Mono', monospace; font-size: 11px; font-weight: 500; color: var(--accent); letter-spacing: .24em; text-transform: uppercase; margin-bottom: 24px; display:block;">AI AGENT FOR SALES & SUPPORT</span>
      <h1 class="gsap-fade-up" style="margin-bottom: 24px;">It answers.<br>Then it acts.</h1>
      <p class="gsap-fade-up" style="margin-bottom: 48px;">StepsAI answers customer questions on WhatsApp, Instagram and your website. Then it books the meeting, saves the lead, or updates the order. Nobody on your team has to be awake for it.</p>
      <div class="hero-actions gsap-fade-up" style="display:flex; gap:16px;">
        <a href="./partners/apply/index.html"><button class="btn-primary" style="padding: 16px 32px; font-size: 18px;">Start free trial</button></a>
        <button class="btn-outline" style="padding: 16px 32px; font-size: 18px;">Book a demo</button>
      </div>
      <div class="gsap-fade-up" style="margin-top:24px; font-size:14px; color:var(--text-tertiary);">Works with Shopify, HubSpot, Calendly and your inbox.</div>
    </div>
    <div class="hero-mockup-wrapper gsap-scale-in" style="flex:1; display:flex; justify-content:center; align-items:center;">
      <div class="phone-mockup">
        <div class="phone-notch"></div>
        <div class="mockup-screen" id="screen-wa" style="opacity:1; z-index:2;">
          <div class="mockup-header whatsapp">
            <div style="width:36px; height:36px; border-radius:50%; background:#fff; display:flex; align-items:center; justify-content:center; color:#008069; font-weight:800; font-size:18px;">S</div>
            <div style="line-height:1.2; font-weight:600; font-size:15px;">StepsAI<br><span style="font-size:12px; font-weight:400; opacity:0.8;">Online</span></div>
          </div>
          <div class="mockup-body">
            <div class="chat-bubble in stp-1">Do you have the linen shirt in medium? <span class="chat-time">10:42 PM</span></div>
            <div class="chat-bubble out typing stp-t1"><div class="dot"></div><div class="dot"></div><div class="dot"></div></div>
            <div class="chat-bubble out stp-2" style="display:none;">Yes, two left in medium. Want me to hold one? <span class="chat-time out">10:42 PM</span></div>
            <div class="chat-bubble in stp-3" style="opacity:0; transform:translateY(10px);">Yes please <span class="chat-time">10:43 PM</span></div>
            <div class="chat-bubble out typing stp-t2" style="display:none;"><div class="dot"></div><div class="dot"></div><div class="dot"></div></div>
            <div class="chat-bubble out stp-4" style="display:none;">Reserved and added to your cart.<br><b style="display:block; margin-top:8px; padding-top:8px; border-top:1px solid rgba(0,0,0,0.1);">Linen Shirt · Medium · ₹2,400</b> <span class="chat-time out">10:43 PM</span></div>
            <div class="receipt-pill stp-5"><span class="check">✓</span> <span>SHOPIFY</span> · CART UPDATED</div>
          </div>
        </div>
        <div class="mockup-screen" id="screen-ig" style="opacity:0; z-index:1;">
          <div class="mockup-header instagram">
            <div style="width:36px; height:36px; border-radius:50%; background:linear-gradient(135deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%); padding:2px; display:flex; align-items:center; justify-content:center;"><div style="width:100%; height:100%; background:#fff; border-radius:50%;"></div></div>
            <div style="line-height:1.2; font-weight:600; font-size:15px; color:#111;">StepsAI Real Estate<br><span style="font-size:12px; font-weight:400; color:#888;">StepsAI Real Estate</span></div>
          </div>
          <div class="mockup-body instagram">
            <div class="chat-bubble in ig-in stp-ig-1">Is the 3BHK still available? <span class="chat-time">9:15 PM</span></div>
            <div class="chat-bubble out ig-out typing stp-ig-t1"><div class="dot" style="background:rgba(255,255,255,0.5);"></div><div class="dot" style="background:rgba(255,255,255,0.5);"></div><div class="dot" style="background:rgba(255,255,255,0.5);"></div></div>
            <div class="chat-bubble out ig-out stp-ig-2" style="display:none;">It is. Want to see it this weekend? <span class="chat-time out" style="color:rgba(255,255,255,0.7);">9:15 PM</span></div>
            <div class="chat-bubble in ig-in stp-ig-3" style="opacity:0; transform:translateY(10px);">Saturday works <span class="chat-time">9:16 PM</span></div>
            <div class="chat-bubble out ig-out typing stp-ig-t2" style="display:none;"><div class="dot" style="background:rgba(255,255,255,0.5);"></div><div class="dot" style="background:rgba(255,255,255,0.5);"></div><div class="dot" style="background:rgba(255,255,255,0.5);"></div></div>
            <div class="chat-bubble out ig-out stp-ig-4" style="display:none;">Booked for Saturday 11 AM. Sending the address.<br><div style="display:flex; gap:8px; margin-top:8px;"><span style="background:rgba(255,255,255,0.2); padding:4px 8px; border-radius:8px; font-size:12px;">Sat 11:00</span><span style="background:rgba(255,255,255,0.2); padding:4px 8px; border-radius:8px; font-size:12px;">Sat 4:00</span></div><span class="chat-time out" style="color:rgba(255,255,255,0.7);">9:16 PM</span></div>
            <div class="receipt-pill stp-ig-5"><span class="check">✓</span> <span>CALENDAR</span> · VISIT BOOKED</div>
          </div>
        </div>
      </div>
    </div>
  </section>
\"\"\"

CUSTOM_FOUR_AGENTS = \"\"\"
  <section class="section-v2" style="padding-top: 160px; max-width: 1200px;">
    <div style="text-align: center; margin-bottom: 80px;">
      <span class="gsap-fade-up" style="font-family: 'Geist Mono', monospace; font-size: 12px; color: var(--accent); letter-spacing: .2em; text-transform: uppercase;">FOUR AGENTS, ONE BRAIN</span>
      <h2 class="gsap-fade-up" style="font-family: 'Outfit'; font-size: clamp(40px, 5vw, 56px); margin: 16px 0 24px; color: var(--text-primary);">Four jobs. One memory.</h2>
      <p class="gsap-fade-up" style="font-size: 20px; color: var(--text-secondary); max-width: 700px; margin: 0 auto; line-height: 1.6;">Your support agent knows what your sales agent promised yesterday. That sounds obvious until you have used four separate tools that all forgot.</p>
    </div>

    <div class="bento-grid gsap-fade-up" style="grid-template-columns: repeat(2, 1fr); gap: 32px;">
      
      <!-- Sales Agent -->
      <div class="bento-card" style="padding: 48px; background: #fbfbfd; border: 1px solid var(--border-subtle); display: flex; flex-direction: column; justify-content: space-between; min-height: 440px; border-radius: 32px;">
        <div>
          <h3 style="font-family: 'Outfit'; font-size: 32px; margin-bottom: 16px; color: var(--text-primary);">Sales Agent</h3>
          <p style="color: var(--text-secondary); font-size: 16px; line-height: 1.6;">Checks what is actually in stock before it promises anything, then closes.</p>
        </div>
        <div class="micro-mockup" style="background: #EFEAE2; border-radius: 16px; padding: 16px; margin-top: 32px; border: 1px solid rgba(0,0,0,0.05);">
          <div class="chat-bubble in" style="color: #111;">Do you have this in large?</div>
          <div class="chat-bubble out" style="color: #111; margin-top: 8px;">Yes, two left! Added to cart.</div>
          <div class="receipt-pill" style="opacity: 1; transform: scale(1); margin: 16px auto 0; box-shadow: none; border: 1px solid rgba(11,158,88,0.2);"><span class="check">✓</span> <span>SHOPIFY</span></div>
        </div>
      </div>

      <!-- Lead Agent -->
      <div class="bento-card" style="padding: 48px; background: #fbfbfd; border: 1px solid var(--border-subtle); display: flex; flex-direction: column; justify-content: space-between; min-height: 440px; border-radius: 32px;">
        <div>
          <h3 style="font-family: 'Outfit'; font-size: 32px; margin-bottom: 16px; color: var(--text-primary);">Lead Agent</h3>
          <p style="color: var(--text-secondary); font-size: 16px; line-height: 1.6;">Finds out budget and timeline the way a good salesperson would, then writes it into your CRM.</p>
        </div>
        <div class="micro-mockup" style="background: #fff; border-radius: 16px; padding: 16px; margin-top: 32px; border: 1px solid var(--border-subtle);">
          <div style="font-family: 'Inter'; font-size: 12px; color: var(--text-tertiary); margin-bottom: 12px; text-transform: uppercase; letter-spacing: 1px;">HubSpot CRM</div>
          <div style="background: #f4f5f7; border-radius: 8px; padding: 16px; border-left: 3px solid #ff7a59;">
            <div style="font-weight: 600; color: #111; font-size: 14px;">New Lead: Sarah Jenkins</div>
            <div style="color: var(--text-secondary); font-size: 13px; margin-top: 6px;">Budget: $5k-$10k · Timeline: Q3</div>
          </div>
          <div class="receipt-pill" style="opacity: 1; transform: scale(1); margin: 16px auto 0; box-shadow: none; border: 1px solid rgba(11,158,88,0.2);"><span class="check">✓</span> <span>HUBSPOT</span></div>
        </div>
      </div>

      <!-- Meetings Agent -->
      <div class="bento-card" style="padding: 48px; background: #fbfbfd; border: 1px solid var(--border-subtle); display: flex; flex-direction: column; justify-content: space-between; min-height: 440px; border-radius: 32px;">
        <div>
          <h3 style="font-family: 'Outfit'; font-size: 32px; margin-bottom: 16px; color: var(--text-primary);">Meetings Agent</h3>
          <p style="color: var(--text-secondary); font-size: 16px; line-height: 1.6;">Offers times that are genuinely free, and puts the meeting in your calendar.</p>
        </div>
        <div class="micro-mockup" style="background: #fff; border-radius: 16px; padding: 16px; margin-top: 32px; border: 1px solid var(--border-subtle);">
          <div class="chat-bubble in ig-in" style="color: #111;">I want to book a site visit.</div>
          <div class="chat-bubble out ig-out" style="margin-top: 8px;">Saturday 11 AM works perfectly!</div>
          <div class="receipt-pill" style="opacity: 1; transform: scale(1); margin: 16px auto 0; box-shadow: none; border: 1px solid rgba(11,158,88,0.2);"><span class="check">✓</span> <span>CALENDAR</span></div>
        </div>
      </div>

      <!-- Support Agent -->
      <div class="bento-card" style="padding: 48px; background: #fbfbfd; border: 1px solid var(--border-subtle); display: flex; flex-direction: column; justify-content: space-between; min-height: 440px; border-radius: 32px;">
        <div>
          <h3 style="font-family: 'Outfit'; font-size: 32px; margin-bottom: 16px; color: var(--text-primary);">Support Agent</h3>
          <p style="color: var(--text-secondary); font-size: 16px; line-height: 1.6;">Tracks the order, explains the return policy, and only wakes you if something is actually wrong.</p>
        </div>
        <div class="micro-mockup" style="background: #fff; border-radius: 16px; padding: 16px; margin-top: 32px; border: 1px solid var(--border-subtle);">
          <div class="chat-bubble in ig-in" style="color: #111; border-radius: 4px;">Where is my order?</div>
          <div class="chat-bubble out ig-in" style="color: #111; margin-top: 8px; border-radius: 4px; border: 1px solid #efefef;">It is out for delivery today at 6PM!</div>
          <div class="receipt-pill" style="opacity: 1; transform: scale(1); margin: 16px auto 0; box-shadow: none; border: 1px solid rgba(11,158,88,0.2);"><span class="check">✓</span> <span>ZENDESK</span></div>
        </div>
      </div>

    </div>
  </section>
\"\"\"

CUSTOM_HOME_ACCORDION = \"\"\"
  <section class="section-v2" style="background: var(--bg-surface-2);">
    <div style="text-align: center; margin-bottom: 64px;">
      <span style="font-family: 'Geist Mono', monospace; font-size: 12px; color: var(--text-secondary); letter-spacing: .2em; text-transform: uppercase;">BUILT AROUND YOUR BUSINESS</span>
      <h2 style="font-family: 'Outfit'; font-size: 48px; margin-top: 16px; color: var(--text-primary);">Made for the way your customers buy.</h2>
    </div>
    <div class="industries-accordion gsap-fade-up">
      <a href="./solutions/ecommerce/index.html" class="accordion-panel" style="background-image: url('https://images.unsplash.com/photo-1607082348824-0a96f2a4b9da?w=800&q=80'); text-decoration:none;">
        <div class="accordion-content"><h3 class="accordion-title">Ecommerce</h3><p class="accordion-desc">Checks live stock before it promises anything. Recovers the cart before the customer forgets.</p></div>
      </a>
      <a href="./solutions/saas/index.html" class="accordion-panel" style="background-image: url('https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&q=80'); text-decoration:none;">
        <div class="accordion-content"><h3 class="accordion-title">SaaS & Tech</h3><p class="accordion-desc">Answers integration questions from your own docs. Compares plans without pushing the expensive one.</p></div>
      </a>
      <a href="./solutions/healthcare/index.html" class="accordion-panel" style="background-image: url('https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=800&q=80'); text-decoration:none;">
        <div class="accordion-content"><h3 class="accordion-title">Healthcare & Wellness</h3><p class="accordion-desc">Shows which doctor is free. Books the appointment inside the conversation. Sends the reminder so the slot isn't wasted.</p></div>
      </a>
      <a href="./solutions/real-estate/index.html" class="accordion-panel" style="background-image: url('https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=800&q=80'); text-decoration:none;">
        <div class="accordion-content"><h3 class="accordion-title">Real Estate</h3><p class="accordion-desc">Qualifies the buyer before anyone picks up the phone. Books the site visit while they're still looking.</p></div>
      </a>
    </div>
  </section>
\"\"\"

def render_s05(kicker, h1, p):
    return f\"\"\"
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
    \"\"\"

FOOTER = \"\"\"
  <!-- S03 CTA Band -->
  <section class="cta-band">
    <h2>Somebody is typing right now.</h2>
    <div style="display:flex; justify-content:center; gap:16px;">
      <a href="{root_prefix}partners/apply/index.html"><button class="btn-primary">Start free trial</button></a>
      <button class="btn-outline">Book a demo</button>
    </div>
  </section>
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
      gsap.to(element, { scrollTrigger: { trigger: element, start: "top 85%", toggleActions: "play none none reverse" }, scale: 1, opacity: 1, duration: 0.8, ease: "power3.out" });
    });
    const stepProgress = document.getElementById('stepLineProgress');
    if(stepProgress) { window.addEventListener('scroll', () => { const docHeight = document.documentElement.scrollHeight - window.innerHeight; const progress = (window.scrollY / docHeight) * 100; stepProgress.style.height = progress + "%"; }); }
    if(document.getElementById('screen-wa')) {
        let tl = gsap.timeline({ repeat: -1, repeatDelay: 2 });
        tl.to(".stp-t1", { display: "none", duration: 0.1 }, "+=1")
          .to(".stp-2", { display: "block", duration: 0.1 }).to(".stp-3", { opacity: 1, y: 0, duration: 0.4, ease: "back.out" }, "+=0.8")
          .to(".stp-t2", { display: "flex", duration: 0.1 }).to(".stp-t2", { display: "none", duration: 0.1 }, "+=1.2")
          .to(".stp-4", { display: "block", duration: 0.1 }).to(".stp-5", { opacity: 1, scale: 1, duration: 0.5, ease: "back.out(1.5)" }, "+=0.5")
          .to("#screen-wa", { opacity: 0, duration: 0.5, ease: "power2.inOut" }, "+=3").to("#screen-ig", { opacity: 1, zIndex: 3, duration: 0.5, ease: "power2.inOut" }, "<")
          .to(".stp-ig-t1", { display: "none", duration: 0.1 }, "+=1").to(".stp-ig-2", { display: "block", duration: 0.1 })
          .to(".stp-ig-3", { opacity: 1, y: 0, duration: 0.4, ease: "back.out" }, "+=0.8").to(".stp-ig-t2", { display: "flex", duration: 0.1 })
          .to(".stp-ig-t2", { display: "none", duration: 0.1 }, "+=1.2").to(".stp-ig-4", { display: "block", duration: 0.1 })
          .to(".stp-ig-5", { opacity: 1, scale: 1, duration: 0.5, ease: "back.out(1.5)" }, "+=0.5")
          .to("#screen-ig", { opacity: 0, duration: 0.5, ease: "power2.inOut" }, "+=3").to("#screen-wa", { opacity: 1, zIndex: 3, duration: 0.5, ease: "power2.inOut" }, "<")
          .set([".stp-2", ".stp-4", ".stp-ig-2", ".stp-ig-4", ".stp-t2", ".stp-ig-t2"], { display: "none" })
          .set([".stp-t1", ".stp-ig-t1"], { display: "flex" })
          .set([".stp-3", ".stp-5", ".stp-ig-3", ".stp-ig-5"], { opacity: 0, scale: 0.94, y: 10 });
    }
  </script>
</body>
</html>
\"\"\"

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
            all_content += f.read() + "\\n\\n"

all_content = re.sub(r'SECTION \d+\s*(?:—|-)\s*', '', all_content, flags=re.IGNORECASE)
pages = re.split(r'\\n# PAGE \d+\s*(?:—|-)\s*', all_content)
pages = pages[1:] 

def parse_page(page_text):
    lines = page_text.strip().split('\\n')
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
    mega_css = \"\"\"<style>.nav-dropdown-wrapper:hover .mega-menu { opacity: 1 !important; visibility: visible !important; transform: translateX(-50%) translateY(0) !important; }.sol-menu:hover .mega-menu { transform: translateX(0) translateY(0) !important; }.res-menu:hover .mega-menu { transform: translateX(0) translateY(0) !important; }</style>\"\"\"
    return mega_css + f\"\"\"
  <nav class="nav" id="mainNav">
    <div class="nav-container">
      <a href="{root_prefix}index.html" class="nav-logo-area">
        <div class="nav-logo-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="white"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg></div>
        <div class="nav-logo-text">StepsAI</div>
      </a>
      <div class="nav-tabs">
        <div class="nav-dropdown-wrapper">
          <a class="nav-tab">Product <span style="font-size: 10px; margin-left: 4px;">▼</span></a>
          <div class="mega-menu">
            <div class="mega-grid">
              <div class="mega-col"><div class="mega-col-title">PRODUCTS</div><a href="{root_prefix}product/ai-agents/index.html">AI Agents</a><a href="{root_prefix}product/copilot/index.html">Internal Copilot</a></div>
              <div class="mega-col"><div class="mega-col-title">WHAT IT DOES</div><a href="{root_prefix}features/sales-agent/index.html">Sales Agent</a><a href="{root_prefix}features/lead-agent/index.html">Lead Agent</a><a href="{root_prefix}features/meetings-agent/index.html">Meetings Agent</a><a href="{root_prefix}features/support-agent/index.html">Support Agent</a></div>
              <div class="mega-col"><div class="mega-col-title">PLATFORM</div><a href="{root_prefix}features/workflows/index.html">Workflows</a><a href="{root_prefix}features/inbox/index.html">One Inbox</a><a href="{root_prefix}features/analytics/index.html">Analytics</a><a href="{root_prefix}integrations/index.html">Integrations</a></div>
              <div class="mega-col"><div class="mega-col-title">CHANNELS</div><a href="{root_prefix}channels/website/index.html">Website</a><a href="{root_prefix}channels/whatsapp/index.html">WhatsApp</a><a href="{root_prefix}channels/instagram/index.html">Instagram</a><a href="{root_prefix}channels/standalone-page/index.html">Standalone Page</a></div>
            </div>
          </div>
        </div>
        <div class="nav-dropdown-wrapper sol-menu">
          <a class="nav-tab">Solutions <span style="font-size: 10px; margin-left: 4px;">▼</span></a>
          <div class="mega-menu" style="min-width: 400px; left: 0; transform: translateX(0) translateY(10px);">
            <div class="mega-grid" style="grid-template-columns: 1fr 1fr;">
              <div class="mega-col"><div class="mega-col-title">BY INDUSTRY</div><a href="{root_prefix}solutions/ecommerce/index.html">E-Commerce <span class="mega-badge">Flagship</span></a><a href="{root_prefix}solutions/saas/index.html">SaaS</a><a href="{root_prefix}solutions/healthcare/index.html">Healthcare</a><a href="{root_prefix}solutions/education/index.html">Education</a><a href="{root_prefix}solutions/real-estate/index.html">Real Estate</a></div>
              <div class="mega-col"><div class="mega-col-title">BY ROLE</div><a href="{root_prefix}use-cases/marketing-growth/index.html">Marketing & Growth</a><a href="{root_prefix}use-cases/sales/index.html">Sales</a><a href="{root_prefix}use-cases/support-cx/index.html">Support & CX</a><a href="{root_prefix}use-cases/operations/index.html">Operations</a></div>
            </div>
          </div>
        </div>
        <a href="{root_prefix}pricing/index.html" class="nav-tab">Pricing</a>
        <a href="{root_prefix}partners/index.html" class="nav-tab">Partner</a>
        <div class="nav-dropdown-wrapper res-menu">
          <a class="nav-tab">Resources <span style="font-size: 10px; margin-left: 4px;">▼</span></a>
          <div class="mega-menu" style="min-width: 300px; left: auto; right: 0; transform: translateX(0) translateY(10px);">
            <div class="mega-grid" style="grid-template-columns: 1fr 1fr;">
              <div class="mega-col"><div class="mega-col-title">LEARN</div><a href="{root_prefix}blog/index.html">Blog</a><a href="{root_prefix}resources/ai-guides/index.html">AI Guides</a><a href="{root_prefix}resources/case-studies/index.html">Case Studies</a></div>
              <div class="mega-col"><div class="mega-col-title">COMPANY</div><a href="{root_prefix}about/index.html">About</a><a href="{root_prefix}team/index.html">Team • Careers</a><a href="{root_prefix}note/index.html">Note • Contact</a></div>
            </div>
          </div>
        </div>
      </div>
      <div class="nav-right">
        <a href="{root_prefix}partners/apply/index.html"><button class="btn-primary">Start free trial</button></a>
      </div>
    </div>
  </nav>
\"\"\"

def parse_markdown_line(line):
    line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line)
    line = re.sub(r'!\[([^\]]*)\]\(([^\)]+)\)', r'<img src="\2" alt="\1" style="width: 100%; border-radius: 12px; margin: 16px 0; border: 1px solid var(--border-subtle); display: block;" />', line)
    return line

def get_micro_mockup(title):
    if "WhatsApp" in title or "Sales Agent" in title:
        return '<div class="micro-mockup"><div class="chat-bubble in">Hi, do you have this in large?</div><div class="chat-bubble out">Yes, two left! Added to cart.</div><div class="receipt-pill" style="opacity:1; transform:scale(1); margin:4px 0 0;"><span class="check">✓</span> <span>SHOPIFY</span></div></div>'
    elif "Instagram" in title or "Meetings Agent" in title:
        return '<div class="micro-mockup micro instagram"><div class="chat-bubble in ig-in">I want to book a visit.</div><div class="chat-bubble out ig-out">Saturday 11 AM works perfectly!</div><div class="receipt-pill" style="opacity:1; transform:scale(1); margin:4px 0 0;"><span class="check">✓</span> <span>CALENDAR</span></div></div>'
    elif "Website" in title or "Lead Agent" in title:
        return '<div class="micro-mockup micro website"><div class="chat-bubble in ig-in">What is the pricing?</div><div class="chat-bubble out ig-in">Plans start at $49. Whats your email?</div><div class="receipt-pill" style="opacity:1; transform:scale(1); margin:4px 0 0;"><span class="check">✓</span> <span>HUBSPOT</span></div></div>'
    elif "Support" in title:
        return '<div class="micro-mockup micro website"><div class="chat-bubble in ig-in">Where is my order?</div><div class="chat-bubble out ig-in">It is out for delivery today at 6PM!</div><div class="receipt-pill" style="opacity:1; transform:scale(1); margin:4px 0 0;"><span class="check">✓</span> <span>ZENDESK</span></div></div>'
    return ""

for p in pages:
    data = parse_page(p)
    if not data: continue
    
    # FOR THIS RUN: We only want to rebuild the Home Page to fix the Four Agents bug.
    if data["route"] != "":
        continue
        
    html_content = ""
    if data["route"] == "" and data["h1"]:
        html_content += CUSTOM_HOME_HERO
    elif data["h1"]:
        html_content += render_s05(data["kicker"], data["h1"], data["sub"])
    
    for block in data["blocks"]:
        if not block["title"] or "Hero" in block["title"]: continue
        
        if data["route"] == "" and "Industries" in block["title"]:
            html_content += CUSTOM_HOME_ACCORDION
            continue
            
        if data["route"] == "" and "Four Agents" in block["title"]:
            html_content += CUSTOM_FOUR_AGENTS
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
                        mockup_html = get_micro_mockup(card_title)
                        html_content += f'''
                        <div class="bento-card gsap-scale-in">
                            <h3 class="bento-title" style="font-size: 24px; margin-bottom: 16px;">{card_title}</h3>
                            <p class="bento-desc" style="font-size:16px;">{' '.join(card_desc)}</p>
                            {mockup_html}
                        </div>'''
                    card_title = c_clean.replace('### ', '')
                    card_desc = []
                else:
                    card_desc.append(parse_markdown_line(c_clean))
                    
            if card_title or card_desc:
                mockup_html = get_micro_mockup(card_title)
                html_content += f'''
                <div class="bento-card gsap-scale-in">
                    <h3 class="bento-title" style="font-size: 24px; margin-bottom: 16px;">{card_title}</h3>
                    <p class="bento-desc" style="font-size:16px;">{' '.join(card_desc)}</p>
                    {mockup_html}
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
    
print(f"V11 Compiler finished. Generated Four Agents layout on Home Page.")
"""

with open('build_v11_compiler.py', 'w', encoding='utf-8') as f:
    f.write(new_code)
