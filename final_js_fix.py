import os

base_dir = r"c:\Users\user\Downloads\HOME STAEP AI"

count = 0
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if "{{" in content or "}}" in content:
                # Replace all double braces
                content = content.replace("{{", "{").replace("}}", "}")
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
                
print(f"Bruteforce fixed JS syntax in {count} HTML files!")
