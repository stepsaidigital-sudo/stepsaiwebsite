import re

with open('build_v11_compiler.py', 'r', encoding='utf-8') as f:
    content = f.read()

FAQ_REPLACEMENT = """
        is_faq = "FAQ" in block["title"].upper()
        
        if is_faq:
            html_content += '''
            <style>
              .faq-split-section { display: flex; gap: 80px; align-items: flex-start; max-width: 1200px; margin: 0 auto; padding: 120px 32px; }
              .faq-left { flex: 1; position: sticky; top: 120px; }
              .faq-right { flex: 1.5; display: flex; flex-direction: column; border-top: 1px solid #eaeaea; }
              .faq-item { border-bottom: 1px solid #eaeaea; overflow: hidden; }
              .faq-question { padding: 24px 0; display: flex; justify-content: space-between; align-items: center; cursor: pointer; font-family: 'Inter', sans-serif; font-size: 18px; font-weight: 700; color: #111; user-select: none; }
              .faq-icon { font-size: 24px; font-weight: 300; color: #111; transition: transform 0.3s ease; }
              .faq-item.active .faq-icon { transform: rotate(45deg); }
              .faq-answer { max-height: 0; overflow: hidden; transition: max-height 0.3s ease, padding 0.3s ease; font-size: 16px; color: #666; line-height: 1.6; padding: 0 0; }
              .faq-item.active .faq-answer { max-height: 500px; padding: 0 0 24px 0; }
              @media (max-width: 900px) {
                 .faq-split-section { flex-direction: column; gap: 40px; padding: 80px 24px; }
                 .faq-left { position: static; }
              }
            </style>
            <section class="section-v2" style="background: #ffffff; padding: 0;">
               <div class="faq-split-section">
                 <div class="faq-left gsap-fade-up">
                    <h2 style="font-family: 'Outfit'; font-size: clamp(40px, 5vw, 56px); font-weight: 800; color: #111; margin-bottom: 24px; line-height: 1.1; letter-spacing: -0.02em;">You should have questions.</h2>
                    <p style="font-size: 18px; color: #666; line-height: 1.6; margin-bottom: 32px; font-family: 'Inter', sans-serif;">The most useful homepage FAQs reduce purchase anxiety.<br>They should not become an SEO keyword dump.</p>
                    <a href="#" style="color: #0B9E58; font-weight: 600; text-decoration: none; font-size: 16px; display: inline-flex; align-items: center; gap: 8px; font-family: 'Inter', sans-serif;">Still unsure? Talk to a human <span style="font-size: 18px;">&rarr;</span></a>
                 </div>
                 <div class="faq-right gsap-fade-up">
            '''
            q = ""
            a = []
            for c in block["content"]:
                c_clean = c.replace('>', '').strip()
                if c_clean.startswith('**') and '?' in c_clean:
                    if q:
                        html_content += f'''
                        <div class="faq-item" onclick="this.classList.toggle('active')">
                            <div class="faq-question">{q} <span class="faq-icon">+</span></div>
                            <div class="faq-answer">{chr(10).join(a)}</div>
                        </div>'''
                    q = c_clean.replace('**', '').strip()
                    a = []
                elif c_clean:
                    a.append(parse_markdown_line(c_clean))
            if q:
                html_content += f'''
                <div class="faq-item" onclick="this.classList.toggle('active')">
                    <div class="faq-question">{q} <span class="faq-icon">+</span></div>
                    <div class="faq-answer">{chr(10).join(a)}</div>
                </div>'''
            html_content += '''
                 </div>
               </div>
            </section>
            '''
"""

# The regex matches from `is_faq = "FAQ" ...` down to the first `html_content += '</div></section>'`
pattern = r'is_faq\s*=\s*"FAQ"\s*in\s*block\["title"\]\.upper\(\)[\s\S]*?html_content\s*\+=\s*\'</div></section>\''

if re.search(pattern, content):
    content = re.sub(pattern, FAQ_REPLACEMENT, content, count=1)
    with open('build_v11_compiler.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Injected custom FAQ layout!")
else:
    print("Could not find FAQ block to replace.")
