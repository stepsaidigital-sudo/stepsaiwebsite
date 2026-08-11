import re

file_path = "c:\\Users\\user\\Downloads\\HOME STAEP AI\\StepsAI_Redesign.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_hero_css = """
    /* --- PIXEL PERFECT HERO & NAV CSS --- */
    body { background-color: #FAFAFA; color: #1F2937; overflow-x: hidden; font-family: 'Inter', sans-serif; }
    h1, h2, h3 { font-family: 'Outfit', sans-serif; }
    
    .nav { position: fixed; top: 0; left: 0; width: 100%; z-index: 1000; background: rgba(255,255,255,0.9); backdrop-filter: blur(10px); border-bottom: 1px solid rgba(0,0,0,0.05); }
    .nav-container { max-width: 1300px; margin: 0 auto; padding: 16px 32px; display: flex; align-items: center; justify-content: space-between; }
    .nav-logo-area { display: flex; align-items: center; gap: 10px; }
    .nav-logo-icon { width: 30px; height: 30px; background: #6366f1; border-radius: 8px; color: white; display: flex; align-items: center; justify-content: center; }
    .nav-logo-text { color: #0F172A; font-weight: 800; font-size: 20px; letter-spacing: -0.5px; }
    .nav-tabs { display: flex; gap: 28px; }
    .nav-tab { color: #334155; font-size: 14px; font-weight: 600; cursor: pointer; transition: color 0.2s; display: flex; align-items: center; gap: 4px; }
    .nav-tab:hover { color: #0F172A; }
    .nav-right { display: flex; align-items: center; gap: 20px; }
    .nav-login { color: #334155; font-size: 14px; font-weight: 600; text-decoration: none; }
    .btn-outline { border: 1px solid #E2E8F0; background: white; color: #0F172A; padding: 8px 16px; border-radius: 8px; font-size: 14px; font-weight: 600; cursor: pointer; }
    .btn-primary { background: #6366f1; color: white; padding: 10px 20px; border-radius: 8px; font-size: 14px; font-weight: 600; border: none; cursor: pointer; box-shadow: 0 4px 12px rgba(99,102,241,0.25); }

    .pixel-hero { position: relative; width: 100%; padding: 160px 0 100px; background: radial-gradient(circle at 50% 0%, #ffffff 0%, #FAFAFA 100%); overflow: hidden; display: flex; flex-direction: column; align-items: center; text-align: center; }
    
    .hero-badge { display: inline-flex; align-items: center; gap: 6px; padding: 6px 16px; border-radius: 100px; color: #6366F1; font-size: 11px; font-weight: 700; letter-spacing: 0.5px; margin-bottom: 24px; background: #EEF2FF; border: 1px solid #E0E7FF; text-transform: uppercase; }
    .hero-title { font-size: 64px; font-weight: 900; color: #0F172A; line-height: 1.1; margin-bottom: 8px; letter-spacing: -2px; }
    .hero-highlight { background: linear-gradient(135deg, #6366F1, #A855F7); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .hero-subtitle { font-size: 16px; color: #64748B; max-width: 600px; line-height: 1.6; margin: 20px auto 40px; font-weight: 400; }

    .hero-visuals { position: relative; width: 100%; max-width: 1300px; height: 600px; display: flex; justify-content: center; align-items: flex-end; margin: 0 auto; }
    
    .central-glow { position: absolute; top: 10%; left: 50%; transform: translateX(-50%); width: 700px; height: 700px; background: radial-gradient(circle, rgba(99,102,241,0.08) 0%, rgba(255,255,255,0) 70%); z-index: 5; pointer-events: none; }
    .central-character { position: relative; z-index: 20; height: 100%; max-height: 580px; object-fit: contain; filter: drop-shadow(0 20px 40px rgba(0,0,0,0.1)); }

    /* SVG Connections */
    .connections { position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none; z-index: 10; }
    .conn-line { fill: none; stroke: #CBD5E1; stroke-width: 2; stroke-dasharray: 6 6; }
    .conn-dot { fill: #6366F1; }

    /* Floating Cards Shared */
    .floating-card { position: absolute; background: white; border-radius: 16px; box-shadow: 0 20px 40px -10px rgba(0,0,0,0.1); padding: 20px; z-index: 30; border: 1px solid rgba(0,0,0,0.03); }
    
    /* Top Left: 2.4X */
    .card-tl { top: 10%; left: 50px; display: flex; align-items: center; gap: 16px; width: 300px; padding: 20px 24px; border-radius: 20px; }
    .card-tl .icon { width: 48px; height: 48px; background: #EEF2FF; border-radius: 12px; display: flex; align-items: center; justify-content: center; color: #6366F1; font-size: 20px; }
    .card-tl .text h3 { font-size: 28px; font-weight: 800; color: #0F172A; margin: 0 0 4px 0; text-align: left; }
    .card-tl .text p { font-size: 11px; color: #64748B; line-height: 1.4; margin: 0; text-align: left; }
    .card-tl .graph { width: 60px; height: 30px; margin-left: auto; }

    /* Bottom Left: WhatsApp */
    .card-bl { bottom: 15%; left: 0px; width: 340px; padding: 16px; border-radius: 24px; background: white; display: flex; flex-direction: column; gap: 10px; }
    .wa-float-icon { position: absolute; top: -15px; left: -15px; width: 44px; height: 44px; background: #25D366; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 8px 16px rgba(37,211,102,0.3); z-index: 31; }
    .wa-bubble { padding: 10px 14px; border-radius: 12px; font-size: 12px; line-height: 1.4; width: 100%; text-align: left; position: relative; border-bottom-left-radius: 4px; }
    .wa-bubble.green { background: #D9FDD3; color: #111827; }
    .wa-bubble.white { background: white; border: 1px solid #F1F5F9; color: #111827; }
    .wa-time { font-size: 9px; color: #94A3B8; text-align: right; display: block; margin-top: 4px; }

    /* Top Right: 35% */
    .card-tr { top: 10%; right: 50px; display: flex; align-items: center; gap: 16px; width: 280px; padding: 20px 24px; border-radius: 20px; }
    .card-tr .icon { width: 48px; height: 48px; background: #ECFDF5; border-radius: 12px; display: flex; align-items: center; justify-content: center; color: #10B981; font-size: 20px; }
    .card-tr .text h3 { font-size: 28px; font-weight: 800; color: #0F172A; margin: 0 0 4px 0; text-align: left; }
    .card-tr .text p { font-size: 11px; color: #64748B; line-height: 1.4; margin: 0; text-align: left; }
    .card-tr .graph { width: 60px; height: 30px; margin-left: auto; }

    /* Middle Right: Assistant Widget */
    .card-mr { bottom: 25%; right: 280px; width: 340px; padding: 0; overflow: hidden; border-radius: 20px; }
    .aw-head { padding: 16px 20px; border-bottom: 1px solid #F1F5F9; display: flex; justify-content: space-between; align-items: center; background: white; }
    .aw-logo { display: flex; align-items: center; gap: 10px; font-weight: 700; font-size: 14px; color: #0F172A; }
    .aw-icon { width: 28px; height: 28px; background: #6366f1; border-radius: 8px; display: flex; align-items: center; justify-content: center; }
    .aw-status { display: flex; align-items: center; gap: 4px; font-size: 10px; color: #10B981; font-weight: 600; margin-top: 2px; }
    .aw-status .dot { width: 6px; height: 6px; background: #10B981; border-radius: 50%; }
    .aw-body { padding: 20px; background: white; display: flex; flex-direction: column; gap: 16px; text-align: left; }
    .aw-bubble { background: #F8FAFC; padding: 12px 16px; border-radius: 12px; border-bottom-left-radius: 4px; font-size: 12px; color: #1F2937; line-height: 1.5; border: 1px solid #F1F5F9; }
    .aw-bot-msg { display: flex; gap: 12px; }
    .aw-bot-icon { width: 24px; height: 24px; background: #6366f1; border-radius: 50%; flex-shrink: 0; display: flex; align-items: center; justify-content: center; }
    .aw-bot-bubble { background: white; padding: 12px 16px; border-radius: 12px; border-bottom-left-radius: 4px; font-size: 12px; color: #1F2937; line-height: 1.5; border: 1px solid #F1F5F9; box-shadow: 0 2px 8px rgba(0,0,0,0.02); }
    .aw-list { margin: 10px 0; padding: 0; list-style: none; }
    .aw-list li { display: flex; align-items: center; gap: 8px; font-size: 12px; color: #374151; margin-bottom: 6px; }
    .aw-list li::before { content: '✓'; color: #3B82F6; font-weight: bold; }
    .aw-btn { width: 100%; background: white; border: 1px solid #E2E8F0; color: #6366f1; padding: 10px; border-radius: 8px; font-size: 12px; font-weight: 600; text-align: center; cursor: pointer; margin-top: 8px; }

    /* Bottom Right: Carousel */
    .card-br { bottom: 10%; right: -20px; width: 440px; padding: 20px; border-radius: 20px; text-align: left; }
    .ig-float-icon { position: absolute; top: -15px; right: -15px; width: 40px; height: 40px; background: radial-gradient(circle at 30% 107%, #fdf497 0%, #fdf497 5%, #fd5949 45%,#d6249f 60%,#285AEB 90%); border-radius: 12px; display: flex; align-items: center; justify-content: center; box-shadow: 0 8px 16px rgba(214,36,159,0.3); z-index: 31; }
    .ig-float-icon-sm { position: absolute; top: 15%; right: 400px; width: 32px; height: 32px; background: radial-gradient(circle at 30% 107%, #fdf497 0%, #fdf497 5%, #fd5949 45%,#d6249f 60%,#285AEB 90%); border-radius: 10px; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 10px rgba(214,36,159,0.2); z-index: 10; }
    .caro-header { font-size: 13px; font-weight: 700; color: #0F172A; margin-bottom: 16px; }
    .caro-items { display: flex; gap: 12px; }
    .c-item { flex: 1; background: white; border: 1px solid #F1F5F9; border-radius: 12px; overflow: hidden; }
    .c-img { height: 100px; background: #E2E8F0; }
    .c-img img { width: 100%; height: 100%; object-fit: cover; }
    .c-info { padding: 12px; }
    .c-info h5 { font-size: 11px; font-weight: 700; margin: 0 0 6px 0; line-height: 1.3; height: 28px; }
    .c-info .rating { font-size: 10px; color: #F59E0B; font-weight: 600; margin-bottom: 6px; }
    .c-info .price { font-size: 12px; font-weight: 800; color: #0F172A; }
    .caro-arrow { position: absolute; right: -15px; top: 50%; transform: translateY(-50%); width: 30px; height: 30px; background: white; border-radius: 50%; box-shadow: 0 4px 10px rgba(0,0,0,0.1); display: flex; align-items: center; justify-content: center; font-weight: bold; color: #64748B; cursor: pointer; }

    /* Trust Elements */
    .hero-trust-strip { background: rgba(255,255,255,0.8); backdrop-filter: blur(10px); padding: 16px 40px; border-radius: 100px; display: inline-flex; align-items: center; justify-content: center; gap: 40px; margin-top: -30px; position: relative; z-index: 40; border: 1px solid rgba(0,0,0,0.05); box-shadow: 0 4px 20px rgba(0,0,0,0.03); }
    .ht-item { display: flex; align-items: center; gap: 8px; font-size: 13px; font-weight: 600; color: #4B5563; }
    .ht-icon { color: #6366f1; font-size: 16px; }

    .hero-logos-strip { background: white; padding: 24px 48px; border-radius: 20px; display: flex; align-items: center; gap: 50px; margin-top: 40px; box-shadow: 0 10px 40px rgba(0,0,0,0.04); max-width: 1200px; width: 100%; position: relative; z-index: 40; }
    .hl-title { font-size: 13px; font-weight: 600; color: #4B5563; max-width: 150px; text-align: left; line-height: 1.5; }
    .hl-img { display: flex; align-items: center; justify-content: space-between; flex: 1; }
    .hl-img img { height: 30px; filter: grayscale(100%) opacity(0.7); mix-blend-mode: multiply; }
"""

new_hero_html = """
  <!-- NAVIGATION -->
  <nav class="nav">
    <div class="nav-container">
      <div class="nav-logo-area">
        <div class="nav-logo-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="white"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg></div>
        <div class="nav-logo-text">StepsAI</div>
      </div>
      <div class="nav-tabs">
        <div class="nav-tab">Product <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg></div>
        <div class="nav-tab">Solutions <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg></div>
        <div class="nav-tab">Integrations</div>
        <div class="nav-tab">Resources <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg></div>
        <div class="nav-tab">Pricing</div>
      </div>
      <div class="nav-right">
        <a href="#" class="nav-login">Log in</a>
        <button class="btn-outline">Book a Demo</button>
        <button class="btn-primary">Start Free Trial →</button>
      </div>
    </div>
  </nav>

  <!-- HERO SECTION -->
  <section class="pixel-hero">
    
    <div class="hero-badge">
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l2.4 7.6L22 12l-7.6 2.4L12 22l-2.4-7.6L2 12l7.6-2.4L12 2z"/></svg>
      AI AGENT PLATFORM FOR MODERN BUSINESSES
    </div>
    
    <h1 class="hero-title">
      One AI agent. Every channel.<br>
      <span class="hero-highlight">Real business outcomes.</span>
    </h1>
    
    <p class="hero-subtitle">
      StepsAI answers questions, recommends, captures leads, books appointments<br>
      and automates work across your website, WhatsApp, Instagram and more.
    </p>

    <div class="hero-visuals">
      <div class="central-glow"></div>
      
      <!-- Connecting Lines -->
      <svg class="connections" viewBox="0 0 1300 600">
          <!-- Left Top (2.4X) -->
          <path class="conn-line" d="M 650 300 Q 400 200 350 200" />
          <circle class="conn-dot" r="4" cx="350" cy="200" />
          
          <!-- Left Bottom (WA) -->
          <path class="conn-line" d="M 600 450 Q 300 450 340 380" />
          <circle class="conn-dot" r="4" cx="340" cy="380" />
          
          <!-- Right Top (35%) -->
          <path class="conn-line" d="M 650 300 Q 900 200 950 200" />
          <circle class="conn-dot" r="4" cx="950" cy="200" />
      </svg>

      <!-- Central Character -->
      <img src="WOMEN.png" alt="Professional User" class="central-character">

      <!-- Top Left: Leads Stat -->
      <div class="floating-card card-tl">
          <div class="icon">👥</div>
          <div class="text">
              <h3>2.4X</h3>
              <p>More qualified leads<br>with AI conversations</p>
          </div>
          <div class="graph">
              <svg viewBox="0 0 60 30" fill="none" stroke="#22c55e" stroke-width="2"><polyline points="0,30 15,20 30,25 45,10 60,5"></polyline><circle cx="60" cy="5" r="3" fill="#22c55e"></circle></svg>
          </div>
      </div>

      <!-- Bottom Left: WA Chat -->
      <div class="floating-card card-bl">
          <div class="wa-float-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="white"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/></svg>
          </div>
          <div class="wa-bubble green">
              Hi, I need to book a consultation for skin acne.
              <span class="wa-time">10:30 AM <span style="color:#3b82f6">✓✓</span></span>
          </div>
          <div class="wa-bubble white">
              Sure! Our dermatologist Dr. Neha Sharma is available tomorrow at 4:30 PM.
              <span class="wa-time">10:30 AM <span style="color:#3b82f6">✓✓</span></span>
          </div>
          <div class="wa-bubble green">
              That works for me.
              <span class="wa-time">10:31 AM <span style="color:#3b82f6">✓✓</span></span>
          </div>
          <div class="wa-bubble white">
              Great! Your appointment is confirmed for tomorrow at 4:30 PM. See you then! 😊
              <span class="wa-time">10:31 AM</span>
          </div>
      </div>

      <!-- Floating Instagram Icon (Left side) -->
      <div class="ig-float-icon-sm">
         <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
      </div>

      <!-- Top Right: Conversion Stat -->
      <div class="floating-card card-tr">
          <div class="icon">📊</div>
          <div class="text">
              <h3>35%</h3>
              <p>Increase in conversion<br>from conversations</p>
          </div>
          <div class="graph">
              <svg viewBox="0 0 60 30" fill="none" stroke="#22c55e" stroke-width="2"><polyline points="0,25 15,30 30,15 45,20 60,5"></polyline><circle cx="60" cy="5" r="3" fill="#22c55e"></circle></svg>
          </div>
      </div>

      <!-- Middle Right: Assistant Widget -->
      <div class="floating-card card-mr">
          <div class="aw-head">
              <div class="aw-logo">
                  <div class="aw-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="white"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg></div>
                  <div>
                      StepsAI Assistant
                      <div class="aw-status"><span class="dot"></span> Online</div>
                  </div>
              </div>
              <span style="color:#94A3B8; font-weight:bold; font-size: 16px; cursor:pointer;">×</span>
          </div>
          <div class="aw-body">
              <div class="aw-bubble" style="margin-left: 36px; border-bottom-left-radius: 12px; border-bottom-right-radius: 4px;">
                  What are the available treatment options for acne?
                  <span class="wa-time">10:30 AM <span style="color:#3b82f6">✓✓</span></span>
              </div>
              <div class="aw-bot-msg">
                  <div class="aw-bot-icon"><svg width="12" height="12" viewBox="0 0 24 24" fill="white"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg></div>
                  <div class="aw-bot-bubble">
                      Based on your concern, here are the most effective acne treatments we offer.
                      <ul class="aw-list">
                          <li>Chemical Peels</li>
                          <li>HydraFacial</li>
                          <li>Laser Therapy</li>
                      </ul>
                      <button class="aw-btn">View Treatments</button>
                  </div>
              </div>
          </div>
      </div>

      <!-- Far Right: Product Carousel -->
      <div class="floating-card card-br">
          <div class="ig-float-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
          </div>
          <div class="caro-header">Recommended for you</div>
          <div class="caro-items">
              <div class="c-item">
                  <div class="c-img"><img src="https://images.unsplash.com/photo-1616394584738-fc6e612e71b9?w=200&h=160&fit=crop"></div>
                  <div class="c-info">
                      <h5>Deep Cleansing HydraFacial</h5>
                      <div class="rating">★ 4.8 <span style="color:#94a3b8;font-weight:400">(128)</span></div>
                      <div class="price">₹3,999</div>
                  </div>
              </div>
              <div class="c-item">
                  <div class="c-img"><img src="https://images.unsplash.com/photo-1570172619644-defd82136d8b?w=200&h=160&fit=crop"></div>
                  <div class="c-info">
                      <h5>Laser Hair Reduction</h5>
                      <div class="rating">★ 4.9 <span style="color:#94a3b8;font-weight:400">(96)</span></div>
                      <div class="price">₹6,499</div>
                  </div>
              </div>
              <div class="c-item">
                  <div class="c-img"><img src="https://images.unsplash.com/photo-1556228578-0d85b1a4d571?w=200&h=160&fit=crop"></div>
                  <div class="c-info">
                      <h5>Anti-Acne Treatment</h5>
                      <div class="rating">★ 4.7 <span style="color:#94a3b8;font-weight:400">(72)</span></div>
                      <div class="price">₹2,999</div>
                  </div>
              </div>
          </div>
          <div class="caro-arrow">›</div>
      </div>
    </div>
    
    <!-- Trust Strip -->
    <div class="hero-trust-strip">
      <div class="ht-item"><span class="ht-icon">✉</span> No credit card</div>
      <div class="ht-item"><span class="ht-icon">⏱</span> Setup in minutes</div>
      <div class="ht-item"><span class="ht-icon">✖</span> Cancel anytime</div>
      <div class="ht-item"><span class="ht-icon">⚙</span> Works on every channel</div>
    </div>
    
    <!-- Logos Section -->
    <div class="hero-logos-strip">
      <div class="hl-title">Trusted by 500+ businesses across healthcare and more</div>
      <div class="hl-img">
          <span style="color:#0284C7; font-weight:800; font-size:22px;">Apollo <span style="font-size:12px; display:block; margin-top:-6px;">HOSPITALS</span></span>
          <span style="color:#0369A1; font-weight:800; font-size:20px;">MAX <span style="font-weight:400;">Healthcare</span></span>
          <span style="color:#C026D3; font-weight:800; font-size:20px;">cloudnine</span>
          <span style="color:#0284C7; font-weight:800; font-size:18px;">manipalhospitals</span>
          <span style="color:#EAB308; font-weight:800; font-size:18px;">Pristyn Care</span>
          <span style="color:#94A3B8; font-weight:600;">& more</span>
      </div>
    </div>

  </section>
"""

# Regex replacement

# 1. Replace CSS
css_pattern = re.compile(r'/\* --- HEALTHCARE HERO & NAV CSS --- \*/.*?/\* --- RECONSTRUCTED CSS FOR REMAINING SECTIONS --- \*/', re.DOTALL)
if css_pattern.search(content):
    content = css_pattern.sub(new_hero_css + '\\n    /* --- RECONSTRUCTED CSS FOR REMAINING SECTIONS --- */', content)
else:
    # Fallback if the previous pattern failed
    # Replace from start of style to RECONSTRUCTED
    alt_css_pattern = re.compile(r'<style>.*?/\* --- RECONSTRUCTED CSS FOR REMAINING SECTIONS --- \*/', re.DOTALL)
    content = alt_css_pattern.sub('<style>\\n' + new_hero_css + '\\n    /* --- RECONSTRUCTED CSS FOR REMAINING SECTIONS --- */', content)

# 2. Replace HTML
html_pattern = re.compile(r'<!-- NAVIGATION -->.*?<!-- CREDIBILITY STRIP -->', re.DOTALL)
if html_pattern.search(content):
    content = html_pattern.sub(new_hero_html + '\\n  <!-- CREDIBILITY STRIP -->', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Pixel-perfect update applied successfully.")
