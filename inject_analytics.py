import os

with open('build_v11_compiler.py', 'r', encoding='utf-8') as f:
    content = f.read()

CUSTOM_ANALYTICS = """
CUSTOM_ANALYTICS = \"\"\"
<section class="section-v2 analytics-section" style="padding-top: 160px; padding-bottom: 160px; max-width: 1400px; margin:0 auto; display:flex; gap:64px; align-items:center;">
  <div style="flex:1;">
    <span class="gsap-fade-up" style="font-family: 'Geist Mono', monospace; font-size: 12px; color: var(--accent); letter-spacing: .2em; text-transform: uppercase; margin-bottom:16px; display:block;">SEE WHAT IT DID</span>
    <h2 class="gsap-fade-up" style="font-family: 'Outfit'; font-size: clamp(40px, 4vw, 56px); margin: 0 0 24px; color: var(--text-primary); line-height:1.1;">A paragraph, not a dashboard.</h2>
    <p class="gsap-fade-up" style="font-size: 18px; color: var(--text-secondary); margin-bottom: 24px; line-height: 1.6; max-width:500px;">Most analytics tell you a number moved. Yours tells you that three people asked for something you do not stock yet.</p>
    <p class="gsap-fade-up" style="font-size: 13px; color: #888; margin-bottom: 0; line-height: 1.5; max-width:500px; border-left: 2px solid var(--border-subtle); padding-left: 12px;">*Every number on this page comes from a real account or is clearly marked as an example. We do not publish numbers we cannot show you.</p>
  </div>
  
  <div style="flex:1.2; display:flex; justify-content:center; align-items:center; min-width:300px; position:relative;">
    <!-- Background Glow -->
    <div style="position:absolute; width:100%; height:100%; background:radial-gradient(circle at center, rgba(26,86,219,0.1) 0%, transparent 70%); z-index:0; pointer-events:none;"></div>
    
    <!-- Analytics Paragraph Card -->
    <div class="analytics-card" style="opacity:0; transform:translateY(40px); width:100%; max-width:600px; background:#fff; border-radius:24px; border:1px solid var(--border-subtle); box-shadow: 0 32px 80px rgba(0,0,0,0.06); padding:48px; position:relative; z-index:1;">
       
       <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:24px; border-bottom:1px solid var(--border-subtle); padding-bottom:16px;">
          <div style="font-family:'Geist Mono', monospace; font-size:12px; color:#888; text-transform:uppercase; letter-spacing:0.1em;">The Weekly Summary</div>
          <div style="background:#f4f5f7; color:#666; font-size:11px; font-weight:600; padding:4px 8px; border-radius:4px;">EXAMPLE ACCOUNT</div>
       </div>
       
       <div style="font-family:'Outfit'; font-size:28px; color:#111; line-height:1.5; font-weight:400;">
          This week your agent handled 
          <span class="hl-stat hl-1" style="display:inline-block; font-weight:700; color:var(--accent); background:#EBF3FF; padding:0 8px; border-radius:8px; margin:0 4px; box-shadow:0 4px 12px rgba(26,86,219,0.15);"><span id="count-1">0</span></span> 
          conversations. It answered 
          <span class="hl-stat hl-2" style="display:inline-block; font-weight:700; color:#0B9E58; background:#E9F8F0; padding:0 8px; border-radius:8px; margin:0 4px; box-shadow:0 4px 12px rgba(11,158,88,0.15);"><span id="count-2">0</span></span> 
          on its own, booked 
          <span class="hl-stat hl-3" style="display:inline-block; font-weight:700; color:#8B5CF6; background:#F5F3FF; padding:0 8px; border-radius:8px; margin:0 4px; box-shadow:0 4px 12px rgba(139,92,246,0.15);"><span id="count-3">0</span></span> 
          meetings, and passed 
          <span class="hl-stat hl-4" style="display:inline-block; font-weight:700; color:#F59E0B; background:#FEF3C7; padding:0 8px; border-radius:8px; margin:0 4px; box-shadow:0 4px 12px rgba(245,158,11,0.15);"><span id="count-4">0</span></span> 
          to your team.
       </div>
       
       <div class="insight-reveal" style="opacity:0; transform:translateY(10px); margin-top:32px; padding:24px; background:#111; border-radius:16px; position:relative; overflow:hidden;">
          <div style="position:absolute; top:0; left:0; width:4px; height:100%; background:linear-gradient(to bottom, #F59E0B, #EA580C);"></div>
          <div style="display:flex; gap:16px; align-items:flex-start;">
             <div style="width:32px; height:32px; background:rgba(245,158,11,0.2); border-radius:8px; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#F59E0B" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 16v-4"></path><path d="M12 8h.01"></path></svg>
             </div>
             <div>
                <div style="color:#F59E0B; font-size:12px; font-weight:700; letter-spacing:0.05em; margin-bottom:4px; text-transform:uppercase;">Key Insight Generated</div>
                <div style="color:#fff; font-size:16px; line-height:1.5;">Three customers asked about a product you do not stock yet.</div>
             </div>
          </div>
       </div>
       
    </div>
  </div>
</section>
\"\"\"
"""

# Inject CUSTOM_ANALYTICS before CUSTOM_HOME_ACCORDION
acc_idx = content.find('CUSTOM_HOME_ACCORDION = """')
if acc_idx != -1:
    content = content[:acc_idx] + CUSTOM_ANALYTICS + "\n\n" + content[acc_idx:]

# Inject logic condition in the blocks loop
logic_marker = 'if data["route"] == "" and "One Inbox" in block["title"]:\n            html_content += CUSTOM_ONE_INBOX\n            continue'
logic_insert = '''
        if data["route"] == "" and "Analytics" in block["title"]:
            html_content += CUSTOM_ANALYTICS
            continue
'''
if logic_marker in content:
    content = content.replace(logic_marker, logic_marker + "\n" + logic_insert)
else:
    print("Logic marker not found!")

# Inject JS Animation
JS_ANALYTICS = """
    // Analytics Storytelling Animation
    let analyticsPlayed = false;
    ScrollTrigger.create({
      trigger: ".analytics-section",
      start: "top 75%",
      onEnter: () => {
        if(analyticsPlayed) return;
        analyticsPlayed = true;
        let tl = gsap.timeline();
        
        tl.to(".analytics-card", { opacity: 1, y: 0, duration: 0.8, ease: "power3.out" })
          .to({}, {duration: 0.4})
          
          // Animate counters
          .add(() => {
              let obj = { val1: 0, val2: 0, val3: 0, val4: 0 };
              gsap.to(obj, {
                  val1: 412, val2: 358, val3: 24, val4: 30,
                  duration: 2.5,
                  ease: "power2.out",
                  onUpdate: () => {
                      document.getElementById("count-1").innerText = Math.floor(obj.val1);
                      document.getElementById("count-2").innerText = Math.floor(obj.val2);
                      document.getElementById("count-3").innerText = Math.floor(obj.val3);
                      document.getElementById("count-4").innerText = Math.floor(obj.val4);
                  }
              });
          })
          
          // Slight pop on the highlight backgrounds during count
          .fromTo(".hl-1", {scale:0.95}, {scale:1, duration:0.5, ease:"back.out(2)"}, "<0.2")
          .fromTo(".hl-2", {scale:0.95}, {scale:1, duration:0.5, ease:"back.out(2)"}, "<0.3")
          .fromTo(".hl-3", {scale:0.95}, {scale:1, duration:0.5, ease:"back.out(2)"}, "<0.2")
          .fromTo(".hl-4", {scale:0.95}, {scale:1, duration:0.5, ease:"back.out(2)"}, "<0.2")
          
          .to({}, {duration: 1.5}) // Let the numbers finish
          
          // Reveal Insight
          .to(".insight-reveal", { opacity: 1, y: 0, duration: 0.6, ease: "back.out(1.2)" });
      }
    });
"""

js_idx = content.find('// Inbox Storytelling Animation')
if js_idx != -1:
    content = content[:js_idx] + JS_ANALYTICS + "\n" + content[js_idx:]
else:
    print("JS marker not found!")

with open('build_v11_compiler.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated compiler with Analytics visualization!")
