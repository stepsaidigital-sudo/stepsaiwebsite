import re

with open('build_v11_compiler.py', 'r', encoding='utf-8') as f:
    content = f.read()

CUSTOM_CHANNELS = """CUSTOM_CHANNELS = \"\"\"
    <section class="section-v2 channels-section" style="padding-top: 120px; padding-bottom: 120px; position: relative; overflow: hidden; background: #fff;">
      
      <div style="text-align: center; margin-bottom: 80px; position: relative; z-index: 1;">
        <span class="gsap-fade-up" style="font-family: 'Geist Mono', monospace; font-size: 12px; color: var(--accent); letter-spacing: .2em; text-transform: uppercase;">EVERY CHANNEL</span>
        <h2 class="gsap-fade-up" style="font-family: 'Outfit'; font-size: clamp(40px, 4vw, 56px); margin: 16px auto 24px; color: var(--text-primary); max-width: 900px; line-height: 1.1;">On Instagram it replies in public, then finishes the sale in private.</h2>
        <p class="gsap-fade-up" style="font-size: 20px; color: var(--text-secondary); max-width: 700px; margin: 0 auto; line-height: 1.6;">A comment under a post and a WhatsApp message at midnight are not the same kind of conversation. Your agent treats them differently, because your customers do.</p>
      </div>
  
      <div class="bento-grid gsap-fade-up" style="grid-template-columns: repeat(3, 1fr); gap: 32px; max-width: 1300px; margin: 0 auto; position: relative; z-index: 1;">
        
        <!-- Instagram Card -->
        <div class="bento-card" style="padding: 40px; background: linear-gradient(145deg, rgba(255, 235, 245, 0.9) 0%, rgba(255, 255, 255, 0.8) 100%); backdrop-filter: blur(20px); border: 1px solid var(--border-subtle); display: flex; flex-direction: column; justify-content: space-between; min-height: 520px; border-radius: 32px; box-shadow: 0 24px 64px rgba(0,0,0,0.03);">
          <div>
            <div style="font-family: 'Inter'; font-size: 14px; font-weight: 700; background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 12px; display: inline-block;">INSTAGRAM</div>
            <h3 style="font-family: 'Outfit'; font-size: 28px; margin-bottom: 16px; color: var(--text-primary); line-height: 1.2;">The comment nobody had time to answer.</h3>
            <p style="color: var(--text-secondary); font-size: 16px; line-height: 1.6;">Someone asks the price under your post. Your agent replies where everyone can see it, slides into the DM, and finishes the conversation there.</p>
          </div>
          <div class="micro-mockup ig-mockup" style="background: #fafafa; border-radius: 16px; padding: 20px; margin-top: 32px; border: 1px solid rgba(0,0,0,0.05); position: relative; overflow: hidden; display: flex; flex-direction: column; gap: 12px;">
            <div class="ig-comment" style="display: flex; gap: 12px; opacity: 0; transform: translateY(10px);">
                <div style="width: 24px; height: 24px; border-radius: 50%; background: #ddd; flex-shrink: 0;"></div>
                <div>
                    <div style="font-size: 12px; font-weight: 600; color: #111;">user123</div>
                    <div style="font-size: 13px; color: #444; margin-top: 2px;">How much is this?</div>
                </div>
            </div>
            <div class="ig-reply" style="display: flex; gap: 12px; padding-left: 36px; opacity: 0; transform: translateY(10px);">
                <div style="width: 24px; height: 24px; border-radius: 50%; background: linear-gradient(45deg, #1A56DB, #0B9E58); flex-shrink: 0;"></div>
                <div>
                    <div style="font-size: 12px; font-weight: 600; color: #111;">yourbrand <span style="color:#0B9E58;">&#10003;</span></div>
                    <div style="font-size: 13px; color: #444; margin-top: 2px;">Hey! Just sent you a DM with the details and a link to buy \U0001F60A</div>
                </div>
            </div>
            <div class="ig-dm" style="background: #fff; border: 1px solid #eee; border-radius: 16px; padding: 12px; margin-top: 8px; opacity: 0; transform: translateY(10px); box-shadow: 0 8px 24px rgba(0,0,0,0.05);">
                <div style="font-size: 11px; color: #888; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px; text-align: center;">Direct Message</div>
                <div style="background: #efefef; color: #111; padding: 10px 12px; border-radius: 16px; border-bottom-left-radius: 4px; font-size: 13px; display: inline-block;">It is $49. Would you like the link?</div>
            </div>
          </div>
        </div>
  
        <!-- WhatsApp Card -->
        <div class="bento-card" style="padding: 40px; background: linear-gradient(145deg, rgba(235, 255, 240, 0.9) 0%, rgba(255, 255, 255, 0.8) 100%); backdrop-filter: blur(20px); border: 1px solid var(--border-subtle); display: flex; flex-direction: column; justify-content: space-between; min-height: 520px; border-radius: 32px; box-shadow: 0 24px 64px rgba(0,0,0,0.03);">
          <div>
            <div style="font-family: 'Inter'; font-size: 14px; font-weight: 700; color: #25D366; margin-bottom: 12px;">WHATSAPP</div>
            <h3 style="font-family: 'Outfit'; font-size: 28px; margin-bottom: 16px; color: var(--text-primary); line-height: 1.2;">Where your customers already spend their evening.</h3>
            <p style="color: var(--text-secondary); font-size: 16px; line-height: 1.6;">Booking links, payment links, delivery updates, all inside the app they already have open.</p>
          </div>
          <div class="micro-mockup wa-mockup" style="background: #E5DDD5; border-radius: 16px; padding: 16px; margin-top: 32px; border: 1px solid rgba(0,0,0,0.05); position: relative; overflow: hidden; display: flex; flex-direction: column; gap: 8px;">
            <div style="text-align: center; font-size: 11px; color: #555; background: rgba(255,255,255,0.6); padding: 4px 8px; border-radius: 8px; margin: 0 auto 8px; width: max-content;">Today</div>
            <div class="wa-msg-1" style="background: #fff; color: #111; padding: 10px 14px; border-radius: 12px; border-top-left-radius: 0; align-self: flex-start; max-width: 85%; font-size: 13px; opacity: 0; transform: translateY(10px); box-shadow: 0 1px 1px rgba(0,0,0,0.05);">When will my order arrive?</div>
            <div class="wa-msg-2" style="background: #DCF8C6; color: #111; padding: 10px 14px; border-radius: 12px; border-top-right-radius: 0; align-self: flex-end; max-width: 85%; font-size: 13px; opacity: 0; transform: translateY(10px); box-shadow: 0 1px 1px rgba(0,0,0,0.05);">It's out for delivery! Track it here: <br><a href="#" style="color: #0367D3; text-decoration: none;">track.link/892</a></div>
          </div>
        </div>
        
        <!-- Website Card -->
        <div class="bento-card" style="padding: 40px; background: linear-gradient(145deg, rgba(235, 245, 255, 0.9) 0%, rgba(255, 255, 255, 0.8) 100%); backdrop-filter: blur(20px); border: 1px solid var(--border-subtle); display: flex; flex-direction: column; justify-content: space-between; min-height: 520px; border-radius: 32px; box-shadow: 0 24px 64px rgba(0,0,0,0.03);">
          <div>
            <div style="font-family: 'Inter'; font-size: 14px; font-weight: 700; color: #0367D3; margin-bottom: 12px;">WEBSITE</div>
            <h3 style="font-family: 'Outfit'; font-size: 28px; margin-bottom: 16px; color: var(--text-primary); line-height: 1.2;">It knows which page they are standing on.</h3>
            <p style="color: var(--text-secondary); font-size: 16px; line-height: 1.6;">Someone asks "does this come in blue" while looking at a specific jacket. Your agent knows which jacket.</p>
          </div>
          <div class="micro-mockup web-mockup" style="background: #fafafa; border-radius: 16px; padding: 0; margin-top: 32px; border: 1px solid rgba(0,0,0,0.05); position: relative; overflow: hidden; height: 180px;">
             <!-- Fake Website BG -->
             <div style="padding: 20px;">
                <div style="width: 60%; height: 80px; background: #eee; border-radius: 8px; margin-bottom: 12px;"></div>
                <div style="width: 80%; height: 12px; background: #eee; border-radius: 4px; margin-bottom: 8px;"></div>
                <div style="width: 40%; height: 12px; background: #eee; border-radius: 4px;"></div>
             </div>
             <!-- Chat Widget -->
             <div class="web-widget" style="position: absolute; bottom: 16px; right: 16px; background: #fff; width: 200px; border-radius: 16px; border-bottom-right-radius: 4px; box-shadow: 0 12px 32px rgba(0,0,0,0.1); border: 1px solid #eaeaea; opacity: 0; transform: translateY(20px) scale(0.9); transform-origin: bottom right;">
                <div style="background: #111; color: #fff; padding: 12px; border-top-left-radius: 16px; border-top-right-radius: 16px; font-size: 12px; font-weight: 600;">Chat with us</div>
                <div style="padding: 12px; font-size: 12px;">
                   <div style="background: #f4f5f7; padding: 8px 12px; border-radius: 12px; border-bottom-left-radius: 4px; display: inline-block; margin-bottom: 8px;">Does this come in blue?</div>
                   <div style="background: #0B9E58; color: #fff; padding: 8px 12px; border-radius: 12px; border-bottom-right-radius: 4px; display: inline-block; align-self: flex-end; float: right;">Yes, the Denim Jacket comes in Navy Blue!</div>
                </div>
             </div>
          </div>
        </div>

      </div>
    </section>
\"\"\""""

JS_CHANNELS = """
    // --- Channels Section Animations ---
    
    // IG Animation
    let igTl = gsap.timeline({ repeat: -1, repeatDelay: 3 });
    igTl.to(".ig-comment", { opacity: 1, y: 0, duration: 0.4, ease: "power2.out" })
        .to({}, {duration: 0.8})
        .to(".ig-reply", { opacity: 1, y: 0, duration: 0.4, ease: "power2.out" })
        .to({}, {duration: 0.8})
        .to(".ig-dm", { opacity: 1, y: 0, duration: 0.5, ease: "back.out(1.5)" })
        .to({}, {duration: 2});

    // WA Animation
    let waTl = gsap.timeline({ repeat: -1, repeatDelay: 3 });
    waTl.to(".wa-msg-1", { opacity: 1, y: 0, duration: 0.4, ease: "power2.out" })
        .to({}, {duration: 0.8})
        .to(".wa-msg-2", { opacity: 1, y: 0, duration: 0.5, ease: "back.out(1.5)" })
        .to({}, {duration: 2});

    // Web Animation
    let webTl = gsap.timeline({ repeat: -1, repeatDelay: 3 });
    webTl.to(".web-widget", { opacity: 1, y: 0, scale: 1, duration: 0.6, ease: "back.out(1.2)" })
         .to({}, {duration: 3});
"""

# Inject CUSTOM_CHANNELS string logic
channels_start = content.find('CUSTOM_CHANNELS = """')
if channels_start == -1:
    # We inject the definition right above GLOBAL_HEAD
    content = content.replace('GLOBAL_HEAD = """', CUSTOM_CHANNELS + '\n\nGLOBAL_HEAD = """')

# Inject the check into the main loop
loop_target = 'if data["route"] == "" and "Internal Copilot" in block["title"]:'
if 'and "Channels" in block["title"]:' not in content:
    channels_check = """
if data["route"] == "" and "Channels" in block["title"]:
            try: html_content += CUSTOM_CHANNELS
            except NameError: pass
            continue
"""
    content = content.replace(loop_target, channels_check.strip('\n') + '\n\n        ' + loop_target)

# Inject JS
script_end = content.find('  </script>\n</body>')
if script_end != -1:
    content = content[:script_end] + JS_CHANNELS + "\n" + content[script_end:]
else:
    print("Could not find closing script tag to inject JS_CHANNELS!")

with open('build_v11_compiler.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected custom Channels logic into compiler!")
