import re

file_path = "c:\\Users\\user\\Downloads\\HOME STAEP AI\\StepsAI_Redesign.html"

reconstructed_css = """
    /* --- RECONSTRUCTED CSS FOR REMAINING SECTIONS --- */
    
    /* CREDIBILITY STRIP */
    .credibility { padding: 40px 5%; background: white; text-align: center; border-bottom: 1px solid #F1F5F9; }
    .credibility-text { font-size: 13px; font-weight: 600; color: #94A3B8; margin-bottom: 20px; text-transform: uppercase; letter-spacing: 1px; }
    .credibility-logos { display: flex; justify-content: center; gap: 40px; flex-wrap: wrap; }
    .credibility-logos span { font-size: 18px; font-weight: 700; color: #cbd5e1; }
    
    /* WORKFLOW (SETUP) */
    .workflow { padding: 100px 5%; background: #FAFAFA; }
    .flow-container { max-width: 1200px; margin: 0 auto; display: flex; align-items: flex-start; justify-content: space-between; gap: 20px; }
    .flow-node { flex: 1; background: white; padding: 24px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.03); border: 1px solid rgba(0,0,0,0.02); }
    .flow-node h3 { font-size: 18px; font-weight: 700; margin-bottom: 8px; color: #111827; }
    .dashed-line { flex-grow: 0; width: 40px; height: 2px; background: repeating-linear-gradient(90deg, #CBD5E1 0, #CBD5E1 4px, transparent 4px, transparent 8px); margin-top: 40px; }
    .tag { display: inline-block; padding: 6px 12px; background: #F1F5F9; border-radius: 8px; font-size: 12px; font-weight: 500; color: #475569; margin-right: 8px; margin-bottom: 8px; }
    .tag-success { display: inline-block; padding: 6px 12px; background: #ECFDF5; border: 1px solid #A7F3D0; border-radius: 8px; font-size: 12px; font-weight: 600; color: #059669; }
    
    /* CHANNELS */
    .channels-section { padding: 100px 5%; background: white; }
    .channels-grid { max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; }
    .channel-card { background: white; border: 1px solid #F1F5F9; padding: 30px; border-radius: 20px; text-align: center; transition: transform 0.2s, box-shadow 0.2s; }
    .channel-card:hover { transform: translateY(-5px); box-shadow: 0 20px 40px rgba(0,0,0,0.05); }
    .channel-icon { font-size: 36px; margin-bottom: 20px; }
    .channel-card h3 { font-size: 18px; font-weight: 700; margin-bottom: 10px; color: #111827; }
    
    /* FOUR AGENTS (BENTO GRID) */
    .agents-section { padding: 100px 5%; background: #FAFAFA; }
    .bento-grid { max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; gap: 30px; }
    .bento-card { background: white; border-radius: 24px; box-shadow: 0 10px 30px rgba(0,0,0,0.03); border: 1px solid rgba(0,0,0,0.02); overflow: hidden; display: flex; flex-direction: column; }
    .bento-header { padding: 30px; display: flex; gap: 20px; align-items: flex-start; border-bottom: 1px solid #F1F5F9; }
    .agent-icon { width: 50px; height: 50px; background: #3B82F6; color: white; font-size: 24px; font-weight: 800; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
    .agent-title { font-size: 20px; font-weight: 700; color: #111827; margin-bottom: 8px; }
    .agent-desc { font-size: 14px; color: #64748B; line-height: 1.5; }
    .bento-content { padding: 30px; flex: 1; background: #F8FAFC; }
    .chat-mockup { background: white; border: 1px solid #E5E7EB; border-radius: 16px; padding: 20px; }
    .chat-bubble { padding: 12px 16px; border-radius: 12px; font-size: 13px; line-height: 1.4; margin-bottom: 12px; max-width: 90%; background: #F1F5F9; color: #1F2937; border-bottom-left-radius: 4px; }
    .chat-bubble.blue { background: #E0E7FF; color: #1E3A8A; margin-left: auto; border-bottom-left-radius: 12px; border-bottom-right-radius: 4px; }
    .glass-pill { padding: 8px 16px; background: white; border: 1px solid #E5E7EB; border-radius: 100px; font-size: 12px; font-weight: 500; color: #4B5563; }
    .glass-pill.blue-bg { background: #4F46E5; color: white; border-color: #4F46E5; }
    
    /* INDUSTRIES (ACCORDION) */
    .industries-section { padding: 100px 5%; background: white; }
    .accordion { max-width: 1200px; margin: 0 auto; height: 400px; display: flex; gap: 20px; }
    .accordion-item { flex: 1; border-radius: 24px; background-size: cover; background-position: center; position: relative; overflow: hidden; transition: flex 0.4s cubic-bezier(0.4, 0, 0.2, 1); cursor: pointer; }
    .accordion-item::before { content: ''; position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0.2) 100%); }
    .accordion-item:hover { flex: 3; }
    .accordion-content { position: absolute; bottom: 0; left: 0; width: 100%; padding: 30px; color: white; }
    .accordion-content h3 { font-size: 24px; font-weight: 700; margin-bottom: 10px; white-space: nowrap; }
    .accordion-content p { font-size: 14px; line-height: 1.5; opacity: 0; transition: opacity 0.3s; }
    .accordion-item:hover .accordion-content p { opacity: 1; }
    
    /* CARDS SECTION */
    .cards-section { padding: 100px 5%; background: #FAFAFA; text-align: center; }
    .cards-section h2 { font-size: 2.5rem; font-weight: 800; color: #111827; margin-bottom: 50px; }
    .grid { max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; gap: 30px; }
    .card { height: 300px; border-radius: 24px; overflow: hidden; position: relative; text-align: left; }
    .card-bg { position: absolute; inset: 0; background-size: cover; background-position: center; transition: transform 0.5s; }
    .card:hover .card-bg { transform: scale(1.05); }
    .card-overlay { position: absolute; inset: 0; background: linear-gradient(to right, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0.2) 100%); padding: 40px; display: flex; flex-direction: column; justify-content: space-between; color: white; }
    .card-logo { font-size: 20px; font-weight: 800; }
    .card-stat { font-size: 48px; font-weight: 800; margin-bottom: 10px; color: #3B82F6; }
    .card-desc { font-size: 16px; font-weight: 500; max-width: 80%; line-height: 1.4; }
"""

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to insert this CSS right before the </style> tag
content = re.sub(r'</style>', reconstructed_css + '\n</style>', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Reconstructed CSS appended successfully.")
