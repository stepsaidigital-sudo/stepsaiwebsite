import re

file_path = "c:\\Users\\user\\Downloads\\HOME STAEP AI\\StepsAI_Redesign.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS to add slide-in animations and typing dots
activity_css = """
    /* --- ACTIVITY LOOP CSS --- */
    @keyframes slideUpMsg {
        0% { opacity: 0; transform: translateY(10px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    .msg-animate { animation: slideUpMsg 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards; }
    
    /* Typing Indicator */
    .typing-dots { display: flex; gap: 4px; padding: 12px 16px; background: white; border-radius: 12px; border-bottom-left-radius: 4px; width: max-content; }
    .typing-dots span { width: 6px; height: 6px; background: #94A3B8; border-radius: 50%; animation: typingBounce 1.4s infinite ease-in-out both; }
    .typing-dots span:nth-child(1) { animation-delay: -0.32s; }
    .typing-dots span:nth-child(2) { animation-delay: -0.16s; }
    @keyframes typingBounce {
        0%, 80%, 100% { transform: scale(0); }
        40% { transform: scale(1); }
    }
    
    /* Hide scrollbar for smooth look */
    .fw-chat-body::-webkit-scrollbar { display: none; }
    .fw-chat-body { -ms-overflow-style: none; scrollbar-width: none; scroll-behavior: smooth; }
    .fw-arrivals::-webkit-scrollbar { display: none; }
    .fw-arrivals { -ms-overflow-style: none; scrollbar-width: none; scroll-behavior: smooth; }
"""

# Insert CSS before </style>
content = content.replace('</style>', activity_css + '\n</style>')

# 2. Empty the hardcoded chat body so JS can populate it
chat_body_pattern = re.compile(r'<div class="fw-chat-body">.*?</div>\s*<div class="fw-chat-input">', re.DOTALL)
empty_chat_body = """<div class="fw-chat-body" id="autoChatStream">
              <!-- Populated by JS -->
          </div>
          <div class="fw-chat-input">"""
content = chat_body_pattern.sub(empty_chat_body, content)

# 3. Add IDs to Home Widget for JS scrolling
content = content.replace('<div class="fw-arrivals">', '<div class="fw-arrivals" id="autoHomeScroll">')


# 4. Inject the JavaScript Loop
js_activity_script = """
<script>
    // --- MOCKUP ACTIVITY LOOP ---
    document.addEventListener("DOMContentLoaded", function() {
        
        // 1. Chat Widget Automated Loop
        const chatStream = document.getElementById('autoChatStream');
        
        const userMsg = `<div class="fw-sent msg-animate" style="opacity:0;">Tell me about Air Max Pro</div>`;
        
        const typingMsg = `
            <div class="fw-bot-row msg-animate" id="typingIndicator" style="opacity:0;">
                <div class="fw-bot-avatar">👟</div>
                <div class="typing-dots"><span></span><span></span><span></span></div>
            </div>
        `;
        
        const botReply = `
            <div class="fw-bot-row msg-animate" style="opacity:0;">
                <div class="fw-bot-avatar">👟</div>
                <div class="fw-bot-content">
                    <div class="fw-bot-text">Based on your request, here are our top recommendations. <strong>Tap any item for details.</strong></div>
                </div>
            </div>
        `;
        
        const card1 = `
            <div class="fw-bot-row msg-animate" style="opacity:0;">
                <div class="fw-bot-avatar" style="visibility:hidden;">👟</div>
                <div class="fw-bot-content">
                    <div class="fw-prod-card active">
                        <div class="fw-pc-top">
                            <img src="https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=200&h=200&fit=crop" class="fw-pc-img">
                            <div class="fw-pc-info">
                                <h4 class="fw-pc-title">Air Max Pro</h4>
                                <h3 class="fw-pc-price">$120.00</h3>
                                <div class="fw-pc-size-row">SIZE: <span class="fw-size-pill active">US 9</span> <span class="fw-size-pill">US 10</span></div>
                            </div>
                        </div>
                        <button class="fw-pc-add">+ Add</button>
                    </div>
                </div>
            </div>
        `;
        
        const card2 = `
            <div class="fw-bot-row msg-animate" style="opacity:0;">
                <div class="fw-bot-avatar" style="visibility:hidden;">👟</div>
                <div class="fw-bot-content">
                    <div class="fw-prod-card">
                        <div class="fw-pc-top">
                            <img src="https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?w=200&h=200&fit=crop" class="fw-pc-img">
                            <div class="fw-pc-info">
                                <h4 class="fw-pc-title" style="color:#0F172A">Urban High Tops</h4>
                                <h3 class="fw-pc-price">$95.00</h3>
                                <div class="fw-pc-size-row">SIZE: <span class="fw-size-pill active">US 9</span> <span class="fw-size-pill">US 10</span></div>
                            </div>
                        </div>
                        <button class="fw-pc-add">+ Add</button>
                    </div>
                </div>
            </div>
        `;

        function runChatLoop() {
            if(!chatStream) return;
            chatStream.innerHTML = '';
            
            // Step 1: User types
            setTimeout(() => { 
                chatStream.insertAdjacentHTML('beforeend', userMsg); 
                chatStream.scrollTop = chatStream.scrollHeight;
            }, 1000);
            
            // Step 2: Bot thinks
            setTimeout(() => { 
                chatStream.insertAdjacentHTML('beforeend', typingMsg); 
                chatStream.scrollTop = chatStream.scrollHeight;
            }, 2000);
            
            // Step 3: Bot replies
            setTimeout(() => { 
                const indicator = document.getElementById('typingIndicator');
                if(indicator) indicator.remove();
                chatStream.insertAdjacentHTML('beforeend', botReply); 
                chatStream.scrollTop = chatStream.scrollHeight;
            }, 4000);
            
            // Step 4: Card 1
            setTimeout(() => { 
                chatStream.insertAdjacentHTML('beforeend', card1); 
                chatStream.scrollTop = chatStream.scrollHeight;
            }, 4500);
            
            // Step 5: Card 2
            setTimeout(() => { 
                chatStream.insertAdjacentHTML('beforeend', card2); 
                chatStream.scrollTop = chatStream.scrollHeight;
            }, 5000);
            
            // Loop it
            setTimeout(runChatLoop, 11000);
        }
        
        runChatLoop();
        
        // 2. Home Widget Automated Scroll Loop
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

content = content.replace('</body>', js_activity_script)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("JS Activity Loop injected successfully.")
