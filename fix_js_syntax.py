import os

base_dir = r"c:\Users\user\Downloads\HOME STAEP AI"

def fix_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The GSAP script was written with {{ and }} because it was in a python string intended for .format(), 
    # but the FOOTER string was never formatted! So the literal {{ and }} ended up in the JS, causing SyntaxError.
    
    if "{{ y: 0" in content or "{{ trigger: element" in content:
        # We only want to replace double braces in the script block
        import re
        content = re.sub(r'\{\{(.*?)\}\}', r'{\1}', content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

count = 0
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            if fix_html_file(os.path.join(root, file)):
                count += 1
                
print(f"Fixed Javascript SyntaxError in {count} HTML files!")
