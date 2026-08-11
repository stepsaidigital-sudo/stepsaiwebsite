import os

# --- V2 GSAP S-BLOCK TEMPLATES ---

GLOBAL_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>StepsAI - {title}</title>
  <link rel="stylesheet" href="/assets/css/style.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
  <style>
    .gsap-fade-up { opacity: 0; transform: translateY(40px); }
    .gsap-scale-in { opacity: 0; transform: scale(0.9); }
    
    .hero-v2 { min-height: 80vh; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 160px 32px 80px; position: relative; overflow: hidden; }
    .hero-bg-glow { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 80vw; height: 80vw; background: radial-gradient(circle, var(--accent-tint) 0%, rgba(251,252,254,0) 70%); z-index: -1; }
    .hero-v2 h1 { font-size: clamp(48px, 6vw, 80px); line-height: 1.05; letter-spacing: -2px; max-width: 1000px; margin: 24px auto; font-family: 'Outfit', sans-serif; }
    .hero-v2 p { font-size: 20px; color: var(--text-secondary); max-width: 720px; margin: 0 auto 48px; line-height: 1.6; }
    
    .section-v2 { padding: 112px 32px; max-width: 1400px; margin: 0 auto; }
    .section-title-v2 { font-size: clamp(36px, 4vw, 54px); letter-spacing: -1px; margin-bottom: 80px; font-family: 'Outfit', sans-serif; text-align: center;}
    
    .bento-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px; grid-auto-flow: dense; }
    .bento-card { background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 24px; padding: 48px; position: relative; overflow: hidden; display: flex; flex-direction: column; justify-content: flex-end; transition: transform 0.5s cubic-bezier(.16,1,.3,1), border-color 0.5s, box-shadow 0.5s; box-shadow: var(--shadow); }
    .bento-card:hover { transform: translateY(-8px); border-color: var(--accent); box-shadow: var(--shadow-lg); }
    .bento-title { font-size: 32px; font-weight: 700; margin-bottom: 16px; font-family: 'Outfit', sans-serif; color: var(--text-primary);}
    .bento-desc { color: var(--text-secondary); font-size: 16px; line-height: 1.6; }
    @media (max-width: 992px) { .bento-grid {{ grid-template-columns: 1fr; } }}
  </style>
</head>
<body>
"""

NAV = """
  <!-- S01 Nav -->
  <nav class="nav" id="mainNav">
    <div class="nav-container">
      <a href="/" class="nav-logo-area">
        <div class="nav-logo-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="white"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg></div>
        <div class="nav-logo-text">StepsAI</div>
      </a>
      <div class="nav-tabs">
        <a href="/product/ai-agents/" class="nav-tab">Product</a>
        <a href="/solutions/ecommerce/" class="nav-tab">Solutions</a>
        <a href="/pricing/" class="nav-tab">Pricing</a>
        <a href="/partners/" class="nav-tab">Partner</a>
      </div>
      <div class="nav-right">
        <a href="/login/" class="nav-login">Sign in</a>
        <a href="/partners/apply/"><button class="btn-primary">Start free trial</button></a>
      </div>
    </div>
  </nav>
"""

FOOTER = """
  <!-- S03 CTA Band -->
  <section class="cta-band">
    <h2>Somebody is typing right now.</h2>
    <div style="display:flex; justify-content:center; gap:16px;">
      <a href="/partners/apply/"><button class="btn-primary">Start free trial</button></a>
      <button class="btn-outline">Book a demo</button>
    </div>
  </section>
  <!-- S02 Footer -->
  <footer class="footer">
    <div class="footer-container">
      <div class="footer-col" style="grid-column: span 2;">
        <div style="font-weight: 800; font-size: 20px; margin-bottom:16px;">StepsAI</div>
        <p style="color:var(--text-secondary); font-size:14px; max-width: 250px;">Your AI agent layer for every business. Answer, capture, and close at any hour.</p>
      </div>
      <div class="footer-col">
        <h4>Product</h4>
        <ul><li><a href="/product/ai-agents/">AI Agents</a></li><li><a href="/pricing/">Pricing</a></li></ul>
      </div>
      <div class="footer-col">
        <h4>Solutions</h4>
        <ul><li><a href="/solutions/ecommerce/">E-Commerce</a></li><li><a href="/solutions/real-estate/">Real Estate</a></li></ul>
      </div>
      <div class="footer-col">
        <h4>Company</h4>
        <ul><li><a href="/about/">About</a></li><li><a href="/contact/">Contact</a></li></ul>
      </div>
    </div>
  </footer>
  <script>
    gsap.registerPlugin(ScrollTrigger);
    gsap.to(".gsap-fade-up", { y: 0, opacity: 1, duration: 1, stagger: 0.15, ease: "power3.out" });
    gsap.utils.toArray('.gsap-scale-in').forEach(element => {{
      gsap.to(element, {{
        scrollTrigger: { trigger: element, start: "top 85%", toggleActions: "play none none reverse" },
        scale: 1, opacity: 1, duration: 0.8, ease: "power3.out"
      }});
    }});
    window.addEventListener('scroll', () => {{
      const nav = document.getElementById('mainNav');
      if (window.scrollY > 20) nav.classList.add('scrolled');
      else nav.classList.remove('scrolled');
    }});
  </script>
</body>
</html>
"""

def render_s05(kicker, h1, sub):
    return f"""
  <section class="hero-v2">
    <div class="hero-bg-glow"></div>
    <span class="kicker gsap-fade-up" style="font-family: 'Geist Mono', monospace; font-size: 11px; font-weight: 500; color: var(--accent); letter-spacing: .24em; text-transform: uppercase; margin-bottom: 24px;">{kicker}</span>
    <h1 class="gsap-fade-up">{h1}</h1>
    <p class="gsap-fade-up">{sub}</p>
    <div class="hero-actions gsap-fade-up" style="display:flex; gap:16px;">
      <a href="/partners/apply/"><button class="btn-primary" style="padding: 14px 28px; font-size: 16px;">Start free trial</button></a>
      <button class="btn-outline" style="padding: 14px 28px; font-size: 16px;">Talk to us</button>
    </div>
  </section>
"""

def render_s17(qlist):
    if not qlist: return ""
    return f"""
  <section class="section-v2" style="background: var(--bg-surface-2);">
    <h2 class="section-title-v2 gsap-fade-up">The questions your customers ask every day</h2>
    <div class="bento-grid">
      """ + "".join([f'<div class="bento-card gsap-scale-in" style="justify-content: center; text-align: center;"><h3 style="font-size:24px; font-family:\'Outfit\';">"{q}"</h3></div>' for q in qlist]) + """
    </div>
  </section>
"""

def render_s12(workflow_name):
    if not workflow_name: return ""
    return f"""
  <section class="section-v2">
    <h2 class="section-title-v2 gsap-fade-up">Workflow: {workflow_name}</h2>
    <div class="bento-card gsap-fade-up" style="min-height: 400px; display:flex; align-items:center; justify-content:center;">
      <div style="text-align:center;">
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2" style="margin-bottom:16px;"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
        <h3 style="font-size: 24px; font-family: 'Outfit'; margin-bottom: 8px;">Automated {workflow_name} Pipeline</h3>
        <p style="color: var(--text-secondary);">The agent captures the intent, executes the logic, and updates your CRM automatically.</p>
        <div style="margin-top:24px; display:inline-block; font-family:'Geist Mono', monospace; font-size:12px; border:1px dashed var(--accent); padding:8px 16px; color:var(--accent); border-radius:4px;">[✓] BILLING · 1 WORKFLOW EXECUTED</div>
      </div>
    </div>
  </section>
"""

def render_s21(integrations):
    if not integrations: return ""
    cards = "".join([f'<div class="bento-card gsap-scale-in" style="padding: 24px;"><h4 style="font-size: 20px; font-weight:600; font-family:Outfit;">{i}</h4><p style="color:var(--text-secondary); margin-top:8px;">Native Sync</p></div>' for i in integrations])
    return f"""
  <section class="section-v2" style="background: var(--bg-surface-2);">
    <h2 class="section-title-v2 gsap-fade-up">Connects directly to your stack</h2>
    <div class="bento-grid" style="grid-template-columns: repeat(4, 1fr);">
      {cards}
    </div>
  </section>
"""

# --- ALL 34 PAGES DATA ---

pages = [
    # Tier 1 (Core)
    {"route": "product/ai-agents", "title": "AI Agents", "kicker": "PRODUCT", "h1": "One brain, four jobs.", "sub": "StepsAI gives you a Sales Agent, Support Agent, Lead Agent, and Meetings Agent all working from the same memory.", "s17": [], "workflow": "Lead Handoff", "integrations": []},
    {"route": "product/copilot", "title": "Internal Copilot", "kicker": "INTERNAL", "h1": "Your team's AI brain.", "sub": "The same knowledge base that powers your customer-facing agents also answers internal questions for HR, Sales, and Support.", "s17": [], "workflow": "Internal Query", "integrations": []},
    
    # Tier 2 (Solutions)
    {"route": "solutions/ecommerce", "title": "E-Commerce", "kicker": "E-COMMERCE SOLUTION", "h1": "Turn night-time window shoppers into orders.", "sub": "Deploy an agent that answers product questions and recovers abandoned carts at 2 AM.", "s17": ["Do you have this in medium?", "Where's my order?", "Can I return this?", "Does it ship to my city?"], "workflow": "Recover Carts", "integrations": ["Shopify", "WooCommerce", "Shiprocket", "Razorpay"]},
    {"route": "solutions/saas", "title": "SaaS", "kicker": "SAAS SOLUTION", "h1": "Turn signups into activated power users.", "sub": "Deploy an agent that guides users through setup and identifies upsell opportunities instantly.", "s17": ["Does it integrate with X?", "What's in the free plan?", "How do I set this up?", "Can I talk to sales?"], "workflow": "Trial Follow-Up", "integrations": ["HubSpot", "Slack", "Zendesk", "Stripe"]},
    {"route": "solutions/healthcare", "title": "Healthcare", "kicker": "HEALTHCARE SOLUTION", "h1": "Never leave a patient waiting for an answer.", "sub": "Deploy a HIPAA-compliant agent to handle scheduling and insurance queries 24/7.", "s17": ["Is the doctor available today?", "How much is a consultation?", "Do you take my insurance?", "Where are you located?"], "workflow": "Appointment Reminders", "integrations": ["Google Calendar", "Practo", "Clinic PMS", "Stripe"]},
    {"route": "solutions/education", "title": "Education", "kicker": "EDUCATION SOLUTION", "h1": "Answer every admissions query instantly.", "sub": "Automate the front desk so counsellors only speak to high-intent leads ready to commit.", "s17": ["What's the fee structure?", "When does the next batch start?", "Is there a placement guarantee?", "Can I talk to a counsellor?"], "workflow": "Enquiry Follow-Up", "integrations": ["Zoho CRM", "Calendar", "Payments", "WhatsApp"]},
    {"route": "solutions/real-estate", "title": "Real Estate", "kicker": "REAL ESTATE SOLUTION", "h1": "Book site visits while you sleep.", "sub": "Stop losing leads on Friday night. The agent qualifies buyers and sets up weekend visits.", "s17": ["Is this property still available?", "What's the price?", "Can I visit this weekend?", "What's the carpet area?"], "workflow": "Site Visit Follow-up", "integrations": ["HubSpot", "Zoho CRM", "Calendar", "WhatsApp"]},
    
    # Tier 3 (Roles)
    {"route": "use-cases/marketing-growth", "title": "Marketing", "kicker": "MARKETING & GROWTH", "h1": "Stop letting paid traffic bounce.", "sub": "Engage them instantly and capture the lead before they leave.", "s17": ["Which campaigns actually start conversations?", "Are we losing leads after hours?", "Can we follow up automatically?", "Where do enquiries come from?"], "workflow": "Re-engage", "integrations": ["Facebook Ads", "Google Ads", "HubSpot", "Zapier"]},
    {"route": "use-cases/sales", "title": "Sales", "kicker": "SALES TEAMS", "h1": "Your SDR that never sleeps.", "sub": "The agent qualifies prospects and books meetings directly onto your calendar.", "s17": ["Which leads are worth calling?", "How fast do we respond?", "Are meetings getting booked?", "Is anything slipping?"], "workflow": "Follow up leads", "integrations": ["Salesforce", "HubSpot", "Calendly", "Chili Piper"]},
    {"route": "use-cases/support-cx", "title": "Support", "kicker": "SUPPORT TEAMS", "h1": "Deflect the noise. Focus on the complex.", "sub": "Let AI handle repetitive tickets so humans handle high-value problems.", "s17": ["How many tickets repeat?", "What's our response time?", "When should a human step in?", "What can't it answer?"], "workflow": "Remind customers", "integrations": ["Zendesk", "Intercom", "Gorgias", "Freshdesk"]},
    {"route": "use-cases/operations", "title": "Operations", "kicker": "OPERATIONS", "h1": "Connect the tools that don't talk.", "sub": "The agent bridges the gap between your inventory and messaging channels automatically.", "s17": ["What's still manual?", "Where do handoffs break?", "Can we cut repeat work?", "Who owns what?"], "workflow": "Recover carts", "integrations": ["Notion", "Airtable", "Make", "Zapier"]},
    
    # Tier 4 (Channels)
    {"route": "channels/website", "title": "Website Agent", "kicker": "WEBSITE CHANNEL", "h1": "Turn your website into a two-way conversation.", "sub": "Capture intent, answer questions, and book meetings directly from the bottom right corner.", "s17": ["Where is the pricing?", "Does this integrate with X?", "Can I talk to a human?", "Do you offer enterprise plans?"], "workflow": "Capture Leads", "integrations": ["WordPress", "Webflow", "Shopify", "React"]},
    {"route": "channels/whatsapp", "title": "WhatsApp Agent", "kicker": "WHATSAPP CHANNEL", "h1": "Sell where they already spend their time.", "sub": "Deploy an agent to handle inbound queries and close sales directly in WhatsApp.", "s17": ["Is this available?", "Send me a picture.", "How much?", "Can you deliver today?"], "workflow": "Order Tracking", "integrations": ["WhatsApp API", "Meta Business", "Shopify", "CRM"]},
    {"route": "channels/instagram", "title": "Instagram Agent", "kicker": "INSTAGRAM CHANNEL", "h1": "From comment to DM to closed deal instantly.", "sub": "The agent replies to comments and instantly drops a purchase link in their DMs.", "s17": ["Price?", "Link?", "Available in blue?", "How to order?"], "workflow": "Comment-to-DM", "integrations": ["Instagram API", "Meta Business", "Shopify", "Stripe"]},
    {"route": "channels/standalone-page", "title": "Standalone Page", "kicker": "STANDALONE CHANNEL", "h1": "Your AI agent on its own dedicated URL.", "sub": "No website needed. Just share the link and start capturing leads instantly.", "s17": [], "workflow": "Share Link", "integrations": []},
    {"route": "channels", "title": "All Channels", "kicker": "CHANNELS", "h1": "One brain. Every channel.", "sub": "Connect StepsAI to WhatsApp, Instagram, and your website simultaneously.", "s17": [], "workflow": "Omnichannel Sync", "integrations": []},
    
    # Tier 5 (Features)
    {"route": "features/sales-agent", "title": "Sales Agent", "kicker": "SALES AGENT", "h1": "The closer that never clocks out.", "sub": "It handles objection handling, quotes pricing, and pushes the prospect down the funnel.", "s17": ["Is this a bot?", "Can I get a discount?", "How does this compare?", "Send me the invoice."], "workflow": "Generate Quotes", "integrations": ["Stripe", "Razorpay", "Salesforce", "HubSpot"]},
    {"route": "features/lead-agent", "title": "Lead Agent", "kicker": "LEAD AGENT", "h1": "Never let a prospect go cold.", "sub": "Instantly qualify inbound leads and route the highest value ones to your human team.", "s17": [], "workflow": "Qualify Leads", "integrations": ["HubSpot", "Salesforce"]},
    {"route": "features/meetings-agent", "title": "Meetings Agent", "kicker": "MEETINGS AGENT", "h1": "Automate your calendar.", "sub": "The agent finds the right time slot and books the meeting without the back-and-forth emails.", "s17": [], "workflow": "Book Meetings", "integrations": ["Google Calendar", "Outlook", "Calendly"]},
    {"route": "features/support-agent", "title": "Support Agent", "kicker": "SUPPORT AGENT", "h1": "Zero-minute resolution times.", "sub": "It reads your knowledge base and resolves 70% of L1 tickets instantly.", "s17": ["I forgot my password", "Cancel my subscription", "How to integrate API?", "Where is my refund?"], "workflow": "Ticket Deflection", "integrations": ["Zendesk", "Intercom", "Freshdesk", "Jira"]},
    {"route": "features/workflows", "title": "Workflows", "kicker": "WORKFLOWS", "h1": "Logic that acts on conversation.", "sub": "Design custom workflows that trigger based on what the user says.", "s17": [], "workflow": "Visual Builder", "integrations": []},
    {"route": "features/inbox", "title": "One Inbox", "kicker": "ONE INBOX", "h1": "See everything in one place.", "sub": "Manage all AI and human conversations across all channels in a single view.", "s17": [], "workflow": "Human Handoff", "integrations": []},
    {"route": "features/analytics", "title": "Analytics", "kicker": "ANALYTICS", "h1": "Know exactly what they're asking.", "sub": "Understand your customers better with deep conversational analytics and topic extraction.", "s17": [], "workflow": "Insight Generation", "integrations": []},
    {"route": "features", "title": "All Features", "kicker": "PLATFORM", "h1": "The complete AI agent platform.", "sub": "Everything you need to build, deploy, and manage conversational AI.", "s17": [], "workflow": "", "integrations": []},
    {"route": "integrations", "title": "Integrations", "kicker": "INTEGRATIONS", "h1": "Plays nice with your stack.", "sub": "Connect StepsAI to your existing CRM, Helpdesk, and internal tools in one click.", "s17": [], "workflow": "", "integrations": ["Salesforce", "Zendesk", "HubSpot", "Slack", "Shopify", "Notion", "Make", "Zapier"]},
    
    # Tier 7 (Company / Resources)
    {"route": "about", "title": "About Us", "kicker": "ABOUT", "h1": "We're building the AI agent layer for every business.", "sub": "Every business needs to talk to its customers at all hours. Almost none of them can afford to hire for it.", "s17": [], "workflow": "", "integrations": []},
    {"route": "note", "title": "Founder's Note", "kicker": "NOTE", "h1": "Why we started this.", "sub": "A letter from the founder on why conversational AI needs to actually take action, not just talk.", "s17": [], "workflow": "", "integrations": []},
    {"route": "team", "title": "Team", "kicker": "TEAM", "h1": "Meet the team.", "sub": "A small group of engineers and designers building the future of business communication.", "s17": [], "workflow": "", "integrations": []},
    {"route": "careers", "title": "Careers", "kicker": "CAREERS", "h1": "Join us.", "sub": "We're hiring talented builders who want to democratize AI agents for every business.", "s17": [], "workflow": "", "integrations": []},
    {"route": "contact", "title": "Contact Us", "kicker": "CONTACT", "h1": "Get in touch.", "sub": "Have a specific use case? Our team is ready to help you map it out.", "s17": [], "workflow": "", "integrations": []},
    {"route": "blog", "title": "Blog", "kicker": "BLOG", "h1": "The StepsAI Blog.", "sub": "Insights, product updates, and thoughts on the future of AI agents.", "s17": [], "workflow": "", "integrations": []},
    {"route": "resources/ai-guides", "title": "AI Guides", "kicker": "GUIDES", "h1": "Learn how to build better agents.", "sub": "In-depth tutorials and strategies for conversational design and workflow automation.", "s17": [], "workflow": "", "integrations": []},
    {"route": "resources/case-studies", "title": "Case Studies", "kicker": "CASE STUDIES", "h1": "See how others are growing.", "sub": "Read how E-commerce stores and SaaS platforms are driving revenue with StepsAI.", "s17": [], "workflow": "", "integrations": []},
    
    # Tier 8 (Legal)
    {"route": "privacy-policy", "title": "Privacy Policy", "kicker": "LEGAL", "h1": "Privacy Policy.", "sub": "How we handle your data.", "s17": [], "workflow": "", "integrations": []},
    {"route": "terms-of-service", "title": "Terms of Service", "kicker": "LEGAL", "h1": "Terms of Service.", "sub": "The rules of using our platform.", "s17": [], "workflow": "", "integrations": []}
]

# --- GENERATE ---
for page in pages:
    dir_path = os.path.join(page["route"])
    os.makedirs(dir_path, exist_ok=True)
    html = GLOBAL_HEAD.format(title=page["title"]) + NAV + render_s05(page["kicker"], page["h1"], page["sub"]) + render_s17(page["s17"]) + render_s12(page["workflow"]) + render_s21(page["integrations"]) + FOOTER
    with open(os.path.join(dir_path, "index.html"), "w", encoding="utf-8") as f: f.write(html)
    print(f"Built /{page['route']}/")

print(f"Successfully generated {len(pages)} V2 GSAP pages!")
