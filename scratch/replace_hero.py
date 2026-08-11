import re

file_path = "c:\\Users\\user\\Downloads\\HOME STAEP AI\\StepsAI_Redesign.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# CSS replacement
new_css = """
    /* --- NEW DARK HERO & NAV CSS --- */
    .nav { position: fixed; top: 0; left: 0; width: 100%; z-index: 100; background: #111827; border-bottom: 1px solid rgba(255,255,255,0.05); }
    .nav-container { max-width: 1400px; margin: 0 auto; padding: 12px 32px; display: flex; align-items: center; justify-content: space-between; }
    .nav-logo-area { display: flex; align-items: center; gap: 12px; }
    .nav-logo-icon { width: 36px; height: 36px; background: white; border-radius: 50%; color: #111827; font-weight: 800; font-size: 20px; display: flex; align-items: center; justify-content: center; }
    .nav-logo-text { color: white; font-weight: 800; font-size: 14px; line-height: 1.2; letter-spacing: 0.5px; }
    .nav-logo-text span { font-size: 11px; font-weight: 400; color: #9CA3AF; letter-spacing: 0; }
    .nav-tabs { display: flex; gap: 8px; background: rgba(255,255,255,0.05); padding: 4px; border-radius: 12px; }
    .nav-tab { color: #D1D5DB; font-size: 13px; font-weight: 500; padding: 8px 16px; border-radius: 8px; cursor: pointer; transition: all 0.2s; display: flex; align-items: center; gap: 6px; }
    .nav-tab:hover { background: rgba(255,255,255,0.1); color: white; }
    .nav-tab.active { background: #3B82F6; color: white; }
    .nav-right { display: flex; align-items: center; }
    .nav-select { background: rgba(255,255,255,0.1); color: white; border: none; padding: 6px 12px; border-radius: 6px; font-size: 12px; }

    .dark-hero { position: relative; width: 100vw; min-height: 100vh; background: #1A1A1A; display: flex; align-items: center; justify-content: center; padding: 120px 5% 60px; overflow: hidden; }
    .hero-bg { position: absolute; inset: 0; background-image: url('assets/hero_section_1785614950866.png'); background-size: cover; background-position: center; opacity: 0.4; filter: blur(5px); z-index: 1; }
    .hero-layout { position: relative; z-index: 10; max-width: 1400px; width: 100%; display: grid; grid-template-columns: 1fr 420px; gap: 60px; align-items: center; margin: 0 auto; }
    
    .hero-badge { display: inline-block; padding: 6px 16px; border: 1px solid rgba(255,255,255,0.2); border-radius: 20px; color: white; font-size: 11px; font-weight: 700; letter-spacing: 1.5px; margin-bottom: 24px; background: rgba(0,0,0,0.3); backdrop-filter: blur(4px); }
    .hero-title { font-size: 4.5rem; font-weight: 800; color: white; line-height: 1.1; margin-bottom: 24px; letter-spacing: -1px; }
    .hero-highlight { background: linear-gradient(135deg, #60A5FA, #2563EB); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .hero-subtitle { font-size: 1.25rem; color: #D1D5DB; max-width: 500px; line-height: 1.6; }

    .widget-mockup { background: white; border-radius: 24px; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5); overflow: hidden; display: flex; flex-direction: column; height: 650px; animation: slideUpReal 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards; opacity: 0; transform: translateY(40px); }
    @keyframes slideUpReal { to { opacity: 1; transform: translateY(0); } }
    
    .widget-header { background: #3B82F6; padding: 24px; color: white; border-radius: 24px 24px 0 0; position: relative; }
    .wh-top { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 20px; }
    .wh-logo { width: 32px; height: 32px; background: white; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: #3B82F6; font-weight: bold; font-size: 18px; }
    .wh-title { font-weight: 700; font-size: 15px; }
    .wh-status { font-size: 11px; color: #D1FAE5; display: flex; align-items: center; gap: 4px; margin-top: 2px; }
    .wh-status .dot { width: 6px; height: 6px; background: #10B981; border-radius: 50%; }
    .wh-greeting { font-size: 28px; font-weight: 800; margin-bottom: 8px; }
    .wh-subgreeting { font-size: 14px; opacity: 0.9; margin-bottom: 24px; }
    .wh-search { display: flex; background: white; border-radius: 24px; padding: 4px; }
    .wh-search input { flex: 1; border: none; outline: none; padding: 10px 16px; font-size: 14px; border-radius: 20px; }
    .wh-search button { background: #3B82F6; border: none; width: 36px; height: 36px; border-radius: 50%; color: white; cursor: pointer; display: flex; align-items: center; justify-content: center; }
    
    .widget-body { padding: 24px; flex: 1; overflow-y: auto; background: #FAFAFA; }
    .wb-section-title { font-size: 13px; font-weight: 700; color: #374151; margin-bottom: 16px; }
    .qa-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 24px; }
    .qa-item { display: flex; flex-direction: column; align-items: center; gap: 8px; cursor: pointer; }
    .qa-item:hover .qa-icon { box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    .qa-icon { width: 50px; height: 50px; background: white; border-radius: 16px; border: 1px solid #E5E7EB; display: flex; align-items: center; justify-content: center; font-size: 20px; transition: all 0.2s; }
    .qa-item span { font-size: 11px; color: #4B5563; font-weight: 500; }
    
    .products-row { display: flex; gap: 16px; margin-top: 16px; }
    .product-card { background: white; border: 1px solid #E5E7EB; border-radius: 16px; overflow: hidden; flex: 1; padding-bottom: 12px; cursor: pointer; transition: transform 0.2s; }
    .product-card:hover { transform: translateY(-2px); }
    .product-img { height: 120px; width: 100%; position: relative; }
    .product-img img { width: 100%; height: 100%; object-fit: cover; }
    .product-info { padding: 12px; }
    .product-info h5 { font-size: 14px; font-weight: 700; color: #111827; margin-bottom: 4px; }
    .product-info p { font-size: 11px; color: #6B7280; font-weight: 500; margin-bottom: 12px; }
    .add-btn { width: 100%; background: #111827; color: white; border: none; padding: 8px; border-radius: 8px; font-size: 12px; font-weight: 600; cursor: pointer; }
    .add-btn:hover { background: #374151; }
    
    .widget-footer { display: flex; justify-content: space-between; padding: 12px 24px; background: white; border-top: 1px solid #E5E7EB; border-radius: 0 0 24px 24px; }
    .wf-item { display: flex; flex-direction: column; align-items: center; gap: 4px; color: #9CA3AF; font-size: 10px; font-weight: 600; cursor: pointer; transition: color 0.2s; }
    .wf-item.active { color: #3B82F6; }
    .wf-item:hover { color: #4B5563; }
"""

new_html = """
  <!-- NAVIGATION -->
  <nav class="nav">
    <div class="nav-container">
      <div class="nav-logo-area">
        <div class="nav-logo-icon">S</div>
        <div class="nav-logo-text">STEPS AI SUITE<br><span>Industry AI Agents</span></div>
      </div>
      <div class="nav-tabs">
        <div class="nav-tab">⚕️ Healthcare</div>
        <div class="nav-tab">🎓 EdTech</div>
        <div class="nav-tab">🏢 Real Estate</div>
        <div class="nav-tab">✈️ Travel</div>
        <div class="nav-tab active">🛒 Retail ▾</div>
      </div>
      <div class="nav-right">
        <span style="font-size: 11px; color: #9CA3AF; margin-right: 10px; font-weight: 600;">LAYOUT:</span>
        <select class="nav-select"><option>Horizontal List</option></select>
      </div>
    </div>
  </nav>

  <!-- HERO SECTION -->
  <section class="dark-hero">
    <div class="hero-bg"></div>
    
    <div class="hero-layout">
      <div class="hero-left">
        <div class="hero-badge">APPAREL E-COMMERCE ACTIVE</div>
        <h1 class="hero-title">Step Into Next-Gen<br><span class="hero-highlight">Style & Comfort</span></h1>
        <p class="hero-subtitle">Reduce front-desk load by guiding patients to the right treatments and doctors instantly via conversational AI.</p>
      </div>
      
      <div class="hero-right">
        <div class="widget-mockup" id="chatWidget">
          <!-- Widget Header -->
          <div class="widget-header">
            <div class="wh-top">
              <div style="display:flex; align-items:center; gap:12px;">
                <div class="wh-logo">👟</div>
                <div>
                  <div class="wh-title">Steps Footwear AI</div>
                  <div class="wh-status"><span class="dot"></span> Online</div>
                </div>
              </div>
              <div style="display:flex; gap:12px; color:white; font-size:16px;">
                <span>🌙</span> <span>✖</span>
              </div>
            </div>
            <h2 class="wh-greeting">Hello! 👋</h2>
            <p class="wh-subgreeting">Find your perfect fit today.</p>
            <div class="wh-search">
              <input type="text" placeholder="Search running, casual, sneakers...">
              <button class="send-btn">➤</button>
            </div>
          </div>

          <!-- Widget Body -->
          <div class="widget-body">
            <h4 class="wb-section-title">Quick Access</h4>
            <div class="qa-grid">
              <div class="qa-item"><div class="qa-icon">🔥</div><span>Trending</span></div>
              <div class="qa-item"><div class="qa-icon">🏃</div><span>Running</span></div>
              <div class="qa-item"><div class="qa-icon">🏷️</div><span>Sale</span></div>
              <div class="qa-item"><div class="qa-icon">🎧</div><span>Support</span></div>
            </div>

            <div style="display:flex; justify-content:space-between; align-items:center; margin-top:24px;">
              <h4 class="wb-section-title" style="margin:0;">New Arrivals</h4>
              <div style="display:flex; gap:8px;">
                <button style="border:1px solid #e5e7eb; background:white; border-radius:50%; width:24px; height:24px; display:flex; align-items:center; justify-content:center; cursor:pointer;">❮</button>
                <button style="border:1px solid #e5e7eb; background:white; border-radius:50%; width:24px; height:24px; display:flex; align-items:center; justify-content:center; cursor:pointer;">❯</button>
              </div>
            </div>
            <div class="products-row">
              <div class="product-card">
                <div class="product-img">
                  <img src="https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=200&h=150&fit=crop" alt="Air Max">
                </div>
                <div class="product-info">
                  <h5>Air Max Pro</h5>
                  <p>$120.00 • Running</p>
                  <button class="add-btn">+ Add</button>
                </div>
              </div>
              <div class="product-card">
                <div class="product-img">
                  <img src="https://images.unsplash.com/photo-1608231387042-66d1773070a5?w=200&h=150&fit=crop" alt="High Tops">
                </div>
                <div class="product-info">
                  <h5>Urban High Tops</h5>
                  <p>$95.00 • Casual</p>
                  <button class="add-btn">+ Add</button>
                </div>
              </div>
            </div>
          </div>

          <!-- Widget Footer -->
          <div class="widget-footer">
            <div class="wf-item active"><span style="font-size:20px;">🏠</span>Home</div>
            <div class="wf-item"><span style="font-size:20px;">⊞</span>Services</div>
            <div class="wf-item"><span style="font-size:20px;">📅</span>Bookings</div>
            <div class="wf-item"><span style="font-size:20px;">👤</span>Profile</div>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

# Replace CSS
# We'll insert new_css right before </style>
content = re.sub(r'</style>', new_css + '\n  </style>', content)

# Replace HTML
# Find <!-- NAVIGATION --> to <!-- CREDIBILITY STRIP -->
html_pattern = re.compile(r'<!-- NAVIGATION -->.*?<!-- CREDIBILITY STRIP -->', re.DOTALL)
content = html_pattern.sub(new_html + '\n  <!-- CREDIBILITY STRIP -->', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Hero section replaced successfully.")
