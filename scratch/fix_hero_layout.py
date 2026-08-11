import re

file_path = "c:\\Users\\user\\Downloads\\HOME STAEP AI\\StepsAI_Redesign.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# I will replace the CSS rules for the hero section to fix the layout.
# This means updating `.light-hero`, `.hero-layout`, `.hero-badge`, `.hero-title`, `.hero-subtitle`, `.hero-visuals`, `.central-character`, and the positioning of the floating cards.

new_hero_css = """
    .light-hero { position: relative; width: 100%; min-height: 100vh; background: radial-gradient(circle at 50% 0%, #ffffff 0%, #F5F3FF 100%); display: flex; align-items: center; justify-content: center; padding: 140px 0 100px; overflow: hidden; }
    
    .hero-layout { position: relative; z-index: 10; max-width: 1200px; width: 100%; margin: 0 auto; display: flex; flex-direction: column; align-items: center; text-align: center; padding: 0 20px; }
    
    .hero-badge { display: inline-flex; align-items: center; gap: 8px; padding: 8px 20px; border-radius: 100px; color: #6366F1; font-size: 12px; font-weight: 700; letter-spacing: 1px; margin-bottom: 24px; background: rgba(99,102,241,0.05); border: 1px solid rgba(99,102,241,0.1); }
    .hero-title { font-size: 4rem; font-weight: 800; color: #0F172A; line-height: 1.1; margin-bottom: 20px; letter-spacing: -1.5px; }
    .hero-highlight { background: linear-gradient(135deg, #4F46E5, #9333EA); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .hero-subtitle { font-size: 1.125rem; color: #64748B; max-width: 650px; line-height: 1.6; margin-bottom: 40px; }

    .hero-visuals { position: relative; width: 100%; max-width: 900px; height: 500px; display: flex; justify-content: center; align-items: flex-end; margin: 0 auto; }
    .central-character { position: relative; z-index: 20; height: 100%; max-height: 500px; object-fit: contain; filter: drop-shadow(0 20px 40px rgba(0,0,0,0.15)); }

    /* Floating Cards Shared */
    .floating-card { position: absolute; background: white; border-radius: 20px; box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.15); padding: 24px; z-index: 30; border: 1px solid rgba(0,0,0,0.05); will-change: transform; }
    
    /* Reposition Cards to stay within the 1200px layout */
    .stat-card.left { top: 10%; left: -50px; }
    .chat-card { bottom: 10%; left: -120px; }
    .stat-card.right { top: 10%; right: -50px; }
    .assistant-widget { bottom: 15%; right: -120px; z-index: 26; }
    .carousel-card { bottom: -20px; right: -80px; transform: scale(0.85); transform-origin: bottom right; }

    /* SVG Connections */
    .connections { position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none; z-index: 15; }
    .conn-line { fill: none; stroke: #94A3B8; stroke-width: 2; stroke-dasharray: 6 6; opacity: 0.5; }
    .conn-dot { fill: #4F46E5; }
    
    .trust-strip { background: rgba(255,255,255,0.8); backdrop-filter: blur(10px); padding: 16px 32px; border-radius: 100px; display: inline-flex; gap: 40px; margin-top: -20px; position: relative; z-index: 40; border: 1px solid rgba(0,0,0,0.05); box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
    .logos-strip { background: white; padding: 24px 48px; border-radius: 24px; display: flex; align-items: center; gap: 40px; margin-top: 40px; box-shadow: 0 10px 30px rgba(0,0,0,0.03); max-width: 1000px; margin-left: auto; margin-right: auto; position: relative; z-index: 40; }
"""

# We need to replace the CSS from .light-hero down to .trust-strip in the original
# Wait, it's easier to just do regex replacement for the specific blocks.
# Let's replace the block from `.light-hero {` up to `/* Stat Cards */`
# And then update the positions in the HTML directly via regex or beautifulsoup.
# Actually, I'll just replace the entire style block again by merging `reconstructed_css` and `new_hero_css` and the base css.
