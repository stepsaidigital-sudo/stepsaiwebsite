import re

with open('build_v11_compiler.py', 'r', encoding='utf-8') as f:
    content = f.read()

CUSTOM_WORKFLOWS = """CUSTOM_WORKFLOWS = \"\"\"
    <style>
      .wf-row { background: var(--bg-surface); padding: 32px; border-radius: 24px; border: 1px solid var(--border-subtle); margin-bottom: 24px; box-shadow: 0 4px 24px rgba(0,0,0,0.02); }
      .wf-title { font-family: 'Outfit'; font-size: 24px; font-weight: 700; color: var(--text-primary); margin-bottom: 24px; display: flex; align-items: center; justify-content: space-between; }
      .wf-path { display: flex; align-items: center; justify-content: space-between; position: relative; padding: 20px 0; }
      .wf-line { position: absolute; top: 50%; left: 0; right: 0; height: 2px; background: #eee; z-index: 0; transform: translateY(-50%); }
      .wf-line-active { position: absolute; top: 50%; left: 0; width: 0; height: 2px; background: #0B9E58; z-index: 1; transform: translateY(-50%); }
      .wf-node { position: relative; z-index: 2; background: #fff; border: 2px solid #eee; padding: 8px 16px; border-radius: 100px; font-size: 13px; font-weight: 600; color: #555; transition: 0.3s; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
      .wf-node.active { border-color: #0B9E58; color: #0B9E58; background: #f0fdf4; box-shadow: 0 0 16px rgba(11,158,88,0.2); }
      .wf-pulse { position: absolute; top: 50%; left: 0; width: 8px; height: 8px; background: #0B9E58; border-radius: 50%; z-index: 3; transform: translate(-50%, -50%); opacity: 0; box-shadow: 0 0 12px #0B9E58; }
      @media (max-width: 900px) {
        .wf-path { flex-direction: column; align-items: flex-start; gap: 24px; padding: 0; }
        .wf-line, .wf-line-active, .wf-pulse { display: none; }
        .wf-node { width: 100%; border-radius: 12px; }
      }
    </style>
    <section class="section-v2 workflows-section" style="padding-top: 120px; padding-bottom: 120px; background: #fafafa;">
      
      <div style="text-align: center; margin-bottom: 80px; position: relative; z-index: 1;">
        <span class="gsap-fade-up" style="font-family: 'Geist Mono', monospace; font-size: 12px; color: var(--accent); letter-spacing: .2em; text-transform: uppercase;">AUTOMATED WORKFLOWS</span>
        <h2 class="gsap-fade-up" style="font-family: 'Outfit'; font-size: clamp(40px, 4vw, 56px); margin: 16px auto 24px; color: var(--text-primary); max-width: 900px; line-height: 1.1;">Most sales do not die from a no. They die from silence.</h2>
        <p class="gsap-fade-up" style="font-size: 20px; color: var(--text-secondary); max-width: 700px; margin: 0 auto; line-height: 1.6;">Somebody fills a cart and then their food arrives. A lead asks one question and disappears for a week. Your agent notices the gap, waits the right amount of time, and starts the conversation up again.</p>
      </div>
  
      <div class="gsap-fade-up" style="max-width: 1000px; margin: 0 auto; position: relative; z-index: 1;">
        
        <!-- Workflow 1 -->
        <div class="wf-row">
            <div class="wf-title">Recover Carts <span style="font-size: 14px; background: #eee; padding: 4px 12px; border-radius: 100px; font-weight: 500; color: #666;">Default</span></div>
            <div class="wf-path wf-path-1">
                <div class="wf-line"></div>
                <div class="wf-line-active wf-line-active-1"></div>
                <div class="wf-pulse wf-pulse-1"></div>
                
                <div class="wf-node wf-n1-1">Cart left behind</div>
                <div class="wf-node wf-n1-2">Wait 30 minutes</div>
                <div class="wf-node wf-n1-3">Send WhatsApp message</div>
                <div class="wf-node wf-n1-4">Share checkout link</div>
                <div class="wf-node wf-n1-5" style="background: #111; color: #fff; border-color: #111;">Checkout Reopened</div>
            </div>
        </div>

        <!-- Workflow 2 -->
        <div class="wf-row">
            <div class="wf-title">Follow up leads</div>
            <div class="wf-path wf-path-2">
                <div class="wf-line"></div>
                <div class="wf-line-active wf-line-active-2"></div>
                <div class="wf-pulse wf-pulse-2"></div>
                
                <div class="wf-node wf-n2-1">New lead captured</div>
                <div class="wf-node wf-n2-2">Save to CRM</div>
                <div class="wf-node wf-n2-3">Send a short follow-up</div>
                <div class="wf-node wf-n2-4">Offer free times</div>
                <div class="wf-node wf-n2-5" style="background: #111; color: #fff; border-color: #111;">Follow-up Sent</div>
            </div>
        </div>

        <!-- Workflow 3 -->
        <div class="wf-row">
            <div class="wf-title">Remind customers</div>
            <div class="wf-path wf-path-3">
                <div class="wf-line"></div>
                <div class="wf-line-active wf-line-active-3"></div>
                <div class="wf-pulse wf-pulse-3"></div>
                
                <div class="wf-node wf-n3-1">Meeting booked</div>
                <div class="wf-node wf-n3-2">Wait until day before</div>
                <div class="wf-node wf-n3-3">Send the reminder</div>
                <div class="wf-node wf-n3-4">Let them confirm</div>
                <div class="wf-node wf-n3-5" style="background: #111; color: #fff; border-color: #111;">Reminder Sent</div>
            </div>
        </div>

        <!-- Workflow 4 -->
        <div class="wf-row">
            <div class="wf-title">Re-engage</div>
            <div class="wf-path wf-path-4">
                <div class="wf-line"></div>
                <div class="wf-line-active wf-line-active-4"></div>
                <div class="wf-pulse wf-pulse-4"></div>
                
                <div class="wf-node wf-n4-1">Quiet for 30 days</div>
                <div class="wf-node wf-n4-2">Work out which group</div>
                <div class="wf-node wf-n4-3">Send relevant message</div>
                <div class="wf-node wf-n4-4">Handle the replies</div>
                <div class="wf-node wf-n4-5" style="background: #111; color: #fff; border-color: #111;">Campaign Live</div>
            </div>
        </div>

      </div>
    </section>
\"\"\""""

JS_WORKFLOWS = """
    // --- Workflows Section Animations ---
    function animateWorkflow(pathIndex) {
        let tl = gsap.timeline({ repeat: -1, repeatDelay: 2 });
        let pulse = `.wf-pulse-${pathIndex}`;
        let lineActive = `.wf-line-active-${pathIndex}`;
        
        tl.set(pulse, { left: "0%", opacity: 1 })
          .set(lineActive, { width: "0%" })
          .call(() => { let el = document.querySelector(`.wf-n${pathIndex}-1`); if(el) el.classList.add('active'); })
          
          .to(pulse, { left: "25%", duration: 1, ease: "power1.inOut" })
          .to(lineActive, { width: "25%", duration: 1, ease: "power1.inOut" }, "<")
          .call(() => { let el = document.querySelector(`.wf-n${pathIndex}-2`); if(el) el.classList.add('active'); })
          
          .to(pulse, { left: "50%", duration: 1, ease: "power1.inOut" })
          .to(lineActive, { width: "50%", duration: 1, ease: "power1.inOut" }, "<")
          .call(() => { let el = document.querySelector(`.wf-n${pathIndex}-3`); if(el) el.classList.add('active'); })
          
          .to(pulse, { left: "75%", duration: 1, ease: "power1.inOut" })
          .to(lineActive, { width: "75%", duration: 1, ease: "power1.inOut" }, "<")
          .call(() => { let el = document.querySelector(`.wf-n${pathIndex}-4`); if(el) el.classList.add('active'); })
          
          .to(pulse, { left: "100%", duration: 1, ease: "power1.inOut" })
          .to(lineActive, { width: "100%", duration: 1, ease: "power1.inOut" }, "<")
          .to(pulse, { opacity: 0, duration: 0.2 })
          
          // Cleanup at end
          .to({}, {duration: 1})
          .call(() => {
              document.querySelectorAll(`.wf-n${pathIndex}-1, .wf-n${pathIndex}-2, .wf-n${pathIndex}-3, .wf-n${pathIndex}-4`).forEach(el => el.classList.remove('active'));
          });
          
        return tl;
    }
    
    // Create ScrollTrigger to start animations when section is visible
    ScrollTrigger.create({
        trigger: ".workflows-section",
        start: "top 60%",
        onEnter: () => {
            setTimeout(() => animateWorkflow(1), 0);
            setTimeout(() => animateWorkflow(2), 500);
            setTimeout(() => animateWorkflow(3), 1000);
            setTimeout(() => animateWorkflow(4), 1500);
        },
        once: true
    });
"""

# Inject CUSTOM_WORKFLOWS string logic
workflows_start = content.find('CUSTOM_WORKFLOWS = """')
if workflows_start == -1:
    # We inject the definition right above GLOBAL_HEAD
    content = content.replace('GLOBAL_HEAD = """', CUSTOM_WORKFLOWS + '\n\nGLOBAL_HEAD = """')

# Inject the check into the main loop
loop_target = 'if data["route"] == "" and "Internal Copilot" in block["title"]:'
if 'and "Workflows" in block["title"]:' not in content:
    workflows_check = """
if data["route"] == "" and "Workflows" in block["title"]:
            try: html_content += CUSTOM_WORKFLOWS
            except NameError: pass
            continue
"""
    content = content.replace(loop_target, workflows_check.strip('\n') + '\n\n        ' + loop_target)

# Inject JS
script_end = content.find('  </script>\n</body>')
if script_end != -1:
    content = content[:script_end] + JS_WORKFLOWS + "\n" + content[script_end:]
else:
    print("Could not find closing script tag to inject JS_WORKFLOWS!")

with open('build_v11_compiler.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected custom Workflows logic into compiler!")
