import re

file_path = "c:\\Users\\user\\Downloads\\HOME STAEP AI\\StepsAI_Redesign.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# --- 1. CSS CHANGES ---

# Background & Grid Polish
css_replacements = [
    (r'body \{ background: #F8FAFC; overflow-x: hidden; font-family: \'Inter\', sans-serif; \}', 
     r':root { --theme-color: #3B82F6; --theme-bg: #EFF6FF; }\n    body { background: #F8FAFC; overflow-x: hidden; font-family: \'Inter\', sans-serif; }\n    .hero-section { background-image: radial-gradient(rgba(0, 0, 0, 0.05) 1px, transparent 1px); background-size: 24px 24px; }'),
     
    # Central glow richer
    (r'.central-glow \{ position: absolute; top: 10%; left: 50%; transform: translateX\(-50%\); width: 700px; height: 700px; background: radial-gradient\(circle, rgba\(99,102,241,0.08\) 0%, rgba\(255,255,255,0\) 70%\); z-index: 5; pointer-events: none; \}',
     r'.central-glow { position: absolute; top: 10%; left: 50%; transform: translateX(-50%); width: 700px; height: 700px; background: radial-gradient(circle, var(--theme-color) 0%, rgba(255,255,255,0) 70%); opacity: 0.15; z-index: 5; pointer-events: none; transition: background 1s ease; }'),

    # Ambient Blobs stronger
    (r'.ambient-blob-1 \{ position: absolute; top: 20%; left: 10%; width: 300px; height: 300px; background: #818CF8; border-radius: 50%; filter: blur\(100px\); opacity: 0.15; z-index: 1; animation: float 8s ease-in-out infinite; \}',
     r'.ambient-blob-1 { position: absolute; top: 20%; left: 10%; width: 400px; height: 400px; background: var(--theme-color); border-radius: 50%; filter: blur(120px); opacity: 0.3; z-index: 1; animation: float 8s ease-in-out infinite; transition: background 1s ease; }'),
    (r'.ambient-blob-2 \{ position: absolute; bottom: 10%; right: 10%; width: 400px; height: 400px; background: #C084FC; border-radius: 50%; filter: blur\(120px\); opacity: 0.15; z-index: 1; animation: float 10s ease-in-out infinite reverse; \}',
     r'.ambient-blob-2 { position: absolute; bottom: 10%; right: 10%; width: 400px; height: 400px; background: #C084FC; border-radius: 50%; filter: blur(120px); opacity: 0.25; z-index: 1; animation: float 10s ease-in-out infinite reverse; transition: background 1s ease; }'),

    # Layout Spreading (De-clutter)
    (r'.hero-visuals \{ position: relative; width: 100%; max-width: 1100px; height: 600px; display: flex; justify-content: center; align-items: flex-end; margin: 0 auto; \}',
     r'.hero-visuals { position: relative; width: 100%; max-width: 1250px; height: 600px; display: flex; justify-content: center; align-items: flex-end; margin: 0 auto; }'),
     
    (r'.stat-card.card-tl \{ top: 15%; left: 10%; animation-delay: 0.2s; \}',
     r'.stat-card.card-tl { top: 5%; left: 15%; animation-delay: 0.2s; }'),
    (r'.stat-card.card-tr \{ top: 15%; right: 10%; animation-delay: 0.4s; \}',
     r'.stat-card.card-tr { top: 5%; right: 15%; animation-delay: 0.4s; }'),

    # Glassmorphism on widgets & Stat Cards
    (r'.floating-card \{ position: absolute; background: white; border-radius: 20px; padding: 20px; box-shadow: 0 20px 40px rgba\(0,0,0,0.08\); z-index: 30; opacity: 0; animation: floatUp 0.8s ease-out forwards, float 6s ease-in-out infinite; border: 1px solid rgba\(255,255,255,0.5\); \}',
     r'.floating-card { position: absolute; background: rgba(255, 255, 255, 0.7); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px); border-radius: 20px; padding: 20px; box-shadow: 0 20px 40px rgba(0,0,0,0.08); z-index: 30; opacity: 0; animation: floatUp 0.8s ease-out forwards, float 6s ease-in-out infinite; border: 1px solid rgba(255,255,255,1); }'),
    
    (r'.footwear-widget \{ position: absolute; width: 340px; height: 500px; background: #F8FAFC; border-radius: 24px; box-shadow: 0 24px 48px -12px rgba\(0,0,0,0.18\); overflow: hidden; display: flex; flex-direction: column; z-index: 30; border: 1px solid rgba\(0,0,0,0.05\); font-family: \'Inter\', sans-serif; \}',
     r'.footwear-widget { position: absolute; width: 340px; height: 500px; background: rgba(248, 250, 252, 0.85); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px); border-radius: 24px; box-shadow: 0 30px 60px -15px rgba(0,0,0,0.25); overflow: hidden; display: flex; flex-direction: column; z-index: 30; border: 1px solid rgba(255,255,255,1); font-family: \'Inter\', sans-serif; }'),
     
    # Widget Layout push
    (r'\.fw-chat \{ bottom: -20px; left: -10px; transform: scale\(0.85\); transform-origin: bottom left; \}',
     r'.fw-chat { bottom: -30px; left: -30px; transform: scale(0.9); transform-origin: bottom left; }'),
    (r'\.fw-home \{ bottom: -20px; right: 0; background: white; transform: scale\(0.85\); transform-origin: bottom right; \}',
     r'.fw-home { bottom: -30px; right: -30px; background: rgba(255, 255, 255, 0.85); transform: scale(0.9); transform-origin: bottom right; backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px); }'),

    # Dynamic Theme CSS Bindings
    (r'background: #2563EB;', r'background: var(--theme-color); transition: background 1s ease;'),
    (r'background: #3B82F6;', r'background: var(--theme-color); transition: background 1s ease;'),
    (r'color: #2563EB;', r'color: var(--theme-color); transition: color 1s ease;'),
    (r'color: #3B82F6;', r'color: var(--theme-color); transition: color 1s ease;'),
    
    # Path glows
    (r'stroke="url\(#grad1\)"', r'stroke="var(--theme-color)" stroke-opacity="0.5"'),
    (r'stroke="url\(#grad2\)"', r'stroke="var(--theme-color)" stroke-opacity="0.5"'),
]

for old, new in css_replacements:
    content = re.sub(old, new, content)


# --- 2. HTML CHANGES FOR DYNAMIC INJECTION ---

# Remove SVG Gradients (replaced with theme color)
content = re.sub(r'<defs>.*?</defs>', '', content, flags=re.DOTALL)

# Add IDs to headers so JS can change them
content = content.replace('<div class="fw-prod-title">Steps Footwear AI</div>', '<div class="fw-prod-title" id="dynChatTitle">Steps Footwear AI</div>')
content = content.replace('<div class="fw-hh-text">Steps Footwear AI</div>', '<div class="fw-hh-text" id="dynHomeTitle">Steps Footwear AI</div>')

# Replace old script with new dynamic cycler script
script_start = content.find('<script>')
if script_start != -1:
    content = content[:script_start] # Snip out old script

dynamic_script = """
<script>
    document.addEventListener("DOMContentLoaded", function() {
        
        // 1. INDUSTRY DATA
        const industries = [
            {
                name: 'Steps Footwear AI',
                color: '#3B82F6', // Blue
                botIcon: '👟',
                homeBg: 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=200&h=200&fit=crop',
                homeHero: 'Hello! 👋',
                homeSub: 'Find your perfect fit today.',
                query: 'Tell me about Air Max Pro',
                reply: 'Based on your request, here are our top running shoe recommendations.',
                card1: { img: 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=200&h=200&fit=crop', title: 'Air Max Pro', price: '$120.00', pills: 'SIZE: <span class="fw-size-pill active">US 9</span> <span class="fw-size-pill">US 10</span>' },
                card2: { img: 'https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?w=200&h=200&fit=crop', title: 'Urban High Tops', price: '$95.00', pills: 'SIZE: <span class="fw-size-pill active">US 9</span> <span class="fw-size-pill">US 10</span>' }
            },
            {
                name: 'CareWell AI',
                color: '#10B981', // Emerald
                botIcon: '🩺',
                homeBg: 'https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?w=200&h=200&fit=crop',
                homeHero: 'Hello! 👋',
                homeSub: 'How can I assist with your health?',
                query: 'Book a cardiology consult',
                reply: 'Here are our top Cardiology specialists available this week.',
                card1: { img: 'https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?w=200&h=200&fit=crop', title: 'Dr. Viren Khatri', price: 'Cardiology', pills: 'AVAIL: <span class="fw-size-pill active">TODAY</span>' },
                card2: { img: 'https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=200&h=200&fit=crop', title: 'Dr. Sarah Jenkins', price: 'Pediatrics', pills: 'AVAIL: <span class="fw-size-pill active">TMRW</span>' }
            },
            {
                name: 'UrbanSpace AI',
                color: '#F59E0B', // Amber
                botIcon: '🏢',
                homeBg: 'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=200&h=200&fit=crop',
                homeHero: 'Welcome! 👋',
                homeSub: 'Find your dream space.',
                query: 'Show me 3BHKs in Gachibowli',
                reply: 'I found these premium properties matching your criteria.',
                card1: { img: 'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=200&h=200&fit=crop', title: '₹1.25 Cr Villa', price: '3 BHK', pills: 'VIEW: <span class="fw-size-pill active">VIRTUAL</span>' },
                card2: { img: 'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=200&h=200&fit=crop', title: '₹85 L Condo', price: '2 BHK', pills: 'VIEW: <span class="fw-size-pill active">IN-PERSON</span>' }
            },
            {
                name: 'LearnPro AI',
                color: '#8B5CF6', // Purple
                botIcon: '🎓',
                homeBg: 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=200&h=200&fit=crop',
                homeHero: 'Hi there! 👋',
                homeSub: 'Guide your learning journey.',
                query: 'Show me UI/UX Design courses',
                reply: 'Here are the top rated design courses starting soon.',
                card1: { img: 'https://images.unsplash.com/photo-1561070791-2526d30994b5?w=200&h=200&fit=crop', title: 'UI/UX Design', price: 'Intermediate', pills: 'FMT: <span class="fw-size-pill active">ONLINE</span>' },
                card2: { img: 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=200&h=200&fit=crop', title: 'Data Science', price: 'Beginner', pills: 'FMT: <span class="fw-size-pill active">CAMPUS</span>' }
            }
        ];
        
        let currentInd = 0;
        
        const chatStream = document.getElementById('autoChatStream');
        
        function updateTheme(ind) {
            document.documentElement.style.setProperty('--theme-color', ind.color);
            document.documentElement.style.setProperty('--theme-bg', ind.color + '15'); // 15% opacity hex
            
            const chatTitle = document.getElementById('dynChatTitle');
            if(chatTitle) chatTitle.innerText = ind.name;
            
            const homeTitle = document.getElementById('dynHomeTitle');
            if(homeTitle) homeTitle.innerText = ind.name;
            
            const avatars = document.querySelectorAll('.fw-ch-avatar, .fw-hh-logo-icon');
            avatars.forEach(el => el.innerText = ind.botIcon);
        }

        function runChatLoop() {
            if(!chatStream) return;
            chatStream.innerHTML = '';
            
            const ind = industries[currentInd];
            updateTheme(ind);
            
            const userMsg = `<div class="fw-sent msg-animate" style="opacity:0;">${ind.query}</div>`;
            const typingMsg = `
                <div class="fw-bot-row msg-animate" id="typingIndicator" style="opacity:0;">
                    <div class="fw-bot-avatar">${ind.botIcon}</div>
                    <div class="typing-dots"><span></span><span></span><span></span></div>
                </div>
            `;
            const botReply = `
                <div class="fw-bot-row msg-animate" style="opacity:0;">
                    <div class="fw-bot-avatar">${ind.botIcon}</div>
                    <div class="fw-bot-content">
                        <div class="fw-bot-text">${ind.reply}</div>
                    </div>
                </div>
            `;
            const card1 = `
                <div class="fw-bot-row msg-animate" style="opacity:0;">
                    <div class="fw-bot-avatar" style="visibility:hidden;">${ind.botIcon}</div>
                    <div class="fw-bot-content">
                        <div class="fw-prod-card active" style="border-color: var(--theme-color)">
                            <div class="fw-pc-top">
                                <img src="${ind.card1.img}" class="fw-pc-img">
                                <div class="fw-pc-info">
                                    <h4 class="fw-pc-title">${ind.card1.title}</h4>
                                    <h3 class="fw-pc-price">${ind.card1.price}</h3>
                                    <div class="fw-pc-size-row">${ind.card1.pills}</div>
                                </div>
                            </div>
                            <button class="fw-pc-add" style="background: var(--theme-color); color: white;">+ View</button>
                        </div>
                    </div>
                </div>
            `;
            const card2 = `
                <div class="fw-bot-row msg-animate" style="opacity:0;">
                    <div class="fw-bot-avatar" style="visibility:hidden;">${ind.botIcon}</div>
                    <div class="fw-bot-content">
                        <div class="fw-prod-card">
                            <div class="fw-pc-top">
                                <img src="${ind.card2.img}" class="fw-pc-img">
                                <div class="fw-pc-info">
                                    <h4 class="fw-pc-title" style="color:#0F172A">${ind.card2.title}</h4>
                                    <h3 class="fw-pc-price">${ind.card2.price}</h3>
                                    <div class="fw-pc-size-row">${ind.card2.pills}</div>
                                </div>
                            </div>
                            <button class="fw-pc-add" style="background: var(--theme-color); color: white;">+ View</button>
                        </div>
                    </div>
                </div>
            `;
            
            setTimeout(() => { chatStream.insertAdjacentHTML('beforeend', userMsg); chatStream.scrollTop = chatStream.scrollHeight; }, 1000);
            setTimeout(() => { chatStream.insertAdjacentHTML('beforeend', typingMsg); chatStream.scrollTop = chatStream.scrollHeight; }, 2000);
            setTimeout(() => { 
                const indicator = document.getElementById('typingIndicator');
                if(indicator) indicator.remove();
                chatStream.insertAdjacentHTML('beforeend', botReply); 
                chatStream.scrollTop = chatStream.scrollHeight;
            }, 4000);
            setTimeout(() => { chatStream.insertAdjacentHTML('beforeend', card1); chatStream.scrollTop = chatStream.scrollHeight; }, 4500);
            setTimeout(() => { chatStream.insertAdjacentHTML('beforeend', card2); chatStream.scrollTop = chatStream.scrollHeight; }, 5000);
            
            // Advance to next industry for next loop
            setTimeout(() => {
                currentInd = (currentInd + 1) % industries.length;
                runChatLoop();
            }, 12000);
        }
        
        runChatLoop();
        
        // Auto Scroll for right widget
        const homeScroll = document.getElementById('autoHomeScroll');
        if(homeScroll) {
            let scrollDir = 1;
            setInterval(() => {
                if(homeScroll.scrollLeft >= (homeScroll.scrollWidth - homeScroll.clientWidth - 10)) {
                    scrollDir = -1;
                } else if(homeScroll.scrollLeft <= 0) {
                    scrollDir = 1;
                }
                homeScroll.scrollBy({ left: 100 * scrollDir, behavior: 'smooth' });
            }, 3000);
        }
    });
</script>
</body>
"""

content += dynamic_script

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Dynamic Industry Cycler & Visual Polish Applied.")
