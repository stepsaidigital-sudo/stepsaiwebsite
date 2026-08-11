import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>StepsAI - Your AI agent layer for every business</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Outfit:wght@500;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    /* BASE VARIABLES */
    :root {
      --primary: #2563EB; /* Main Accent */
      --primary-dark: #1D4ED8;
      --bg-color: #FAFAFA;
      --text-main: #0F172A;
      --text-muted: #64748B;
      --border-light: #E2E8F0;
      --bg-white: #FFFFFF;
      --bg-dark: #0F172A; /* For S03 */
    }

    /* GLOBAL RESET */
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { 
      background-color: var(--bg-color); 
      color: var(--text-main); 
      font-family: 'Inter', sans-serif; 
      line-height: 1.6;
      overflow-x: hidden;
    }
    h1, h2, h3, h4, h5, h6 { font-family: 'Outfit', sans-serif; line-height: 1.2; color: var(--text-main); }
    a { text-decoration: none; color: inherit; }
    ul { list-style: none; }
    
    /* UTILITIES */
    .container { max-width: 1200px; margin: 0 auto; padding: 0 24px; }
    .section-spacing { padding: 120px 0; }
    .text-center { text-align: center; }
    
    .btn {
      display: inline-flex; align-items: center; justify-content: center;
      padding: 12px 24px; border-radius: 8px; font-size: 15px; font-weight: 600;
      cursor: pointer; transition: all 0.2s; border: none;
    }
    .btn-primary { background: var(--primary); color: white; box-shadow: 0 4px 12px rgba(99,102,241,0.25); }
    .btn-primary:hover { background: var(--primary-dark); transform: translateY(-1px); box-shadow: 0 6px 16px rgba(99,102,241,0.3); }
    .btn-outline { border: 1px solid var(--border-light); background: var(--bg-white); color: var(--text-main); }
    .btn-outline:hover { background: #f8fafc; border-color: #cbd5e1; }
    .btn-dark { background: white; color: var(--text-main); }
    .btn-dark:hover { background: #f1f5f9; }

    .kicker {
      display: inline-flex; align-items: center; gap: 6px; padding: 6px 16px;
      border-radius: 100px; color: var(--primary); font-size: 11px; font-weight: 700;
      letter-spacing: 0.5px; margin-bottom: 24px; background: #EEF2FF;
      border: 1px solid #E0E7FF; text-transform: uppercase;
    }

    .section-title { font-size: 48px; font-weight: 800; margin-bottom: 24px; letter-spacing: -1px; }
    .section-subtitle { font-size: 18px; color: var(--text-muted); max-width: 600px; margin: 0 auto; }
    .section-header { margin-bottom: 64px; }

    /* ==================================================
       S01 - NAV
    ================================================== */
    .nav { position: fixed; top: 0; left: 0; width: 100%; z-index: 1000; background: rgba(255,255,255,0.9); backdrop-filter: blur(10px); border-bottom: 1px solid rgba(0,0,0,0.05); }
    .nav-container { max-width: 1300px; margin: 0 auto; padding: 16px 32px; display: flex; align-items: center; justify-content: space-between; }
    .nav-logo { display: flex; align-items: center; gap: 10px; font-weight: 800; font-size: 20px; color: var(--text-main); letter-spacing: -0.5px; }
    .nav-logo-icon { width: 30px; height: 30px; background: var(--primary); border-radius: 8px; color: white; display: flex; align-items: center; justify-content: center; }
    .nav-links { display: flex; gap: 28px; }
    .nav-link { color: #334155; font-size: 14px; font-weight: 600; cursor: pointer; display: flex; align-items: center; gap: 4px; transition: color 0.2s; }
    .nav-link:hover { color: var(--text-main); }
    .nav-actions { display: flex; align-items: center; gap: 20px; }
    
    /* ==================================================
       S04 - LANDING HERO
    ================================================== */
    .hero {
      position: relative; padding: 180px 0 120px; text-align: center; overflow: hidden;
      background: radial-gradient(circle at 50% 0%, #ffffff 0%, #FAFAFA 100%);
    }
    .hero h1 { font-size: 64px; font-weight: 900; line-height: 1.1; margin-bottom: 24px; letter-spacing: -2px; }
    .hero p { font-size: 18px; color: var(--text-muted); max-width: 700px; margin: 0 auto 40px; }
    .hero-actions { display: flex; align-items: center; justify-content: center; gap: 16px; margin-bottom: 32px; }
    .hero-integrations { font-size: 14px; color: #94A3B8; font-weight: 500; }
    
    /* Morphing Card Area */
    .hero-visuals { margin-top: 80px; position: relative; height: 400px; display: flex; justify-content: center; }
    .morph-card {
      width: 380px; background: white; border-radius: 24px; box-shadow: 0 20px 40px -10px rgba(0,0,0,0.1);
      border: 1px solid var(--border-light); overflow: hidden; position: relative;
      display: flex; flex-direction: column;
    }
    .morph-header { padding: 16px; border-bottom: 1px solid var(--border-light); font-weight: 600; font-size: 14px; display: flex; align-items: center; gap: 12px;}
    .morph-body { padding: 24px 16px; flex: 1; display: flex; flex-direction: column; gap: 16px; font-size: 13px; }
    .msg-user { align-self: flex-end; background: #F1F5F9; padding: 10px 14px; border-radius: 12px 12px 0 12px; }
    .msg-agent { align-self: flex-start; background: var(--primary); color: white; padding: 10px 14px; border-radius: 12px 12px 12px 0; }
    .receipt { margin-top: auto; padding: 12px; background: #F8FAFC; border-top: 1px solid var(--border-light); font-size: 11px; font-weight: 700; color: var(--primary); text-align: center; letter-spacing: 0.5px; }

    /* ==================================================
       S08 - FOUR AGENTS
    ================================================== */
    .four-agents { background: white; }
    .grid-2x2 { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }
    .agent-card {
      background: var(--bg-color); padding: 32px; border-radius: 16px; border: 1px solid var(--border-light);
      display: flex; flex-direction: column;
    }
    .agent-card h3 { font-size: 20px; margin-bottom: 12px; }
    .agent-card p { color: var(--text-muted); font-size: 15px; margin-bottom: 24px; flex: 1; }
    .agent-receipt { font-family: monospace; font-size: 12px; color: var(--primary); font-weight: 600; background: #EEF2FF; padding: 8px 12px; border-radius: 6px; display: inline-block; align-self: flex-start; }

    /* ==================================================
       S09 - INDUSTRIES SWITCHER
    ================================================== */
    .industries { background: var(--bg-color); }
    .ind-container { display: grid; grid-template-columns: 1fr 1fr; gap: 64px; align-items: center; }
    .ind-tabs { display: flex; flex-direction: column; gap: 8px; }
    .ind-tab { padding: 16px 24px; font-size: 16px; font-weight: 600; color: var(--text-muted); cursor: pointer; border-radius: 12px; transition: all 0.2s; text-align: left; background: transparent; border: 1px solid transparent; }
    .ind-tab.active { background: white; color: var(--text-main); border-color: var(--border-light); box-shadow: 0 4px 12px rgba(0,0,0,0.02); }
    
    .ind-content { display: none; }
    .ind-content.active { display: block; animation: fadeIn 0.3s ease; }
    .ind-content ul { display: flex; flex-direction: column; gap: 16px; margin-bottom: 32px; }
    .ind-content li { display: flex; gap: 12px; align-items: flex-start; font-size: 16px; color: var(--text-muted); }
    .ind-content li::before { content: '→'; color: var(--primary); font-weight: bold; }
    
    .ind-visual { background: white; height: 420px; border-radius: 24px; border: 1px solid var(--border-light); box-shadow: 0 20px 40px -10px rgba(0,0,0,0.05); display: flex; align-items: center; justify-content: center; }

    /* ==================================================
       S10 - CHANNELS
    ================================================== */
    .channels { background: white; }
    .channel-row { display: grid; grid-template-columns: 1fr 1fr; gap: 64px; align-items: center; margin-bottom: 120px; }
    .channel-row:nth-child(even) { direction: rtl; }
    .channel-row:nth-child(even) > * { direction: ltr; }
    .channel-row:last-child { margin-bottom: 0; }
    .ch-content h3 { font-size: 32px; margin-bottom: 16px; letter-spacing: -0.5px; }
    .ch-content p { font-size: 18px; color: var(--text-muted); margin-bottom: 24px; }
    .ch-visual { height: 400px; background: var(--bg-color); border-radius: 24px; border: 1px solid var(--border-light); }

    /* ==================================================
       S11 - SETUP
    ================================================== */
    .setup { background: var(--bg-color); }
    .setup-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 64px; align-items: center; }
    .setup-steps { display: flex; flex-direction: column; gap: 32px; }
    .setup-step { display: flex; gap: 20px; }
    .step-num { width: 32px; height: 32px; border-radius: 50%; background: white; border: 1px solid var(--border-light); display: flex; align-items: center; justify-content: center; font-weight: 700; color: var(--primary); flex-shrink: 0; }
    .step-content h4 { font-size: 18px; margin-bottom: 8px; }
    .step-content p { color: var(--text-muted); font-size: 15px; }
    
    /* ==================================================
       S12 - WORKFLOWS
    ================================================== */
    .workflows { background: white; }
    .wf-tabs { display: flex; gap: 16px; margin-bottom: 48px; justify-content: center; }
    .wf-tab { padding: 10px 20px; border-radius: 100px; border: 1px solid var(--border-light); background: var(--bg-color); font-weight: 600; cursor: pointer; font-size: 14px; color: var(--text-muted); }
    .wf-tab.active { background: var(--primary); color: white; border-color: var(--primary); }
    
    .wf-rail { display: flex; align-items: center; justify-content: space-between; position: relative; margin-bottom: 64px; max-width: 800px; margin-left: auto; margin-right: auto; }
    .wf-rail::before { content: ''; position: absolute; top: 50%; left: 0; width: 100%; height: 2px; background: var(--border-light); z-index: 1; transform: translateY(-50%); }
    .wf-node { position: relative; z-index: 2; background: white; border: 2px solid var(--border-light); padding: 12px 16px; border-radius: 8px; font-size: 13px; font-weight: 600; width: 140px; text-align: center; }
    .wf-node.active { border-color: var(--primary); color: var(--primary); box-shadow: 0 4px 12px rgba(99,102,241,0.1); }

    /* ==================================================
       S13 - ONE INBOX
    ================================================== */
    .inbox { background: var(--bg-color); }
    .inbox-frame { max-width: 1000px; margin: 0 auto; background: white; border-radius: 16px; border: 1px solid var(--border-light); overflow: hidden; box-shadow: 0 20px 40px -10px rgba(0,0,0,0.05); }
    .inbox-header { padding: 16px 24px; border-bottom: 1px solid var(--border-light); display: flex; gap: 8px; background: #F8FAFC; }
    .inbox-dot { width: 10px; height: 10px; border-radius: 50%; background: #CBD5E1; }
    .inbox-body { display: flex; height: 400px; }
    .inbox-list { width: 300px; border-right: 1px solid var(--border-light); overflow-y: auto; }
    .inbox-item { padding: 16px; border-bottom: 1px solid var(--border-light); cursor: pointer; }
    .inbox-item.active { background: #EEF2FF; border-left: 3px solid var(--primary); }
    .inbox-detail { flex: 1; padding: 24px; display: flex; flex-direction: column; align-items: center; justify-content: center; color: var(--text-muted); }
    
    .inbox-points { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; max-width: 800px; margin: 48px auto 0; }
    .inbox-points p { font-size: 16px; font-weight: 500; display: flex; align-items: flex-start; gap: 12px; }
    .inbox-points p::before { content: '✓'; color: var(--primary); font-weight: bold; }

    /* ==================================================
       S14 - ANALYTICS
    ================================================== */
    .analytics { background: white; }
    .stat-card { max-width: 700px; margin: 0 auto; padding: 48px; background: var(--bg-color); border-radius: 24px; border: 1px solid var(--border-light); font-size: 24px; line-height: 1.5; font-weight: 500; text-align: center; }
    .stat-highlight { color: var(--primary); font-weight: 700; }
    .honesty-line { text-align: center; font-size: 13px; color: var(--text-muted); max-width: 500px; margin: 24px auto 0; }

    /* ==================================================
       S15 - COPILOT
    ================================================== */
    .copilot { background: var(--bg-color); text-align: center; }
    .copilot-demo { max-width: 600px; margin: 48px auto 0; text-align: left; background: white; padding: 32px; border-radius: 16px; border: 1px solid var(--border-light); }
    .cp-query { font-size: 16px; font-weight: 600; margin-bottom: 16px; }
    .cp-answer { font-size: 15px; color: var(--text-muted); margin-bottom: 24px; }
    
    /* ==================================================
       S23 - WHO THIS IS FOR
    ================================================== */
    .who-for { background: white; }
    .fit-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 48px; max-width: 900px; margin: 0 auto; }
    .fit-col h3 { font-size: 24px; margin-bottom: 24px; padding-bottom: 16px; border-bottom: 1px solid var(--border-light); }
    .fit-col ul { display: flex; flex-direction: column; gap: 16px; }
    .fit-col li { display: flex; gap: 12px; font-size: 15px; color: var(--text-muted); }
    .good-fit li::before { content: '✓'; color: #10B981; font-weight: bold; }
    .bad-fit li::before { content: '✕'; color: #EF4444; font-weight: bold; }

    /* ==================================================
       S24 - FAQ
    ================================================== */
    .faq { background: var(--bg-color); }
    .faq-container { max-width: 800px; margin: 0 auto; }
    .faq-item { border-bottom: 1px solid var(--border-light); }
    .faq-q { padding: 24px 0; font-size: 18px; font-weight: 600; cursor: pointer; display: flex; justify-content: space-between; align-items: center; }
    .faq-q::after { content: '+'; font-size: 24px; color: var(--text-muted); transition: transform 0.3s; }
    .faq-a { padding-bottom: 24px; font-size: 15px; color: var(--text-muted); display: none; }
    .faq-item.active .faq-q::after { transform: rotate(45deg); }
    .faq-item.active .faq-a { display: block; animation: fadeIn 0.3s ease; }

    /* ==================================================
       S03 - CTA BAND (The ONLY dark block)
    ================================================== */
    .cta-band { background: var(--bg-dark); color: white; padding: 120px 0; text-align: center; position: relative; overflow: hidden; }
    .cta-band h2 { color: white; font-size: 56px; font-weight: 900; margin-bottom: 24px; letter-spacing: -1px; }
    .cta-band p { font-size: 20px; color: #94A3B8; margin-bottom: 40px; }
    .cta-actions { display: flex; justify-content: center; gap: 16px; margin-bottom: 32px; }
    .cta-sub { font-size: 13px; color: #64748B; }
    
    .bg-receipts { position: absolute; inset: 0; display: flex; flex-wrap: wrap; gap: 40px; align-items: center; justify-content: center; opacity: 0.03; pointer-events: none; font-family: monospace; font-size: 24px; font-weight: 700; user-select: none; }

    /* ==================================================
       S02 - FOOTER
    ================================================== */
    .footer { background: white; padding: 64px 0 32px; border-top: 1px solid var(--border-light); }
    .footer-container { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr 1fr; gap: 48px; margin-bottom: 64px; }
    .footer-col h4 { font-size: 14px; font-weight: 700; margin-bottom: 20px; }
    .footer-col ul { display: flex; flex-direction: column; gap: 12px; }
    .footer-col a { color: var(--text-muted); font-size: 14px; }
    .footer-col a:hover { color: var(--primary); }
    .footer-bottom { border-top: 1px solid var(--border-light); padding-top: 32px; display: flex; justify-content: space-between; color: var(--text-muted); font-size: 14px; }

    @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

  </style>
</head>
<body>

  <!-- S01 NAV -->
  <nav class="nav">
    <div class="nav-container">
      <a href="/" class="nav-logo">
        <div class="nav-logo-icon">S</div>
        StepsAI
      </a>
      <div class="nav-links">
        <a class="nav-link">Product ▾</a>
        <a class="nav-link">Solutions ▾</a>
        <a href="/pricing/" class="nav-link">Pricing</a>
        <a href="/partners/" class="nav-link">Partner</a>
        <a class="nav-link">Resources ▾</a>
      </div>
      <div class="nav-actions">
        <a href="#" class="nav-link">Sign in</a>
        <button class="btn btn-primary">Start free trial</button>
      </div>
    </div>
  </nav>

  <!-- S04 LANDING HERO -->
  <section class="hero">
    <div class="container">
      <div class="kicker">AI AGENT FOR SALES & SUPPORT</div>
      <h1>It sold something at<br>11:47 last night.</h1>
      <p>You were asleep. Someone wanted the linen shirt in medium, so your agent checked the stock, held one back, and sent them the checkout link. It does this on WhatsApp, Instagram and your website, all night, without waking anyone.</p>
      
      <div class="hero-actions">
        <button class="btn btn-primary">Start free trial</button>
        <button class="btn btn-outline">Book a demo</button>
      </div>
      <div class="hero-integrations">Works with Shopify, HubSpot, Calendly and your inbox.</div>

      <div class="hero-visuals">
        <!-- Morphing Card -->
        <div class="morph-card" id="morphCard">
          <div class="morph-header" id="morphHeader">
            <span style="color: #25D366;">WhatsApp</span>
          </div>
          <div class="morph-body" id="morphBody">
            <div class="msg-user">Do you have the linen shirt in medium? <span style="font-size:9px;color:#94A3B8;margin-left:4px;">10:42 PM</span></div>
            <div class="msg-agent">Yes, two left in medium. Want me to hold one? <span style="font-size:9px;color:rgba(255,255,255,0.7);margin-left:4px;">10:42 PM</span></div>
            <div class="msg-user">Yes please <span style="font-size:9px;color:#94A3B8;margin-left:4px;">10:43 PM</span></div>
            <div class="msg-agent">Reserved and added to your cart.<br><br><span style="font-size:11px;background:white;color:var(--text-main);padding:4px 8px;border-radius:4px;display:block;">Linen Shirt · Medium · ₹2,400 · Add to cart</span></div>
          </div>
          <div class="receipt" id="morphReceipt">SHOPIFY · CART UPDATED</div>
        </div>
      </div>
    </div>
  </section>

  <!-- S08 FOUR AGENTS -->
  <section class="section-spacing four-agents">
    <div class="container">
      <div class="section-header text-center">
        <div class="kicker">FOUR AGENTS, ONE BRAIN</div>
        <h2 class="section-title">Four jobs. One memory.</h2>
        <p class="section-subtitle">Your support agent knows what your sales agent promised yesterday. That sounds obvious until you have used four separate tools that all forgot.</p>
      </div>

      <div class="grid-2x2">
        <div class="agent-card">
          <h3>Sales Agent</h3>
          <p>Checks what is actually in stock before it promises anything, then closes.</p>
          <div class="agent-receipt">SHOPIFY · CART UPDATED</div>
        </div>
        <div class="agent-card">
          <h3>Lead Agent</h3>
          <p>Finds out budget and timeline the way a good salesperson would, then writes it into your CRM.</p>
          <div class="agent-receipt">HUBSPOT · LEAD CREATED</div>
        </div>
        <div class="agent-card">
          <h3>Meetings Agent</h3>
          <p>Offers times that are genuinely free, and puts the meeting in your calendar.</p>
          <div class="agent-receipt">CALENDAR · MEETING BOOKED</div>
        </div>
        <div class="agent-card">
          <h3>Support Agent</h3>
          <p>Tracks the order, explains the return policy, and only wakes you if something is actually wrong.</p>
          <div class="agent-receipt">ZENDESK · TICKET RESOLVED</div>
        </div>
      </div>
    </div>
  </section>

  <!-- S09 INDUSTRIES -->
  <section class="section-spacing industries">
    <div class="container">
      <div class="section-header text-center">
        <div class="kicker">BUILT FOR YOUR BUSINESS</div>
        <h2 class="section-title">A dental clinic and a sneaker store<br>do not get asked the same questions.</h2>
        <p class="section-subtitle">So they should not give the same answers. Your agent learns your catalogue, your prices, and the ten things people ask you every single week.</p>
      </div>

      <div class="ind-container">
        <div class="ind-tabs">
          <button class="ind-tab active" data-target="ind-ecommerce">E-Commerce</button>
          <button class="ind-tab" data-target="ind-saas">SaaS</button>
          <button class="ind-tab" data-target="ind-health">Healthcare</button>
          <button class="ind-tab" data-target="ind-edu">Education</button>
          <button class="ind-tab" data-target="ind-real">Real Estate</button>
        </div>
        
        <div class="ind-content-area">
          <div id="ind-ecommerce" class="ind-content active">
            <ul>
              <li>Checks live stock before promising anything.</li>
              <li>Goes after the abandoned cart while the customer still wants it.</li>
              <li>Handles "where is my order" so nobody on your team has to.</li>
            </ul>
            <div class="agent-receipt" style="margin-bottom:24px;">SHOPIFY · ORDER PLACED</div>
            <div class="ind-visual">Product UI Mockup</div>
          </div>
          
          <div id="ind-saas" class="ind-content">
            <ul>
              <li>Answers integration questions straight from your own docs.</li>
              <li>Compares plans without steering everyone to the expensive one.</li>
              <li>Passes the serious buyer to sales, whatever time it is.</li>
            </ul>
            <div class="agent-receipt" style="margin-bottom:24px;">HUBSPOT · TRIAL STARTED</div>
            <div class="ind-visual">SaaS UI Mockup</div>
          </div>
          
          <div id="ind-health" class="ind-content">
            <ul>
              <li>Says which doctor is free and when, without a phone call.</li>
              <li>Books the appointment inside the conversation.</li>
              <li>Sends the reminder so the slot does not go empty.</li>
            </ul>
            <div class="agent-receipt" style="margin-bottom:24px;">CALENDAR · APPOINTMENT BOOKED</div>
            <div class="ind-visual">Health UI Mockup</div>
          </div>
          
          <div id="ind-edu" class="ind-content">
            <ul>
              <li>Answers fee and batch questions before the parent loses interest.</li>
              <li>Captures their details while they are still asking.</li>
              <li>Books the counsellor call before they ring the institute down the road.</li>
            </ul>
            <div class="agent-receipt" style="margin-bottom:24px;">CRM · ENQUIRY CAPTURED</div>
            <div class="ind-visual">Edu UI Mockup</div>
          </div>

          <div id="ind-real" class="ind-content">
            <ul>
              <li>Finds out the budget before anyone picks up a phone.</li>
              <li>Books the site visit while they are still browsing listings.</li>
              <li>Sends the address, then the reminder, on its own.</li>
            </ul>
            <div class="agent-receipt" style="margin-bottom:24px;">CRM · SITE VISIT SCHEDULED</div>
            <div class="ind-visual">Real Estate UI Mockup</div>
          </div>
        </div>
      </div>
      
      <div class="text-center" style="margin-top: 48px;">
        <a href="#" class="btn btn-outline" style="border:none; color:var(--primary);">See how it works for you &rarr;</a>
      </div>
    </div>
  </section>

  <!-- S10 CHANNELS -->
  <section class="section-spacing channels">
    <div class="container">
      <div class="section-header text-center">
        <div class="kicker">EVERY CHANNEL</div>
        <h2 class="section-title">On Instagram it replies in public,<br>then finishes the sale in private.</h2>
        <p class="section-subtitle">A comment under a post and a WhatsApp message at midnight are not the same kind of conversation. Your agent treats them differently, because your customers do.</p>
      </div>

      <div class="channel-row">
        <div class="ch-content">
          <h3>The comment nobody had time to answer.</h3>
          <p>Someone asks the price under your post. Your agent replies where everyone can see it, slides into the DM, and finishes the conversation there. A scripted chatbot cannot do this, because it needs a customer to start the conversation first.</p>
          <div class="agent-receipt">INSTAGRAM · COMMENT CONVERTED TO DM</div>
        </div>
        <div class="ch-visual">Instagram Mockup</div>
      </div>
      
      <div class="channel-row">
        <div class="ch-content">
          <h3>Where your customers already spend their evening.</h3>
          <p>Booking links, payment links, delivery updates, all inside the app they already have open. Broadcasts only go to people who asked to hear from you.</p>
          <div class="agent-receipt">WHATSAPP · MESSAGE DELIVERED</div>
        </div>
        <div class="ch-visual">WhatsApp Mockup</div>
      </div>
      
      <div class="channel-row">
        <div class="ch-content">
          <h3>It knows which page they are standing on.</h3>
          <p>Someone asks "does this come in blue" while looking at a specific jacket. Your agent knows which jacket. It answers about that one, and captures the lead without sending anyone to a form.</p>
          <div class="agent-receipt">HUBSPOT · LEAD CAPTURED FROM WEBSITE</div>
        </div>
        <div class="ch-visual">Website Mockup</div>
      </div>
    </div>
  </section>

  <!-- S11 SETUP -->
  <section class="section-spacing setup">
    <div class="container">
      <div class="section-header text-center">
        <div class="kicker">LIVE IN AN AFTERNOON</div>
        <h2 class="section-title">Paste your website link.<br>That is genuinely the hard part.</h2>
        <p class="section-subtitle">Your agent reads your pages and works out what you sell. You check it, change the greeting so it sounds like you, and switch on the channels you want. Most people are finished before their coffee goes cold.</p>
      </div>

      <div class="setup-grid">
        <div class="setup-steps">
          <div class="setup-step">
            <div class="step-num">1</div>
            <div class="step-content">
              <h4>Teach it</h4>
              <p>Paste the link. It reads your site and learns your products, your prices, and your policies.</p>
            </div>
          </div>
          <div class="setup-step">
            <div class="step-num">2</div>
            <div class="step-content">
              <h4>Make it yours</h4>
              <p>Pick the name, the colour, and the first thing it says. Keep changing the tone until it sounds like someone who works for you.</p>
            </div>
          </div>
          <div class="setup-step">
            <div class="step-num">3</div>
            <div class="step-content">
              <h4>Connect it</h4>
              <p>Shopify, your calendar, your CRM, your inbox. Each one you connect gives your agent something new it can actually do rather than just talk about.</p>
            </div>
          </div>
          <div class="setup-step">
            <div class="step-num">4</div>
            <div class="step-content">
              <h4>Go live</h4>
              <p>Try to trip it up first. When you cannot, switch on your channels.</p>
              <div class="agent-receipt" style="margin-top:12px;">AGENT · LIVE ON 3 CHANNELS</div>
            </div>
          </div>
        </div>
        <div class="ch-visual">Setup UI Mockup</div>
      </div>
    </div>
  </section>

  <!-- S12 WORKFLOWS -->
  <section class="section-spacing workflows">
    <div class="container">
      <div class="section-header text-center">
        <div class="kicker">AUTOMATED WORKFLOWS</div>
        <h2 class="section-title">Most sales do not die from a no.<br>They die from silence.</h2>
        <p class="section-subtitle">Somebody fills a cart and then their food arrives. A lead asks one question and disappears for a week. Your agent notices the gap, waits the right amount of time, and starts the conversation up again.</p>
      </div>

      <div class="wf-tabs">
        <button class="wf-tab active">Recover carts</button>
        <button class="wf-tab">Follow up leads</button>
        <button class="wf-tab">Remind customers</button>
        <button class="wf-tab">Re-engage</button>
      </div>
      
      <div class="wf-rail">
        <div class="wf-node active">Cart left behind<br><span style="font-size:11px;font-weight:400;">₹2,400</span></div>
        <div class="wf-node">Wait 30 minutes</div>
        <div class="wf-node">Check, order still<br>not placed</div>
        <div class="wf-node">Send a WhatsApp<br>message</div>
        <div class="wf-node active" style="border-color:#10B981; color:#10B981;">CHECKOUT REOPENED</div>
      </div>
      
      <p class="text-center" style="font-size:14px;color:var(--text-muted);">Answer whatever is holding them up, share the checkout.</p>
    </div>
  </section>

  <!-- S13 ONE INBOX -->
  <section class="section-spacing inbox">
    <div class="container">
      <div class="section-header text-center">
        <div class="kicker">YOU STAY IN CONTROL</div>
        <h2 class="section-title">It never sends a message<br>you cannot read.</h2>
        <p class="section-subtitle">Every conversation, from every channel, lands in one inbox. Jump in whenever you feel like it and your agent goes quiet on that thread until you are finished.</p>
      </div>

      <div class="inbox-frame">
        <div class="inbox-header">
          <div class="inbox-dot" style="background:#EF4444;"></div>
          <div class="inbox-dot" style="background:#F59E0B;"></div>
          <div class="inbox-dot" style="background:#10B981;"></div>
        </div>
        <div class="inbox-body">
          <div class="inbox-list">
            <div class="inbox-item active">
              <strong>+91 98*** ***45</strong>
              <div style="font-size:13px;color:var(--text-muted);margin-top:4px;">WhatsApp &bull; Handoff active</div>
            </div>
            <div class="inbox-item">
              <strong>@david_sneakers</strong>
              <div style="font-size:13px;color:var(--text-muted);margin-top:4px;">Instagram &bull; Resolved</div>
            </div>
          </div>
          <div class="inbox-detail">
            <div>Message thread view</div>
          </div>
        </div>
      </div>
      
      <div class="inbox-points">
        <p>You decide what it is allowed to answer.</p>
        <p>You decide where it has to stop.</p>
        <p>Every conversation is there to read.</p>
        <p>When it hands over, the whole history comes with it.</p>
      </div>
    </div>
  </section>

  <!-- S14 ANALYTICS -->
  <section class="section-spacing analytics">
    <div class="container">
      <div class="section-header text-center">
        <div class="kicker">SEE WHAT IT DID</div>
        <h2 class="section-title">A paragraph, not a dashboard.</h2>
        <p class="section-subtitle">Most analytics tell you a number moved. Yours tells you that three people asked for something you do not stock yet.</p>
      </div>

      <div class="stat-card">
        This week your agent handled <span class="stat-highlight">412 conversations</span>. It answered <span class="stat-highlight">358</span> on its own, booked <span class="stat-highlight">24</span> meetings, and passed <span class="stat-highlight">30</span> to your team. Three customers asked about a product you do not stock yet.
      </div>
      
      <p class="honesty-line">Every number on this page comes from a real account or is clearly marked as an example. We do not publish numbers we cannot show you.</p>
    </div>
  </section>

  <!-- S15 COPILOT -->
  <section class="section-spacing copilot">
    <div class="container">
      <div class="section-header text-center">
        <div class="kicker">INTERNAL COPILOT</div>
        <h2 class="section-title">The same brain, pointed inwards.</h2>
        <p class="section-subtitle">Your team asks it where the leave policy lives, what you agreed with that client in March, which version of the deck is the current one. It looks through everything you have connected, answers, and shows you exactly which document it got that from.</p>
      </div>
      
      <div class="copilot-demo">
        <div class="cp-query">What is our current sick leave policy?</div>
        <div class="cp-answer">Employees are entitled to 12 days of paid sick leave per year, prorated for new joiners. A medical certificate is required for absences exceeding 3 consecutive days.</div>
        <div class="agent-receipt">CITED FROM &middot; HR_MANUAL_2024.PDF</div>
      </div>
      
      <div style="margin-top: 48px;">
        <a href="/product/copilot/" class="btn btn-outline">See Internal Copilot &rarr;</a>
      </div>
    </div>
  </section>

  <!-- S16 REAL PROOF (Hidden as per spec) -->
  <!--
  <section class="section-spacing real-proof">
    <div class="container">
       Hidden until real, attributed material exists. 
    </div>
  </section>
  -->

  <!-- S23 WHO THIS IS FOR -->
  <section class="section-spacing who-for">
    <div class="container">
      <div class="section-header text-center">
        <div class="kicker">HONEST FIT</div>
        <h2 class="section-title">You might not need this.</h2>
        <p class="section-subtitle">Some businesses are better off without it, and it is cheaper for both of us if you work that out now rather than in month three.</p>
      </div>

      <div class="fit-grid">
        <div class="fit-col good-fit">
          <h3>Worth trying if</h3>
          <ul>
            <li>People are messaging you on WhatsApp, Instagram or your website in real numbers.</li>
            <li>You are losing sales because nobody replied fast enough.</li>
            <li>You answer the same handful of questions every day and have started to resent them.</li>
            <li>You want to decide what the AI is allowed to say.</li>
          </ul>
        </div>
        <div class="fit-col bad-fit">
          <h3>Probably not, if</h3>
          <ul>
            <li>You want an AI running loose with nobody checking on it.</li>
            <li>You are hoping to let your support team go.</li>
            <li>You expect it to work properly without anyone setting it up.</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- S24 FAQ -->
  <section class="section-spacing faq">
    <div class="container">
      <div class="section-header text-center">
        <div class="kicker">QUESTIONS</div>
        <h2 class="section-title">Everything else.</h2>
      </div>

      <div class="faq-container">
        <div class="faq-item">
          <div class="faq-q">Is this just a chatbot?</div>
          <div class="faq-a">No. A chatbot picks an answer off a list. Your agent checks live stock, books a real slot in your calendar, writes the lead into your CRM, and pulls up an actual order. When it tells a customer something is reserved, it is reserved.</div>
        </div>
        <div class="faq-item">
          <div class="faq-q">Will it sound like a robot?</div>
          <div class="faq-a">Only if you write like one. You set the greeting, the tone, and the things it is never allowed to say. Most people spend ten minutes on this and never open it again.</div>
        </div>
        <div class="faq-item">
          <div class="faq-q">Do I need a developer?</div>
          <div class="faq-a">No. If you can set up a business account on Instagram, you can do this.</div>
        </div>
        <div class="faq-item">
          <div class="faq-q">What if it does not know something?</div>
          <div class="faq-a">It says so and hands the conversation to your team with the full history attached. It will not invent an answer to sound clever.</div>
        </div>
        <div class="faq-item">
          <div class="faq-q">Can I see what it is saying to customers?</div>
          <div class="faq-a">All of it. Nothing happens in a window you cannot open.</div>
        </div>
        <div class="faq-item">
          <div class="faq-q">What happens when I want to take over?</div>
          <div class="faq-a">You start typing and it stops. It stays out of that conversation until you are done with it.</div>
        </div>
        <div class="faq-item">
          <div class="faq-q">Which languages does it speak?</div>
          <div class="faq-a">It answers in whatever language your customer writes in.</div>
        </div>
        <div class="faq-item">
          <div class="faq-q">How long before it is live?</div>
          <div class="faq-a">Most people are running the same afternoon.</div>
        </div>
      </div>
    </div>
  </section>

  <!-- S03 CTA BAND (The ONLY dark block) -->
  <section class="cta-band">
    <div class="bg-receipts">
      CART UPDATED &middot; MEETING BOOKED &middot; LEAD CREATED &middot; ORDER TRACKED &middot; TICKET RESOLVED
    </div>
    <div class="container" style="position:relative; z-index:2;">
      <h2>Somebody is typing right now.</h2>
      <p>Set it up this afternoon. Find out what it did over breakfast.</p>
      <div class="cta-actions">
        <button class="btn btn-primary">Start free trial</button>
        <button class="btn btn-dark">Book a demo</button>
      </div>
      <div class="cta-sub">No credit card. Live in under an hour.</div>
    </div>
  </section>

  <!-- S02 FOOTER -->
  <footer class="footer">
    <div class="container">
      <div class="footer-container">
        <div class="footer-col" style="grid-column: span 2;">
          <a href="/" class="nav-logo" style="margin-bottom:16px;">
            <div class="nav-logo-icon">S</div>
            StepsAI
          </a>
          <p style="color:var(--text-muted); font-size:14px; max-width:250px;">Your AI agent layer for every business</p>
        </div>
        <div class="footer-col">
          <h4>Product</h4>
          <ul>
            <li><a href="/product/ai-agents/">AI Agents</a></li>
            <li><a href="/product/copilot/">Internal Copilot</a></li>
            <li><a href="/pricing/">Pricing</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Solutions</h4>
          <ul>
            <li><a href="/solutions/ecommerce/">E-Commerce</a></li>
            <li><a href="/solutions/saas/">SaaS</a></li>
            <li><a href="/solutions/real-estate/">Real Estate</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Resources</h4>
          <ul>
            <li><a href="/blog/">Blog</a></li>
            <li><a href="/about/">About</a></li>
            <li><a href="/contact/">Contact</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <div>&copy; 2024 StepsAI. All rights reserved.</div>
        <div style="display:flex; gap:24px;">
          <a href="/privacy-policy/">Privacy</a>
          <a href="/terms-of-service/">Terms</a>
        </div>
      </div>
    </div>
  </footer>

  <script>
    // FAQ Accordion
    document.querySelectorAll('.faq-q').forEach(q => {
      q.addEventListener('click', () => {
        const item = q.parentElement;
        const isActive = item.classList.contains('active');
        document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('active'));
        if (!isActive) item.classList.add('active');
      });
    });

    // Industries Tabs
    const indTabs = document.querySelectorAll('.ind-tab');
    const indContents = document.querySelectorAll('.ind-content');
    indTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        indTabs.forEach(t => t.classList.remove('active'));
        indContents.forEach(c => c.classList.remove('active'));
        
        tab.classList.add('active');
        document.getElementById(tab.getAttribute('data-target')).classList.add('active');
      });
    });

    // Morphing Hero Logic (Simplified 8s loop)
    const morphScenarios = [
      {
        channel: 'WhatsApp', color: '#25D366',
        messages: [
          { u: 'Do you have the linen shirt in medium?', t1: '10:42 PM', a: 'Yes, two left in medium. Want me to hold one?', t2: '10:42 PM' },
          { u: 'Yes please', t1: '10:43 PM', a: 'Reserved and added to your cart.<br><br><span style="font-size:11px;background:white;color:var(--text-main);padding:4px 8px;border-radius:4px;display:block;">Linen Shirt &middot; Medium &middot; ₹2,400 &middot; Add to cart</span>', t2: '10:43 PM' }
        ],
        receipt: 'SHOPIFY &middot; CART UPDATED'
      },
      {
        channel: 'Instagram', color: '#E1306C',
        messages: [
          { u: 'Is the 3BHK still available?', t1: '9:15 PM', a: 'It is. Want to see it this weekend?', t2: '9:15 PM' },
          { u: 'Saturday works', t1: '9:16 PM', a: 'Booked for Saturday 11 AM. Sending the address.<br><br><span style="font-size:11px;background:white;color:var(--text-main);padding:4px 8px;border-radius:4px;display:block;">Sat 11:00 &middot; Sat 4:00 &middot; Sun 11:00</span>', t2: '9:16 PM' }
        ],
        receipt: 'CALENDAR &middot; SITE VISIT BOOKED'
      },
      {
        channel: 'Website', color: '#6366F1',
        messages: [
          { u: 'Where is my order?', t1: '11:58 PM', a: 'Order #2453 is out for delivery. It arrives tomorrow before 6 PM.<br><br><span style="font-size:11px;background:white;color:var(--text-main);padding:4px 8px;border-radius:4px;display:block;">#2453 &middot; Out for delivery</span>', t2: '11:58 PM' },
          { u: 'Perfect, thanks', t1: '11:59 PM', a: 'Anytime. I\\'ll message you when it\\'s delivered.', t2: '11:59 PM' }
        ],
        receipt: 'ORDER &middot; TRACKED & CUSTOMER NOTIFIED'
      }
    ];

    let currentMorph = 0;
    const morphHeader = document.getElementById('morphHeader');
    const morphBody = document.getElementById('morphBody');
    const morphReceipt = document.getElementById('morphReceipt');

    function updateMorph() {
      const data = morphScenarios[currentMorph];
      morphHeader.innerHTML = `<span style="color: ${data.color};">${data.channel}</span>`;
      
      let bodyHtml = '';
      data.messages.forEach(m => {
        bodyHtml += `<div class="msg-user">${m.u} <span style="font-size:9px;color:#94A3B8;margin-left:4px;">${m.t1}</span></div>`;
        bodyHtml += `<div class="msg-agent">${m.a} <span style="font-size:9px;color:rgba(255,255,255,0.7);margin-left:4px;">${m.t2}</span></div>`;
      });
      morphBody.innerHTML = bodyHtml;
      morphReceipt.innerHTML = data.receipt;

      currentMorph = (currentMorph + 1) % morphScenarios.length;
    }

    setInterval(updateMorph, 8000); // 8s loop
  </script>
</body>
</html>
"""

with open(r"C:\Users\user\Downloads\HOME STAEP AI\StepsAI_Redesign.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("StepsAI_Redesign.html successfully updated to match the master specification.")
