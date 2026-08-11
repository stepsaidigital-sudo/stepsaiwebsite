import os
import re

# Sections to append (using the new blue brand)
css_to_append = """
    /* --- NEW SECTIONS CSS (Appended) --- */
    .setup { background: var(--bg-color); }
    .setup-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 64px; align-items: center; max-width: 1200px; margin: 0 auto; padding: 0 24px; }
    .setup-steps { display: flex; flex-direction: column; gap: 32px; }
    .setup-step { display: flex; gap: 20px; }
    .step-num { width: 32px; height: 32px; border-radius: 50%; background: white; border: 1px solid var(--border-light); display: flex; align-items: center; justify-content: center; font-weight: 700; color: #2563EB; flex-shrink: 0; }
    .step-content h4 { font-size: 18px; margin-bottom: 8px; }
    .step-content p { color: var(--text-muted); font-size: 15px; }
    
    .workflows { background: white; }
    .wf-tabs { display: flex; gap: 16px; margin-bottom: 48px; justify-content: center; }
    .wf-tab { padding: 10px 20px; border-radius: 100px; border: 1px solid var(--border-light); background: var(--bg-color); font-weight: 600; cursor: pointer; font-size: 14px; color: var(--text-muted); }
    .wf-tab.active { background: #2563EB; color: white; border-color: #2563EB; }
    
    .wf-rail { display: flex; align-items: center; justify-content: space-between; position: relative; margin-bottom: 64px; max-width: 800px; margin-left: auto; margin-right: auto; }
    .wf-rail::before { content: ''; position: absolute; top: 50%; left: 0; width: 100%; height: 2px; background: var(--border-light); z-index: 1; transform: translateY(-50%); }
    .wf-node { position: relative; z-index: 2; background: white; border: 2px solid var(--border-light); padding: 12px 16px; border-radius: 8px; font-size: 13px; font-weight: 600; width: 140px; text-align: center; }
    .wf-node.active { border-color: #2563EB; color: #2563EB; box-shadow: 0 4px 12px rgba(37,99,235,0.1); }

    .inbox { background: var(--bg-color); }
    .inbox-frame { max-width: 1000px; margin: 0 auto; background: white; border-radius: 16px; border: 1px solid var(--border-light); overflow: hidden; box-shadow: 0 20px 40px -10px rgba(0,0,0,0.05); }
    .inbox-header { padding: 16px 24px; border-bottom: 1px solid var(--border-light); display: flex; gap: 8px; background: #F8FAFC; }
    .inbox-dot { width: 10px; height: 10px; border-radius: 50%; background: #CBD5E1; }
    .inbox-body { display: flex; height: 400px; }
    .inbox-list { width: 300px; border-right: 1px solid var(--border-light); overflow-y: auto; }
    .inbox-item { padding: 16px; border-bottom: 1px solid var(--border-light); cursor: pointer; }
    .inbox-item.active { background: #EEF2FF; border-left: 3px solid #2563EB; }
    .inbox-detail { flex: 1; padding: 24px; display: flex; flex-direction: column; align-items: center; justify-content: center; color: var(--text-muted); }
    .inbox-points { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; max-width: 800px; margin: 48px auto 0; }
    .inbox-points p { font-size: 16px; font-weight: 500; display: flex; align-items: flex-start; gap: 12px; }
    .inbox-points p::before { content: '✓'; color: #2563EB; font-weight: bold; }

    .analytics { background: white; }
    .stat-card { max-width: 700px; margin: 0 auto; padding: 48px; background: var(--bg-color); border-radius: 24px; border: 1px solid var(--border-light); font-size: 24px; line-height: 1.5; font-weight: 500; text-align: center; }
    .stat-highlight { color: #2563EB; font-weight: 700; }
    .honesty-line { text-align: center; font-size: 13px; color: var(--text-muted); max-width: 500px; margin: 24px auto 0; }

    .copilot { background: var(--bg-color); text-align: center; }
    .copilot-demo { max-width: 600px; margin: 48px auto 0; text-align: left; background: white; padding: 32px; border-radius: 16px; border: 1px solid var(--border-light); }
    .cp-query { font-size: 16px; font-weight: 600; margin-bottom: 16px; }
    .cp-answer { font-size: 15px; color: var(--text-muted); margin-bottom: 24px; }
    
    .who-for { background: white; }
    .fit-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 48px; max-width: 900px; margin: 0 auto; }
    .fit-col h3 { font-size: 24px; margin-bottom: 24px; padding-bottom: 16px; border-bottom: 1px solid var(--border-light); }
    .fit-col ul { display: flex; flex-direction: column; gap: 16px; }
    .fit-col li { display: flex; gap: 12px; font-size: 15px; color: var(--text-muted); }
    .good-fit li::before { content: '✓'; color: #10B981; font-weight: bold; }
    .bad-fit li::before { content: '✕'; color: #EF4444; font-weight: bold; }

    .faq { background: var(--bg-color); }
    .faq-container { max-width: 800px; margin: 0 auto; }
    .faq-item { border-bottom: 1px solid var(--border-light); }
    .faq-q { padding: 24px 0; font-size: 18px; font-weight: 600; cursor: pointer; display: flex; justify-content: space-between; align-items: center; }
    .faq-q::after { content: '+'; font-size: 24px; color: var(--text-muted); transition: transform 0.3s; }
    .faq-a { padding-bottom: 24px; font-size: 15px; color: var(--text-muted); display: none; }
    .faq-item.active .faq-q::after { transform: rotate(45deg); }
    .faq-item.active .faq-a { display: block; }

    .cta-band { background: #0F172A; color: white; padding: 120px 0; text-align: center; position: relative; overflow: hidden; }
    .cta-band h2 { color: white; font-size: 56px; font-weight: 900; margin-bottom: 24px; letter-spacing: -1px; }
    .cta-band p { font-size: 20px; color: #94A3B8; margin-bottom: 40px; }
    .cta-actions { display: flex; justify-content: center; gap: 16px; margin-bottom: 32px; }
    .cta-sub { font-size: 13px; color: #64748B; }
    
    .footer { background: white; padding: 64px 0 32px; border-top: 1px solid var(--border-light); }
    .footer-container { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr 1fr; gap: 48px; max-width: 1200px; margin: 0 auto 64px; padding: 0 24px; }
    .footer-col h4 { font-size: 14px; font-weight: 700; margin-bottom: 20px; }
    .footer-col ul { display: flex; flex-direction: column; gap: 12px; list-style: none;}
    .footer-col a { color: var(--text-muted); font-size: 14px; text-decoration: none;}
    .footer-col a:hover { color: #2563EB; }
    .footer-bottom { border-top: 1px solid var(--border-light); padding-top: 32px; display: flex; justify-content: space-between; color: var(--text-muted); font-size: 14px; max-width: 1200px; margin: 0 auto; padding: 32px 24px 0; }
"""

html_to_append = """
  <!-- S11 SETUP -->
  <section class="setup" style="padding: 120px 0;">
    <div style="text-align: center; margin-bottom: 64px;">
        <div style="color: #2563EB; font-size: 11px; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase; margin-bottom: 16px;">LIVE IN AN AFTERNOON</div>
        <h2 style="font-size: 48px; font-weight: 800; margin-bottom: 16px; letter-spacing: -1px;">Paste your website link.<br>That is genuinely the hard part.</h2>
        <p style="color: var(--text-muted); font-size: 18px; max-width: 600px; margin: 0 auto;">Your agent reads your pages and works out what you sell. You check it, change the greeting so it sounds like you, and switch on the channels you want. Most people are finished before their coffee goes cold.</p>
    </div>
    <div class="setup-grid">
      <div class="setup-steps">
        <div class="setup-step"><div class="step-num">1</div><div class="step-content"><h4>Teach it</h4><p>Paste the link. It reads your site and learns your products, your prices, and your policies.</p></div></div>
        <div class="setup-step"><div class="step-num">2</div><div class="step-content"><h4>Make it yours</h4><p>Pick the name, the colour, and the first thing it says. Keep changing the tone until it sounds like someone who works for you.</p></div></div>
        <div class="setup-step"><div class="step-num">3</div><div class="step-content"><h4>Connect it</h4><p>Shopify, your calendar, your CRM, your inbox. Each one you connect gives your agent something new it can actually do rather than just talk about.</p></div></div>
        <div class="setup-step"><div class="step-num">4</div><div class="step-content"><h4>Go live</h4><p>Try to trip it up first. When you cannot, switch on your channels.</p></div></div>
      </div>
      <div style="background: white; border: 1px solid var(--border-light); border-radius: 24px; height: 400px; display: flex; align-items: center; justify-content: center; color: var(--text-muted);">Setup UI Mockup</div>
    </div>
  </section>

  <!-- S12 WORKFLOWS -->
  <section class="workflows" style="padding: 120px 0;">
    <div style="text-align: center; margin-bottom: 64px;">
        <div style="color: #2563EB; font-size: 11px; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase; margin-bottom: 16px;">AUTOMATED WORKFLOWS</div>
        <h2 style="font-size: 48px; font-weight: 800; margin-bottom: 16px; letter-spacing: -1px;">Most sales do not die from a no.<br>They die from silence.</h2>
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
  </section>

  <!-- S13 ONE INBOX -->
  <section class="inbox" style="padding: 120px 0;">
    <div style="text-align: center; margin-bottom: 64px;">
        <div style="color: #2563EB; font-size: 11px; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase; margin-bottom: 16px;">YOU STAY IN CONTROL</div>
        <h2 style="font-size: 48px; font-weight: 800; margin-bottom: 16px; letter-spacing: -1px;">It never sends a message<br>you cannot read.</h2>
    </div>
    <div class="inbox-frame">
      <div class="inbox-header"><div class="inbox-dot" style="background:#EF4444;"></div><div class="inbox-dot" style="background:#F59E0B;"></div><div class="inbox-dot" style="background:#10B981;"></div></div>
      <div class="inbox-body">
        <div class="inbox-list">
          <div class="inbox-item active"><strong>+91 98*** ***45</strong><div style="font-size:13px;color:var(--text-muted);margin-top:4px;">WhatsApp &bull; Handoff active</div></div>
        </div>
        <div class="inbox-detail"><div>Message thread view</div></div>
      </div>
    </div>
    <div class="inbox-points">
      <p>You decide what it is allowed to answer.</p>
      <p>You decide where it has to stop.</p>
      <p>Every conversation is there to read.</p>
      <p>When it hands over, the whole history comes with it.</p>
    </div>
  </section>

  <!-- S14 ANALYTICS -->
  <section class="analytics" style="padding: 120px 0;">
    <div style="text-align: center; margin-bottom: 64px;">
        <div style="color: #2563EB; font-size: 11px; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase; margin-bottom: 16px;">SEE WHAT IT DID</div>
        <h2 style="font-size: 48px; font-weight: 800; margin-bottom: 16px; letter-spacing: -1px;">A paragraph, not a dashboard.</h2>
    </div>
    <div class="stat-card">
      This week your agent handled <span class="stat-highlight">412 conversations</span>. It answered <span class="stat-highlight">358</span> on its own, booked <span class="stat-highlight">24</span> meetings, and passed <span class="stat-highlight">30</span> to your team. Three customers asked about a product you do not stock yet.
    </div>
    <p class="honesty-line">Every number on this page comes from a real account or is clearly marked as an example. We do not publish numbers we cannot show you.</p>
  </section>

  <!-- S15 COPILOT -->
  <section class="copilot" style="padding: 120px 0;">
    <div style="text-align: center; margin-bottom: 64px;">
        <div style="color: #2563EB; font-size: 11px; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase; margin-bottom: 16px;">INTERNAL COPILOT</div>
        <h2 style="font-size: 48px; font-weight: 800; margin-bottom: 16px; letter-spacing: -1px;">The same brain, pointed inwards.</h2>
    </div>
    <div class="copilot-demo">
      <div class="cp-query">What is our current sick leave policy?</div>
      <div class="cp-answer">Employees are entitled to 12 days of paid sick leave per year. A medical certificate is required for absences exceeding 3 days.</div>
      <div style="font-family: monospace; font-size: 12px; color: #2563EB; font-weight: 600; background: #EEF2FF; padding: 8px 12px; border-radius: 6px; display: inline-block;">CITED FROM &middot; HR_MANUAL.PDF</div>
    </div>
  </section>

  <!-- S23 WHO THIS IS FOR -->
  <section class="who-for" style="padding: 120px 0;">
    <div style="text-align: center; margin-bottom: 64px;">
        <div style="color: #2563EB; font-size: 11px; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase; margin-bottom: 16px;">HONEST FIT</div>
        <h2 style="font-size: 48px; font-weight: 800; margin-bottom: 16px; letter-spacing: -1px;">You might not need this.</h2>
    </div>
    <div class="fit-grid">
      <div class="fit-col good-fit">
        <h3>Worth trying if</h3>
        <ul>
          <li>People are messaging you on WhatsApp or Instagram in real numbers.</li>
          <li>You are losing sales because nobody replied fast enough.</li>
          <li>You want to decide what the AI is allowed to say.</li>
        </ul>
      </div>
      <div class="fit-col bad-fit">
        <h3>Probably not, if</h3>
        <ul>
          <li>You want an AI running loose with nobody checking on it.</li>
          <li>You expect it to work properly without anyone setting it up.</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- S24 FAQ -->
  <section class="faq" style="padding: 120px 0;">
    <div style="text-align: center; margin-bottom: 64px;">
        <div style="color: #2563EB; font-size: 11px; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase; margin-bottom: 16px;">QUESTIONS</div>
        <h2 style="font-size: 48px; font-weight: 800; margin-bottom: 16px; letter-spacing: -1px;">Everything else.</h2>
    </div>
    <div class="faq-container">
      <div class="faq-item">
        <div class="faq-q">Is this just a chatbot?</div>
        <div class="faq-a">No. A chatbot picks an answer off a list. Your agent checks live stock, books a real slot in your calendar, and pulls up an actual order.</div>
      </div>
      <div class="faq-item">
        <div class="faq-q">Will it sound like a robot?</div>
        <div class="faq-a">Only if you write like one. You set the greeting, the tone, and the things it is never allowed to say.</div>
      </div>
      <div class="faq-item">
        <div class="faq-q">Can I see what it is saying to customers?</div>
        <div class="faq-a">All of it. Nothing happens in a window you cannot open.</div>
      </div>
    </div>
  </section>

  <!-- S03 CTA BAND -->
  <section class="cta-band">
    <h2>Somebody is typing right now.</h2>
    <p>Set it up this afternoon. Find out what it did over breakfast.</p>
    <div class="cta-actions">
      <button style="background: #2563EB; color: white; padding: 12px 24px; border-radius: 8px; font-size: 15px; font-weight: 600; border: none; cursor: pointer;">Start free trial</button>
      <button style="background: white; color: #0F172A; padding: 12px 24px; border-radius: 8px; font-size: 15px; font-weight: 600; border: none; cursor: pointer;">Book a demo</button>
    </div>
    <div class="cta-sub">No credit card. Live in under an hour.</div>
  </section>

  <!-- S02 FOOTER -->
  <footer class="footer">
    <div class="footer-container">
      <div class="footer-col" style="grid-column: span 2;">
        <div style="font-weight: 800; font-size: 20px; margin-bottom:16px;">StepsAI</div>
        <p style="color:var(--text-muted); font-size:14px;">Your AI agent layer for every business</p>
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
        <h4>Resources</h4>
        <ul><li><a href="/blog/">Blog</a></li><li><a href="/about/">About</a></li><li><a href="/contact/">Contact</a></li></ul>
      </div>
    </div>
  </footer>
"""

script_to_append = """
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
</script>
"""

file_path = r"c:\Users\user\Downloads\HOME STAEP AI\StepsAI_Redesign.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace primary color in old CSS if it's there
content = content.replace("#6366f1", "#2563EB")
content = content.replace("#6366F1", "#2563EB")

# Inject CSS before </style> or </head>
if "</style>" in content:
    content = content.replace("</style>", css_to_append + "\n</style>")
else:
    content = content.replace("</head>", "<style>" + css_to_append + "</style>\n</head>")

# Remove any existing footer or dark sections at the end to prevent duplication
# For safety, just insert HTML before </body>
content = content.replace("</body>", html_to_append + "\n" + script_to_append + "\n</body>")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("StepsAI_Redesign.html patched with missing sections and new brand blue.")
