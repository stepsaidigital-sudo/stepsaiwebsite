import os

with open('build_v11_compiler.py', 'r', encoding='utf-8') as f:
    content = f.read()

CUSTOM_CTA = """
CUSTOM_CTA = \"\"\"
<section class="section-v2 cta-section" style="padding-top: 200px; padding-bottom: 200px; background: #0A0A0B; color: #fff; position: relative; overflow: hidden; text-align: center;">
  
  <!-- Drifting Receipts Background -->
  <div class="drifting-bg" style="position: absolute; top: 0; left: 0; width: 200%; height: 100%; display: flex; align-items: center; justify-content: flex-start; z-index: 0; opacity: 0.03; pointer-events: none;">
     <div class="receipt-track" style="display: flex; gap: 40px; font-family: 'Geist Mono', monospace; font-size: 80px; font-weight: 700; white-space: nowrap; text-transform: uppercase;">
        <span>CART UPDATED &bull; MEETING BOOKED &bull; LEAD CREATED &bull; ORDER TRACKED &bull; TICKET RESOLVED &bull;</span>
        <span>CART UPDATED &bull; MEETING BOOKED &bull; LEAD CREATED &bull; ORDER TRACKED &bull; TICKET RESOLVED &bull;</span>
        <span>CART UPDATED &bull; MEETING BOOKED &bull; LEAD CREATED &bull; ORDER TRACKED &bull; TICKET RESOLVED &bull;</span>
     </div>
  </div>
  
  <!-- Content -->
  <div style="position: relative; z-index: 1; max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; align-items: center;">
     
     <h2 class="gsap-fade-up" style="font-family: 'Outfit'; font-size: clamp(48px, 6vw, 80px); margin: 0 0 24px; color: #fff; line-height: 1.1; letter-spacing: -0.02em;">Somebody is typing right now.</h2>
     
     <p class="gsap-fade-up" style="font-size: 24px; color: #888; margin-bottom: 48px; line-height: 1.5; max-width: 600px;">
        Set it up this afternoon.<br>Find out what it did over breakfast.
     </p>
     
     <div class="gsap-fade-up" style="display: flex; gap: 16px; align-items: center; justify-content: center; margin-bottom: 24px; flex-wrap: wrap;">
        <a href="#" class="btn-primary" style="background: #fff; color: #111; padding: 18px 36px; border-radius: 100px; font-weight: 600; font-size: 16px; text-decoration: none; transition: 0.3s; border: 1px solid #fff;">
           Start free trial
        </a>
        <a href="#" class="btn-secondary" style="background: transparent; color: #fff; padding: 18px 36px; border-radius: 100px; font-weight: 600; font-size: 16px; text-decoration: none; transition: 0.3s; border: 1px solid rgba(255,255,255,0.2);">
           Book a demo
        </a>
     </div>
     
     <div class="gsap-fade-up" style="display: flex; gap: 16px; align-items: center; justify-content: center; color: #666; font-size: 14px; font-family: 'Geist Mono', monospace;">
        <span><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-right:6px; vertical-align:-2px;"><polyline points="20 6 9 17 4 12"></polyline></svg> No credit card</span>
        <span>&bull;</span>
        <span><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-right:6px; vertical-align:-2px;"><polyline points="20 6 9 17 4 12"></polyline></svg> Live in under an hour</span>
     </div>
     
  </div>
  
</section>
<style>
@keyframes drift {
    0% { transform: translateX(0); }
    100% { transform: translateX(-33.33%); }
}
.receipt-track {
    animation: drift 30s linear infinite;
}
.btn-primary:hover { background: #eee !important; transform: translateY(-2px); box-shadow: 0 10px 20px rgba(255,255,255,0.1); }
.btn-secondary:hover { background: rgba(255,255,255,0.1) !important; border-color: rgba(255,255,255,0.4) !important; transform: translateY(-2px); }
</style>
\"\"\"
"""

# Inject CUSTOM_CTA before CUSTOM_HOME_ACCORDION (as it's a convenient place)
acc_idx = content.find('CUSTOM_HOME_ACCORDION = """')
if acc_idx != -1:
    content = content[:acc_idx] + CUSTOM_CTA + "\n\n" + content[acc_idx:]

# Inject logic condition in the blocks loop
logic_marker = 'if data["route"] == "" and "Who this is for" in block["title"]:\n            html_content += CUSTOM_FIT\n            continue'
logic_insert = '''
        if data["route"] == "" and "Closing CTA" in block["title"]:
            html_content += CUSTOM_CTA
            continue
'''
if logic_marker in content:
    content = content.replace(logic_marker, logic_marker + "\n" + logic_insert)
else:
    print("Logic marker not found!")

with open('build_v11_compiler.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated compiler with Closing CTA visualization!")
