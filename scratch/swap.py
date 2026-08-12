import re

with open("inject_copilot.py", "r", encoding="utf-8") as file:
    content = file.read()

text_div = """  <div style="flex:1;">
    <span class="gsap-fade-up" style="font-family: 'Geist Mono', monospace; font-size: 12px; color: var(--accent); letter-spacing: .2em; text-transform: uppercase; margin-bottom:16px; display:block;">INTERNAL COPILOT</span>
    <h2 class="gsap-fade-up" style="font-family: 'Outfit'; font-size: clamp(40px, 4vw, 56px); margin: 0 0 24px; color: var(--text-primary); line-height:1.1;">The same brain, pointed inwards.</h2>
    <p class="gsap-fade-up" style="font-size: 18px; color: var(--text-secondary); margin-bottom: 24px; line-height: 1.6; max-width:500px;">Your team asks it where the leave policy lives, what you agreed with that client in March, which version of the deck is the current one.</p>
    <p class="gsap-fade-up" style="font-size: 18px; color: var(--text-secondary); margin-bottom: 32px; line-height: 1.6; max-width:500px;">It looks through everything you have connected, answers, and shows you exactly which document it got that from.</p>
    
    <a href="#" class="gsap-fade-up" style="display:inline-flex; align-items:center; gap:8px; color:var(--text-primary); font-weight:600; text-decoration:none; border-bottom:1px solid var(--text-primary); padding-bottom:4px;">
       See Internal Copilot
       <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14"></path><path d="M12 5l7 7-7 7"></path></svg>
    </a>
  </div>"""

content = content.replace(text_div, "|||TEXT_DIV|||")
content = content.replace('</section>', text_div + "\n</section>")
content = content.replace("|||TEXT_DIV|||\n  \n", "")

with open("inject_copilot.py", "w", encoding="utf-8") as file:
    file.write(content)
print("Swapped successfully")
