import re

file_path = "c:\\Users\\user\\Downloads\\HOME STAEP AI\\StepsAI_Redesign.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_css = """
    /* --- HEALTHCARE HERO & NAV CSS --- */
    body { background-color: #FAFAFA; color: #1F2937; overflow-x: hidden; font-family: 'Inter', sans-serif; }
    h1, h2, h3 { font-family: 'Outfit', sans-serif; }
    
    .nav { position: fixed; top: 0; left: 0; width: 100%; z-index: 100; background: rgba(255,255,255,0.9); backdrop-filter: blur(10px); border-bottom: 1px solid rgba(0,0,0,0.05); }
    .nav-container { max-width: 1400px; margin: 0 auto; padding: 16px 32px; display: flex; align-items: center; justify-content: space-between; }
    .nav-logo-area { display: flex; align-items: center; gap: 12px; }
    .nav-logo-icon { width: 32px; height: 32px; background: #3B82F6; border-radius: 8px; color: white; font-weight: 800; font-size: 20px; display: flex; align-items: center; justify-content: center; }
    .nav-logo-text { color: #111827; font-weight: 800; font-size: 22px; letter-spacing: -0.5px; }
    .nav-tabs { display: flex; gap: 24px; }
    .nav-tab { color: #4B5563; font-size: 14px; font-weight: 600; cursor: pointer; transition: color 0.2s; }
    .nav-tab:hover { color: #111827; }
    .nav-right { display: flex; align-items: center; gap: 16px; }
    .nav-login { color: #4B5563; font-size: 14px; font-weight: 600; text-decoration: none; }
    .btn-outline { border: 1px solid #E5E7EB; background: white; color: #111827; padding: 8px 16px; border-radius: 8px; font-size: 14px; font-weight: 600; cursor: pointer; }
    .btn-primary { background: #4F46E5; color: white; padding: 8px 16px; border-radius: 8px; font-size: 14px; font-weight: 600; border: none; cursor: pointer; box-shadow: 0 4px 6px rgba(79,70,229,0.2); }

    .light-hero { position: relative; width: 100vw; min-height: 100vh; background: radial-gradient(circle at 50% 0%, #ffffff 0%, #F5F3FF 80%); display: flex; align-items: center; justify-content: center; padding: 140px 5% 100px; overflow: hidden; }
    
    .hero-layout { position: relative; z-index: 10; max-width: 1400px; width: 100%; display: flex; flex-direction: column; align-items: center; text-align: center; }
    
    .hero-badge { display: inline-flex; align-items: center; gap: 8px; padding: 8px 20px; border-radius: 100px; color: #6366F1; font-size: 12px; font-weight: 700; letter-spacing: 1px; margin-bottom: 24px; background: rgba(99,102,241,0.05); border: 1px solid rgba(99,102,241,0.1); }
    .hero-title { font-size: 4.5rem; font-weight: 800; color: #0F172A; line-height: 1.1; margin-bottom: 24px; letter-spacing: -1.5px; }
    .hero-highlight { background: linear-gradient(135deg, #4F46E5, #9333EA); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .hero-subtitle { font-size: 1.125rem; color: #64748B; max-width: 650px; line-height: 1.6; margin-bottom: 60px; }

    .hero-visuals { position: relative; width: 100%; height: 500px; display: flex; justify-content: center; align-items: flex-end; }
    .central-character { position: relative; z-index: 20; height: 110%; object-fit: contain; filter: drop-shadow(0 20px 40px rgba(0,0,0,0.15)); }

    /* Floating Cards Shared */
    .floating-card { position: absolute; background: white; border-radius: 20px; box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.08); padding: 24px; z-index: 30; border: 1px solid rgba(0,0,0,0.03); will-change: transform; }
    
    /* Stat Cards */
    .stat-card { display: flex; align-items: center; gap: 16px; width: 280px; }
    .stat-icon { width: 54px; height: 54px; border-radius: 14px; display: flex; align-items: center; justify-content: center; font-size: 24px; }
    .stat-icon.purple { background: #F3F0FF; color: #8B5CF6; }
    .stat-icon.green { background: #ECFDF5; color: #10B981; }
    .stat-text { text-align: left; }
    .stat-text h3 { font-size: 28px; font-weight: 800; color: #0F172A; margin-bottom: 4px; }
    .stat-text p { font-size: 11px; color: #64748B; line-height: 1.4; font-weight: 500; }
    .stat-graph { width: 60px; height: 30px; margin-left: auto; }

    /* WA Chat */
    .chat-card { width: 340px; background: rgba(255,255,255,0.85); backdrop-filter: blur(20px); padding: 20px; text-align: left; }
    .bubble { padding: 12px 16px; border-radius: 16px; font-size: 12px; margin-bottom: 12px; max-width: 90%; line-height: 1.5; position: relative; box-shadow: 0 4px 6px rgba(0,0,0,0.02); }
    .bubble.sent { background: #E0FFD4; color: #111827; margin-left: auto; border-bottom-right-radius: 4px; }
    .bubble.received { background: white; color: #111827; border-bottom-left-radius: 4px; border: 1px solid #F1F5F9; }
    .time { font-size: 9px; color: #94A3B8; text-align: right; margin-top: 6px; display: block; }
    
    .wa-icon { position: absolute; left: -20px; top: 50%; transform: translateY(-50%); width: 48px; height: 48px; background: #25D366; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 10px 20px rgba(37, 211, 102, 0.3); }

    /* StepsAI Assistant Widget */
    .assistant-widget { width: 340px; padding: 0; overflow: hidden; display: flex; flex-direction: column; text-align: left; }
    .aw-header { padding: 16px; border-bottom: 1px solid #F1F5F9; display: flex; justify-content: space-between; align-items: center; }
    .aw-logo { display: flex; align-items: center; gap: 10px; font-weight: 700; font-size: 14px; color: #0F172A; }
    .aw-icon { width: 28px; height: 28px; background: #4F46E5; border-radius: 8px; color: white; display: flex; align-items: center; justify-content: center; font-size: 14px; }
    .aw-status { display: flex; align-items: center; gap: 4px; font-size: 10px; color: #10B981; font-weight: 600; margin-top: 2px; }
    .aw-status .dot { width: 6px; height: 6px; background: #10B981; border-radius: 50%; }
    .aw-body { padding: 16px; background: #F8FAFC; }
    .aw-bubble { background: white; padding: 12px 16px; border-radius: 12px; font-size: 12px; color: #1F2937; line-height: 1.5; margin-bottom: 12px; border: 1px solid #F1F5F9; box-shadow: 0 2px 4px rgba(0,0,0,0.02); }
    .aw-list { margin-top: 10px; margin-bottom: 12px; padding-left: 20px; color: #374151; font-size: 12px; line-height: 1.6; }
    .aw-btn { width: 100%; background: white; border: 1px solid #E5E7EB; color: #4F46E5; padding: 10px; border-radius: 8px; font-size: 12px; font-weight: 600; text-align: center; cursor: pointer; transition: all 0.2s; }
    .aw-btn:hover { background: #F3F0FF; border-color: #4F46E5; }

    /* Recommended Carousel */
    .carousel-card { width: 440px; padding: 20px; z-index: 25; text-align: left; }
    .carousel-header { font-size: 13px; font-weight: 700; color: #0F172A; margin-bottom: 16px; }
    .carousel-items { display: flex; gap: 12px; }
    .course-item { flex: 1; background: white; border: 1px solid #F1F5F9; border-radius: 12px; overflow: hidden; }
    .course-img { height: 80px; position: relative; }
    .course-img img { width: 100%; height: 100%; object-fit: cover; }
    .course-info { padding: 12px; }
    .course-info h5 { font-size: 11px; font-weight: 700; margin-bottom: 6px; line-height: 1.3; height: 28px; }
    .course-info .rating { font-size: 10px; color: #F59E0B; font-weight: 600; margin-bottom: 6px; }
    .course-info .price { font-size: 12px; font-weight: 800; color: #0F172A; }
    .ig-icon { position: absolute; right: -20px; top: 50%; transform: translateY(-50%); width: 48px; height: 48px; background: linear-gradient(45deg, #f09433, #dc2743, #bc1888); border-radius: 14px; display: flex; align-items: center; justify-content: center; box-shadow: 0 10px 20px rgba(220, 39, 67, 0.3); }

    /* SVG Connections */
    .connections { position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none; z-index: 15; }
    .conn-line { fill: none; stroke: #94A3B8; stroke-width: 2; stroke-dasharray: 6 6; opacity: 0.5; }
    .conn-dot { fill: #4F46E5; }

    /* Trust Strips */
    .trust-strip { background: rgba(255,255,255,0.6); backdrop-filter: blur(10px); padding: 16px 32px; border-radius: 100px; display: inline-flex; gap: 40px; margin-top: 40px; border: 1px solid rgba(0,0,0,0.05); }
    .trust-item { display: flex; align-items: center; gap: 8px; font-size: 13px; font-weight: 600; color: #4B5563; }
    
    .logos-strip { background: white; padding: 24px 48px; border-radius: 24px; display: flex; align-items: center; gap: 40px; margin-top: 32px; box-shadow: 0 10px 30px rgba(0,0,0,0.03); max-width: 1200px; margin-left: auto; margin-right: auto; }
    .logos-title { font-size: 13px; font-weight: 600; color: #4B5563; max-width: 150px; text-align: left; line-height: 1.5; }
    .logos-img { display: flex; align-items: center; gap: 32px; flex: 1; justify-content: space-between; }
    .logos-img span { font-weight: 800; font-size: 20px; color: #94A3B8; }
"""

new_html = """
  <!-- NAVIGATION -->
  <nav class="nav">
    <div class="nav-container">
      <div class="nav-logo-area">
        <div class="nav-logo-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="white"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg></div>
        <div class="nav-logo-text">StepsAI</div>
      </div>
      <div class="nav-tabs">
        <div class="nav-tab">Product ▾</div>
        <div class="nav-tab">Solutions ▾</div>
        <div class="nav-tab">Integrations</div>
        <div class="nav-tab">Resources ▾</div>
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
  <section class="light-hero">
    <div class="hero-layout">
      
      <div class="hero-badge gs-up">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l2.4 7.6L22 12l-7.6 2.4L12 22l-2.4-7.6L2 12l7.6-2.4L12 2z"/></svg>
        AI AGENT PLATFORM FOR MODERN BUSINESSES
      </div>
      
      <h1 class="hero-title gs-up">
        One AI agent. Every channel.<br>
        <span class="hero-highlight">Real business outcomes.</span>
      </h1>
      
      <p class="hero-subtitle gs-up">
        StepsAI answers questions, recommends, captures leads, books appointments and automates work across your website, WhatsApp, Instagram and more.
      </p>

      <div class="hero-visuals">
        <!-- Connecting Lines -->
        <svg class="connections" width="100%" height="100%">
            <!-- Left Top -->
            <path class="conn-line" d="M 600 250 Q 400 150 250 150" />
            <circle class="conn-dot" r="4" cx="250" cy="150" />
            <!-- Left Bottom -->
            <path class="conn-line" d="M 550 350 Q 300 450 250 400" />
            <circle class="conn-dot" r="4" cx="250" cy="400" />
            <!-- Right Top -->
            <path class="conn-line" d="M 650 250 Q 800 180 950 180" />
            <circle class="conn-dot" r="4" cx="950" cy="180" />
        </svg>

        <!-- Central Character -->
        <img src="assets/hero_woman_grey_suit.png" alt="Professional User" class="central-character gs-hero">

        <!-- Top Left: Leads Stat -->
        <div class="floating-card stat-card gs-float" style="top: 15%; left: -5%;">
            <div class="stat-icon purple">👥</div>
            <div class="stat-text">
                <h3>2.4X</h3>
                <p>More qualified leads<br>with AI conversations</p>
            </div>
            <div class="stat-graph">
                <svg viewBox="0 0 60 30" fill="none" stroke="#22c55e" stroke-width="2"><polyline points="0,30 15,20 30,25 45,10 60,5"></polyline></svg>
            </div>
        </div>

        <!-- Bottom Left: WA Chat -->
        <div class="floating-card chat-card gs-float-delayed" style="top: 55%; left: -10%;">
            <div class="wa-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="white"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/></svg>
            </div>
            <div class="bubble sent">
                Hi, I need to book a consultation for skin acne.
                <span class="time">10:30 AM <span style="color:#3b82f6">✓✓</span></span>
            </div>
            <div class="bubble received">
                Sure! Our dermatologist Dr. Neha Sharma is available tomorrow at 4:30 PM.
                <span class="time">10:30 AM <span style="color:#3b82f6">✓✓</span></span>
            </div>
            <div class="bubble sent">
                That works for me.
                <span class="time">10:31 AM <span style="color:#3b82f6">✓✓</span></span>
            </div>
            <div class="bubble received">
                Great! Your appointment is confirmed for tomorrow at 4:30 PM. See you then! 😊
                <span class="time">10:31 AM</span>
            </div>
        </div>

        <!-- Top Right: Conversion Stat -->
        <div class="floating-card stat-card gs-float" style="top: 15%; right: -5%;">
            <div class="stat-icon green">📊</div>
            <div class="stat-text">
                <h3>35%</h3>
                <p>Increase in conversion<br>from conversations</p>
            </div>
            <div class="stat-graph">
                <svg viewBox="0 0 60 30" fill="none" stroke="#22c55e" stroke-width="2"><polyline points="0,25 15,30 30,15 45,20 60,5"></polyline><circle cx="60" cy="5" r="3" fill="#22c55e"></circle></svg>
            </div>
        </div>

        <!-- Middle Right: Assistant Widget -->
        <div class="floating-card assistant-widget gs-float-delayed" style="top: 45%; right: 5%; z-index: 26;">
            <div class="aw-header">
                <div class="aw-logo">
                    <div class="aw-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="white"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg></div>
                    <div>
                        StepsAI Assistant
                        <div class="aw-status"><span class="dot"></span> Online</div>
                    </div>
                </div>
                <span style="color:#94A3B8; cursor:pointer;">✖</span>
            </div>
            <div class="aw-body">
                <div class="aw-bubble" style="margin-left: 20px;">
                    What are the available treatment options for acne?
                    <span class="time" style="text-align:right;">10:30 AM</span>
                </div>
                <div style="display:flex; gap:8px;">
                    <div class="aw-icon" style="flex-shrink:0; width:24px; height:24px; border-radius:50%;"><svg width="12" height="12" viewBox="0 0 24 24" fill="white"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg></div>
                    <div>
                        <div class="aw-bubble" style="margin-bottom:0;">
                            Based on your concern, here are the most effective acne treatments we offer.
                            <ul class="aw-list">
                                <li>Chemical Peels</li>
                                <li>HydraFacial</li>
                                <li>Laser Therapy</li>
                            </ul>
                            <button class="aw-btn">View Treatments</button>
                        </div>
                        <span class="time" style="text-align:right;">10:30 AM</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- Far Right: Product Carousel -->
        <div class="floating-card carousel-card gs-float" style="top: 60%; right: -25%;">
            <div class="ig-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
            </div>
            <div class="carousel-header">Recommended for you</div>
            <div class="carousel-items">
                <!-- Course 1 -->
                <div class="course-item">
                    <div class="course-img"><img src="https://images.unsplash.com/photo-1616394584738-fc6e612e71b9?w=200&h=120&fit=crop"></div>
                    <div class="course-info">
                        <h5>Deep Cleansing HydraFacial</h5>
                        <div class="rating">★ 4.8 <span style="color:#94a3b8;font-weight:400">(128)</span></div>
                        <div class="price">₹3,999</div>
                    </div>
                </div>
                <!-- Course 2 -->
                <div class="course-item">
                    <div class="course-img"><img src="https://images.unsplash.com/photo-1570172619644-defd82136d8b?w=200&h=120&fit=crop"></div>
                    <div class="course-info">
                        <h5>Laser Hair Reduction</h5>
                        <div class="rating">★ 4.9 <span style="color:#94a3b8;font-weight:400">(96)</span></div>
                        <div class="price">₹6,499</div>
                    </div>
                </div>
                <!-- Course 3 -->
                <div class="course-item">
                    <div class="course-img"><img src="https://images.unsplash.com/photo-1556228578-0d85b1a4d571?w=200&h=120&fit=crop"></div>
                    <div class="course-info">
                        <h5>Anti-Acne Treatment</h5>
                        <div class="rating">★ 4.7 <span style="color:#94a3b8;font-weight:400">(72)</span></div>
                        <div class="price">₹2,999</div>
                    </div>
                </div>
            </div>
        </div>
      </div>
      
      <!-- Trust Strip -->
      <div class="trust-strip gs-up">
        <div class="trust-item"><span style="color:#8B5CF6; font-size:16px;">✉</span> No credit card</div>
        <div class="trust-item"><span style="color:#8B5CF6; font-size:16px;">⏱</span> Setup in minutes</div>
        <div class="trust-item"><span style="color:#8B5CF6; font-size:16px;">✖</span> Cancel anytime</div>
        <div class="trust-item"><span style="color:#8B5CF6; font-size:16px;">⚙</span> Works on every channel</div>
      </div>
      
    </div>
  </section>

  <!-- Logos Section -->
  <div class="logos-strip gs-up">
    <div class="logos-title">Trusted by 500+ businesses across healthcare and more</div>
    <div class="logos-img">
        <span style="color:#0284C7;">Apollo HOSPITALS</span>
        <span style="color:#0369A1;">MAX Healthcare</span>
        <span style="color:#C026D3;">cloudnine</span>
        <span style="color:#0284C7;">manipalhospitals</span>
        <span style="color:#EAB308;">Pristyn Care</span>
        <span style="color:#94A3B8;">& more</span>
    </div>
  </div>
"""

js_code = """
  <!-- GSAP Animations -->
  <script>
    document.addEventListener("DOMContentLoaded", () => {
        gsap.registerPlugin();
        const tl = gsap.timeline();

        // Elegant, non-bouncy entrances
        tl.from(".gs-up", {
            y: 30,
            opacity: 0,
            duration: 1.2,
            stagger: 0.1,
            ease: "power3.out"
        });

        tl.from(".gs-hero", {
            y: 40,
            opacity: 0,
            duration: 1.5,
            ease: "power2.out"
        }, "-=0.8");

        tl.from(".gs-float", {
            y: 40,
            opacity: 0,
            duration: 1.2,
            stagger: 0.1,
            ease: "power4.out"
        }, "-=1");

        tl.from(".gs-float-delayed", {
            y: 40,
            opacity: 0,
            duration: 1.2,
            stagger: 0.1,
            ease: "power4.out"
        }, "-=0.8");

        // SVG lines
        tl.from(".conn-line", {
            strokeDashoffset: 50,
            strokeDasharray: "50",
            opacity: 0,
            duration: 1.5,
            ease: "power2.inOut"
        }, "-=1");
        
        tl.from(".conn-dot", {
            scale: 0,
            transformOrigin: "center",
            duration: 0.5,
            stagger: 0.1,
            ease: "back.out(1.5)"
        }, "-=0.8");

        // Subtle Spatial Float
        gsap.utils.toArray('.gs-float').forEach(card => {
            gsap.to(card, {
                y: "-=8",
                duration: 3.5 + Math.random(),
                yoyo: true,
                repeat: -1,
                ease: "sine.inOut"
            });
        });

        gsap.utils.toArray('.gs-float-delayed').forEach(card => {
            gsap.to(card, {
                y: "+=8",
                duration: 4 + Math.random(),
                yoyo: true,
                repeat: -1,
                ease: "sine.inOut",
                delay: Math.random()
            });
        });
    });
  </script>
"""

# We'll use regex to replace everything from <style> to <!-- CREDIBILITY STRIP --> (or the end if not found)
# Actually, it's safer to just replace from <style> to </style> and then the hero section.

css_pattern = re.compile(r'<style>.*?</style>', re.DOTALL)
content = css_pattern.sub('<style>' + new_css + '</style>', content)

# Replace the body content from <body> to whatever was after the hero
# Let's see what the structure is. It likely has <!-- NAVIGATION --> and <!-- HERO SECTION -->
html_pattern = re.compile(r'<!-- NAVIGATION -->.*?<!-- CREDIBILITY STRIP -->', re.DOTALL)
if html_pattern.search(content):
    content = html_pattern.sub(new_html + '\\n  <!-- CREDIBILITY STRIP -->', content)
else:
    # If not found, replace everything inside <body> except script tags at the very bottom
    body_pattern = re.compile(r'<body.*?>', re.IGNORECASE)
    content = body_pattern.sub('<body>\\n' + new_html, content)

# Append JS before </body>
content = content.replace('</body>', js_code + '\\n</body>')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Redesign applied successfully.")
