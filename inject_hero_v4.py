import os

with open('build_v11_compiler.py', 'r', encoding='utf-8') as f:
    content = f.read()

# We will replace the entire hero section with V4 which includes the dynamic chat widget logic

CUSTOM_HOME_HERO_V4 = """
CUSTOM_HOME_HERO = \"\"\"
  <!-- S01 Landing Hero - Centered with Dynamic Chat Widget -->
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
    <div id="hero-main-web" class="gsap-fade-up" style="position: relative; z-index: 5; margin-top: 80px; width: 100%; max-width: 400px; opacity: 0; transform: translateY(100px);">
        
        <!-- Real Chat Widget Mockup container -->
        <div style="width: 100%; background: #fbfbfd; border-radius: 24px; box-shadow: 0 32px 80px rgba(0,0,0,0.15); border: 1px solid var(--border-subtle); overflow: hidden; display: flex; flex-direction: column; height: 500px; position: relative;">
           
           <!-- SCREEN 1: HOME -->
           <div id="chat-screen-home" style="position: absolute; inset: 0; display: flex; flex-direction: column; z-index: 2; background: #fbfbfd; transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);">
               <div style="background: linear-gradient(180deg, #24252e 0%, #17181e 100%); padding: 24px 20px 32px; position: relative; text-align: center;">
                  <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 24px;">
                     <div style="width: 36px; height: 36px; background: linear-gradient(135deg, #7b2cbf, #5a189a); border-radius: 8px; display: flex; justify-content: center; align-items: center;">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.5"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path></svg>
                     </div>
                     <div style="width: 32px; height: 32px; border-radius: 50%; background: rgba(255,255,255,0.15); display: flex; justify-content: center; align-items: center; color: #fff;">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
                     </div>
                  </div>
                  <h3 style="margin: 0 0 8px; font-size: 26px; font-family: 'Inter', sans-serif; font-weight: 800; color: #fff;">Hi there 👋</h3>
                  <p style="margin: 0; font-size: 15px; color: rgba(255,255,255,0.8);">How can I help you today</p>
               </div>
               <div style="padding: 0 20px; position: relative; margin-top: -26px;">
                  <div style="background: #fff; border-radius: 20px; padding: 18px 24px; display: flex; align-items: center; justify-content: space-between; box-shadow: 0 8px 24px rgba(0,0,0,0.06); border: 1px solid #efefef;">
                     <div style="color: #111; font-size: 16px; font-weight: 500;">Ask me anything</div>
                     <div style="width: 36px; height: 36px; border-radius: 50%; background: #f4f5f7; display: flex; justify-content: center; align-items: center; color: #444;">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
                     </div>
                  </div>
               </div>
               <div style="flex: 1;"></div>
               <div style="background: #fff; border-top: 1px solid #efefef; display: flex; padding: 12px 0;">
                  <div style="flex: 1; display: flex; flex-direction: column; align-items: center; gap: 4px; color: #111; border-right: 1px solid #efefef;">
                     <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
                     <span style="font-size: 13px; font-weight: 600;">Home</span>
                  </div>
                  <div style="flex: 1; display: flex; flex-direction: column; align-items: center; gap: 4px; color: #999;">
                     <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
                     <span style="font-size: 13px; font-weight: 500;">Messages</span>
                  </div>
               </div>
           </div>
           
           <!-- SCREEN 2: MESSAGES (Active Chat) -->
           <div id="chat-screen-msg" style="position: absolute; inset: 0; display: flex; flex-direction: column; z-index: 1; background: #fff; transform: translateX(100%); transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);">
               
               <!-- White Header -->
               <div style="background: #fff; padding: 16px 20px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #efefef;">
                  <div style="width: 36px; height: 36px; border-radius: 8px; border: 1px solid #efefef; display: flex; justify-content: center; align-items: center; color: #666;">
                     <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"></polyline></svg>
                  </div>
                  <div style="display: flex; align-items: center; gap: 12px; flex: 1; margin-left: 16px;">
                     <div style="width: 44px; height: 44px; background: linear-gradient(135deg, #7b2cbf, #5a189a); border-radius: 50%; display: flex; justify-content: center; align-items: center;">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.5"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path></svg>
                     </div>
                     <div>
                        <div style="font-weight: 700; font-size: 16px; font-family: 'Inter', sans-serif; color: #111;">HABITIQ</div>
                        <div style="font-size: 12px; color: #888;">Online</div>
                     </div>
                  </div>
                  <div style="width: 36px; height: 36px; border-radius: 8px; border: 1px solid #efefef; display: flex; justify-content: center; align-items: center; color: #666;">
                     <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="1"></circle><circle cx="12" cy="5" r="1"></circle><circle cx="12" cy="19" r="1"></circle></svg>
                  </div>
               </div>
               
               <!-- Chat Body -->
               <div style="flex: 1; padding: 24px 20px; overflow-y: hidden; display: flex; flex-direction: column; justify-content: flex-end; position: relative;">
                  
                  <div id="dynamic-chat-content" style="display: flex; flex-direction: column; gap: 16px;">
                     <!-- Messages injected via JS -->
                  </div>
                  
               </div>
               
               <!-- Input Area -->
               <div style="padding: 16px 20px; background: #fbfbfd; border-top: 1px solid #efefef; display: flex; flex-direction: column; gap: 12px;">
                  <div style="background: #fff; border-radius: 20px; padding: 12px 16px; border: 1px solid #efefef; display: flex; align-items: center;">
                     <div id="dynamic-typewriter" style="flex: 1; font-size: 15px; color: #111; border-right: 1px solid transparent;">Ask me anything</div>
                     <div style="display: flex; gap: 8px;">
                        <div style="width: 36px; height: 36px; border-radius: 50%; border: 1px solid #efefef; display: flex; justify-content: center; align-items: center; color: #555;">
                           <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="23"></line><line x1="8" y1="23" x2="16" y2="23"></line></svg>
                        </div>
                        <div style="width: 36px; height: 36px; border-radius: 50%; background: #f4f5f9; display: flex; justify-content: center; align-items: center; color: #a1a5b7;">
                           <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
                        </div>
                     </div>
                  </div>
                  <div style="text-align: center; font-size: 11px; color: #888;">
                     Powered by <span style="color: #dc2743; font-weight: 700;">STEPS AI</span>
                  </div>
               </div>
               
           </div>
           
        </div>
    </div>

  </section>
  <style>
    /* Chat Bubble Styles */
    .msg-user-container { display: flex; align-items: flex-end; gap: 8px; align-self: flex-end; margin-bottom: 24px; opacity: 0; transform: translateY(10px); }
    .msg-user-bubble { background: #625df5; color: #fff; padding: 12px 16px; border-radius: 12px; border-bottom-right-radius: 4px; font-size: 14px; max-width: 240px; font-weight: 500; }
    .msg-user-avatar { width: 32px; height: 32px; border-radius: 50%; background: #e0e4f5; color: #625df5; display: flex; justify-content: center; align-items: center; }
    
    .msg-bot-container { display: flex; flex-direction: column; align-items: flex-start; gap: 8px; margin-bottom: 16px; opacity: 0; transform: translateY(10px); }
    .msg-bot-header { display: flex; align-items: center; gap: 8px; }
    .msg-bot-avatar { width: 28px; height: 28px; border-radius: 50%; background: url('https://i.pravatar.cc/100?img=11') center/cover; }
    .msg-bot-name { font-size: 13px; color: #444; }
    .msg-bot-bubble { background: #f4f5f7; color: #111; padding: 16px; border-radius: 12px; border-top-left-radius: 4px; font-size: 14px; max-width: 300px; line-height: 1.5; }
    .msg-bot-bubble ul { margin: 8px 0 0 20px; padding: 0; }
    .msg-bot-bubble li { margin-bottom: 4px; }
    
    .typing-indicator { display: flex; gap: 4px; padding: 12px 16px; background: #f4f5f7; border-radius: 12px; border-top-left-radius: 4px; width: fit-content; opacity: 0; }
    .typing-indicator .dot { width: 6px; height: 6px; background: #888; border-radius: 50%; animation: type-dot 1.4s infinite ease-in-out both; }
    .typing-indicator .dot:nth-child(1) { animation-delay: -0.32s; }
    .typing-indicator .dot:nth-child(2) { animation-delay: -0.16s; }
    @keyframes type-dot { 0%, 80%, 100% { transform: scale(0); } 40% { transform: scale(1); } }
    
    /* Typewriter cursor */
    .typing-cursor { border-right: 2px solid #111; animation: blink 1s step-end infinite; }
    @keyframes blink { 50% { border-color: transparent; } }
  </style>
  <script>
    document.addEventListener("DOMContentLoaded", () => {
        let htl = gsap.timeline();
        
        // Initial hero intro
        htl.to(".gsap-fade-up", { opacity: 1, y: 0, duration: 0.8, stagger: 0.1, ease: "power3.out" })
           .to("#hero-main-web", { opacity: 1, y: 0, duration: 1, ease: "power4.out" }, "-=0.4")
           .to("#hero-bg-wa", { opacity: 1, x: 50, duration: 1.5, ease: "power3.out" }, "-=0.8")
           .to("#hero-bg-ig", { opacity: 1, x: -50, duration: 1.5, ease: "power3.out" }, "-=1.2");
           
        // After 2 seconds, slide to messages screen
        htl.to("#chat-screen-home", { x: "-100%", duration: 0.6, ease: "power3.inOut" }, "+=2")
           .to("#chat-screen-msg", { x: "0%", duration: 0.6, ease: "power3.inOut" }, "<");
           
        // Define industries data
        const industries = [
            {
                query: "ABOUT PRODUCT",
                botResponse: `I found <b>general market/product context</b> about <b>Habitiq</b> and the <b>flatmate/PG discovery market</b>, including:
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
        
        const typeWriterEl = document.getElementById('dynamic-typewriter');
        const chatContentEl = document.getElementById('dynamic-chat-content');
        
        function playIndustryLoop(index) {
            const data = industries[index % industries.length];
            
            // Reset chat content
            chatContentEl.innerHTML = `
                <div class="msg-user-container" id="msg-u">
                   <div style="display:flex; flex-direction:column; align-items:flex-end; gap:4px;">
                     <span style="font-size:12px; color:#888; margin-right:8px;">You</span>
                     <div class="msg-user-bubble">${data.query}</div>
                   </div>
                   <div class="msg-user-avatar">
                      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
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
            
            typeWriterEl.innerHTML = "";
            typeWriterEl.classList.add('typing-cursor');
            
            let queryText = data.query;
            let ctl = gsap.timeline({ onComplete: () => {
                setTimeout(() => playIndustryLoop(index + 1), 4000);
            }});
            
            // 1. Type out query
            ctl.to(typeWriterEl, { 
                duration: queryText.length * 0.05, 
                text: queryText,
                ease: "none",
                onUpdate: function() {
                    typeWriterEl.innerHTML = queryText.substring(0, Math.round(this.progress() * queryText.length));
                }
            }, "+=1");
            
            // 2. Submit query (clear box, show user bubble)
            ctl.call(() => { 
                typeWriterEl.innerHTML = "Ask me anything"; 
                typeWriterEl.classList.remove('typing-cursor'); 
                typeWriterEl.style.color = "#888";
            }, null, "+=0.2")
               .to("#msg-u", { opacity: 1, y: 0, duration: 0.4, ease: "power3.out" });
               
            // 3. Show typing indicator
            ctl.to("#msg-b", { opacity: 1, y: 0, duration: 0.4, ease: "power3.out" }, "+=0.3")
               .to("#msg-t", { opacity: 1, duration: 0.2 });
               
            // 4. Swap typing for response
            ctl.call(() => {
                document.getElementById('msg-t').style.display = 'none';
                document.getElementById('msg-r').style.display = 'block';
            }, null, "+=1.5")
            // 5. Fade out entire chat to repeat
            .to(chatContentEl, { opacity: 0, duration: 0.5, ease: "power2.inOut" }, "+=3")
            .call(() => {
                chatContentEl.style.opacity = 1;
                typeWriterEl.style.color = "#111";
            });
        }
        
        // Start loop after messages screen is visible
        setTimeout(() => playIndustryLoop(0), 3000);
    });
  </script>
\"\"\"
"""

start_marker = 'CUSTOM_HOME_HERO = """'
end_marker = 'CUSTOM_FOUR_AGENTS = """'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + CUSTOM_HOME_HERO_V4 + "\n" + content[end_idx:]
    with open('build_v11_compiler.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Injected V4 Centered Hero with Dynamic Chat Loop")
else:
    print("Could not find markers for hero replacement.")
