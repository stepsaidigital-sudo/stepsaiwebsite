import os
import re

base_dir = r"c:\Users\user\Downloads\HOME STAEP AI"

def fix_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Calculate depth to root based on path
    rel_path = os.path.relpath(filepath, base_dir)
    depth = rel_path.count(os.sep)
    if rel_path == "." or rel_path == "StepsAI_Redesign.html" or rel_path == "index.html":
        depth = 0
        
    root_prefix = "../" * depth if depth > 0 else "./"
    
    # We will use string replacements because regex replacement can be dangerous if we already messed it up.
    # First, let's normalize everything back to absolute paths to start fresh.
    # Wait, it's easier to just do a smart regex.
    
    # 1. Fix CSS link
    # It might be href="/assets/css/style.css" or href="../assets/css/style.cssindex.html"
    content = re.sub(r'href="[^"]*assets/css/style\.css[^"]*"', f'href="{root_prefix}assets/css/style.css"', content)
    
    # 2. Fix JS links just in case (though they are absolute https://)
    
    # 3. Fix internal navigation links. 
    # Any link that starts with / and is not assets should be converted to relative.
    # Since we might have already messed them up like `href="../../product/ai-agents/index.htmlindex.html"`,
    # let's just use a clean predefined dictionary or a clean regex.
    
    # Clean up double index.html
    content = content.replace("index.htmlindex.html", "index.html")
    
    # Find all hrefs
    def replacer(match):
        original = match.group(1)
        if original.startswith("http") or original.startswith("mailto:") or original.startswith("#"):
            return f'href="{original}"'
            
        # If it's an asset, we already fixed CSS, but for other assets:
        if "assets/" in original:
            if original.startswith("/"):
                return f'href="{root_prefix}{original.lstrip("/")}"'
            return f'href="{original}"'
            
        # Clean the original link to get the core route
        core_route = original.replace(root_prefix, "").replace("index.html", "").strip("/")
        
        if not core_route:
            return f'href="{root_prefix}StepsAI_Redesign.html"'
            
        return f'href="{root_prefix}{core_route}/index.html"'

    # Replace any href that doesn't point to .css
    content = re.sub(r'href="([^"]+)"', lambda m: m.group(0) if '.css' in m.group(1) else replacer(m), content)

    # Some extra cleanup for root index.html reference
    content = content.replace(f'href="{root_prefix}/index.html"', f'href="{root_prefix}StepsAI_Redesign.html"')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return True

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            fix_html_file(os.path.join(root, file))
            
print("Fixed all relative links for offline viewing!")
