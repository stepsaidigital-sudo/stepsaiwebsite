import os

with open('build_v11_compiler.py', 'r', encoding='utf-8') as f:
    content = f.read()

CUSTOM_HOME_HERO_V8 = """
CUSTOM_HOME_HERO = \"\"\"
  <!-- S01 Landing Hero - Centered with Dynamic Chat Widget (V8 Advanced Gradient Background) -->
  <section class="hero-v2 centered-hero" style="position: relative; padding-top: 120px; padding-bottom: 0px; overflow: hidden; display: flex; flex-direction: column; align-items: center; text-align: center; max-width: 1400px; margin: 0 auto; min-height: 100vh;">
    
    <!-- Advanced Animated Mesh Gradient Background -->
    <div class="advanced-mesh-bg">
        <div class="mesh-orb-1"></div>
        <div class="mesh-orb-2"></div>
        <div class="mesh-orb-3"></div>
        <div class="hero-glass-overlay"></div>
    </div>
    
    <!-- Floating Background Mockups -->
    <div id="hero-bg-wa" style="position: absolute; left: -120px; top: 15%; transform: translateY(-50%) rotate(-8deg); z-index: 1; opacity: 0; filter: blur(2px); transition: filter 0.5s;" onmouseover="this.style.filter='blur(0)'" onmouseout="this.style.filter='blur(2px)'">
        <div class="phone-mockup" style="transform: scale(0.65); box-shadow: -20px 20px 60px rgba(0,0,0,0.15);">
            <div class="phone-notch"></div>
            <div class="mockup-screen" style="opacity:1; z-index:2; background:#EFEAE2;">
              <div class="mockup-header whatsapp">
                <div style="width:36px; height:36px; border-radius:50%; background:#fff; display:flex; align-items:center; justify-content:center; color:#008069; font-weight:800; font-size:18px;">S</div>
                <div style="line-height:1.2; font-weight:600; font-size:15px; text-align:left;">StepsAI<br><span style="font-size:12px; font-weight:400; opacity:0.8;">Online</span></div>
              </div>
              <div class="mockup-body" style="background:#EFEAE2;">
                <div class="chat-bubble in" style="text-align:left;">Do you have the linen shirt in medium? <span class="chat-time">10:42 PM</span></div>
                <div class="chat-bubble out" style="text-align:left;">Yes, two left in medium. Want me to hold one? <span class="chat-time out">10:42 PM</span></div>
                <div class="chat-bubble in" style="text-align:left;">Yes please <span class="chat-time">10:43 PM</span></div>
                <div class="chat-bubble out" style="text-align:left;">Reserved and added to your cart.<br><b style="display:block; margin-top:8px; padding-top:8px; border-top:1px solid rgba(0,0,0,0.1);">Linen Shirt · Medium · ₹2,400</b> <span class="chat-time out">10:43 PM</span></div>
                <div class="receipt-pill"><span class="check">✓</span> <span>SHOPIFY</span></div>
              </div>
            </div>
        </div>
    </div>
    
    <div id="hero-bg-ig" style="position: absolute; right: -120px; top: 25%; transform: translateY(-50%) rotate(8deg); z-index: 1; opacity: 0; filter: blur(2px); transition: filter 0.5s;" onmouseover="this.style.filter='blur(0)'" onmouseout="this.style.filter='blur(2px)'">
        <div class="phone-mockup" style="transform: scale(0.65); box-shadow: 20px 20px 60px rgba(0,0,0,0.15);">
            <div class="phone-notch"></div>
            <div class="mockup-screen" style="opacity:1; z-index:1;">
              <div class="mockup-header instagram">
                <div style="width:36px; height:36px; border-radius:50%; background:linear-gradient(135deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%); padding:2px; display:flex; align-items:center; justify-content:center;"><div style="width:100%; height:100%; background:#fff; border-radius:50%;"></div></div>
                <div style="line-height:1.2; font-weight:600; font-size:15px; color:#111; text-align:left;">StepsAI Real Estate<br><span style="font-size:12px; font-weight:400; color:#888;">StepsAI Real Estate</span></div>
              </div>
              <div class="mockup-body instagram">
                <div class="chat-bubble in ig-in" style="text-align:left;">Is the 3BHK still available? <span class="chat-time">9:15 PM</span></div>
                <div class="chat-bubble out ig-out" style="text-align:left;">It is. Want to see it this weekend? <span class="chat-time out" style="color:rgba(255,255,255,0.7);">9:15 PM</span></div>
                <div class="chat-bubble in ig-in" style="text-align:left;">Saturday works <span class="chat-time">9:16 PM</span></div>
                <div class="chat-bubble out ig-out" style="text-align:left;">Booked for Saturday 11 AM. Sending the address.<br><div style="display:flex; gap:8px; margin-top:8px;"><span style="background:rgba(255,255,255,0.2); padding:4px 8px; border-radius:8px; font-size:12px;">Sat 11:00</span></div><span class="chat-time out" style="color:rgba(255,255,255,0.7);">9:16 PM</span></div>
                <div class="receipt-pill"><span class="check">✓</span> <span>CALENDAR</span></div>
              </div>
            </div>
        </div>
    </div>

    <!-- Center Content -->
    <div style="position: relative; z-index: 10; max-width: 1000px; display: flex; flex-direction: column; align-items: center; width: 100%;">
      <span class="kicker gsap-fade-up" style="font-family: 'Geist Mono', monospace; font-size: 11px; font-weight: 500; color: var(--accent); letter-spacing: .24em; text-transform: uppercase; margin-bottom: 12px; display:block;">AI AGENT FOR SALES & SUPPORT</span>
      
      <h1 class="gsap-fade-up" style="font-family: 'Outfit'; font-size: clamp(40px, 6vw, 72px); margin-bottom: 16px; line-height: 1.05; letter-spacing: -0.03em; color: var(--text-primary); font-weight: 700; white-space: nowrap;">It answers. Then it acts.</h1>
      
      <p class="gsap-fade-up" style="font-size: clamp(16px, 1.8vw, 18px); color: var(--text-secondary); margin-bottom: 32px; max-width: 600px; line-height: 1.5;">StepsAI answers customer questions on WhatsApp, Instagram and your website. Then it books the meeting, saves the lead, or updates the order.</p>
      
      <div class="hero-actions gsap-fade-up" style="display:flex; gap:12px; flex-wrap: wrap; justify-content: center; align-items: center;">
        <a href="./partners/apply/index.html" style="text-decoration: none;">
           <button class="btn-primary" style="padding: 14px 28px; font-size: 16px; border-radius: 100px; display: flex; align-items: center; gap: 8px; box-shadow: 0 8px 24px rgba(26,86,219,0.3);">
              Start Free Trial 
              <span style="background: rgba(255,255,255,0.2); padding: 4px 8px; border-radius: 6px; font-size: 11px; font-family: 'Geist Mono', monospace; margin-left: 8px;">ENTER ↵</span>
           </button>
        </a>
        <button class="btn-outline" style="padding: 14px 28px; font-size: 16px; border-radius: 100px; background: rgba(255,255,255,0.8); backdrop-filter: blur(10px);">Book an Appointment</button>
      </div>
      
      <div class="gsap-fade-up" style="margin-top: 16px; font-size: 12px; color: var(--text-tertiary); display: flex; align-items: center; gap: 12px; font-weight: 500;">
         <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#0B9E58" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> No credit card required
         <span style="color: var(--border-subtle);">&bull;</span>
         Works with Shopify, HubSpot and Calendly.
      </div>
    </div>
    
    <!-- Main Center Web Chat Mockup -->
    <div id="hero-main-web" class="gsap-fade-up" style="position: relative; z-index: 15; margin-top: 32px; width: 100%; max-width: 380px; opacity: 0; transform: translateY(100px);">
        
        <!-- Real Chat Widget Mockup container -->
        <!-- Enhanced Shadow to make it POP off the advanced background -->
        <div style="width: 100%; background: #fbfbfd; border-radius: 20px 20px 0 0; box-shadow: 0 40px 100px rgba(26,86,219,0.25), 0 0 0 1px rgba(255,255,255,0.6) inset, 0 10px 30px rgba(123,44,191,0.1); border: 1px solid var(--border-subtle); border-bottom: none; overflow: hidden; display: flex; flex-direction: column; height: 400px; position: relative;">
           
           <!-- SCREEN 1: HOME -->
           <div id="chat-screen-home" style="position: absolute; inset: 0; display: flex; flex-direction: column; z-index: 2; background: #fbfbfd; opacity: 1;">
               <div style="background: linear-gradient(180deg, #24252e 0%, #17181e 100%); padding: 20px 16px 24px; position: relative; text-align: center;">
                  <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 16px;">
                     <div style="width: 32px; height: 32px; background: linear-gradient(135deg, #7b2cbf, #5a189a); border-radius: 8px; display: flex; justify-content: center; align-items: center; box-shadow: 0 4px 12px rgba(123,44,191,0.4);">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.5"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path></svg>
                     </div>
                     <div style="width: 28px; height: 28px; border-radius: 50%; background: rgba(255,255,255,0.15); display: flex; justify-content: center; align-items: center; color: #fff;">
                        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
                     </div>
                  </div>
                  <h3 style="margin: 0 0 4px; font-size: 22px; font-family: 'Inter', sans-serif; font-weight: 800; color: #fff;">Hi there 👋</h3>
                  <p style="margin: 0; font-size: 13px; color: rgba(255,255,255,0.8);">How can I help you today</p>
               </div>
               <div style="padding: 0 16px; position: relative; margin-top: -20px;">
                  <div style="background: #fff; border-radius: 20px; padding: 14px 16px; display: flex; align-items: center; justify-content: space-between; box-shadow: 0 8px 24px rgba(0,0,0,0.06); border: 1px solid #efefef;">
                     <div id="home-typewriter" style="color: #888; font-size: 14px; font-weight: 500; flex: 1; text-align: left; white-space: nowrap; overflow: hidden;">Ask me anything</div>
                     <div id="home-send-btn" style="width: 32px; height: 32px; border-radius: 50%; background: #f4f5f7; display: flex; justify-content: center; align-items: center; color: #444; transition: background 0.3s, color 0.3s;">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
                     </div>
                  </div>
               </div>
               <div style="flex: 1;"></div>
               <div style="background: #fff; border-top: 1px solid #efefef; display: flex; padding: 10px 0;">
                  <div style="flex: 1; display: flex; flex-direction: column; align-items: center; gap: 4px; color: #111; border-right: 1px solid #efefef;">
                     <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
                     <span style="font-size: 12px; font-weight: 600;">Home</span>
                  </div>
                  <div style="flex: 1; display: flex; flex-direction: column; align-items: center; gap: 4px; color: #999;">
                     <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
                     <span style="font-size: 12px; font-weight: 500;">Messages</span>
                  </div>
               </div>
           </div>
           
           <!-- SCREEN 2: MESSAGES (Active Chat) -->
           <div id="chat-screen-msg" style="position: absolute; inset: 0; display: flex; flex-direction: column; z-index: 1; background: #fff; opacity: 0; pointer-events: none;">
               
               <!-- White Header -->
               <div style="background: #fff; padding: 12px 16px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #efefef;">
                  <div style="width: 32px; height: 32px; border-radius: 8px; border: 1px solid #efefef; display: flex; justify-content: center; align-items: center; color: #666;">
                     <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"></polyline></svg>
                  </div>
                  <div style="display: flex; align-items: center; gap: 10px; flex: 1; margin-left: 12px;">
                     <div style="width: 36px; height: 36px; background: linear-gradient(135deg, #7b2cbf, #5a189a); border-radius: 50%; display: flex; justify-content: center; align-items: center; box-shadow: 0 4px 8px rgba(123,44,191,0.3);">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.5"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path></svg>
                     </div>
                     <div style="text-align: left;">
                        <div style="font-weight: 700; font-size: 14px; font-family: 'Inter', sans-serif; color: #111;">HABITIQ</div>
                        <div style="font-size: 11px; color: #888;">Online</div>
                     </div>
                  </div>
                  <div style="width: 32px; height: 32px; border-radius: 8px; border: 1px solid #efefef; display: flex; justify-content: center; align-items: center; color: #666;">
                     <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="1"></circle><circle cx="12" cy="5" r="1"></circle><circle cx="12" cy="19" r="1"></circle></svg>
                  </div>
               </div>
               
               <!-- Chat Body -->
               <div style="flex: 1; padding: 16px; overflow-y: hidden; display: flex; flex-direction: column; justify-content: flex-end; position: relative;">
                  <div id="dynamic-chat-content" style="display: flex; flex-direction: column; gap: 12px;">
                     <!-- Messages injected via JS -->
                  </div>
               </div>
               
               <!-- Input Area -->
               <div style="padding: 12px 16px; background: #fbfbfd; border-top: 1px solid #efefef; display: flex; flex-direction: column; gap: 8px;">
                  <div style="background: #fff; border-radius: 20px; padding: 8px 12px; border: 1px solid #efefef; display: flex; align-items: center;">
                     <div style="flex: 1; font-size: 13px; color: #888; text-align: left;">Ask me anything</div>
                     <div style="display: flex; gap: 6px;">
                        <div style="width: 28px; height: 28px; border-radius: 50%; border: 1px solid #efefef; display: flex; justify-content: center; align-items: center; color: #555;">
                           <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="23"></line><line x1="8" y1="23" x2="16" y2="23"></line></svg>
                        </div>
                        <div style="width: 28px; height: 28px; border-radius: 50%; background: #f4f5f9; display: flex; justify-content: center; align-items: center; color: #a1a5b7;">
                           <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
                        </div>
                     </div>
                  </div>
                  <div style="text-align: center; font-size: 10px; color: #888;">
                     Powered by <span style="color: #dc2743; font-weight: 700;">STEPS AI</span>
                  </div>
               </div>
               
           </div>
           
        </div>
    </div>

  </section>
  <style>
    /* Advanced Mesh Gradient Background */
    .advanced-mesh-bg {
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        z-index: 0;
        overflow: hidden;
        background: #fdfdfd;
    }
    .mesh-orb-1 {
        position: absolute;
        top: -15%; left: -5%;
        width: 800px; height: 800px;
        background: radial-gradient(circle, rgba(26,86,219,0.18) 0%, rgba(26,86,219,0) 65%);
        border-radius: 50%;
        filter: blur(60px);
        animation: float1 15s infinite ease-in-out;
    }
    .mesh-orb-2 {
        position: absolute;
        top: 20%; right: -10%;
        width: 900px; height: 900px;
        background: radial-gradient(circle, rgba(123,44,191,0.15) 0%, rgba(123,44,191,0) 65%);
        border-radius: 50%;
        filter: blur(80px);
        animation: float2 20s infinite ease-in-out;
    }
    .mesh-orb-3 {
        position: absolute;
        bottom: -20%; left: 30%;
        width: 1000px; height: 1000px;
        background: radial-gradient(circle, rgba(11,158,88,0.1) 0%, rgba(11,158,88,0) 65%);
        border-radius: 50%;
        filter: blur(100px);
        animation: float3 25s infinite ease-in-out;
    }
    .hero-glass-overlay {
        position: absolute;
        inset: 0;
        background: linear-gradient(180deg, rgba(255,255,255,0.2) 0%, rgba(255,255,255,0.9) 100%);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
    }
    
    @keyframes float1 {
        0%, 100% { transform: translate(0, 0) scale(1); }
        50% { transform: translate(60px, -40px) scale(1.1); }
    }
    @keyframes float2 {
        0%, 100% { transform: translate(0, 0) scale(1); }
        50% { transform: translate(-50px, 60px) scale(0.95); }
    }
    @keyframes float3 {
        0%, 100% { transform: translate(0, 0) scale(1); }
        50% { transform: translate(-40px, -80px) scale(1.05); }
    }

    /* Chat Bubble Styles Tightened */
    .msg-user-container { display: flex; align-items: flex-end; gap: 6px; align-self: flex-end; margin-bottom: 16px; opacity: 0; transform: translateY(10px); }
    .msg-user-bubble { background: #625df5; color: #fff; padding: 10px 14px; border-radius: 12px; border-bottom-right-radius: 4px; font-size: 13px; max-width: 220px; font-weight: 500; text-align: left; }
    .msg-user-avatar { width: 28px; height: 28px; border-radius: 50%; background: #e0e4f5; color: #625df5; display: flex; justify-content: center; align-items: center; }
    
    .msg-bot-container { display: flex; flex-direction: column; align-items: flex-start; gap: 6px; margin-bottom: 12px; opacity: 0; transform: translateY(10px); }
    .msg-bot-header { display: flex; align-items: center; gap: 6px; }
    .msg-bot-avatar { width: 24px; height: 24px; border-radius: 50%; background: url('https://i.pravatar.cc/100?img=11') center/cover; }
    .msg-bot-name { font-size: 12px; color: #444; }
    .msg-bot-bubble { background: #f4f5f7; color: #111; padding: 12px 14px; border-radius: 12px; border-top-left-radius: 4px; font-size: 13px; max-width: 260px; line-height: 1.4; text-align: left; }
    .msg-bot-bubble ul { margin: 6px 0 0 16px; padding: 0; }
    .msg-bot-bubble li { margin-bottom: 2px; }
    
    .typing-indicator { display: flex; gap: 4px; padding: 10px 14px; background: #f4f5f7; border-radius: 12px; border-top-left-radius: 4px; width: fit-content; opacity: 0; }
    .typing-indicator .dot { width: 5px; height: 5px; background: #888; border-radius: 50%; animation: type-dot 1.4s infinite ease-in-out both; }
    .typing-indicator .dot:nth-child(1) { animation-delay: -0.32s; }
    .typing-indicator .dot:nth-child(2) { animation-delay: -0.16s; }
    @keyframes type-dot { 0%, 80%, 100% { transform: scale(0); } 40% { transform: scale(1); } }
    
    /* Typewriter cursor */
    .typing-cursor { border-right: 2px solid #111; animation: blink 1s step-end infinite; }
    @keyframes blink { 50% { border-color: transparent; } }
  </style>
  <script>
    document.addEventListener("DOMContentLoaded", () => {
        gsap.registerPlugin(ScrollTrigger);
        
        let htl = gsap.timeline();
        
        // Initial hero intro
        htl.to(".gsap-fade-up", { opacity: 1, y: 0, duration: 0.8, stagger: 0.1, ease: "power3.out" })
           .to("#hero-main-web", { opacity: 1, y: 0, duration: 1, ease: "power4.out" }, "-=0.4")
           .to("#hero-bg-wa", { opacity: 1, x: 50, duration: 1.5, ease: "power3.out" }, "-=0.8")
           .to("#hero-bg-ig", { opacity: 1, x: -50, duration: 1.5, ease: "power3.out" }, "-=1.2");
           
        // Scroll Parallax for Background Mockups
        gsap.to("#hero-bg-wa", {
            scrollTrigger: { trigger: ".hero-v2", start: "top top", end: "bottom top", scrub: 1 },
            y: -80, rotation: -12, ease: "none"
        });
        gsap.to("#hero-bg-ig", {
            scrollTrigger: { trigger: ".hero-v2", start: "top top", end: "bottom top", scrub: 1 },
            y: -100, rotation: 12, ease: "none"
        });
           
        // Define industries data
        const industries = [
            {
                query: "ABOUT PRODUCT",
                botResponse: `I found <b>general market context</b> about <b>Habitiq</b>, including:
                              <ul>
                                <li>Market size and growth</li>
                                <li>Key players in India</li>
                              </ul>`
            },
            {
                query: "WHERE IS MY ORDER?",
                botResponse: `Your order <b>#8842</b> is out for delivery. It will arrive today between <b>4:00 PM and 6:00 PM</b> via FedEx.`
            },
            {
                query: "BOOK A DEMO",
                botResponse: `Great! I have available slots on <b>Tuesday</b>. Would you prefer morning or afternoon?`
            }
        ];
        
        const homeTypewriterEl = document.getElementById('home-typewriter');
        const homeSendBtn = document.getElementById('home-send-btn');
        const chatContentEl = document.getElementById('dynamic-chat-content');
        
        const screenHome = document.getElementById('chat-screen-home');
        const screenMsg = document.getElementById('chat-screen-msg');
        
        let currentIndustryIndex = 0;
        let isAnimating = false;
        let ctl = null;
        
        function resetToHomeScreen() {
            if(ctl) { ctl.kill(); ctl = null; }
            screenHome.style.opacity = 1;
            screenHome.style.zIndex = 2;
            screenMsg.style.opacity = 0;
            screenMsg.style.zIndex = 1;
            
            homeTypewriterEl.innerHTML = "Ask me anything";
            homeTypewriterEl.classList.remove('typing-cursor');
            homeTypewriterEl.style.color = "#888";
            homeSendBtn.style.background = "#f4f5f7";
            homeSendBtn.style.color = "#444";
            isAnimating = false;
        }
        
        function playIndustryScenario(index) {
            isAnimating = true;
            const data = industries[index % industries.length];
            
            resetToHomeScreen();
            isAnimating = true;
            
            homeTypewriterEl.innerHTML = "";
            homeTypewriterEl.classList.add('typing-cursor');
            homeTypewriterEl.style.color = "#111";
            
            chatContentEl.innerHTML = `
                <div class="msg-user-container" id="msg-u">
                   <div style="display:flex; flex-direction:column; align-items:flex-end; gap:4px;">
                     <span style="font-size:11px; color:#888; margin-right:6px;">You</span>
                     <div class="msg-user-bubble">${data.query}</div>
                   </div>
                   <div class="msg-user-avatar">
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                   </div>
                </div>
                
                <div class="msg-bot-container" id="msg-b">
                   <div class="msg-bot-header">
                      <div class="msg-bot-avatar"></div>
                      <span class="msg-bot-name">Product Guide</span>
                   </div>
                   <div class="typing-indicator" id="msg-t"><div class="dot"></div><div class="dot"></div><div class="dot"></div></div>
                   <div class="msg-bot-bubble" id="msg-r" style="display:none;">${data.botResponse}</div>
                </div>
            `;
            
            let queryText = data.query;
            ctl = gsap.timeline();
            
            // Wait 1s so user sees the home screen state
            ctl.to({}, { duration: 1 });
            
            // Type out query FAST
            ctl.to(homeTypewriterEl, { 
                duration: queryText.length * 0.03, 
                text: queryText,
                ease: "none",
                onUpdate: function() {
                    homeTypewriterEl.innerHTML = queryText.substring(0, Math.round(this.progress() * queryText.length));
                }
            });
            
            // Highlight send button
            ctl.call(() => { 
                homeTypewriterEl.classList.remove('typing-cursor');
                homeSendBtn.style.background = "#625df5";
                homeSendBtn.style.color = "#fff";
            }, null, "+=0.1");
            
            // Instant Crossfade to Messages Screen
            ctl.to(screenHome, { opacity: 0, duration: 0.3, ease: "power2.inOut" }, "+=0.2")
               .to(screenMsg, { opacity: 1, duration: 0.3, ease: "power2.inOut" }, "<")
               .call(() => {
                   screenHome.style.zIndex = 1;
                   screenMsg.style.zIndex = 2;
               });
               
            // Show user bubble pop in
            ctl.to("#msg-u", { opacity: 1, y: 0, duration: 0.3, ease: "back.out(1.2)" }, "+=0.1");
               
            // Show typing indicator
            ctl.to("#msg-b", { opacity: 1, y: 0, duration: 0.3, ease: "power3.out" }, "+=0.2")
               .to("#msg-t", { opacity: 1, duration: 0.1 });
               
            // Swap typing for response (FAST)
            ctl.call(() => {
                document.getElementById('msg-t').style.display = 'none';
                document.getElementById('msg-r').style.display = 'block';
            }, null, "+=0.8");
            
            // NO AUTO-FADEOUT! 
            // It stays on the chat indefinitely until the user scrolls away!
        }
        
        // Use IntersectionObserver to play animations ONLY when widget is in view
        // and reset/switch industries when it leaves view.
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    if (!isAnimating) {
                        playIndustryScenario(currentIndustryIndex);
                    }
                } else {
                    if (isAnimating) {
                        // Kill current animation timeline
                        if(ctl) { ctl.kill(); }
                        // Increment industry
                        currentIndustryIndex++;
                        // Reset instantly to home screen so it's ready for next scroll-in
                        resetToHomeScreen();
                    }
                }
            });
        }, { threshold: 0.2 });
        
        // Start observing after initial intro delay
        setTimeout(() => {
            observer.observe(document.getElementById('hero-main-web'));
        }, 2000);
    });
  </script>
\"\"\"
"""

start_marker = 'CUSTOM_HOME_HERO = """'
end_marker = 'CUSTOM_FOUR_AGENTS = """'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + CUSTOM_HOME_HERO_V8 + "\n" + content[end_idx:]
    with open('build_v11_compiler.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Injected V8 Centered Hero with Advanced Animated Background")
else:
    print("Could not find markers for hero replacement.")
