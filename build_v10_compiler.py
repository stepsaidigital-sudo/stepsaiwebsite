import os
import re

GLOBAL_HEAD = """<!DOCTYPE html>
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
    
    /* Interactive S09 Accordion */
    .industries-accordion {{ max-width: 1200px; margin: 0 auto; display: flex; gap: 16px; height: 500px; }}
    .accordion-panel {{ position: relative; flex: 1; border-radius: 24px; overflow: hidden; background-size: cover; background-position: center; transition: flex 0.6s cubic-bezier(0.16, 1, 0.3, 1); cursor: pointer; }}
    .accordion-panel::after {{ content: ''; position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0) 100%); transition: opacity 0.4s; }}
    .accordion-panel:hover {{ flex: 3; }}
    .accordion-content {{ position: absolute; bottom: 0; left: 0; width: 100%; padding: 32px; color: white; z-index: 2; display: flex; flex-direction: column; justify-content: flex-end; }}
    .accordion-title {{ font-family: 'Outfit', sans-serif; font-size: 28px; font-weight: 700; margin: 0; white-space: nowrap; }}
    .accordion-desc {{ font-size: 16px; color: rgba(255,255,255,0.8); margin-top: 12px; line-height: 1.5; opacity: 0; transform: translateY(10px); transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); }}
    .accordion-panel:hover .accordion-desc {{ opacity: 1; transform: translateY(0); transition-delay: 0.1s; }}
    
    /* --- THE STEP LINE --- */
    .step-line-container {{ position: fixed; top: 0; left: 40px; width: 6px; height: 100%; z-index: 0; pointer-events: none; }}
    .step-line {{ width: 2px; height: 100%; background: var(--line); position: absolute; left: 2px; }}
    .step-line-progress {{ width: 2px; height: 0%; background: var(--accent); position: absolute; left: 2px; transition: height 0.1s linear; }}
    
    /* --- MOCKUP SYSTEM --- */
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
    
    .micro-mockup {{ background: #EFEAE2; border-radius: 16px; padding: 16px; margin-top: auto; display: flex; flex-direction: column; gap: 10px; opacity:0.6; transition: 0.3s; transform: translateY(20px); }}
    .bento-card:hover .micro-mockup {{ opacity: 1; transform: translateY(0); }}
    .micro.instagram {{ background: #fff; border: 1px solid #efefef; }}
    .micro.website {{ background: #f7f9fc; border: 1px solid var(--border-subtle); }}
    
    .typing {{ display:flex; gap:4px; padding:16px 20px; align-items:center; }}
    .dot {{ width:6px; height:6px; background:rgba(0,0,0,0.3); border-radius:50%; animation: type 1.4s infinite ease-in-out both; }}
    .dot:nth-child(1) {{ animation-delay: -0.32s; }}
    .dot:nth-child(2) {{ animation-delay: -0.16s; }}
    @keyframes type {{ 0%, 80%, 100% {{ transform: scale(0); }} 40% {{ transform: scale(1); }} }}
    
    /* CUSTOM LAYOUTS CSS (Light Mode Professional) */
    .pricing-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; max-width: 1400px; margin: 48px auto; }}
    .pricing-card {{ background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 24px; padding: 40px 32px; display: flex; flex-direction: column; box-shadow: var(--shadow); position: relative; }}
    .pricing-card.popular {{ border-color: var(--accent); box-shadow: var(--shadow-lg); }}
    .popular-badge {{ position: absolute; top: -12px; left: 50%; transform: translateX(-50%); background: var(--accent); color: white; padding: 4px 12px; border-radius: 99px; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; }}
    .pricing-price {{ font-size: 48px; font-weight: 700; font-family: 'Outfit'; margin: 24px 0 8px; }}
    .pricing-features {{ list-style: none; padding: 0; margin: 32px 0 0; flex: 1; }}
    .pricing-features li {{ margin-bottom: 16px; display: flex; align-items: flex-start; gap: 12px; font-size: 15px; color: var(--text-secondary); }}
    .pricing-features li::before {{ content: '✓'; color: var(--accent); font-weight: bold; }}
    
    .comparison-table {{ width: 100%; border-collapse: collapse; margin-top: 64px; text-align: left; background: var(--bg-surface); border-radius: 24px; overflow: hidden; box-shadow: var(--shadow); }}
    .comparison-table th, .comparison-table td {{ padding: 24px; border-bottom: 1px solid var(--border-subtle); }}
    .comparison-table th {{ background: var(--bg-surface-2); font-weight: 600; font-size: 14px; text-transform: uppercase; letter-spacing: 1px; color: var(--text-secondary); }}
    .comparison-table td:not(:first-child) {{ text-align: center; }}
    .comparison-table .check {{ color: var(--accent); font-weight: bold; font-size: 18px; }}
    
    .beliefs-list {{ display: flex; flex-direction: column; gap: 48px; max-width: 800px; margin: 64px auto; }}
    .belief-item {{ display: flex; gap: 32px; align-items: flex-start; }}
    .belief-icon {{ width: 64px; height: 64px; background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 16px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; box-shadow: var(--shadow); }}
    .belief-content h3 {{ font-size: 24px; font-family: 'Outfit'; margin-bottom: 12px; }}
    .belief-content p {{ font-size: 16px; color: var(--text-secondary); line-height: 1.6; }}
    
    .partner-rev-calc {{ background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 24px; padding: 48px; margin: 64px auto; max-width: 1000px; box-shadow: var(--shadow-lg); text-align: center; }}
    .partner-rev-bars {{ display: flex; align-items: flex-end; justify-content: space-between; height: 200px; margin-top: 48px; border-bottom: 1px solid var(--border-subtle); padding-bottom: 8px; }}
    .bar {{ width: 24px; background: var(--accent-tint); border-radius: 4px 4px 0 0; transition: 0.3s; }}
    .bar:hover {{ background: var(--accent); }}
  </style>
</head>
<body>
  <div class="step-line-container">
    <div class="step-line"></div>
    <div class="step-line-progress" id="stepLineProgress"></div>
  </div>
"""

CUSTOM_HOME_HERO = """
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
"""

CUSTOM_HOME_ACCORDION = """
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
"""

CUSTOM_PRICING_HTML = """
  <section class="section-v2" style="text-align:center; padding-top:160px;">
    <h1 style="font-size: clamp(48px, 5vw, 64px); font-family:'Outfit'; margin-bottom:24px;">Plans that scale<br>with every AI reply.</h1>
    <p style="font-size: 20px; color: var(--text-secondary); max-width: 600px; margin: 0 auto 48px;">No hidden fees. You only pay for the replies the AI sends. Unlimited users, channels, and training sources on all plans.</p>
    
    <div style="display:inline-flex; background:var(--bg-surface-2); padding:8px; border-radius:99px; gap:8px;">
      <button style="padding:12px 24px; border-radius:99px; background:var(--text-primary); color:var(--bg-surface); border:none; font-weight:600; font-size:16px;">Monthly</button>
      <button style="padding:12px 24px; border-radius:99px; background:transparent; color:var(--text-primary); border:none; font-weight:600; font-size:16px;">Annually <span style="color:var(--accent); font-size:12px; margin-left:4px;">Save 20%</span></button>
    </div>
    
    <div class="pricing-grid gsap-fade-up">
      <div class="pricing-card">
        <h3 style="font-size:24px; font-family:'Outfit';">Starter</h3>
        <p style="color:var(--text-secondary); font-size:14px;">Perfect for small stores</p>
        <div class="pricing-price">₹2,499<span style="font-size:16px; color:var(--text-secondary);">/mo</span></div>
        <p style="font-size:14px; font-weight:600; color:var(--accent);">500 AI Replies included</p>
        <button class="btn-outline" style="width:100%; margin-top:24px;">Start free trial</button>
        <ul class="pricing-features">
          <li>1 AI Agent</li>
          <li>WhatsApp & Website</li>
          <li>Basic Analytics</li>
          <li>Community Support</li>
        </ul>
      </div>
      <div class="pricing-card popular">
        <div class="popular-badge">Most Popular</div>
        <h3 style="font-size:24px; font-family:'Outfit';">Pro</h3>
        <p style="color:var(--text-secondary); font-size:14px;">For growing businesses</p>
        <div class="pricing-price">₹4,999<span style="font-size:16px; color:var(--text-secondary);">/mo</span></div>
        <p style="font-size:14px; font-weight:600; color:var(--accent);">1,200 AI Replies included</p>
        <button class="btn-primary" style="width:100%; margin-top:24px;">Start free trial</button>
        <ul class="pricing-features">
          <li>3 AI Agents</li>
          <li>All Channels (IG, WA, Web)</li>
          <li>CRM Integrations</li>
          <li>Priority Support</li>
          <li>Advanced Analytics</li>
        </ul>
      </div>
      <div class="pricing-card">
        <h3 style="font-size:24px; font-family:'Outfit';">Elite</h3>
        <p style="color:var(--text-secondary); font-size:14px;">For high-volume brands</p>
        <div class="pricing-price">₹19,999<span style="font-size:16px; color:var(--text-secondary);">/mo</span></div>
        <p style="font-size:14px; font-weight:600; color:var(--accent);">5,000 AI Replies included</p>
        <button class="btn-outline" style="width:100%; margin-top:24px;">Start free trial</button>
        <ul class="pricing-features">
          <li>Unlimited AI Agents</li>
          <li>Custom Workflows</li>
          <li>API Access</li>
          <li>Dedicated Success Manager</li>
        </ul>
      </div>
      <div class="pricing-card">
        <h3 style="font-size:24px; font-family:'Outfit';">Custom</h3>
        <p style="color:var(--text-secondary); font-size:14px;">For enterprise scale</p>
        <div class="pricing-price">Let's talk</div>
        <p style="font-size:14px; font-weight:600; color:transparent;">-</p>
        <button class="btn-outline" style="width:100%; margin-top:24px;">Book a demo</button>
        <ul class="pricing-features">
          <li>Custom AI Replies</li>
          <li>On-premise deployment options</li>
          <li>Custom Integrations</li>
          <li>SLA Guarantee</li>
        </ul>
      </div>
    </div>
    
    <div style="margin-top:96px;">
      <h2 style="font-size:40px; font-family:'Outfit'; margin-bottom:16px;">Full feature comparison</h2>
      <table class="comparison-table gsap-fade-up">
        <thead>
          <tr>
            <th style="width:40%;">Feature</th>
            <th>Starter</th>
            <th>Pro</th>
            <th>Elite</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>AI Replies per month</td><td>500</td><td>1,200</td><td>5,000</td></tr>
          <tr><td>Channels</td><td>WA, Web</td><td>All</td><td>All</td></tr>
          <tr><td>Training Data Sources</td><td>Website only</td><td>Web, Docs, PDF</td><td>Unlimited</td></tr>
          <tr><td>CRM Integrations (HubSpot, Salesforce)</td><td>-</td><td><span class="check">✓</span></td><td><span class="check">✓</span></td></tr>
          <tr><td>Shopify / WooCommerce Sync</td><td><span class="check">✓</span></td><td><span class="check">✓</span></td><td><span class="check">✓</span></td></tr>
          <tr><td>API Access</td><td>-</td><td>-</td><td><span class="check">✓</span></td></tr>
          <tr><td>Dedicated Success Manager</td><td>-</td><td>-</td><td><span class="check">✓</span></td></tr>
        </tbody>
      </table>
    </div>
  </section>
"""

CUSTOM_ABOUT_HTML = """
  <section class="section-v2" style="text-align:center; padding-top:160px; max-width:800px;">
    <h1 style="font-size: clamp(48px, 5vw, 64px); font-family:'Outfit'; margin-bottom:24px;">We're building the AI agent layer for every business.</h1>
    <p style="font-size: 20px; color: var(--text-secondary); line-height: 1.6;">StepsAI started with a simple observation: every business needs to talk to its customers 24/7, but most can't afford to hire for it. AI changes that. We're making it accessible to everyone, from solo founders to enterprises.</p>
  </section>
  
  <section class="section-v2" style="background:var(--bg-surface-2); padding:96px 32px;">
    <h2 style="text-align:center; font-family:'Outfit'; font-size:40px;">Our beliefs shape our product.</h2>
    <div class="beliefs-list gsap-fade-up">
      <div class="belief-item">
        <div class="belief-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg></div>
        <div class="belief-content">
          <h3>AI should do things, not just talk.</h3>
          <p>Most chatbots are glorified FAQ pages. We build agents that take real action: creating tickets, booking meetings, checking inventory, capturing leads. The difference between a chatbot and an agent is what happens after the conversation.</p>
        </div>
      </div>
      <div class="belief-item">
        <div class="belief-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg></div>
        <div class="belief-content">
          <h3>One brain is better than ten tools.</h3>
          <p>Your customer data, product catalog, support docs, and team inbox shouldn't live in silos. StepsAI connects all of it into one AI brain that serves your customers AND your team.</p>
        </div>
      </div>
      <div class="belief-item">
        <div class="belief-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></div>
        <div class="belief-content">
          <h3>Setup should take minutes, not months.</h3>
          <p>Enterprise AI shouldn't require an enterprise budget or timeline. Our fastest deployment was 3 minutes from signup to live agent. We optimize for that speed every day.</p>
        </div>
      </div>
    </div>
  </section>
  
  <section class="section-v2" style="text-align:center;">
    <h2 style="font-family:'Outfit'; font-size:40px; margin-bottom:16px;">Meet the team</h2>
    <p style="color:var(--text-secondary); max-width:600px; margin:0 auto 32px;">We're a small, focused team building the AI agent layer for every business.</p>
    <button class="btn-outline">See Our Team</button>
  </section>
"""

CUSTOM_PARTNER_HTML = """
  <section class="section-v2" style="text-align:center; padding-top:160px;">
    <h1 style="font-size: clamp(48px, 5vw, 64px); font-family:'Outfit'; margin-bottom:24px;">Partner with StepsAI.<br>Earn recurring revenue.</h1>
    <p style="font-size: 20px; color: var(--text-secondary); max-width: 600px; margin: 0 auto 48px;">Build AI agents for your clients on our platform. Keep 15% of their subscription revenue forever.</p>
    
    <div class="partner-rev-calc gsap-fade-up">
      <h3 style="font-family:'Outfit'; font-size:32px;">Get paid for 24 months. <span style="color:var(--accent);">Do the math.</span></h3>
      <p style="color:var(--text-secondary); margin-top:16px;">See how your recurring revenue stacks up as you onboard more clients.</p>
      
      <div class="partner-rev-bars">
        <div class="bar" style="height: 10%;"></div><div class="bar" style="height: 15%;"></div><div class="bar" style="height: 20%;"></div>
        <div class="bar" style="height: 30%;"></div><div class="bar" style="height: 35%;"></div><div class="bar" style="height: 45%;"></div>
        <div class="bar" style="height: 60%;"></div><div class="bar" style="height: 75%;"></div><div class="bar" style="height: 85%;"></div>
        <div class="bar" style="height: 100%; background:var(--accent);"></div>
      </div>
      
      <div style="display:flex; justify-content:space-between; margin-top:24px; align-items:center;">
        <div style="text-align:left;">
          <div style="font-size:14px; color:var(--text-secondary);">Estimated Monthly Revenue</div>
          <div style="font-size:40px; font-weight:700; font-family:'Outfit'; color:var(--accent);">₹45,000+</div>
        </div>
        <div style="text-align:right;">
          <div style="font-size:14px; color:var(--text-secondary);">Active Clients</div>
          <div style="font-size:24px; font-weight:700;">20 Clients</div>
        </div>
      </div>
    </div>
  </section>
  
  <section class="section-v2" style="background:var(--bg-surface-2);">
    <h2 style="text-align:center; font-family:'Outfit'; font-size:40px; margin-bottom:64px;">How it works</h2>
    <div class="bento-grid gsap-fade-up">
      <div class="bento-card">
        <div style="font-family:'Geist Mono', monospace; color:var(--accent); margin-bottom:16px;">01</div>
        <h3 class="bento-title">Sign up a client</h3>
        <p class="bento-desc">Use your unique partner link or register the client in your dashboard.</p>
      </div>
      <div class="bento-card">
        <div style="font-family:'Geist Mono', monospace; color:var(--accent); margin-bottom:16px;">02</div>
        <h3 class="bento-title">Build their agent</h3>
        <p class="bento-desc">Use our visual builder to create their AI agent in minutes. No coding required.</p>
      </div>
      <div class="bento-card">
        <div style="font-family:'Geist Mono', monospace; color:var(--accent); margin-bottom:16px;">03</div>
        <h3 class="bento-title">Go live</h3>
        <p class="bento-desc">Deploy to WhatsApp, Instagram, or their website instantly.</p>
      </div>
      <div class="bento-card">
        <div style="font-family:'Geist Mono', monospace; color:var(--accent); margin-bottom:16px;">04</div>
        <h3 class="bento-title">Get paid monthly</h3>
        <p class="bento-desc">Receive 15% of their subscription fee automatically every month for 2 years.</p>
      </div>
    </div>
  </section>
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

FOOTER = """
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
    return {"route": route, "title": title}

def get_nav(root_prefix):
    mega_css = """<style>.nav-dropdown-wrapper:hover .mega-menu { opacity: 1 !important; visibility: visible !important; transform: translateX(-50%) translateY(0) !important; }.sol-menu:hover .mega-menu { transform: translateX(0) translateY(0) !important; }.res-menu:hover .mega-menu { transform: translateX(0) translateY(0) !important; }</style>"""
    return mega_css + f"""
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
"""

for p in pages:
    data = parse_page(p)
    if not data: continue
    
    # We only want to re-compile the specific customized routes
    if data["route"] not in ["pricing", "about", "partners"]:
        continue
        
    depth = len(data["route"].split('/')) if data["route"] else 0
    root_prefix = "../" * depth if depth > 0 else "./"
    
    head = GLOBAL_HEAD.format(title=data["title"], root_prefix=root_prefix)
    footer = FOOTER.replace("{root_prefix}", root_prefix)
    
    html_content = ""
    if data["route"] == "pricing":
        html_content = CUSTOM_PRICING_HTML
    elif data["route"] == "about":
        html_content = CUSTOM_ABOUT_HTML
    elif data["route"] == "partners":
        html_content = CUSTOM_PARTNER_HTML
        
    full_html = head + get_nav(root_prefix) + html_content + footer
    
    dir_path = os.path.join(data["route"])
    os.makedirs(dir_path, exist_ok=True)
    
    with open(os.path.join(dir_path, "index.html"), "w", encoding="utf-8") as f:
        f.write(full_html)
    
print(f"V10 Structural Layout Compiler finished. Generated Pricing, About, Partners.")
