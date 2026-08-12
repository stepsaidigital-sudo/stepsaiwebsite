import os

with open('build_v11_compiler.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace CUSTOM_SETUP
old_setup_start = content.find('CUSTOM_SETUP = """')

NEW_SETUP = '''CUSTOM_SETUP = """
<section class="section-v2 setup-section" style="padding-top: 160px; max-width: 1400px; margin:0 auto; display:flex; gap:64px; align-items:center;">
  <div style="flex:1;">
    <span class="gsap-fade-up" style="font-family: 'Geist Mono', monospace; font-size: 12px; color: var(--accent); letter-spacing: .2em; text-transform: uppercase; margin-bottom:16px; display:block;">LIVE IN AN AFTERNOON</span>
    <h2 class="gsap-fade-up" style="font-family: 'Outfit'; font-size: clamp(40px, 4vw, 56px); margin: 0 0 24px; color: var(--text-primary); line-height:1.1;">Paste your website link.<br>That is genuinely the hard part.</h2>
    <p class="gsap-fade-up" style="font-size: 18px; color: var(--text-secondary); margin-bottom: 48px; line-height: 1.6; max-width:500px;">Your agent reads your pages and works out what you sell. You check it, change the greeting so it sounds like you, and switch on the channels you want. Most people are finished before their coffee goes cold.</p>
    
    <div class="setup-steps" style="display:flex; flex-direction:column; gap:32px;">
      <div class="gsap-fade-up step-txt-1" style="display:flex; gap:16px; transition:0.3s;">
        <div class="step-num-1" style="width:32px; height:32px; border-radius:50%; background:var(--text-primary); border:1px solid var(--border-subtle); display:flex; align-items:center; justify-content:center; font-weight:700; color:var(--bg-surface); flex-shrink:0; transition:0.3s;">1</div>
        <div>
          <h4 style="font-size:18px; font-weight:700; margin-bottom:8px;">Teach it</h4>
          <p style="color:var(--text-secondary); font-size:15px; line-height:1.5; margin:0;">Paste the link. It reads your site and learns your products, your prices, and your policies.</p>
        </div>
      </div>
      <div class="gsap-fade-up step-txt-2" style="display:flex; gap:16px; opacity:0.4; transition:0.3s;">
        <div class="step-num-2" style="width:32px; height:32px; border-radius:50%; background:var(--bg-surface); border:1px solid var(--border-subtle); display:flex; align-items:center; justify-content:center; font-weight:700; color:var(--text-primary); flex-shrink:0; transition:0.3s;">2</div>
        <div>
          <h4 style="font-size:18px; font-weight:700; margin-bottom:8px;">Make it yours</h4>
          <p style="color:var(--text-secondary); font-size:15px; line-height:1.5; margin:0;">Pick the name, the colour, and the first thing it says. Keep changing the tone until it sounds like someone who works for you.</p>
        </div>
      </div>
      <div class="gsap-fade-up step-txt-3" style="display:flex; gap:16px; opacity:0.4; transition:0.3s;">
        <div class="step-num-3" style="width:32px; height:32px; border-radius:50%; background:var(--bg-surface); border:1px solid var(--border-subtle); display:flex; align-items:center; justify-content:center; font-weight:700; color:var(--text-primary); flex-shrink:0; transition:0.3s;">3</div>
        <div>
          <h4 style="font-size:18px; font-weight:700; margin-bottom:8px;">Connect it</h4>
          <p style="color:var(--text-secondary); font-size:15px; line-height:1.5; margin:0;">Shopify, your calendar, your CRM, your inbox. Each one you connect gives your agent something new it can actually do rather than just talk about.</p>
        </div>
      </div>
    </div>
  </div>
  
  <div style="flex:1; display:flex; justify-content:center; align-items:center; min-width:300px; position:relative; padding: 60px;">
    <!-- Dark Gradient Backdrop for Mockup -->
    <div style="position:absolute; top:0; left:0; width:100%; height:100%; background: linear-gradient(135deg, #060B16 0%, #12264E 100%); border-radius: 40px; z-index: 0;"></div>
    
    <!-- Subtle Inner Glow for Extra Depth -->
    <div style="position:absolute; top:50%; left:50%; transform:translate(-50%, -50%); width:80%; height:80%; background: radial-gradient(circle at center, rgba(61, 116, 236, 0.4) 0%, transparent 70%); filter: blur(60px); z-index: 1; pointer-events: none;"></div>
    
    <!-- Dark Mode Setup Mockup container -->
    <div class="setup-mockup gsap-scale-in" style="width:100%; max-width:460px; height:500px; background:#111; border-radius:24px; border:1px solid #222; box-shadow: 0 24px 64px rgba(0,0,0,0.2); color:#fff; font-family:'Inter', sans-serif; position:relative; overflow:hidden; z-index:2;">
      
      <!-- STEP 1: Connect Website -->
      <div id="setup-step-1" style="position:absolute; inset:32px; display:flex; flex-direction:column; z-index:3;">
          <div style="display:flex; align-items:center; gap:16px; margin-bottom:12px;">
            <div style="width:40px; height:40px; border-radius:12px; background:#222; border:1px solid #333; display:flex; align-items:center; justify-content:center;">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
            </div>
            <h3 style="font-family:'Outfit'; font-size:24px; font-weight:700; margin:0;">Connect your website</h3>
          </div>
          <p style="color:#888; font-size:15px; margin-bottom:32px; line-height:1.5;">Enter your website URL so we can learn about your brand and content.</p>
          
          <div style="margin-bottom:24px;">
            <label style="display:block; font-size:14px; font-weight:500; margin-bottom:12px;">Website URL</label>
            <div style="width:100%; height:52px; background:#1f2228; border:1px solid #3a3f4a; border-radius:12px; padding:0 16px; display:flex; align-items:center; font-family:monospace; font-size:15px; color:#fff; position:relative; overflow:hidden;">
              <span id="typewriter-url"></span><span class="cursor" style="display:inline-block; width:2px; height:18px; background:#fff; margin-left:4px; animation:blink 1s infinite;"></span>
            </div>
            <p style="color:#666; font-size:13px; margin-top:12px;">We'll detect your logo, colors, and content automatically.</p>
          </div>
          
          <div id="mockup-success-state" style="opacity:0; height:0; overflow:hidden; display:flex; flex-direction:column; gap:12px;">
            <div style="background:#1f2228; border:1px solid #3a3f4a; border-radius:12px; padding:16px; display:flex; align-items:center; gap:12px;">
              <div style="width:24px; height:24px; border-radius:50%; background:#fff; color:#111; display:flex; align-items:center; justify-content:center; font-size:14px; font-weight:800;">✓</div>
              <div style="font-size:14px; font-weight:500;">Connected — branding fetched</div>
            </div>
            
            <div style="background:#1f2228; border:1px solid #3a3f4a; border-radius:12px; padding:16px; display:flex; align-items:center; justify-content:space-between;">
              <div>
                <div style="font-size:14px; font-weight:600; margin-bottom:4px;">2 pages found</div>
                <div style="font-size:12px; color:#888;">2 selected · Click to review and edit</div>
              </div>
              <button style="background:transparent; border:1px solid #3a3f4a; color:#fff; border-radius:8px; padding:6px 12px; font-size:13px; font-weight:500;">See all</button>
            </div>
          </div>
          
          <div style="display:flex; justify-content:space-between; align-items:center; margin-top:auto; border-top:1px solid #222; padding-top:24px;">
            <button style="background:transparent; border:1px solid #333; color:#fff; border-radius:8px; padding:12px 24px; font-size:14px; font-weight:500;">Back</button>
            <button id="mockup-proceed-btn" style="background:#333; border:none; color:#888; border-radius:8px; padding:12px 24px; font-size:14px; font-weight:600; transition:all 0.3s;">Connect</button>
          </div>
      </div>
      
      <!-- STEP 2: Make It Yours -->
      <div id="setup-step-2" style="position:absolute; inset:32px; display:flex; flex-direction:column; z-index:2; opacity:0; pointer-events:none;">
          <div style="display:flex; align-items:center; gap:16px; margin-bottom:12px;">
            <div style="width:40px; height:40px; border-radius:12px; background:#222; border:1px solid #333; display:flex; align-items:center; justify-content:center;">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><path d="M12 20h9"></path><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path></svg>
            </div>
            <h3 style="font-family:'Outfit'; font-size:24px; font-weight:700; margin:0;">Make it yours</h3>
          </div>
          <p style="color:#888; font-size:15px; margin-bottom:32px; line-height:1.5;">Customize your agent's personality and appearance.</p>
          
          <div style="margin-bottom:20px;">
            <label style="display:block; font-size:14px; font-weight:500; margin-bottom:8px;">Agent Name</label>
            <div style="width:100%; height:48px; background:#1f2228; border:1px solid #3a3f4a; border-radius:12px; padding:0 16px; display:flex; align-items:center; font-size:15px; color:#fff;">
              <span id="typewriter-name"></span><span class="cursor2" style="display:inline-block; width:2px; height:18px; background:#fff; margin-left:4px; opacity:0; animation:blink 1s infinite;"></span>
            </div>
          </div>
          
          <div style="margin-bottom:20px;">
            <label style="display:block; font-size:14px; font-weight:500; margin-bottom:8px;">Brand Color</label>
            <div style="display:flex; gap:12px;">
              <div class="color-swatch" style="width:36px; height:36px; border-radius:50%; background:#1A56DB; border:2px solid transparent;"></div>
              <div class="color-swatch" id="target-color" style="width:36px; height:36px; border-radius:50%; background:#0B9E58; border:2px solid transparent;"></div>
              <div class="color-swatch" style="width:36px; height:36px; border-radius:50%; background:#E63946; border:2px solid transparent;"></div>
              <!-- Simulated Cursor for Click Animation -->
              <div id="sim-cursor-1" style="position:absolute; width:20px; height:20px; background:rgba(255,255,255,0.8); border-radius:50%; pointer-events:none; opacity:0; z-index:10; top:200px; left:200px; box-shadow:0 0 10px rgba(0,0,0,0.2);"></div>
            </div>
          </div>
          
          <div style="display:flex; justify-content:space-between; align-items:center; margin-top:auto; border-top:1px solid #222; padding-top:24px;">
            <button style="background:transparent; border:1px solid #333; color:#fff; border-radius:8px; padding:12px 24px; font-size:14px; font-weight:500;">Back</button>
            <button id="mockup-proceed-btn-2" style="background:#fff; border:none; color:#111; border-radius:8px; padding:12px 24px; font-size:14px; font-weight:600; transition:all 0.3s;">Next Step</button>
          </div>
      </div>
      
      <!-- STEP 3: Connect It & Go Live -->
      <div id="setup-step-3" style="position:absolute; inset:32px; display:flex; flex-direction:column; z-index:1; opacity:0; pointer-events:none;">
          <div id="step-3-content" style="display:flex; flex-direction:column; height:100%;">
              <div style="display:flex; align-items:center; gap:16px; margin-bottom:12px;">
                <div style="width:40px; height:40px; border-radius:12px; background:#222; border:1px solid #333; display:flex; align-items:center; justify-content:center;">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                </div>
                <h3 style="font-family:'Outfit'; font-size:24px; font-weight:700; margin:0;">Connect Channels</h3>
              </div>
              <p style="color:#888; font-size:15px; margin-bottom:32px; line-height:1.5;">Where should your agent talk to customers?</p>
              
              <div style="display:flex; flex-direction:column; gap:16px;">
                <div style="background:#1f2228; border:1px solid #3a3f4a; border-radius:12px; padding:16px; display:flex; align-items:center; justify-content:space-between;">
                  <div style="display:flex; align-items:center; gap:12px;">
                     <span style="display:inline-block; width:24px; height:24px; border-radius:50%; background:#25D366;"></span> <span style="font-size:15px; font-weight:500;">WhatsApp</span>
                  </div>
                  <div class="toggle-track" id="toggle-wa" style="width:40px; height:24px; background:#333; border-radius:12px; position:relative; transition:0.3s;">
                     <div class="toggle-thumb" style="width:20px; height:20px; background:#888; border-radius:50%; position:absolute; top:2px; left:2px; transition:0.3s;"></div>
                  </div>
                </div>
                
                <div style="background:#1f2228; border:1px solid #3a3f4a; border-radius:12px; padding:16px; display:flex; align-items:center; justify-content:space-between;">
                  <div style="display:flex; align-items:center; gap:12px;">
                     <span style="display:inline-block; width:24px; height:24px; border-radius:6px; background:var(--accent);"></span> <span style="font-size:15px; font-weight:500;">Website Widget</span>
                  </div>
                  <div class="toggle-track" id="toggle-web" style="width:40px; height:24px; background:#333; border-radius:12px; position:relative; transition:0.3s;">
                     <div class="toggle-thumb" style="width:20px; height:20px; background:#888; border-radius:50%; position:absolute; top:2px; left:2px; transition:0.3s;"></div>
                  </div>
                </div>
              </div>
              
              <div id="sim-cursor-2" style="position:absolute; width:20px; height:20px; background:rgba(255,255,255,0.8); border-radius:50%; pointer-events:none; opacity:0; z-index:10; top:300px; left:200px; box-shadow:0 0 10px rgba(0,0,0,0.2);"></div>
              
              <div style="display:flex; justify-content:center; align-items:center; margin-top:auto; padding-top:24px;">
                <button id="mockup-go-live-btn" style="width:100%; background:linear-gradient(45deg, #1A56DB, #0B9E58); border:none; color:#fff; border-radius:12px; padding:16px; font-size:16px; font-weight:700; transition:all 0.3s;">Go Live 🚀</button>
              </div>
          </div>
          
          <!-- SUCCESS SCREEN -->
          <div id="step-success-screen" style="position:absolute; inset:0; background:#111; display:flex; flex-direction:column; align-items:center; justify-content:center; opacity:0; pointer-events:none; z-index:20;">
              <div class="loader-circle" style="width:48px; height:48px; border:4px solid #333; border-top-color:#0B9E58; border-radius:50%; margin-bottom:24px; animation:spin 1s linear infinite;"></div>
              
              <div id="success-content" style="opacity:0; display:flex; flex-direction:column; align-items:center; position:absolute; inset:0; justify-content:center; background:#111;">
                <div id="success-confetti" style="font-size:64px; margin-bottom:16px; transform:scale(0);">🎉</div>
                <h2 style="font-family:'Outfit'; font-size:32px; font-weight:700; margin-bottom:12px; text-align:center; background:linear-gradient(45deg, #1A56DB, #0B9E58); -webkit-background-clip:text; -webkit-text-fill-color:transparent;">Congratulations!</h2>
                <p style="color:#888; text-align:center; line-height:1.5;">Your agent is live and talking to customers.</p>
              </div>
              
              <!-- Web Chat Bubble Pop -->
              <div id="demo-chat-bubble" style="position:absolute; bottom:-120px; right:0; background:#fff; border-radius:16px 16px 0 16px; padding:16px; color:#111; width:260px; box-shadow:0 10px 30px rgba(0,0,0,0.3); border:1px solid #efefef;">
                 <div style="font-size:13px; font-weight:700; color:var(--accent); margin-bottom:4px;">Sales Agent</div>
                 <div style="font-size:14px; line-height:1.4;">Hi! I'm live on your site. How can I help? 👋</div>
              </div>
          </div>
      </div>
      
    </div>
  </div>
</section>
<style>
@keyframes spin { 100% { transform: rotate(360deg); } }
</style>
"""'''

if old_setup_start != -1:
    old_setup_end = content.find('"""', old_setup_start + 20) + 3
    content = content[:old_setup_start] + NEW_SETUP + "\n\n" + content[old_setup_end:]
else:
    acc_idx = content.find('CUSTOM_HOME_ACCORDION = """')
    if acc_idx != -1:
        content = content[:acc_idx] + NEW_SETUP + "\n\n" + content[acc_idx:]

# 2. Replace JS
NEW_JS = """    // Setup Storytelling Animation
    let setupPlayed = false;
    ScrollTrigger.create({
      trigger: ".setup-section",
      start: "top 60%",
      onEnter: () => {
        if(setupPlayed) return;
        setupPlayed = true;
        let setupTl = gsap.timeline({
          repeat: -1,
          repeatDelay: 2,
          onRepeat: () => {
            let urlEl = document.getElementById("typewriter-url");
            if (urlEl) urlEl.textContent = "";
            let btn = document.getElementById("mockup-proceed-btn");
            if (btn) btn.textContent = "Connect";
            let nameEl = document.getElementById("typewriter-name");
            if (nameEl) nameEl.textContent = "";
          }
        });
        
        // --- STEP 1 ---
        let urlText = "https://habitiq.app/";
        let el = document.getElementById("typewriter-url");
        if(el) {
            setupTl.to({}, {duration: 0.5}) // delay
            .add(() => {
              let i = 0;
              let interval = setInterval(() => {
                if(i < urlText.length) { el.textContent += urlText.charAt(i); i++; }
                else { clearInterval(interval); }
              }, 60);
            })
            .to({}, {duration: 1.8}) // wait after typing
            .to("#mockup-success-state", { height: "auto", opacity: 1, duration: 0.6, ease: "power2.out" })
            .to("#mockup-proceed-btn", { background: "#fff", color: "#111", duration: 0.3 }, "<")
            .add(() => { document.getElementById("mockup-proceed-btn").textContent = "Proceed"; }, "<")
            
            // Highlight step 1 text dim
            .to(".step-txt-1", { opacity: 0.4 }, "+=1")
            .to(".step-num-1", { background: "var(--bg-surface)", color: "var(--text-primary)" }, "<")
            
            // Transition to Step 2
            .to("#mockup-proceed-btn", { scale: 0.95, duration: 0.1 })
            .to("#mockup-proceed-btn", { scale: 1, duration: 0.1 })
            .to("#setup-step-1", { opacity: 0, x: -50, duration: 0.4 }, "+=0.2")
            .to("#setup-step-2", { opacity: 1, x: 0, zIndex: 10, duration: 0.4 }, "<")
            .fromTo("#setup-step-2", { x: 50 }, { x: 0, duration: 0.4 }, "<")
            
            // Highlight step 2 text
            .to(".step-txt-2", { opacity: 1 }, "<")
            .to(".step-num-2", { background: "var(--text-primary)", color: "var(--bg-surface)" }, "<")

            // --- STEP 2 ---
            .add(() => {
                let nameEl = document.getElementById("typewriter-name");
                let nameText = "StepsAI Sales Agent";
                let j = 0;
                let c = document.querySelector(".cursor2");
                if(c) c.style.opacity = 1;
                let nameInterval = setInterval(() => {
                if(j < nameText.length) { nameEl.textContent += nameText.charAt(j); j++; }
                else { clearInterval(nameInterval); }
                }, 50);
            })
            .to({}, {duration: 1.5})
            .to("#sim-cursor-1", { opacity: 1, top: "180px", left: "150px", duration: 0.5 }) 
            .to("#sim-cursor-1", { scale: 0.8, duration: 0.1 })
            .to("#target-color", { border: "2px solid #fff", scale: 1.1, duration: 0.2 })
            .to("#sim-cursor-1", { scale: 1, opacity: 0, duration: 0.2 })
            
            // Highlight step 2 text dim
            .to(".step-txt-2", { opacity: 0.4 }, "+=0.5")
            .to(".step-num-2", { background: "var(--bg-surface)", color: "var(--text-primary)" }, "<")

            // Transition to Step 3
            .to("#mockup-proceed-btn-2", { scale: 0.95, duration: 0.1 })
            .to("#mockup-proceed-btn-2", { scale: 1, duration: 0.1 })
            .to("#setup-step-2", { opacity: 0, x: -50, duration: 0.4 }, "+=0.2")
            .to("#setup-step-3", { opacity: 1, zIndex: 10, duration: 0.4 }, "<")
            .fromTo("#setup-step-3", { x: 50 }, { x: 0, duration: 0.4 }, "<")
            
            // Highlight step 3 text
            .to(".step-txt-3", { opacity: 1 }, "<")
            .to(".step-num-3", { background: "var(--text-primary)", color: "var(--bg-surface)" }, "<")

            // --- STEP 3 ---
            .to("#sim-cursor-2", { opacity: 1, top: "140px", left: "380px", duration: 0.5 }, "+=0.5")
            .to("#sim-cursor-2", { scale: 0.8, duration: 0.1 })
            .to("#toggle-wa", { background: "#0B9E58", duration: 0.2 })
            .to("#toggle-wa .toggle-thumb", { left: "18px", background: "#fff", duration: 0.2 }, "<")
            .to("#sim-cursor-2", { scale: 1, top: "220px", left: "380px", duration: 0.4 })
            .to("#sim-cursor-2", { scale: 0.8, duration: 0.1 })
            .to("#toggle-web", { background: "#0B9E58", duration: 0.2 })
            .to("#toggle-web .toggle-thumb", { left: "18px", background: "#fff", duration: 0.2 }, "<")
            .to("#sim-cursor-2", { scale: 1, opacity: 0, duration: 0.2 })

            // Click Go Live
            .to("#mockup-go-live-btn", { scale: 0.95, duration: 0.1 }, "+=0.5")
            .to("#mockup-go-live-btn", { scale: 1, duration: 0.1 })

            // 3 second Loading & Success Screen
            .to("#step-3-content", { opacity: 0, duration: 0.3 }, "+=0.2")
            .to("#step-success-screen", { opacity: 1, duration: 0.3 })
            .to({}, { duration: 2.5 }) // simulate 2.5s loading
            .to(".loader-circle", { opacity: 0, duration: 0.2 })
            .to("#success-content", { opacity: 1, duration: 0.3 })
            .to("#success-confetti", { scale: 1, rotation: 360, duration: 0.8, ease: "back.out(1.5)" }, "<")
            .to("#demo-chat-bubble", { bottom: "32px", duration: 0.6, ease: "back.out(1.2)" }, "+=0.5");
        }
      }
    });\n"""

old_js_start = content.find('    // Setup Storytelling Animation')
if old_js_start != -1:
    old_js_end = content.find('// Analytics Storytelling Animation')
    if old_js_end == -1:
        old_js_end = content.find('  </script>\n</body>')
    content = content[:old_js_start] + NEW_JS + "\n" + content[old_js_end:]
else:
    script_end = content.find('  </script>\n</body>')
    if script_end != -1:
        content = content[:script_end] + NEW_JS + "\n" + content[script_end:]

with open('build_v11_compiler.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected!")
