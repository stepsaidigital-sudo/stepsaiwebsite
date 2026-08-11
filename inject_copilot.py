import os

with open('build_v11_compiler.py', 'r', encoding='utf-8') as f:
    content = f.read()

CUSTOM_COPILOT = """
CUSTOM_COPILOT = \"\"\"
<section class="section-v2 copilot-section" style="padding-top: 160px; padding-bottom: 160px; max-width: 1400px; margin:0 auto; display:flex; gap:64px; align-items:center;">
  <div style="flex:1;">
    <span class="gsap-fade-up" style="font-family: 'Geist Mono', monospace; font-size: 12px; color: var(--accent); letter-spacing: .2em; text-transform: uppercase; margin-bottom:16px; display:block;">INTERNAL COPILOT</span>
    <h2 class="gsap-fade-up" style="font-family: 'Outfit'; font-size: clamp(40px, 4vw, 56px); margin: 0 0 24px; color: var(--text-primary); line-height:1.1;">The same brain, pointed inwards.</h2>
    <p class="gsap-fade-up" style="font-size: 18px; color: var(--text-secondary); margin-bottom: 24px; line-height: 1.6; max-width:500px;">Your team asks it where the leave policy lives, what you agreed with that client in March, which version of the deck is the current one.</p>
    <p class="gsap-fade-up" style="font-size: 18px; color: var(--text-secondary); margin-bottom: 32px; line-height: 1.6; max-width:500px;">It looks through everything you have connected, answers, and shows you exactly which document it got that from.</p>
    
    <a href="#" class="gsap-fade-up" style="display:inline-flex; align-items:center; gap:8px; color:var(--text-primary); font-weight:600; text-decoration:none; border-bottom:1px solid var(--text-primary); padding-bottom:4px;">
       See Internal Copilot
       <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14"></path><path d="M12 5l7 7-7 7"></path></svg>
    </a>
  </div>
  
  <div style="flex:1.2; display:flex; justify-content:center; align-items:center; min-width:300px; position:relative;">
    
    <!-- Copilot Mockup -->
    <div class="copilot-mockup" style="opacity:0; transform:scale(0.9); width:100%; max-width:640px; background:#1f2228; border-radius:24px; border:1px solid #3a3f4a; box-shadow: 0 32px 80px rgba(0,0,0,0.4); padding:32px; display:flex; flex-direction:column; gap:24px; font-family:'Inter', sans-serif;">
       
       <!-- Search Bar -->
       <div style="display:flex; align-items:center; gap:16px; background:#111; border:1px solid #333; border-radius:16px; padding:16px 24px;">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#666" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><path d="M21 21l-4.35-4.35"></path></svg>
          <div style="flex:1; color:#fff; font-size:16px; font-family:'Geist Mono', monospace;">
             <span id="cp-typewriter"></span><span class="cp-cursor" style="display:inline-block; width:2px; height:18px; background:var(--accent); margin-left:4px; animation:blink 1s infinite;"></span>
          </div>
          <div class="cp-enter" style="opacity:0; transform:scale(0.8); background:#333; color:#aaa; font-size:12px; font-weight:600; padding:4px 8px; border-radius:6px; border:1px solid #444;">ENTER</div>
       </div>
       
       <!-- Scanning Animation -->
       <div class="cp-scanning" style="height:0; overflow:hidden; opacity:0; display:flex; flex-direction:column; gap:12px;">
          <div style="display:flex; gap:12px; align-items:center;">
             <div class="cp-spinner" style="width:16px; height:16px; border:2px solid #333; border-top-color:var(--accent); border-radius:50%;"></div>
             <div style="color:#888; font-size:14px; font-family:'Geist Mono', monospace;">Searching internal knowledge base...</div>
          </div>
          <div style="display:flex; gap:8px;">
             <div class="cp-doc doc-1" style="opacity:0; transform:translateY(10px); background:#2A2D35; border:1px solid #3a3f4a; padding:6px 12px; border-radius:8px; font-size:12px; color:#aaa; display:flex; align-items:center; gap:6px;">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#DB4437" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg> Gmail
             </div>
             <div class="cp-doc doc-2" style="opacity:0; transform:translateY(10px); background:#2A2D35; border:1px solid #3a3f4a; padding:6px 12px; border-radius:8px; font-size:12px; color:#aaa; display:flex; align-items:center; gap:6px;">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#0F9D58" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg> Google Drive
             </div>
             <div class="cp-doc doc-3" style="opacity:0; transform:translateY(10px); background:#2A2D35; border:1px solid #3a3f4a; padding:6px 12px; border-radius:8px; font-size:12px; color:#aaa; display:flex; align-items:center; gap:6px;">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#4A154B" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg> Slack
             </div>
          </div>
       </div>
       
       <!-- Answer Result -->
       <div class="cp-result" style="height:0; overflow:hidden; opacity:0; display:flex; flex-direction:column; gap:16px;">
          <div style="background:#2A2D35; border:1px solid #3a3f4a; border-radius:16px; padding:24px; position:relative;">
             <div style="position:absolute; top:-12px; left:24px; background:linear-gradient(45deg, #1A56DB, #8B5CF6); padding:4px 12px; border-radius:100px; font-size:11px; font-weight:700; color:#fff; letter-spacing:0.05em;">ANSWER</div>
             <p style="color:#fff; font-size:15px; line-height:1.6; margin:0; margin-top:8px;">
                We agreed to a <strong style="color:var(--accent);">10% discount on the Enterprise tier</strong> for Acme Corp, starting April 1st. They also requested a custom SLA, which was approved by Legal.
             </p>
             
             <!-- Sources -->
             <div style="margin-top:20px; border-top:1px solid #3a3f4a; padding-top:16px;">
                <div style="font-size:12px; color:#888; font-weight:600; margin-bottom:12px;">SOURCES</div>
                <div style="display:flex; gap:12px; flex-wrap:wrap;">
                   <div style="background:#111; border:1px solid #333; padding:8px 12px; border-radius:8px; display:flex; align-items:center; gap:8px; cursor:pointer;">
                      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#0F9D58" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path></svg>
                      <div>
                         <div style="color:#ddd; font-size:13px; font-weight:500;">Acme_Contract_March.pdf</div>
                         <div style="color:#666; font-size:11px;">Google Drive &bull; Page 4</div>
                      </div>
                   </div>
                   <div style="background:#111; border:1px solid #333; padding:8px 12px; border-radius:8px; display:flex; align-items:center; gap:8px; cursor:pointer;">
                      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#4A154B" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect></svg>
                      <div>
                         <div style="color:#ddd; font-size:13px; font-weight:500;">#legal-approvals</div>
                         <div style="color:#666; font-size:11px;">Slack &bull; Mar 15</div>
                      </div>
                   </div>
                </div>
             </div>
          </div>
       </div>
       
    </div>
  </div>
</section>
\"\"\"
"""

# Inject CUSTOM_COPILOT before CUSTOM_HOME_ACCORDION
acc_idx = content.find('CUSTOM_HOME_ACCORDION = """')
if acc_idx != -1:
    content = content[:acc_idx] + CUSTOM_COPILOT + "\n\n" + content[acc_idx:]

# Inject logic condition in the blocks loop
logic_marker = 'if data["route"] == "" and "Analytics" in block["title"]:\n            html_content += CUSTOM_ANALYTICS\n            continue'
logic_insert = '''
        if data["route"] == "" and "Internal Copilot" in block["title"]:
            html_content += CUSTOM_COPILOT
            continue
'''
if logic_marker in content:
    content = content.replace(logic_marker, logic_marker + "\n" + logic_insert)
else:
    print("Logic marker not found!")

# Inject JS Animation
JS_COPILOT = """
    // Copilot Storytelling Animation
    let copilotPlayed = false;
    ScrollTrigger.create({
      trigger: ".copilot-section",
      start: "top 75%",
      onEnter: () => {
        if(copilotPlayed) return;
        copilotPlayed = true;
        let tl = gsap.timeline();
        
        // 1. Enter mockup
        tl.to(".copilot-mockup", { opacity: 1, scale: 1, duration: 0.8, ease: "power3.out" })
          .to({}, {duration: 0.4})
          
          // 2. Type question
          .add(() => {
              let text = "What did we agree with Acme in March?";
              let el = document.getElementById("cp-typewriter");
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
          .to({}, {duration: 1.8}) // Wait for typing
          
          // 3. Hit Enter
          .to(".cp-enter", { opacity: 1, scale: 1, duration: 0.2, ease: "back.out(2)" })
          .to(".cp-enter", { background: "var(--accent)", color: "#fff", duration: 0.1 })
          .to(".cp-enter", { background: "#333", color: "#aaa", duration: 0.2 }, "+=0.1")
          .add(() => { let c = document.querySelector(".cp-cursor"); if(c) c.style.display="none"; })
          
          // 4. Show scanning
          .to(".cp-scanning", { height: "auto", opacity: 1, duration: 0.4, ease: "power2.out" })
          .to(".doc-1", { opacity: 1, y: 0, duration: 0.3, ease: "back.out" }, "+=0.2")
          .to(".doc-2", { opacity: 1, y: 0, duration: 0.3, ease: "back.out" }, "+=0.2")
          .to(".doc-3", { opacity: 1, y: 0, duration: 0.3, ease: "back.out" }, "+=0.2")
          
          // Animate spinner
          .to(".cp-spinner", { rotation: 720, duration: 2.5, ease: "power1.inOut" }, "<")
          
          // 5. Show Result
          .to(".cp-scanning", { height: 0, opacity: 0, duration: 0.3, ease: "power2.in" })
          .to(".cp-result", { height: "auto", opacity: 1, duration: 0.6, ease: "power3.out" });
      }
    });
"""

js_idx = content.find('// Analytics Storytelling Animation')
if js_idx != -1:
    content = content[:js_idx] + JS_COPILOT + "\n" + content[js_idx:]
else:
    print("JS marker not found!")

with open('build_v11_compiler.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated compiler with Copilot visualization!")
