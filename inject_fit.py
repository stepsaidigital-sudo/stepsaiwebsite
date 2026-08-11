import os

with open('build_v11_compiler.py', 'r', encoding='utf-8') as f:
    content = f.read()

CUSTOM_FIT = """
CUSTOM_FIT = \"\"\"
<section class="section-v2 fit-section" style="padding-top: 160px; padding-bottom: 160px; max-width: 1400px; margin:0 auto; display:flex; gap:64px; align-items:center;">
  
  <div style="flex:1;">
    <span class="gsap-fade-up" style="font-family: 'Geist Mono', monospace; font-size: 12px; color: var(--accent); letter-spacing: .2em; text-transform: uppercase; margin-bottom:16px; display:block;">HONEST FIT</span>
    <h2 class="gsap-fade-up" style="font-family: 'Outfit'; font-size: clamp(40px, 4vw, 56px); margin: 0 0 24px; color: var(--text-primary); line-height:1.1;">You might not need this.</h2>
    <p class="gsap-fade-up" style="font-size: 18px; color: var(--text-secondary); margin-bottom: 24px; line-height: 1.6; max-width:500px;">Some businesses are better off without it, and it is cheaper for both of us if you work that out now rather than in month three.</p>
  </div>
  
  <div class="gsap-fade-up" style="flex:1.5; display:flex; flex-direction:column; gap:24px; min-width:300px;">
    
    <!-- Good Fit Card -->
    <div style="background:#fff; border:1px solid var(--border-subtle); border-radius:24px; padding:40px; box-shadow: 0 12px 40px rgba(0,0,0,0.04); display:flex; flex-direction:column; gap:24px; transition:0.3s; position:relative; overflow:hidden;" onmouseover="this.style.borderColor='#0B9E58'; this.style.boxShadow='0 12px 40px rgba(11,158,88,0.1)'" onmouseout="this.style.borderColor='var(--border-subtle)'; this.style.boxShadow='0 12px 40px rgba(0,0,0,0.04)'">
       <div style="position:absolute; top:0; left:0; width:6px; height:100%; background:#0B9E58;"></div>
       <div style="display:flex; align-items:center; gap:12px;">
          <div style="width:40px; height:40px; border-radius:12px; background:#E9F8F0; display:flex; align-items:center; justify-content:center;">
             <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#0B9E58" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
          </div>
          <h3 style="font-family:'Outfit'; font-size:24px; font-weight:600; margin:0; color:#111;">Worth trying if...</h3>
       </div>
       
       <div style="display:flex; flex-direction:column; gap:16px;">
          <div style="display:flex; gap:12px; align-items:flex-start;">
             <div style="color:#0B9E58; margin-top:2px;">•</div>
             <div style="font-size:16px; color:#555; line-height:1.5;">People are messaging you on WhatsApp, Instagram or your website in real numbers.</div>
          </div>
          <div style="display:flex; gap:12px; align-items:flex-start;">
             <div style="color:#0B9E58; margin-top:2px;">•</div>
             <div style="font-size:16px; color:#555; line-height:1.5;">You are losing sales because nobody replied fast enough.</div>
          </div>
          <div style="display:flex; gap:12px; align-items:flex-start;">
             <div style="color:#0B9E58; margin-top:2px;">•</div>
             <div style="font-size:16px; color:#555; line-height:1.5;">You answer the same handful of questions every day and have started to resent them.</div>
          </div>
          <div style="display:flex; gap:12px; align-items:flex-start;">
             <div style="color:#0B9E58; margin-top:2px;">•</div>
             <div style="font-size:16px; color:#555; line-height:1.5;">You want to decide what the AI is allowed to say.</div>
          </div>
       </div>
    </div>
    
    <!-- Bad Fit Card -->
    <div style="background:#fff; border:1px solid var(--border-subtle); border-radius:24px; padding:40px; box-shadow: 0 12px 40px rgba(0,0,0,0.04); display:flex; flex-direction:column; gap:24px; transition:0.3s; position:relative; overflow:hidden;" onmouseover="this.style.borderColor='#DB4437'; this.style.boxShadow='0 12px 40px rgba(219,68,55,0.1)'" onmouseout="this.style.borderColor='var(--border-subtle)'; this.style.boxShadow='0 12px 40px rgba(0,0,0,0.04)'">
       <div style="position:absolute; top:0; left:0; width:6px; height:100%; background:#DB4437;"></div>
       <div style="display:flex; align-items:center; gap:12px;">
          <div style="width:40px; height:40px; border-radius:12px; background:#FCE8E6; display:flex; align-items:center; justify-content:center;">
             <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#DB4437" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
          </div>
          <h3 style="font-family:'Outfit'; font-size:24px; font-weight:600; margin:0; color:#111;">Probably not, if...</h3>
       </div>
       
       <div style="display:flex; flex-direction:column; gap:16px;">
          <div style="display:flex; gap:12px; align-items:flex-start;">
             <div style="color:#DB4437; margin-top:2px;">•</div>
             <div style="font-size:16px; color:#555; line-height:1.5;">You want an AI running loose with nobody checking on it.</div>
          </div>
          <div style="display:flex; gap:12px; align-items:flex-start;">
             <div style="color:#DB4437; margin-top:2px;">•</div>
             <div style="font-size:16px; color:#555; line-height:1.5;">You are hoping to let your support team go.</div>
          </div>
          <div style="display:flex; gap:12px; align-items:flex-start;">
             <div style="color:#DB4437; margin-top:2px;">•</div>
             <div style="font-size:16px; color:#555; line-height:1.5;">You expect it to work properly without anyone setting it up.</div>
          </div>
       </div>
    </div>
    
  </div>
  
</section>
\"\"\"
"""

# Inject CUSTOM_FIT before CUSTOM_HOME_ACCORDION
acc_idx = content.find('CUSTOM_HOME_ACCORDION = """')
if acc_idx != -1:
    content = content[:acc_idx] + CUSTOM_FIT + "\n\n" + content[acc_idx:]

# Inject logic condition in the blocks loop
logic_marker = 'if data["route"] == "" and "Internal Copilot" in block["title"]:\n            html_content += CUSTOM_COPILOT\n            continue'
logic_insert = '''
        if data["route"] == "" and "Honest Fit" in block["title"]:
            html_content += CUSTOM_FIT
            continue
'''
if logic_marker in content:
    content = content.replace(logic_marker, logic_marker + "\n" + logic_insert)
else:
    print("Logic marker not found!")

with open('build_v11_compiler.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated compiler with Honest Fit visualization!")
