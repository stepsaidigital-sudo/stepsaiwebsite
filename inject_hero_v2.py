import os

with open('build_v11_compiler.py', 'r', encoding='utf-8') as f:
    content = f.read()

CUSTOM_HOME_HERO_V3 = """
CUSTOM_HOME_HERO = \"\"\"
  <!-- S01 Landing Hero - Centered with 3 Mockups -->
  <section class="hero-v2 centered-hero" style="position: relative; padding-top: 180px; padding-bottom: 0px; overflow: hidden; display: flex; flex-direction: column; align-items: center; text-align: center; max-width: 1400px; margin: 0 auto; min-height: 100vh;">
    <div class="hero-bg-glow" style="position: absolute; top: -20%; left: 50%; transform: translateX(-50%); width: 800px; height: 800px; background: radial-gradient(circle, rgba(26,86,219,0.15) 0%, transparent 70%); z-index: 0; pointer-events: none;"></div>
    
    <!-- Floating Background Mockups -->
    <div id="hero-bg-wa" style="position: absolute; left: -120px; top: 15%; transform: translateY(-50%) rotate(-8deg); z-index: 0; opacity: 0; filter: blur(2px); transition: filter 0.5s;" onmouseover="this.style.filter='blur(0)'" onmouseout="this.style.filter='blur(2px)'">
        <div class="phone-mockup" style="transform: scale(0.75);">
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
    
    <div id="hero-bg-ig" style="position: absolute; right: -120px; top: 25%; transform: translateY(-50%) rotate(8deg); z-index: 0; opacity: 0; filter: blur(2px); transition: filter 0.5s;" onmouseover="this.style.filter='blur(0)'" onmouseout="this.style.filter='blur(2px)'">
        <div class="phone-mockup" style="transform: scale(0.75);">
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
    <div style="position: relative; z-index: 10; max-width: 800px; display: flex; flex-direction: column; align-items: center; width: 100%;">
      <span class="kicker gsap-fade-up" style="font-family: 'Geist Mono', monospace; font-size: 11px; font-weight: 500; color: var(--accent); letter-spacing: .24em; text-transform: uppercase; margin-bottom: 24px; display:block;">AI AGENT FOR SALES & SUPPORT</span>
      
      <h1 class="gsap-fade-up" style="font-family: 'Outfit'; font-size: clamp(56px, 8vw, 96px); margin-bottom: 24px; line-height: 1.05; letter-spacing: -0.03em; color: var(--text-primary); font-weight: 700;">It answers.<br>Then it acts.</h1>
      
      <p class="gsap-fade-up" style="font-size: clamp(18px, 2vw, 22px); color: var(--text-secondary); margin-bottom: 48px; max-width: 640px; line-height: 1.5;">StepsAI answers customer questions on WhatsApp, Instagram and your website. Then it books the meeting, saves the lead, or updates the order. Nobody on your team has to be awake for it.</p>
      
      <div class="hero-actions gsap-fade-up" style="display:flex; gap:16px; flex-wrap: wrap; justify-content: center; align-items: center;">
        <a href="./partners/apply/index.html" style="text-decoration: none;">
           <button class="btn-primary" style="padding: 16px 36px; font-size: 18px; border-radius: 100px; display: flex; align-items: center; gap: 8px;">
              Start Free Trial 
              <span style="background: rgba(255,255,255,0.2); padding: 4px 8px; border-radius: 6px; font-size: 12px; font-family: 'Geist Mono', monospace; margin-left: 8px;">ENTER ↵</span>
           </button>
        </a>
        <button class="btn-outline" style="padding: 16px 36px; font-size: 18px; border-radius: 100px;">Book an Appointment</button>
      </div>
      
      <div class="gsap-fade-up" style="margin-top: 24px; font-size: 14px; color: var(--text-tertiary); display: flex; align-items: center; gap: 12px; font-weight: 500;">
         <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#0B9E58" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> No credit card required
         <span style="color: var(--border-subtle);">&bull;</span>
         Works with Shopify, HubSpot, Calendly and your inbox.
      </div>
    </div>
    
    <!-- Main Center Web Chat Mockup -->
    <div id="hero-main-web" class="gsap-fade-up" style="position: relative; z-index: 5; margin-top: 80px; width: 100%; max-width: 800px; opacity: 0; transform: translateY(100px);">
        <!-- Browser Window Mockup -->
        <div style="background: #fff; border-radius: 16px 16px 0 0; border: 1px solid var(--border-subtle); border-bottom: none; box-shadow: 0 -20px 40px rgba(0,0,0,0.05); overflow: hidden; display: flex; flex-direction: column;">
            <!-- Browser Header -->
            <div style="background: #f4f5f7; height: 48px; border-bottom: 1px solid var(--border-subtle); display: flex; align-items: center; padding: 0 16px; gap: 8px;">
                <div style="width: 12px; height: 12px; border-radius: 50%; background: #ff5f56;"></div>
                <div style="width: 12px; height: 12px; border-radius: 50%; background: #ffbd2e;"></div>
                <div style="width: 12px; height: 12px; border-radius: 50%; background: #27c93f;"></div>
                <div style="flex: 1; display: flex; justify-content: center;">
                    <div style="background: #fff; border-radius: 6px; padding: 4px 64px; font-size: 11px; color: #888; font-family: 'Geist Mono', monospace; border: 1px solid #e0e4e8;">yourwebsite.com</div>
                </div>
            </div>
            
            <!-- Web Chat Interface -->
            <div style="background: #fbfbfd; height: 400px; position: relative; padding: 40px; display: flex; flex-direction: column; align-items: flex-end; justify-content: flex-end;">
               
               <!-- Floating Web Widget -->
               <div style="width: 380px; background: #fff; border-radius: 20px; box-shadow: 0 12px 40px rgba(0,0,0,0.1); border: 1px solid var(--border-subtle); overflow: hidden; display: flex; flex-direction: column; transform-origin: bottom right; animation: float-in 1s cubic-bezier(0.16, 1, 0.3, 1) forwards; animation-delay: 1.5s; opacity: 0;">
                  <div style="background: var(--accent); padding: 24px; color: #fff;">
                     <h3 style="margin: 0; font-size: 18px; font-family: 'Outfit'; font-weight: 600;">Chat with us</h3>
                     <p style="margin: 4px 0 0; font-size: 13px; opacity: 0.8;">We typically reply instantly.</p>
                  </div>
                  <div style="padding: 20px; background: #fbfbfd; display: flex; flex-direction: column; gap: 12px; height: 280px; overflow-y: auto;">
                     <div class="chat-bubble out ig-in" style="align-self: flex-start; color: #111; text-align: left;">Hi there! Can I help you find anything?</div>
                     <div class="chat-bubble in ig-in" style="align-self: flex-end; background: var(--accent); color: #fff; text-align: right;">Do you offer enterprise plans?</div>
                     <div class="chat-bubble out ig-in" style="align-self: flex-start; color: #111; text-align: left;">Yes, we do. Our enterprise plans start at $499/mo and include custom integrations. Would you like me to book a demo for you?</div>
                  </div>
                  <div style="padding: 16px; border-top: 1px solid var(--border-subtle); background: #fff; display: flex; align-items: center; gap: 12px;">
                     <div style="flex: 1; background: #f4f5f7; border-radius: 100px; padding: 10px 16px; font-size: 14px; color: #888;">Type your message...</div>
                     <div style="width: 36px; height: 36px; border-radius: 50%; background: var(--accent); display: flex; align-items: center; justify-content: center; color: #fff;">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
                     </div>
                  </div>
               </div>
               
               <!-- Widget Launcher Button -->
               <div style="width: 64px; height: 64px; border-radius: 50%; background: var(--accent); position: absolute; bottom: 40px; right: 40px; box-shadow: 0 8px 24px rgba(26,86,219,0.3); display: flex; align-items: center; justify-content: center; color: #fff; z-index: -1;">
                  <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
               </div>
            </div>
        </div>
    </div>

  </section>
  <style>
    @keyframes float-in {
        0% { opacity: 0; transform: scale(0.9) translateY(20px); }
        100% { opacity: 1; transform: scale(1) translateY(0); }
    }
  </style>
  <script>
    document.addEventListener("DOMContentLoaded", () => {
        let htl = gsap.timeline();
        htl.to(".gsap-fade-up", { opacity: 1, y: 0, duration: 0.8, stagger: 0.1, ease: "power3.out" })
           .to("#hero-main-web", { opacity: 1, y: 0, duration: 1, ease: "power4.out" }, "-=0.4")
           .to("#hero-bg-wa", { opacity: 1, x: 50, duration: 1.5, ease: "power3.out" }, "-=0.8")
           .to("#hero-bg-ig", { opacity: 1, x: -50, duration: 1.5, ease: "power3.out" }, "-=1.2");
    });
  </script>
\"\"\"
"""

start_marker = 'CUSTOM_HOME_HERO = """'
end_marker = 'CUSTOM_FOUR_AGENTS = """'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + CUSTOM_HOME_HERO_V3 + "\n" + content[end_idx:]
    with open('build_v11_compiler.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Injected V3 Centered Hero")
else:
    print("Could not find markers for hero replacement.")
