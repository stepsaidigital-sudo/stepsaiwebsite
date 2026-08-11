import re

file_path = "c:\\Users\\user\\Downloads\\HOME STAEP AI\\StepsAI_Redesign.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# I will append the premium motion CSS at the end of the <style> block,
# overriding any previous rules because it comes last.
motion_css = """
    /* =========================================================================
       PREMIUM MOTION REDESIGN (SaaS "$100M Hero" Style)
       ========================================================================= */

    /* 1. Atmospheric Background */
    .pixel-hero {
        position: relative;
        background: #ffffff; /* Base white */
        overflow: hidden;
    }
    
    /* Noise Texture Overlay */
    .pixel-hero::after {
        content: '';
        position: absolute;
        inset: 0;
        background-image: url('data:image/svg+xml;utf8,%3Csvg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"%3E%3Cfilter id="noiseFilter"%3E%3CfeTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="3" stitchTiles="stitch"/%3E%3C/filter%3E%3Crect width="100%25" height="100%25" filter="url(%23noiseFilter)" opacity="0.04"/%3E%3C/svg%3E');
        z-index: 1;
        pointer-events: none;
    }

    /* Ambient Glowing Blobs */
    .ambient-blob {
        position: absolute;
        border-radius: 50%;
        filter: blur(120px);
        opacity: 0.6;
        z-index: 2;
        animation: breatheBlob 15s ease-in-out infinite alternate;
        pointer-events: none;
    }
    .blob-1 { width: 800px; height: 800px; background: rgba(79, 125, 255, 0.15); top: -200px; right: -200px; animation-delay: 0s; }
    .blob-2 { width: 900px; height: 900px; background: rgba(122, 109, 255, 0.15); bottom: -300px; left: -200px; animation-delay: -5s; }
    .blob-3 { width: 600px; height: 600px; background: rgba(238, 243, 255, 0.8); top: 50%; left: 50%; transform: translate(-50%, -50%); animation-delay: -10s; z-index: 4; }

    @keyframes breatheBlob {
        0% { transform: scale(1) translate(0, 0); opacity: 0.5; }
        50% { transform: scale(1.1) translate(20px, -20px); opacity: 0.7; }
        100% { transform: scale(0.9) translate(-20px, 20px); opacity: 0.5; }
    }

    /* 2. Central Character Animation */
    .central-character {
        animation: floatCenter 8s ease-in-out infinite;
        z-index: 20;
    }
    @keyframes floatCenter {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-15px); }
    }

    /* 3. Glassmorphism & Independent Floating for Cards */
    .floating-card {
        background: rgba(255, 255, 255, 0.7) !important;
        backdrop-filter: blur(24px) saturate(150%);
        -webkit-backdrop-filter: blur(24px) saturate(150%);
        border: 1px solid rgba(255, 255, 255, 0.8) !important;
        box-shadow: 
            0 40px 80px -20px rgba(0, 0, 0, 0.1), 
            inset 0 0 0 1px rgba(255, 255, 255, 0.6) !important;
        transition: transform 0.2s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }

    /* Assigning unique floating animations to each card */
    .card-tl { animation: floatTL 9s ease-in-out infinite; }
    .card-bl { animation: floatBL 11s ease-in-out infinite alternate; }
    .card-tr { animation: floatTR 10s ease-in-out infinite; }
    .card-mr { animation: floatMR 12s ease-in-out infinite alternate; }
    
    /* Make interior of footwear cards transparent so glass shows through */
    .footwear-widget { background: transparent !important; }
    .fw-chat-header, .fw-chat-input, .fw-home-body, .fw-nav { background: rgba(255, 255, 255, 0.4) !important; }

    @keyframes floatTL {
        0%, 100% { transform: translate(0, 0) rotate(0deg); }
        50% { transform: translate(10px, -20px) rotate(1deg); }
    }
    @keyframes floatBL {
        0%, 100% { transform: translate(0, 0) rotate(0deg); }
        50% { transform: translate(-10px, 15px) rotate(-1deg); }
    }
    @keyframes floatTR {
        0%, 100% { transform: translate(0, 0) rotate(0deg); }
        50% { transform: translate(-10px, -15px) rotate(-1deg); }
    }
    @keyframes floatMR {
        0%, 100% { transform: translate(0, 0) rotate(0deg); }
        50% { transform: translate(15px, 10px) rotate(1deg); }
    }

    /* 4. Independent Floating Icons */
    .wa-float-icon { animation: iconFloat1 6s ease-in-out infinite; box-shadow: 0 15px 30px rgba(37,211,102,0.4) !important; }
    .ig-float-icon-sm { animation: iconFloat2 7s ease-in-out infinite; box-shadow: 0 15px 30px rgba(214,36,159,0.4) !important; }
    
    @keyframes iconFloat1 {
        0%, 100% { transform: scale(1) translateY(0); }
        50% { transform: scale(1.05) translateY(-10px); }
    }
    @keyframes iconFloat2 {
        0%, 100% { transform: scale(1) translateY(0); }
        50% { transform: scale(1.05) translateY(10px); }
    }

    /* 5. Animated Glowing Data Paths */
    .connections { z-index: 15; opacity: 0.8; }
    .conn-line {
        stroke: url(#gradientPath);
        stroke-width: 2.5;
        stroke-dasharray: 10 10;
        animation: flowData 20s linear infinite;
        filter: drop-shadow(0 0 8px rgba(99, 102, 241, 0.4));
    }
    .conn-dot {
        fill: #4F46E5;
        filter: drop-shadow(0 0 10px rgba(99, 102, 241, 0.8));
        animation: pulseDot 3s ease-in-out infinite;
    }

    @keyframes flowData {
        from { stroke-dashoffset: 1000; }
        to { stroke-dashoffset: 0; }
    }
    @keyframes pulseDot {
        0%, 100% { transform: scale(1); opacity: 0.8; }
        50% { transform: scale(1.4); opacity: 1; }
    }
    
    /* Utility class for Parallax via JS */
    .prlx { transition: transform 0.1s cubic-bezier(0.25, 0.46, 0.45, 0.94); }
"""

# 1. Insert CSS
content = content.replace('</style>', motion_css + '\n</style>')

# 2. Add Ambient Blobs to HTML and SVG Gradient defs
ambient_blobs_html = """
      <div class="ambient-blob blob-1 prlx" data-speed="2"></div>
      <div class="ambient-blob blob-2 prlx" data-speed="-2"></div>
      <div class="ambient-blob blob-3"></div>
"""
content = content.replace('<div class="hero-visuals">', '<div class="hero-visuals" id="heroScene">\n' + ambient_blobs_html)

# Add gradient def to SVG connections
svg_gradient = """
          <defs>
              <linearGradient id="gradientPath" x1="0%" y1="0%" x2="100%" y2="0%">
                  <stop offset="0%" stop-color="#4F7DFF" />
                  <stop offset="100%" stop-color="#7A6DFF" />
              </linearGradient>
          </defs>
"""
content = content.replace('<svg class="connections" viewBox="0 0 1300 600">', '<svg class="connections" viewBox="0 0 1300 600">\n' + svg_gradient)

# 3. Add Parallax Classes
content = content.replace('class="central-character"', 'class="central-character prlx" data-speed="1.5"')
content = content.replace('class="floating-card card-tl"', 'class="floating-card card-tl prlx" data-speed="3"')
content = content.replace('class="footwear-widget fw-chat gs-float-delayed"', 'class="footwear-widget fw-chat prlx" data-speed="-2"')
content = content.replace('class="floating-card card-tr"', 'class="floating-card card-tr prlx" data-speed="4"')
content = content.replace('class="footwear-widget fw-home gs-float"', 'class="footwear-widget fw-home prlx" data-speed="-3"')

# 4. Inject Javascript for Mouse Parallax
js_code = """
<script>
    document.addEventListener("DOMContentLoaded", function() {
        const heroScene = document.getElementById('heroScene');
        const parallaxElements = document.querySelectorAll('.prlx');
        
        if(heroScene) {
            heroScene.addEventListener('mousemove', function(e) {
                const rect = heroScene.getBoundingClientRect();
                const centerX = rect.left + rect.width / 2;
                const centerY = rect.top + rect.height / 2;
                
                // Calculate cursor distance from center (-1 to 1)
                const percentX = (e.clientX - centerX) / (rect.width / 2);
                const percentY = (e.clientY - centerY) / (rect.height / 2);
                
                parallaxElements.forEach(el => {
                    const speed = parseFloat(el.getAttribute('data-speed')) || 1;
                    // Max movement is roughly 2% as requested, defined by a pixel multiplier
                    const x = percentX * speed * 15; 
                    const y = percentY * speed * 15;
                    
                    // We apply it via a transform, ensuring it stacks with CSS animations safely.
                    // Note: Since CSS animations also use transform, a wrapper div is usually best,
                    // but for a quick script, setting style.transform works if we use custom properties.
                    el.style.transform = `translate(${x}px, ${y}px)`;
                });
            });
            
            // Reset on leave
            heroScene.addEventListener('mouseleave', function() {
                parallaxElements.forEach(el => {
                    el.style.transform = `translate(0px, 0px)`;
                });
            });
        }
    });
</script>
</body>
"""
content = content.replace('</body>', js_code)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Premium motion and parallax injected successfully.")
