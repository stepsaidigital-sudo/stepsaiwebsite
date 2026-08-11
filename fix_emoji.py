with open('build_v11_compiler.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('🛑', '!')
text = text.replace('🎉', '!')
text = text.replace('👋', '!')
text = text.replace('🚀', '>')

with open('build_v11_compiler.py', 'w', encoding='utf-8') as f:
    f.write(text)
