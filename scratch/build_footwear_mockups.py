import re

file_path = "c:\\Users\\user\\Downloads\\HOME STAEP AI\\StepsAI_Redesign.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# --- CSS FOR FOOTWEAR MOCKUPS ---
footwear_css = """
    /* --- FOOTWEAR MOCKUPS CSS --- */
    
    /* Shared Widget Container */
    .footwear-widget { position: absolute; width: 340px; height: 500px; background: #F8FAFC; border-radius: 24px; box-shadow: 0 24px 48px -12px rgba(0,0,0,0.18); overflow: hidden; display: flex; flex-direction: column; z-index: 30; border: 1px solid rgba(0,0,0,0.05); font-family: 'Inter', sans-serif; }
    
    /* Chat Widget (Left) */
    .fw-chat { bottom: -20px; left: -140px; }
    .fw-chat-header { padding: 16px; background: white; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #F1F5F9; }
    .fw-ch-left { display: flex; align-items: center; gap: 12px; }
    .fw-back { color: #64748B; font-size: 16px; }
    .fw-avatar { width: 36px; height: 36px; background: #3B82F6; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; }
    .fw-ch-title { font-size: 13px; font-weight: 700; color: #0F172A; line-height: 1.2; }
    .fw-ch-status { font-size: 10px; color: #10B981; font-weight: 600; display: flex; align-items: center; gap: 4px; }
    .fw-ch-status::before { content: ''; display: block; width: 6px; height: 6px; background: #10B981; border-radius: 50%; }
    .fw-ch-right { display: flex; align-items: center; gap: 12px; color: #64748B; font-size: 16px; font-weight: bold; }
    
    .fw-chat-body { flex: 1; padding: 16px; overflow-y: auto; display: flex; flex-direction: column; gap: 16px; }
    .fw-sent { background: #3B82F6; color: white; padding: 10px 16px; border-radius: 16px; border-top-right-radius: 4px; font-size: 12px; align-self: flex-end; max-width: 80%; }
    
    .fw-bot-row { display: flex; gap: 10px; }
    .fw-bot-avatar { width: 24px; height: 24px; background: #3B82F6; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; flex-shrink: 0; font-size: 12px; }
    .fw-bot-content { flex: 1; }
    .fw-bot-text { font-size: 12px; color: #334155; line-height: 1.5; margin-bottom: 12px; }
    
    .fw-prod-card { background: white; border: 1px solid #E2E8F0; border-radius: 16px; padding: 12px; margin-bottom: 12px; }
    .fw-prod-card.active { border-color: #3B82F6; box-shadow: 0 4px 12px rgba(59,130,246,0.1); }
    .fw-pc-top { display: flex; gap: 12px; margin-bottom: 12px; }
    .fw-pc-img { width: 80px; height: 80px; border-radius: 12px; object-fit: cover; background: #F1F5F9; }
    .fw-pc-info { flex: 1; }
    .fw-pc-title { font-size: 13px; font-weight: 700; color: #3B82F6; margin: 0 0 4px 0; }
    .fw-pc-price { font-size: 15px; font-weight: 800; color: #0F172A; margin: 0 0 6px 0; }
    .fw-pc-size-row { display: flex; align-items: center; gap: 6px; font-size: 9px; font-weight: 700; color: #64748B; }
    .fw-size-pill { padding: 4px 8px; background: #F1F5F9; border-radius: 6px; color: #334155; }
    .fw-size-pill.active { background: #3B82F6; color: white; }
    .fw-pc-add { width: 100%; background: #0F172A; color: white; border: none; padding: 8px; border-radius: 8px; font-size: 12px; font-weight: 700; cursor: pointer; }
    .fw-pc-desc { font-size: 10px; color: #64748B; line-height: 1.4; padding-top: 10px; border-top: 1px solid #F1F5F9; }
    
    .fw-chat-input { padding: 16px; background: white; border-top: 1px solid #F1F5F9; }
    .fw-input-box { background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 100px; padding: 8px 12px 8px 16px; display: flex; justify-content: space-between; align-items: center; }
    .fw-input-box span { color: #94A3B8; font-size: 12px; }
    .fw-send-btn { width: 28px; height: 28px; background: #3B82F6; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; }

    /* Home Widget (Right) */
    .fw-home { bottom: -20px; right: -140px; background: white; }
    .fw-home-header { background: #2563EB; padding: 20px; border-bottom-left-radius: 24px; border-bottom-right-radius: 24px; color: white; position: relative; }
    .fw-hh-top { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 20px; }
    .fw-hh-logo { display: flex; align-items: center; gap: 10px; }
    .fw-hh-icon { width: 32px; height: 32px; background: white; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 16px; }
    .fw-hh-text h4 { margin: 0; font-size: 14px; font-weight: 700; }
    .fw-hh-text p { margin: 0; font-size: 10px; color: #A7F3D0; font-weight: 600; display: flex; align-items: center; gap: 4px; }
    .fw-hh-text p::before { content: ''; display: block; width: 6px; height: 6px; background: #10B981; border-radius: 50%; }
    .fw-hh-right { display: flex; gap: 12px; font-size: 16px; font-weight: bold; }
    .fw-hh-hello { font-size: 32px; font-weight: 800; margin: 0 0 4px 0; letter-spacing: -1px; }
    .fw-hh-sub { font-size: 12px; font-weight: 500; margin: 0 0 16px 0; opacity: 0.9; }
    
    .fw-search { background: white; border-radius: 100px; padding: 6px 6px 6px 16px; display: flex; justify-content: space-between; align-items: center; }
    .fw-search span { color: #94A3B8; font-size: 12px; }
    
    .fw-home-body { padding: 20px; flex: 1; overflow-y: auto; padding-bottom: 70px; }
    .fw-section-title { font-size: 13px; font-weight: 800; color: #0F172A; margin: 0 0 12px 0; display: flex; justify-content: space-between; align-items: center; }
    
    .fw-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-bottom: 24px; }
    .fw-grid-item { display: flex; flex-direction: column; align-items: center; gap: 8px; }
    .fw-gi-icon { width: 48px; height: 48px; background: white; border: 1px solid #E2E8F0; border-radius: 16px; display: flex; align-items: center; justify-content: center; color: #3B82F6; font-size: 18px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); }
    .fw-gi-text { font-size: 10px; font-weight: 600; color: #475569; }
    
    .fw-arr-arrows { display: flex; gap: 8px; }
    .fw-arrow { width: 20px; height: 20px; border: 1px solid #E2E8F0; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 10px; color: #64748B; }
    
    .fw-arrivals { display: flex; gap: 12px; overflow-x: auto; padding-bottom: 10px; }
    .fw-arr-card { min-width: 130px; background: white; border: 1px solid #E2E8F0; border-radius: 16px; overflow: hidden; padding-bottom: 12px; position: relative; }
    .fw-arr-img { width: 100%; height: 100px; object-fit: cover; }
    .fw-arr-heart { position: absolute; top: 8px; right: 8px; width: 20px; height: 20px; background: rgba(255,255,255,0.2); backdrop-filter: blur(4px); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 10px; }
    .fw-arr-info { padding: 10px 10px 0; }
    .fw-arr-title { font-size: 11px; font-weight: 700; color: #0F172A; margin: 0 0 2px 0; }
    .fw-arr-price { font-size: 9px; color: #64748B; font-weight: 500; }
    
    .fw-nav { position: absolute; bottom: 0; left: 0; width: 100%; background: white; border-top: 1px solid #F1F5F9; padding: 12px 20px; display: flex; justify-content: space-between; z-index: 10; }
    .fw-nav-item { display: flex; flex-direction: column; align-items: center; gap: 4px; color: #94A3B8; font-size: 9px; font-weight: 600; }
    .fw-nav-item.active { color: #3B82F6; }
    .fw-nav-icon { font-size: 16px; }
"""

footwear_chat_html = """
      <!-- Bottom Left: Chat Widget (Replaces WhatsApp) -->
      <div class="footwear-widget fw-chat gs-float-delayed">
          <div class="fw-chat-header">
              <div class="fw-ch-left">
                  <div class="fw-back">←</div>
                  <div class="fw-avatar">👟</div>
                  <div>
                      <div class="fw-ch-title">Steps Footwear AI</div>
                      <div class="fw-ch-status">Online</div>
                  </div>
              </div>
              <div class="fw-ch-right">
                  <span>☾</span>
                  <span>⋮</span>
                  <span>×</span>
              </div>
          </div>
          <div class="fw-chat-body">
              <div class="fw-sent">Tell me about Air Max Pro</div>
              <div class="fw-bot-row">
                  <div class="fw-bot-avatar">👟</div>
                  <div class="fw-bot-content">
                      <div class="fw-bot-text">Based on your request, here are our top recommendations. <strong>Tap any item for details.</strong></div>
                      
                      <div class="fw-prod-card active">
                          <div class="fw-pc-top">
                              <img src="https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=200&h=200&fit=crop" class="fw-pc-img">
                              <div class="fw-pc-info">
                                  <h4 class="fw-pc-title">Air Max Pro</h4>
                                  <h3 class="fw-pc-price">$120.00</h3>
                                  <div class="fw-pc-size-row">
                                      SIZE: <span class="fw-size-pill active">US 9</span> <span class="fw-size-pill">US 10</span>
                                  </div>
                              </div>
                          </div>
                          <button class="fw-pc-add">+ Add</button>
                          <div class="fw-pc-desc">Engineered for optimal impact absorption and high energy response.</div>
                      </div>

                      <div class="fw-prod-card">
                          <div class="fw-pc-top">
                              <img src="https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?w=200&h=200&fit=crop" class="fw-pc-img">
                              <div class="fw-pc-info">
                                  <h4 class="fw-pc-title" style="color:#0F172A">Urban High Tops</h4>
                                  <h3 class="fw-pc-price">$95.00</h3>
                                  <div class="fw-pc-size-row">
                                      SIZE: <span class="fw-size-pill active">US 9</span> <span class="fw-size-pill">US 10</span>
                                  </div>
                              </div>
                          </div>
                          <button class="fw-pc-add">+ Add</button>
                      </div>
                  </div>
              </div>
          </div>
          <div class="fw-chat-input">
              <div class="fw-input-box">
                  <span>Type a message...</span>
                  <div class="fw-send-btn">➤</div>
              </div>
          </div>
      </div>
"""

footwear_home_html = """
      <!-- Middle Right: Home Widget (Replaces Assistant) -->
      <div class="footwear-widget fw-home gs-float">
          <div class="fw-home-header">
              <div class="fw-hh-top">
                  <div class="fw-hh-logo">
                      <div class="fw-hh-icon"><span style="color:#2563EB">👟</span></div>
                      <div class="fw-hh-text">
                          <h4>Steps Footwear AI</h4>
                          <p>Online</p>
                      </div>
                  </div>
                  <div class="fw-hh-right">
                      <span>☾</span>
                      <span>×</span>
                  </div>
              </div>
              <h2 class="fw-hh-hello">Hello! 👋</h2>
              <h3 class="fw-hh-sub">Find your perfect fit today.</h3>
              <div class="fw-search">
                  <span>Search running, casual, sneakers...</span>
                  <div class="fw-send-btn">➤</div>
              </div>
          </div>
          
          <div class="fw-home-body">
              <h3 class="fw-section-title">Quick Access</h3>
              <div class="fw-grid">
                  <div class="fw-grid-item">
                      <div class="fw-gi-icon">🔥</div>
                      <div class="fw-gi-text">Trending</div>
                  </div>
                  <div class="fw-grid-item">
                      <div class="fw-gi-icon">🏃</div>
                      <div class="fw-gi-text">Running</div>
                  </div>
                  <div class="fw-grid-item">
                      <div class="fw-gi-icon">🏷️</div>
                      <div class="fw-gi-text">Sale</div>
                  </div>
                  <div class="fw-grid-item">
                      <div class="fw-gi-icon">🎧</div>
                      <div class="fw-gi-text">Support</div>
                  </div>
              </div>

              <h3 class="fw-section-title">
                  New Arrivals
                  <div class="fw-arr-arrows">
                      <div class="fw-arrow">‹</div>
                      <div class="fw-arrow">›</div>
                  </div>
              </h3>
              <div class="fw-arrivals">
                  <div class="fw-arr-card">
                      <div class="fw-arr-heart">♥</div>
                      <img src="https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=200&h=160&fit=crop" class="fw-arr-img">
                      <div class="fw-arr-info">
                          <h4 class="fw-arr-title">Air Max Pro</h4>
                          <div class="fw-arr-price">$120.00 • Running</div>
                      </div>
                  </div>
                  <div class="fw-arr-card">
                      <div class="fw-arr-heart" style="color:#ddd">♥</div>
                      <img src="https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?w=200&h=160&fit=crop" class="fw-arr-img">
                      <div class="fw-arr-info">
                          <h4 class="fw-arr-title">Urban High Tops</h4>
                          <div class="fw-arr-price">$95.00 • Casual</div>
                      </div>
                  </div>
              </div>
          </div>

          <div class="fw-nav">
              <div class="fw-nav-item active">
                  <div class="fw-nav-icon">🏠</div>
                  Home
              </div>
              <div class="fw-nav-item">
                  <div class="fw-nav-icon">⊞</div>
                  Services
              </div>
              <div class="fw-nav-item">
                  <div class="fw-nav-icon">📅</div>
                  Bookings
              </div>
              <div class="fw-nav-item">
                  <div class="fw-nav-icon">👤</div>
                  Profile
              </div>
          </div>
      </div>
"""

# Insert CSS
css_insert_point = content.find('/* --- FOOTWEAR MOCKUPS CSS --- */')
if css_insert_point == -1:
    content = content.replace('/* Floating Cards Shared */', footwear_css + '\n    /* Floating Cards Shared */')

# Remove the old card-bl (WhatsApp) and card-mr (Assistant) and insert the new ones.
# Because regex can be tricky with nested divs, I will use precise regex substitution based on the HTML comments.

bl_pattern = re.compile(r'<!-- Bottom Left: WA Chat -->.*?<!-- Floating Instagram Icon \(Left side\) -->', re.DOTALL)
content = bl_pattern.sub(footwear_chat_html + '\n      <!-- Floating Instagram Icon (Left side) -->', content)

mr_pattern = re.compile(r'<!-- Middle Right: Assistant Widget -->.*?<!-- Far Right: Product Carousel -->', re.DOTALL)
content = mr_pattern.sub(footwear_home_html + '\n      <!-- Far Right: Product Carousel -->', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Footwear mockups injected successfully.")
