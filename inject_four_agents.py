import re

with open('build_v11_compiler.py', 'r', encoding='utf-8') as f:
    content = f.read()

CUSTOM_FOUR_AGENTS = """CUSTOM_FOUR_AGENTS = \"\"\"
    <section class="section-v2 four-agents-section" style="padding-top: 160px; padding-bottom: 120px; position: relative; overflow: hidden;">
      <!-- Animated Background Mesh (Inspired by Logo Colors: Red #D04859 and Blue #5B6DB0) -->
      <div class="mesh-bg" style="position: absolute; top: -50%; left: -50%; width: 200%; height: 200%; z-index: 0; background: radial-gradient(circle at 50% 50%, rgba(208, 72, 89, 0.06) 0%, transparent 40%), radial-gradient(circle at 80% 20%, rgba(91, 109, 176, 0.06) 0%, transparent 40%), radial-gradient(circle at 20% 80%, rgba(208, 72, 89, 0.04) 0%, transparent 40%); filter: blur(60px); pointer-events: none; opacity:0;"></div>
      
      <div style="text-align: center; margin-bottom: 80px; position: relative; z-index: 1;">
        <span class="gsap-fade-up" style="font-family: 'Geist Mono', monospace; font-size: 12px; color: var(--accent); letter-spacing: .2em; text-transform: uppercase;">FOUR AGENTS, ONE BRAIN</span>
        <h2 class="gsap-fade-up" style="font-family: 'Outfit'; font-size: clamp(40px, 5vw, 56px); margin: 16px 0 24px; color: var(--text-primary);">Four jobs. One memory.</h2>
        <p class="gsap-fade-up" style="font-size: 20px; color: var(--text-secondary); max-width: 700px; margin: 0 auto; line-height: 1.6;">Your support agent knows what your sales agent promised yesterday. That sounds obvious until you have used four separate tools that all forgot.</p>
      </div>
  
      <div class="bento-grid gsap-fade-up" style="grid-template-columns: repeat(2, 1fr); gap: 32px; max-width: 1200px; margin: 0 auto; position: relative; z-index: 1;">
        
        <!-- Sales Agent -->
        <div class="bento-card" style="padding: 48px; background: linear-gradient(145deg, rgba(255, 245, 235, 0.95) 0%, rgba(255, 255, 255, 0.8) 100%); backdrop-filter: blur(20px); border: 1px solid var(--border-subtle); display: flex; flex-direction: column; justify-content: space-between; min-height: 480px; border-radius: 32px; box-shadow: 0 24px 64px rgba(0,0,0,0.03);">
          <div>
            <h3 style="font-family: 'Outfit'; font-size: 32px; margin-bottom: 16px; color: var(--text-primary);">Sales Agent</h3>
            <p style="color: var(--text-secondary); font-size: 16px; line-height: 1.6;">Checks what is actually in stock before it promises anything, then closes.</p>
          </div>
          <div class="micro-mockup sales-mockup" style="background: #EFEAE2; border-radius: 16px; padding: 24px; margin-top: 32px; border: 1px solid rgba(0,0,0,0.05); position: relative; overflow: hidden; display: flex; flex-direction: column; gap: 12px;">
            <div class="sales-msg-1" style="background: #fff; color: #111; padding: 12px 16px; border-radius: 16px; border-bottom-left-radius: 4px; align-self: flex-start; max-width: 90%; font-size: 14px; opacity: 0; transform: translateY(10px); box-shadow: 0 4px 12px rgba(0,0,0,0.05);">Do you have this in large?</div>
            <div class="sales-typing" style="align-self: flex-start; background: #e5dfd6; padding: 8px 16px; border-radius: 16px; opacity: 0; display: flex; gap: 4px; align-items: center; transform: scale(0.9); transform-origin: left bottom;"><span class="dot" style="width:6px;height:6px;background:#aaa;border-radius:50%;display:inline-block;"></span><span class="dot" style="width:6px;height:6px;background:#aaa;border-radius:50%;display:inline-block;"></span><span class="dot" style="width:6px;height:6px;background:#aaa;border-radius:50%;display:inline-block;"></span></div>
            <div class="sales-msg-2" style="background: #DDF3D5; color: #155724; padding: 12px 16px; border-radius: 16px; border-bottom-right-radius: 4px; align-self: flex-end; max-width: 90%; font-size: 14px; opacity: 0; transform: translateY(10px); box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
               <span id="sales-tw"></span><span class="sales-cursor" style="display:inline-block; width:2px; height:14px; background:#155724; margin-left:2px; animation:blink 1s infinite;"></span>
            </div>
            <div class="receipt-pill sales-receipt" style="opacity: 0; transform: scale(0.9); margin: 8px auto 0; background: #fff; padding: 8px 16px; border-radius: 100px; display: flex; align-items: center; gap: 8px; font-size: 12px; font-weight: 600; color: #111; border: 1px solid rgba(11,158,88,0.2); box-shadow: 0 8px 24px rgba(11,158,88,0.1);"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#0B9E58" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg> <span>SHOPIFY</span></div>
          </div>
        </div>
  
        <!-- Lead Agent -->
        <div class="bento-card" style="padding: 48px; background: linear-gradient(145deg, rgba(249, 240, 255, 0.95) 0%, rgba(255, 255, 255, 0.8) 100%); backdrop-filter: blur(20px); border: 1px solid var(--border-subtle); display: flex; flex-direction: column; justify-content: space-between; min-height: 480px; border-radius: 32px; box-shadow: 0 24px 64px rgba(0,0,0,0.03);">
          <div>
            <h3 style="font-family: 'Outfit'; font-size: 32px; margin-bottom: 16px; color: var(--text-primary);">Lead Agent</h3>
            <p style="color: var(--text-secondary); font-size: 16px; line-height: 1.6;">Finds out budget and timeline the way a good salesperson would, then writes it into your CRM.</p>
          </div>
          <div class="micro-mockup lead-mockup" style="background: #fafafa; border-radius: 16px; padding: 24px; margin-top: 32px; border: 1px solid var(--border-subtle); position: relative; overflow: hidden;">
            <div style="font-family: 'Inter'; font-size: 12px; color: var(--text-tertiary); margin-bottom: 12px; text-transform: uppercase; letter-spacing: 1px;">HubSpot CRM</div>
            <div class="lead-hs-card" style="background: #fff; border-radius: 8px; padding: 16px; border-left: 4px solid #ff7a59; box-shadow: 0 4px 12px rgba(0,0,0,0.05); opacity: 0; transform: translateX(20px);">
              <div style="font-weight: 600; color: #111; font-size: 14px;">New Lead: <span id="lead-name-tw" style="color:#ff7a59;"></span><span class="lead-cursor-1" style="display:inline-block; width:2px; height:12px; background:#ff7a59; margin-left:2px; animation:blink 1s infinite;"></span></div>
              <div style="color: var(--text-secondary); font-size: 13px; margin-top: 8px; display: flex; flex-direction: column; gap: 4px;">
                 <div class="lead-budget" style="opacity:0; transform:translateX(10px);">Budget: <strong style="color:#111;">$5k-$10k</strong></div>
                 <div class="lead-timeline" style="opacity:0; transform:translateX(10px);">Timeline: <strong style="color:#111;">Q3</strong></div>
              </div>
            </div>
            <div class="receipt-pill lead-receipt" style="opacity: 0; transform: scale(0.9); margin: 24px auto 0; background: #fff; padding: 8px 16px; border-radius: 100px; display: flex; align-items: center; justify-content: center; gap: 8px; font-size: 12px; font-weight: 600; color: #111; border: 1px solid rgba(255,122,89,0.3); box-shadow: 0 8px 24px rgba(255,122,89,0.15); width: max-content;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#ff7a59" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg> <span>HUBSPOT</span></div>
          </div>
        </div>
  
        <!-- Meetings Agent -->
        <div class="bento-card" style="padding: 48px; background: linear-gradient(145deg, rgba(239, 245, 255, 0.95) 0%, rgba(255, 255, 255, 0.8) 100%); backdrop-filter: blur(20px); border: 1px solid var(--border-subtle); display: flex; flex-direction: column; justify-content: space-between; min-height: 480px; border-radius: 32px; box-shadow: 0 24px 64px rgba(0,0,0,0.03);">
          <div>
            <h3 style="font-family: 'Outfit'; font-size: 32px; margin-bottom: 16px; color: var(--text-primary);">Meetings Agent</h3>
            <p style="color: var(--text-secondary); font-size: 16px; line-height: 1.6;">Offers times that are genuinely free, and puts the meeting in your calendar.</p>
          </div>
          <div class="micro-mockup meet-mockup" style="background: #F9FAFB; border-radius: 16px; padding: 24px; margin-top: 32px; border: 1px solid var(--border-subtle); position: relative; overflow: hidden; display: flex; flex-direction: column; gap: 12px;">
            <div class="meet-msg-1" style="background: #E5E7EB; color: #111; padding: 12px 16px; border-radius: 16px; border-bottom-left-radius: 4px; align-self: flex-start; max-width: 90%; font-size: 14px; opacity: 0; transform: translateY(10px); box-shadow: 0 4px 12px rgba(0,0,0,0.05);">I want to book a site visit.</div>
            
            <div class="meet-cal-card" style="background: #fff; border-radius: 12px; border: 1px solid #eee; padding: 12px; box-shadow: 0 8px 24px rgba(0,0,0,0.05); align-self: center; width: 100%; opacity: 0; transform: translateY(10px);">
               <div style="font-size: 11px; color: #888; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px;">Pick a time</div>
               <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
                  <div style="border: 1px solid #eee; padding: 8px; border-radius: 6px; font-size: 12px; text-align: center; color: #666;">Friday 2 PM</div>
                  <div class="meet-slot-target" style="border: 1px solid #eee; padding: 8px; border-radius: 6px; font-size: 12px; text-align: center; color: #666; position: relative;">Saturday 11 AM
                     <div class="meet-slot-pulse" style="position: absolute; top:0; left:0; right:0; bottom:0; background: rgba(139,92,246,0.3); border-radius: 6px; opacity: 0; transform: scale(1);"></div>
                  </div>
               </div>
            </div>

            <div class="meet-msg-2" style="background: #8B5CF6; color: #fff; padding: 12px 16px; border-radius: 16px; border-bottom-right-radius: 4px; align-self: flex-end; max-width: 90%; font-size: 14px; opacity: 0; transform: translateY(10px); box-shadow: 0 4px 12px rgba(139,92,246,0.2);">Saturday 11 AM works perfectly!</div>
            <div class="receipt-pill meet-receipt" style="opacity: 0; transform: scale(0.9); margin: 8px auto 0; background: #fff; padding: 8px 16px; border-radius: 100px; display: flex; align-items: center; justify-content: center; gap: 8px; font-size: 12px; font-weight: 600; color: #111; border: 1px solid rgba(139,92,246,0.3); box-shadow: 0 8px 24px rgba(139,92,246,0.15); width: max-content;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#8B5CF6" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg> <span>CALENDAR</span></div>
          </div>
        </div>
  
        <!-- Support Agent -->
        <div class="bento-card" style="padding: 48px; background: linear-gradient(145deg, rgba(236, 251, 249, 0.95) 0%, rgba(255, 255, 255, 0.8) 100%); backdrop-filter: blur(20px); border: 1px solid var(--border-subtle); display: flex; flex-direction: column; justify-content: space-between; min-height: 480px; border-radius: 32px; box-shadow: 0 24px 64px rgba(0,0,0,0.03);">
          <div>
            <h3 style="font-family: 'Outfit'; font-size: 32px; margin-bottom: 16px; color: var(--text-primary);">Support Agent</h3>
            <p style="color: var(--text-secondary); font-size: 16px; line-height: 1.6;">Tracks the order, explains the return policy, and only wakes you if something is actually wrong.</p>
          </div>
          <div class="micro-mockup supp-mockup" style="background: #fafafa; border-radius: 16px; padding: 24px; margin-top: 32px; border: 1px solid var(--border-subtle); position: relative; overflow: hidden; display: flex; flex-direction: column; gap: 12px;">
            <div class="supp-msg-1" style="background: #fff; color: #111; padding: 12px 16px; border-radius: 16px; border-bottom-left-radius: 4px; align-self: flex-start; max-width: 90%; font-size: 14px; opacity: 0; transform: translateY(10px); box-shadow: 0 4px 12px rgba(0,0,0,0.05); border: 1px solid #eee;">Where is my order?</div>
            
            <div class="supp-zd-card" style="background: #fff; border-radius: 12px; padding: 16px; border: 1px solid #eee; border-left: 4px solid #00363D; opacity: 0; transform: translateX(-20px); align-self: center; width: 100%; display: flex; align-items: center; justify-content: space-between;">
               <div>
                  <div style="font-size: 12px; color: #666;">Order #8924</div>
                  <div class="supp-status" style="font-weight: 600; color: #111; font-size: 14px; margin-top: 4px;">Processing...</div>
               </div>
               <div class="supp-icon" style="background: #f4f5f7; padding: 8px; border-radius: 50%;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#666" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg></div>
            </div>

            <div class="supp-msg-2" style="background: #f4f5f7; color: #111; padding: 12px 16px; border-radius: 16px; border-bottom-right-radius: 4px; align-self: flex-end; max-width: 90%; font-size: 14px; opacity: 0; transform: translateY(10px); box-shadow: 0 4px 12px rgba(0,0,0,0.05); border: 1px solid #efefef;">It is out for delivery today at 6PM!</div>
            
            <div class="receipt-pill supp-receipt" style="opacity: 0; transform: scale(0.9); margin: 8px auto 0; background: #fff; padding: 8px 16px; border-radius: 100px; display: flex; align-items: center; justify-content: center; gap: 8px; font-size: 12px; font-weight: 600; color: #111; border: 1px solid rgba(0,54,61,0.3); box-shadow: 0 8px 24px rgba(0,54,61,0.15); width: max-content;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#00363D" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg> <span>ZENDESK</span></div>
          </div>
        </div>
  
      </div>
    </section>
\"\"\""""

JS_FOUR_AGENTS = """
    // --- Animated Mesh Gradient Background ---
    gsap.to(".mesh-bg", {
      opacity: 1,
      duration: 2,
      scrollTrigger: { trigger: ".four-agents-section", start: "top 60%" }
    });
    
    // Rotate the mesh gradient slowly
    gsap.to(".mesh-bg", {
      rotation: 360,
      duration: 40,
      repeat: -1,
      ease: "linear",
      transformOrigin: "center center"
    });

    // --- 1. Sales Agent Animation ---
    let salesTl = gsap.timeline({ repeat: -1, repeatDelay: 2, 
      onRepeat: () => {
         let el = document.getElementById("sales-tw"); if(el) el.textContent = "";
      }
    });
    salesTl.to(".sales-msg-1", { opacity: 1, y: 0, duration: 0.4, ease: "power2.out" })
           .to({}, {duration: 0.5})
           .to(".sales-typing", { opacity: 1, scale: 1, duration: 0.2 })
           .to(".sales-typing .dot", { y: -3, duration: 0.2, stagger: 0.1, yoyo: true, repeat: 3 })
           .to(".sales-typing", { opacity: 0, scale: 0.9, duration: 0.2 })
           .to(".sales-msg-2", { opacity: 1, y: 0, duration: 0.4, ease: "power2.out" })
           .add(() => {
              let text = "Yes, two left! Added to cart.";
              let el = document.getElementById("sales-tw");
              let i = 0;
              let interval = setInterval(() => {
                if(i < text.length) {
                  if(el) el.textContent += text.charAt(i);
                  i++;
                } else {
                  clearInterval(interval);
                }
              }, 40);
           })
           .to({}, {duration: 1.5})
           .to(".sales-receipt", { opacity: 1, scale: 1, duration: 0.5, ease: "back.out(2)" });

    // --- 2. Lead Agent Animation ---
    let leadTl = gsap.timeline({ repeat: -1, repeatDelay: 2,
      onRepeat: () => {
         let el = document.getElementById("lead-name-tw"); if(el) el.textContent = "";
      }
    });
    leadTl.to(".lead-hs-card", { opacity: 1, x: 0, duration: 0.6, ease: "power3.out" })
          .add(() => {
              let text = "Sarah Jenkins";
              let el = document.getElementById("lead-name-tw");
              let i = 0;
              let interval = setInterval(() => {
                if(i < text.length) {
                  if(el) el.textContent += text.charAt(i);
                  i++;
                } else {
                  clearInterval(interval);
                }
              }, 60);
          })
          .to({}, {duration: 1.2})
          .to(".lead-budget", { opacity: 1, x: 0, duration: 0.3 })
          .to(".lead-timeline", { opacity: 1, x: 0, duration: 0.3 }, "+=0.2")
          .to({}, {duration: 0.5})
          .to(".lead-receipt", { opacity: 1, scale: 1, duration: 0.5, ease: "back.out(2)" });

    // --- 3. Meetings Agent Animation ---
    let meetTl = gsap.timeline({ repeat: -1, repeatDelay: 2,
      onRepeat: () => {
         let el = document.querySelector(".meet-slot-target");
         if(el) {
            el.style.background = "none";
            el.style.color = "#666";
            el.style.borderColor = "#eee";
            el.style.fontWeight = "normal";
         }
      }
    });
    meetTl.to(".meet-msg-1", { opacity: 1, y: 0, duration: 0.4, ease: "power2.out" })
          .to({}, {duration: 0.5})
          .to(".meet-cal-card", { opacity: 1, y: 0, duration: 0.5, ease: "power2.out" })
          .to({}, {duration: 0.5})
          .add(() => {
             let el = document.querySelector(".meet-slot-target");
             if(el) {
                el.style.background = "rgba(139,92,246,0.1)";
                el.style.color = "#8B5CF6";
                el.style.borderColor = "#8B5CF6";
                el.style.fontWeight = "600";
             }
          })
          .to(".meet-slot-pulse", { opacity: 1, scale: 1.5, duration: 0.4, ease: "power2.out" })
          .to(".meet-slot-pulse", { opacity: 0, duration: 0.2 })
          .to({}, {duration: 0.4})
          .to(".meet-msg-2", { opacity: 1, y: 0, duration: 0.4, ease: "power2.out" })
          .to({}, {duration: 0.5})
          .to(".meet-receipt", { opacity: 1, scale: 1, duration: 0.5, ease: "back.out(2)" });

    // --- 4. Support Agent Animation ---
    let suppTl = gsap.timeline({ repeat: -1, repeatDelay: 2,
      onRepeat: () => {
         let st = document.querySelector(".supp-status"); if(st) { st.textContent = "Processing..."; st.style.color = "#111"; }
         let ic = document.querySelector(".supp-icon svg"); if(ic) { ic.innerHTML = '<path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>'; ic.style.stroke = "#666"; }
         let bg = document.querySelector(".supp-icon"); if(bg) bg.style.background = "#f4f5f7";
         let cd = document.querySelector(".supp-zd-card"); if(cd) cd.style.borderLeftColor = "#00363D";
      }
    });
    suppTl.to(".supp-msg-1", { opacity: 1, y: 0, duration: 0.4, ease: "power2.out" })
          .to({}, {duration: 0.5})
          .to(".supp-zd-card", { opacity: 1, x: 0, duration: 0.5, ease: "power2.out" })
          .to({}, {duration: 0.8})
          // Status change
          .add(() => {
             let st = document.querySelector(".supp-status"); if(st) { st.textContent = "Out for Delivery"; st.style.color = "#0B9E58"; }
             let ic = document.querySelector(".supp-icon svg"); if(ic) { ic.innerHTML = '<polyline points="20 6 9 17 4 12"></polyline>'; ic.style.stroke = "#0B9E58"; }
             let bg = document.querySelector(".supp-icon"); if(bg) bg.style.background = "#E9F8F0";
          })
          .to(".supp-zd-card", { borderLeftColor: "#0B9E58", duration: 0.3 })
          .to({}, {duration: 0.8})
          .to(".supp-msg-2", { opacity: 1, y: 0, duration: 0.4, ease: "power2.out" })
          .to({}, {duration: 0.5})
          .to(".supp-receipt", { opacity: 1, scale: 1, duration: 0.5, ease: "back.out(2)" });
"""

# Replace the CUSTOM_FOUR_AGENTS block safely using regex
pattern = r'CUSTOM_FOUR_AGENTS\s*=\s*\"\"\"[\s\S]*?</section>\s*\"\"\"'
if re.search(pattern, content):
    content = re.sub(pattern, CUSTOM_FOUR_AGENTS, content, count=1)
else:
    print("Regex could not find CUSTOM_FOUR_AGENTS block!")

# Inject JS Logic
script_end = content.find('  </script>\\n</body>')
if script_end != -1:
    content = content[:script_end] + JS_FOUR_AGENTS + "\\n" + content[script_end:]
else:
    # Try finding it without double escape
    script_end = content.find('  </script>\n</body>')
    if script_end != -1:
        content = content[:script_end] + JS_FOUR_AGENTS + "\n" + content[script_end:]
    else:
        print("Could not find closing script tag to inject JS_FOUR_AGENTS!")

with open('build_v11_compiler.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated compiler with animated Four Agents visualization!")
