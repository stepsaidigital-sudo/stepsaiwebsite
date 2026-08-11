with open('build_v11_compiler.py', 'r', encoding='utf-8') as f:
    content = f.read()

# The string "\nCUSTOM_ONE_INBOX =" was injected before '"""\n\nCUSTOM_HOME_ACCORDION'
# This means we have a chunk inside the file that looks like this:
# </style>
# 
# CUSTOM_ONE_INBOX = """
# ...
# </style>
# """
# """
# 
# CUSTOM_HOME_ACCORDION = """

# Let's fix this by splitting out CUSTOM_ONE_INBOX.
marker1 = '\\nCUSTOM_ONE_INBOX = """'
inbox_start = content.find(marker1)
if inbox_start != -1:
    inbox_end = content.find('"""\\n"""\\n\\nCUSTOM_HOME_ACCORDION')
    if inbox_end != -1:
        # Extract the entire NEW_INBOX chunk
        new_inbox = content[inbox_start : inbox_end + 3] # captures up to the first """
        
        # Remove it from inside CUSTOM_SETUP
        content = content[:inbox_start] + content[inbox_end + 3:]
        
        # Now content looks like:
        # ...
        # </style>
        # """
        # 
        # CUSTOM_HOME_ACCORDION = """
        
        # We want to place new_inbox AFTER CUSTOM_SETUP closing quotes
        target = '"""\\n\\nCUSTOM_HOME_ACCORDION'
        content = content.replace(target, target + "\\n" + new_inbox + "\\n")
        
with open('build_v11_compiler.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Fix applied.")
