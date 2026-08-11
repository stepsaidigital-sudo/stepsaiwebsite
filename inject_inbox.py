import os

with open('build_v11_compiler.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Inject CUSTOM_ONE_INBOX
setup_end = content.find('"""\n\nCUSTOM_HOME_ACCORDION')

NEW_INBOX = '''
CUSTOM_ONE_INBOX = """
<section class="section-v2 inbox-section" style="padding-top: 160px; max-width: 1400px; margin:0 auto; display:flex; gap:64px; align-items:center;">
  <div style="flex:1;">
    <span class="gsap-fade-up" style="font-family: 'Geist Mono', monospace; font-size: 12px; color: var(--accent); letter-spacing: .2em; text-transform: uppercase; margin-bottom:16px; display:block;">YOU STAY IN CONTROL</span>
    <h2 class="gsap-fade-up" style="font-family: 'Outfit'; font-size: clamp(40px, 4vw, 56px); margin: 0 0 24px; color: var(--text-primary); line-height:1.1;">It never sends a message you cannot read.</h2>
    <p class="gsap-fade-up" style="font-size: 18px; color: var(--text-secondary); margin-bottom: 24px; line-height: 1.6; max-width:500px;">Every conversation, from every channel, lands in one inbox. Jump in whenever you feel like it and your agent goes quiet on that thread until you are finished.</p>
    <p class="gsap-fade-up" style="font-size: 18px; color: var(--text-secondary); margin-bottom: 0; line-height: 1.6; max-width:500px;">You decide what it is allowed to answer. You decide where it has to stop. Every conversation is there to read. When it hands over, the whole history comes with it.</p>
  </div>
  
  <div style="flex:1.5; display:flex; justify-content:center; align-items:center; min-width:300px;">
    <!-- Inbox UI Mockup -->
    <div class="inbox-mockup" style="opacity:0; transform:scale(0.9); width:100%; max-width:800px; height:500px; background:#fff; border-radius:24px; border:1px solid var(--border-subtle); box-shadow: 0 32px 80px rgba(0,0,0,0.08); display:flex; overflow:hidden; font-family:'Inter', sans-serif;">
      
      <!-- Sidebar -->
      <div style="width:260px; background:#fbfbfd; border-right:1px solid var(--border-subtle); display:flex; flex-direction:column;">
         <div style="padding:24px; border-bottom:1px solid var(--border-subtle);">
            <div style="font-weight:700; font-size:18px; font-family:'Outfit'; color:#111;">Steps Inbox</div>
         </div>
         <div style="flex:1; overflow-y:auto; padding:12px;">
            <div style="padding:12px; background:#fff; border-radius:12px; border:1px solid var(--accent); box-shadow:0 4px 12px rgba(0,0,0,0.05); margin-bottom:8px; cursor:pointer;">
               <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
                  <div style="font-weight:600; font-size:14px; color:#111; display:flex; align-items:center; gap:6px;">
                     <span class="pulse-dot" style="display:inline-block; width:8px; height:8px; background:var(--accent); border-radius:50%;"></span> Sarah Jenkins
                  </div>
                  <div style="font-size:12px; color:#888;">Just now</div>
               </div>
               <div style="font-size:13px; color:#666; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">Can I speak to a human about this?</div>
               <div style="display:flex; gap:6px; margin-top:8px;">
                  <span class="tag-handover" style="background:#E9F8F0; color:#0B9E58; padding:2px 6px; border-radius:4px; font-size:10px; font-weight:700; opacity:0; transition:0.3s;">HANDOVER</span>
                  <span style="background:#f4f5f7; color:#666; padding:2px 6px; border-radius:4px; font-size:10px; font-weight:600;">WHATSAPP</span>
               </div>
            </div>
            
            <div style="padding:12px; background:transparent; border-radius:12px; border:1px solid transparent; margin-bottom:8px; opacity:0.6;">
               <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
                  <div style="font-weight:600; font-size:14px; color:#111;">Mike Davies</div>
                  <div style="font-size:12px; color:#888;">10:42 AM</div>
               </div>
               <div style="font-size:13px; color:#666; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">Thanks for the sizing info!</div>
               <div style="display:flex; gap:6px; margin-top:8px;">
                  <span style="background:#EBF3FF; color:var(--accent); padding:2px 6px; border-radius:4px; font-size:10px; font-weight:700;">AI HANDLED</span>
                  <span style="background:#f4f5f7; color:#666; padding:2px 6px; border-radius:4px; font-size:10px; font-weight:600;">INSTAGRAM</span>
               </div>
            </div>
         </div>
      </div>
      
      <!-- Main Chat Area -->
      <div style="flex:1; display:flex; flex-direction:column; background:#fff;">
         <!-- Chat Header -->
         <div style="padding:20px 24px; border-bottom:1px solid var(--border-subtle); display:flex; justify-content:space-between; align-items:center;">
            <div>
               <div style="font-weight:700; font-size:16px; color:#111;">Sarah Jenkins</div>
               <div style="font-size:13px; color:#666;">WhatsApp • Order #8821</div>
            </div>
            <div class="inbox-status" style="background:#EBF3FF; color:var(--accent); padding:6px 12px; border-radius:100px; font-size:12px; font-weight:600; display:flex; align-items:center; gap:6px; transition:0.3s;">
               <span class="status-dot-h" style="display:inline-block; width:6px; height:6px; background:var(--accent); border-radius:50%;"></span> <span class="status-text">AI is reading...</span>
            </div>
         </div>
         
         <!-- Chat History -->
         <div class="chat-scroll-area" style="flex:1; padding:24px; overflow-y:auto; display:flex; flex-direction:column; gap:16px; background:#fbfbfd; scroll-behavior: smooth;">
            <div style="align-self:center; font-size:12px; color:#888; font-weight:500;">Today 10:15 AM</div>
            
            <div style="display:flex; gap:12px; max-width:85%;">
               <div style="width:28px; height:28px; border-radius:50%; background:#e0e0e0; flex-shrink:0;"></div>
               <div style="background:#fff; padding:12px 16px; border-radius:16px 16px 16px 0; border:1px solid var(--border-subtle); font-size:14px; color:#111; line-height:1.5;">Do you ship to Germany? And how long does it take?</div>
            </div>
            
            <div style="display:flex; gap:12px; max-width:85%; align-self:flex-end;">
               <div style="background:#EBF3FF; padding:12px 16px; border-radius:16px 16px 0 16px; border:1px solid #d4e5ff; font-size:14px; color:#111; line-height:1.5; position:relative;">
                  <div style="position:absolute; top:-8px; right:12px; font-size:10px; font-weight:700; color:var(--accent); background:#fff; padding:0 4px; border-radius:4px;">AI AGENT</div>
                  Yes! We ship to Germany via DHL Express. It usually takes 2-3 business days. Shipping is free on orders over €150.
               </div>
            </div>
            
            <div class="human-req" style="display:flex; gap:12px; max-width:85%;">
               <div style="width:28px; height:28px; border-radius:50%; background:#e0e0e0; flex-shrink:0;"></div>
               <div style="background:#fff; padding:12px 16px; border-radius:16px 16px 16px 0; border:1px solid var(--border-subtle); font-size:14px; color:#111; line-height:1.5;">Great. I have a custom tax exemption code for my business, can I speak to a human about applying it to this order?</div>
            </div>
            
            <div class="handover-banner" style="display:none; background:#E9F8F0; border:1px solid #c2ebd5; padding:12px; border-radius:12px; align-items:center; justify-content:center; gap:8px; margin:8px 0; opacity:0; transform:translateY(10px);">
               <span style="font-size:16px;">🛑</span>
               <span style="font-size:13px; font-weight:600; color:#0B9E58;">Agent automatically paused. Thread handed over to human.</span>
            </div>
            
            <div class="human-reply" style="display:none; gap:12px; max-width:85%; align-self:flex-end; opacity:0; transform:translateY(10px);">
               <div style="background:var(--text-primary); padding:12px 16px; border-radius:16px 16px 0 16px; font-size:14px; color:#fff; line-height:1.5; position:relative;">
                  <div style="position:absolute; top:-8px; right:12px; font-size:10px; font-weight:700; color:var(--text-primary); background:#fff; padding:0 4px; border-radius:4px; border:1px solid var(--text-primary);">YOU</div>
                  <span id="typewriter-human"></span><span class="cursor-human" style="display:inline-block; width:2px; height:14px; background:#fff; margin-left:2px; animation:blink 1s infinite;"></span>
               </div>
            </div>
            <div id="scroll-anchor" style="height:1px;"></div>
         </div>
         
         <!-- Chat Input -->
         <div style="padding:16px 24px; border-top:1px solid var(--border-subtle); background:#fff;">
            <div style="background:#f4f5f7; border:1px solid var(--border-subtle); border-radius:12px; padding:12px 16px; display:flex; align-items:center; justify-content:space-between;">
               <div class="input-placeholder" style="color:#888; font-size:14px;">Reply to Sarah...</div>
               <div style="color:#aaa; font-weight:600; font-size:12px;">Press Enter to send</div>
            </div>
         </div>
      </div>
      
    </div>
  </div>
</section>
<style>
@keyframes pulse { 0% { box-shadow: 0 0 0 0 rgba(26, 86, 219, 0.4); } 70% { box-shadow: 0 0 0 6px rgba(26, 86, 219, 0); } 100% { box-shadow: 0 0 0 0 rgba(26, 86, 219, 0); } }
.pulse-dot { animation: pulse 2s infinite; }
</style>
"""
'''
content = content[:setup_end] + NEW_INBOX + content[setup_end:]

# 2. Inject python rendering logic
logic_marker = 'if data["route"] == "" and "Setup" in block["title"]:\\n            html_content += CUSTOM_SETUP\\n            continue'
logic_insert = '''
        if data["route"] == "" and "One Inbox" in block["title"]:
            html_content += CUSTOM_ONE_INBOX
            continue
'''
content = content.replace(logic_marker, logic_marker + logic_insert)

# 3. Inject JS Animation
js_marker = '});\\n  </script>'
JS_INBOX = """
    // Inbox Storytelling Animation
    let inboxPlayed = false;
    ScrollTrigger.create({
      trigger: ".inbox-section",
      start: "top 75%",
      onEnter: () => {
        if(inboxPlayed) return;
        inboxPlayed = true;
        let tl = gsap.timeline();
        
        tl.to(".inbox-mockup", { opacity: 1, scale: 1, duration: 0.8, ease: "power3.out" })
          .to({}, {duration: 0.8}) // reading the question
          
          // Handover triggers
          .to(".handover-banner", { display: "flex", duration: 0.1 })
          .to(".handover-banner", { opacity: 1, y: 0, duration: 0.5, ease: "back.out" })
          
          // Change status pill
          .to(".inbox-status", { background: "#E9F8F0", color: "#0B9E58", duration: 0.3 }, "<")
          .to(".status-dot-h", { background: "#0B9E58", duration: 0.3 }, "<")
          .add(() => { 
             let st = document.querySelector(".status-text"); if(st) st.textContent = "You are in control";
             let pd = document.querySelector(".pulse-dot"); if(pd) pd.style.background = "#0B9E58";
             let th = document.querySelector(".tag-handover"); if(th) th.style.opacity = "1";
          }, "<")
          
          .to({}, {duration: 1.0}) // pause for user to read
          
          // Start typing human reply
          .to(".human-reply", { display: "flex", duration: 0.1 })
          .to(".human-reply", { opacity: 1, y: 0, duration: 0.4 })
          .add(() => {
              let text = "Hi Sarah! I can absolutely help with that. Please send the code here.";
              let el = document.getElementById("typewriter-human");
              let inputPh = document.querySelector(".input-placeholder");
              let i = 0;
              
              // Scroll to bottom
              let scrollArea = document.querySelector(".chat-scroll-area");
              
              let interval = setInterval(() => {
                if(i < text.length) {
                  if(el) el.textContent += text.charAt(i);
                  if(inputPh) inputPh.textContent = "Reply to Sarah... " + text.substring(0, i + 1);
                  if(scrollArea) scrollArea.scrollTop = scrollArea.scrollHeight;
                  i++;
                } else {
                  clearInterval(interval);
                  let c = document.querySelector(".cursor-human"); if(c) c.style.display = "none";
                  if(inputPh) inputPh.textContent = "Reply to Sarah...";
                }
              }, 40);
          });
      }
    });
"""
content = content.replace(js_marker, JS_INBOX + js_marker)

with open('build_v11_compiler.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Injected Inbox!")
