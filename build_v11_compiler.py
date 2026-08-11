# -*- coding: utf-8 -*-
import os
import re

GLOBAL_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>StepsAI - {title}</title>
  <link rel="stylesheet" href="{root_prefix}assets/css/style.css">
  <link href="https://fonts.googleapis.com/css2?family=Geist+Mono:wght@400;500;700&family=Inter:wght@400;500;600&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
  <style>
    .gsap-fade-up { opacity: 0; transform: translateY(40px); }
    .gsap-scale-in { opacity: 0; transform: scale(0.9); }
    
    .hero-v2 { min-height: 80vh; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 160px 32px 80px; position: relative; overflow: hidden; }
    .hero-v2.split-hero { flex-direction: row; text-align: left; max-width: 1300px; margin: 0 auto; gap: 64px; }
    @media (max-width: 1000px) { .hero-v2.split-hero { flex-direction: column; text-align: center; } }
    
    .hero-bg-glow { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 80vw; height: 80vw; background: radial-gradient(circle, var(--accent-tint) 0%, rgba(251,252,254,0) 70%); z-index: -1; }
    .hero-v2 h1 { font-size: clamp(48px, 6vw, 80px); line-height: 1.05; letter-spacing: -2px; font-family: 'Outfit', sans-serif; }
    .hero-v2 p { font-size: 20px; color: var(--text-secondary); max-width: 720px; line-height: 1.6; }
    
    .section-v2 { padding: 112px 32px; max-width: 1400px; margin: 0 auto; }
    .section-title-v2 { font-size: clamp(36px, 4vw, 54px); letter-spacing: -1px; margin-bottom: 80px; font-family: 'Outfit', sans-serif; text-align: center;}
    
    .bento-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px; grid-auto-flow: dense; }
    .bento-card { background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 24px; padding: 48px; position: relative; overflow: hidden; display: flex; flex-direction: column; transition: transform 0.5s cubic-bezier(.16,1,.3,1), border-color 0.5s, box-shadow 0.5s; box-shadow: var(--shadow); }
    .bento-card:hover { transform: translateY(-8px); border-color: var(--accent); box-shadow: var(--shadow-lg); }
    .bento-title { font-size: 32px; font-weight: 700; margin-bottom: 16px; font-family: 'Outfit', sans-serif; color: var(--text-primary);}
    .bento-desc { color: var(--text-secondary); font-size: 16px; line-height: 1.6; }
    @media (max-width: 992px) { .bento-grid { grid-template-columns: 1fr; } }
    
    .industries-accordion { max-width: 1200px; margin: 0 auto; display: flex; gap: 16px; height: 500px; }
    .accordion-panel { position: relative; flex: 1; border-radius: 24px; overflow: hidden; background-size: cover; background-position: center; transition: flex 0.6s cubic-bezier(0.16, 1, 0.3, 1); cursor: pointer; }
    .accordion-panel::after { content: ''; position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0) 100%); transition: opacity 0.4s; }
    .accordion-panel:hover { flex: 3; }
    .accordion-content { position: absolute; bottom: 0; left: 0; width: 100%; padding: 32px; color: white; z-index: 2; display: flex; flex-direction: column; justify-content: flex-end; }
    .accordion-title { font-family: 'Outfit', sans-serif; font-size: 28px; font-weight: 700; margin: 0; white-space: nowrap; }
    .accordion-desc { font-size: 16px; color: rgba(255,255,255,0.8); margin-top: 12px; line-height: 1.5; opacity: 0; transform: translateY(10px); transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); }
    .accordion-panel:hover .accordion-desc { opacity: 1; transform: translateY(0); transition-delay: 0.1s; }
    
    .step-line-container { position: fixed; top: 0; left: 40px; width: 6px; height: 100%; z-index: 0; pointer-events: none; }
    .step-line { width: 2px; height: 100%; background: var(--line); position: absolute; left: 2px; }
    .step-line-progress { width: 2px; height: 0%; background: var(--accent); position: absolute; left: 2px; transition: height 0.1s linear; }
    
    .phone-mockup { width: 340px; height: 640px; background: #fff; border-radius: 48px; box-shadow: 0 32px 80px rgba(0,0,0,0.15), inset 0 0 0 10px #e0e4e8, inset 0 0 0 12px #f4f5f7; position: relative; overflow: hidden; display: flex; flex-direction: column; flex-shrink:0; }
    .phone-notch { position: absolute; top: 10px; left: 50%; transform: translateX(-50%); width: 120px; height: 28px; background: #e0e4e8; border-radius: 14px; z-index: 10; }
    .mockup-screen { position: absolute; inset: 12px; border-radius: 36px; overflow: hidden; display: flex; flex-direction: column; background:#fff; z-index:1; opacity:0; }
    .mockup-header { height: 80px; padding: 40px 16px 12px; display: flex; align-items: center; gap: 12px; font-family: 'Inter', sans-serif; }
    .mockup-header.whatsapp { background: #008069; color: white; }
    .mockup-header.instagram { background: #fff; color: #111; border-bottom: 1px solid #efefef; }
    .mockup-body { flex: 1; padding: 16px; display: flex; flex-direction: column; gap: 12px; background: #EFEAE2; font-family: 'Inter', sans-serif; }
    .mockup-body.instagram { background: #fff; }
    .chat-bubble { max-width: 85%; padding: 12px 14px; border-radius: 12px; font-size: 14px; line-height: 1.4; position: relative; }
    .chat-bubble.in { align-self: flex-start; background: #fff; border-top-left-radius: 4px; box-shadow: 0 1px 2px rgba(0,0,0,0.05); color:#111; }
    .chat-bubble.out { align-self: flex-end; background: #D9FDD3; border-top-right-radius: 4px; box-shadow: 0 1px 2px rgba(0,0,0,0.05); color:#111; }
    .chat-bubble.ig-in { background: #efefef; border-radius: 18px; color:#111; }
    .chat-bubble.ig-out { background: linear-gradient(135deg, #4F5BD5, #962FBF); color: white; border-radius: 18px; }
    .chat-time { font-size: 10px; color: rgba(0,0,0,0.4); float: right; margin: 8px 0 -4px 8px; }
    .chat-time.out { color: rgba(0,0,0,0.5); }
    .receipt-pill { display: inline-flex; align-items: center; justify-content:center; gap: 8px; background: #E9F8F0; border-radius: 8px; padding: 8px 16px; font-family: 'Geist Mono', monospace; font-size: 11px; font-weight: 500; color: #0C1322; letter-spacing: 0.12em; text-transform: uppercase; margin-top: 16px; align-self:center; opacity: 0; transform: scale(0.94); box-shadow:0 4px 12px rgba(11,158,88,0.15); }
    .receipt-pill .check { color: #0B9E58; font-size: 14px; font-weight: 800; }
    .receipt-pill span { color: #46536B; }
    
    .micro-mockup { transition: 0.3s; transform: translateY(10px); }
    .bento-card:hover .micro-mockup { transform: translateY(0); box-shadow: 0 20px 40px rgba(0,0,0,0.08) !important; }
    
    .typing { display:flex; gap:4px; padding:16px 20px; align-items:center; }
    .dot { width:6px; height:6px; background:rgba(0,0,0,0.3); border-radius:50%; animation: type 1.4s infinite ease-in-out both; }
    .dot:nth-child(1) { animation-delay: -0.32s; }
    .dot:nth-child(2) { animation-delay: -0.16s; }
    @keyframes type { 0%, 80%, 100% { transform: scale(0); } 40% { transform: scale(1); } }
  </style>
</head>
<body>
  <div class="step-line-container">
    <div class="step-line"></div>
    <div class="step-line-progress" id="stepLineProgress"></div>
  </div>
"""









CUSTOM_HOME_HERO = """
  <!-- S01 Landing Hero - Centered with Dynamic Chat Widget (V8 Advanced Gradient Background) -->
  <section class="hero-v2 centered-hero" style="position: relative; padding-top: 120px; padding-bottom: 0px; overflow: hidden; display: flex; flex-direction: column; align-items: center; text-align: center; max-width: 1400px; margin: 0 auto; min-height: 100vh;">
    
    <!-- Advanced Animated Mesh Gradient Background -->
    <div class="advanced-mesh-bg">
        <div class="mesh-orb-1"></div>
        <div class="mesh-orb-2"></div>
        <div class="mesh-orb-3"></div>
        <div class="hero-glass-overlay"></div>
    </div>
    
    <!-- Floating Background Mockups -->
    <div id="hero-bg-wa" style="position: absolute; left: -120px; top: 15%; transform: translateY(-50%) rotate(-8deg); z-index: 1; opacity: 0; filter: blur(2px); transition: filter 0.5s;" onmouseover="this.style.filter='blur(0)'" onmouseout="this.style.filter='blur(2px)'">
        <div class="phone-mockup" style="transform: scale(0.65); box-shadow: -20px 20px 60px rgba(0,0,0,0.15);">
            <div class="phone-notch"></div>
            <div class="mockup-screen" style="opacity:1; z-index:2; background:#EFEAE2;">
              <div class="mockup-header whatsapp">
                <div style="width:36px; height:36px; border-radius:50%; background:#fff; display:flex; align-items:center; justify-content:center; color:#008069; font-weight:800; font-size:18px;">S</div>
                <div style="line-height:1.2; font-weight:600; font-size:15px; text-align:left;">StepsAI<br><span style="font-size:12px; font-weight:400; opacity:0.8;">Online</span></div>
              </div>
              <div class="mockup-body" style="background:#EFEAE2;">
                <div class="chat-bubble in" style="text-align:left;">Do you have the linen shirt in medium? <span class="chat-time">10:42 PM</span></div>
                <div class="chat-bubble out" style="text-align:left;">Yes, two left in medium. Want me to hold one? <span class="chat-time out">10:42 PM</span></div>
                <div class="chat-bubble in" style="text-align:left;">Yes please <span class="chat-time">10:43 PM</span></div>
                <div class="chat-bubble out" style="text-align:left;">Reserved and added to your cart.<br><b style="display:block; margin-top:8px; padding-top:8px; border-top:1px solid rgba(0,0,0,0.1);">Linen Shirt · Medium · ₹2,400</b> <span class="chat-time out">10:43 PM</span></div>
                <div class="receipt-pill"><span class="check">✓</span> <span>SHOPIFY</span></div>
              </div>
            </div>
        </div>
    </div>
    
    <div id="hero-bg-ig" style="position: absolute; right: -120px; top: 25%; transform: translateY(-50%) rotate(8deg); z-index: 1; opacity: 0; filter: blur(2px); transition: filter 0.5s;" onmouseover="this.style.filter='blur(0)'" onmouseout="this.style.filter='blur(2px)'">
        <div class="phone-mockup" style="transform: scale(0.65); box-shadow: 20px 20px 60px rgba(0,0,0,0.15);">
            <div class="phone-notch"></div>
            <div class="mockup-screen" style="opacity:1; z-index:1;">
              <div class="mockup-header instagram">
                <div style="width:36px; height:36px; border-radius:50%; background:linear-gradient(135deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%); padding:2px; display:flex; align-items:center; justify-content:center;"><div style="width:100%; height:100%; background:#fff; border-radius:50%;"></div></div>
                <div style="line-height:1.2; font-weight:600; font-size:15px; color:#111; text-align:left;">StepsAI Real Estate<br><span style="font-size:12px; font-weight:400; color:#888;">StepsAI Real Estate</span></div>
              </div>
              <div class="mockup-body instagram">
                <div class="chat-bubble in ig-in" style="text-align:left;">Is the 3BHK still available? <span class="chat-time">9:15 PM</span></div>
                <div class="chat-bubble out ig-out" style="text-align:left;">It is. Want to see it this weekend? <span class="chat-time out" style="color:rgba(255,255,255,0.7);">9:15 PM</span></div>
                <div class="chat-bubble in ig-in" style="text-align:left;">Saturday works <span class="chat-time">9:16 PM</span></div>
                <div class="chat-bubble out ig-out" style="text-align:left;">Booked for Saturday 11 AM. Sending the address.<br><div style="display:flex; gap:8px; margin-top:8px;"><span style="background:rgba(255,255,255,0.2); padding:4px 8px; border-radius:8px; font-size:12px;">Sat 11:00</span></div><span class="chat-time out" style="color:rgba(255,255,255,0.7);">9:16 PM</span></div>
                <div class="receipt-pill"><span class="check">✓</span> <span>CALENDAR</span></div>
              </div>
            </div>
        </div>
    </div>

    <!-- Center Content -->
    <div style="position: relative; z-index: 10; max-width: 1000px; display: flex; flex-direction: column; align-items: center; width: 100%;">
      <span class="kicker gsap-fade-up" style="font-family: 'Geist Mono', monospace; font-size: 11px; font-weight: 500; color: var(--accent); letter-spacing: .24em; text-transform: uppercase; margin-bottom: 12px; display:block;">AI AGENT FOR SALES & SUPPORT</span>
      
      <h1 class="gsap-fade-up" style="font-family: 'Outfit'; font-size: clamp(40px, 6vw, 72px); margin-bottom: 16px; line-height: 1.05; letter-spacing: -0.03em; color: var(--text-primary); font-weight: 700; white-space: nowrap;">It answers. Then it acts.</h1>
      
      <p class="gsap-fade-up" style="font-size: clamp(16px, 1.8vw, 18px); color: var(--text-secondary); margin-bottom: 32px; max-width: 600px; line-height: 1.5;">StepsAI answers customer questions on WhatsApp, Instagram and your website. Then it books the meeting, saves the lead, or updates the order.</p>
      
      <div class="hero-actions gsap-fade-up" style="display:flex; gap:12px; flex-wrap: wrap; justify-content: center; align-items: center;">
        <a href="./partners/apply/index.html" style="text-decoration: none;">
           <button class="btn-primary" style="padding: 14px 28px; font-size: 16px; border-radius: 100px; display: flex; align-items: center; gap: 8px; box-shadow: 0 8px 24px rgba(26,86,219,0.3);">
              Start Free Trial 
              <span style="background: rgba(255,255,255,0.2); padding: 4px 8px; border-radius: 6px; font-size: 11px; font-family: 'Geist Mono', monospace; margin-left: 8px;">ENTER ↵</span>
           </button>
        </a>
        <button class="btn-outline" style="padding: 14px 28px; font-size: 16px; border-radius: 100px; background: rgba(255,255,255,0.8); backdrop-filter: blur(10px);">Book an Appointment</button>
      </div>
      
      <div class="gsap-fade-up" style="margin-top: 16px; font-size: 12px; color: var(--text-tertiary); display: flex; align-items: center; gap: 12px; font-weight: 500;">
         <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#0B9E58" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> No credit card required
         <span style="color: var(--border-subtle);">&bull;</span>
         Works with Shopify, HubSpot and Calendly.
      </div>
    </div>
    
    <!-- Main Center Web Chat Mockup -->
    <div id="hero-main-web" class="gsap-fade-up" style="position: relative; z-index: 15; margin-top: 32px; width: 100%; max-width: 380px; opacity: 0; transform: translateY(100px);">
        
        <!-- Real Chat Widget Mockup container -->
        <!-- Enhanced Shadow to make it POP off the advanced background -->
        <div style="width: 100%; background: #fbfbfd; border-radius: 20px 20px 0 0; box-shadow: 0 40px 100px rgba(26,86,219,0.25), 0 0 0 1px rgba(255,255,255,0.6) inset, 0 10px 30px rgba(123,44,191,0.1); border: 1px solid var(--border-subtle); border-bottom: none; overflow: hidden; display: flex; flex-direction: column; height: 400px; position: relative;">
           
           <!-- SCREEN 1: HOME -->
           <div id="chat-screen-home" style="position: absolute; inset: 0; display: flex; flex-direction: column; z-index: 2; background: #fbfbfd; opacity: 1;">
               <div style="background: linear-gradient(180deg, #24252e 0%, #17181e 100%); padding: 20px 16px 24px; position: relative; text-align: center;">
                  <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 16px;">
                     <div style="width: 32px; height: 32px; background: linear-gradient(135deg, #7b2cbf, #5a189a); border-radius: 8px; display: flex; justify-content: center; align-items: center; box-shadow: 0 4px 12px rgba(123,44,191,0.4);">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.5"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path></svg>
                     </div>
                     <div style="width: 28px; height: 28px; border-radius: 50%; background: rgba(255,255,255,0.15); display: flex; justify-content: center; align-items: center; color: #fff;">
                        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
                     </div>
                  </div>
                  <h3 style="margin: 0 0 4px; font-size: 22px; font-family: 'Inter', sans-serif; font-weight: 800; color: #fff;">Hi there 👋</h3>
                  <p style="margin: 0; font-size: 13px; color: rgba(255,255,255,0.8);">How can I help you today</p>
               </div>
               <div style="padding: 0 16px; position: relative; margin-top: -20px;">
                  <div style="background: #fff; border-radius: 20px; padding: 14px 16px; display: flex; align-items: center; justify-content: space-between; box-shadow: 0 8px 24px rgba(0,0,0,0.06); border: 1px solid #efefef;">
                     <div id="home-typewriter" style="color: #888; font-size: 14px; font-weight: 500; flex: 1; text-align: left; white-space: nowrap; overflow: hidden;">Ask me anything</div>
                     <div id="home-send-btn" style="width: 32px; height: 32px; border-radius: 50%; background: #f4f5f7; display: flex; justify-content: center; align-items: center; color: #444; transition: background 0.3s, color 0.3s;">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
                     </div>
                  </div>
               </div>
               <div style="flex: 1;"></div>
               <div style="background: #fff; border-top: 1px solid #efefef; display: flex; padding: 10px 0;">
                  <div style="flex: 1; display: flex; flex-direction: column; align-items: center; gap: 4px; color: #111; border-right: 1px solid #efefef;">
                     <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
                     <span style="font-size: 12px; font-weight: 600;">Home</span>
                  </div>
                  <div style="flex: 1; display: flex; flex-direction: column; align-items: center; gap: 4px; color: #999;">
                     <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
                     <span style="font-size: 12px; font-weight: 500;">Messages</span>
                  </div>
               </div>
           </div>
           
           <!-- SCREEN 2: MESSAGES (Active Chat) -->
           <div id="chat-screen-msg" style="position: absolute; inset: 0; display: flex; flex-direction: column; z-index: 1; background: #fff; opacity: 0; pointer-events: none;">
               
               <!-- White Header -->
               <div style="background: #fff; padding: 12px 16px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #efefef;">
                  <div style="width: 32px; height: 32px; border-radius: 8px; border: 1px solid #efefef; display: flex; justify-content: center; align-items: center; color: #666;">
                     <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"></polyline></svg>
                  </div>
                  <div style="display: flex; align-items: center; gap: 10px; flex: 1; margin-left: 12px;">
                     <div style="width: 36px; height: 36px; background: linear-gradient(135deg, #7b2cbf, #5a189a); border-radius: 50%; display: flex; justify-content: center; align-items: center; box-shadow: 0 4px 8px rgba(123,44,191,0.3);">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.5"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path></svg>
                     </div>
                     <div style="text-align: left;">
                        <div style="font-weight: 700; font-size: 14px; font-family: 'Inter', sans-serif; color: #111;">HABITIQ</div>
                        <div style="font-size: 11px; color: #888;">Online</div>
                     </div>
                  </div>
                  <div style="width: 32px; height: 32px; border-radius: 8px; border: 1px solid #efefef; display: flex; justify-content: center; align-items: center; color: #666;">
                     <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="1"></circle><circle cx="12" cy="5" r="1"></circle><circle cx="12" cy="19" r="1"></circle></svg>
                  </div>
               </div>
               
               <!-- Chat Body -->
               <div style="flex: 1; padding: 16px; overflow-y: hidden; display: flex; flex-direction: column; justify-content: flex-end; position: relative;">
                  <div id="dynamic-chat-content" style="display: flex; flex-direction: column; gap: 12px;">
                     <!-- Messages injected via JS -->
                  </div>
               </div>
               
               <!-- Input Area -->
               <div style="padding: 12px 16px; background: #fbfbfd; border-top: 1px solid #efefef; display: flex; flex-direction: column; gap: 8px;">
                  <div style="background: #fff; border-radius: 20px; padding: 8px 12px; border: 1px solid #efefef; display: flex; align-items: center;">
                     <div style="flex: 1; font-size: 13px; color: #888; text-align: left;">Ask me anything</div>
                     <div style="display: flex; gap: 6px;">
                        <div style="width: 28px; height: 28px; border-radius: 50%; border: 1px solid #efefef; display: flex; justify-content: center; align-items: center; color: #555;">
                           <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="23"></line><line x1="8" y1="23" x2="16" y2="23"></line></svg>
                        </div>
                        <div style="width: 28px; height: 28px; border-radius: 50%; background: #f4f5f9; display: flex; justify-content: center; align-items: center; color: #a1a5b7;">
                           <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
                        </div>
                     </div>
                  </div>
                  <div style="text-align: center; font-size: 10px; color: #888;">
                     Powered by <span style="color: #dc2743; font-weight: 700;">STEPS AI</span>
                  </div>
               </div>
               
           </div>
           
        </div>
    </div>

  </section>
  <style>
    /* Advanced Mesh Gradient Background */
    .advanced-mesh-bg {
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        z-index: 0;
        overflow: hidden;
        background: #fdfdfd;
    }
    .mesh-orb-1 {
        position: absolute;
        top: -15%; left: -5%;
        width: 800px; height: 800px;
        background: radial-gradient(circle, rgba(26,86,219,0.18) 0%, rgba(26,86,219,0) 65%);
        border-radius: 50%;
        filter: blur(60px);
        animation: float1 15s infinite ease-in-out;
    }
    .mesh-orb-2 {
        position: absolute;
        top: 20%; right: -10%;
        width: 900px; height: 900px;
        background: radial-gradient(circle, rgba(123,44,191,0.15) 0%, rgba(123,44,191,0) 65%);
        border-radius: 50%;
        filter: blur(80px);
        animation: float2 20s infinite ease-in-out;
    }
    .mesh-orb-3 {
        position: absolute;
        bottom: -20%; left: 30%;
        width: 1000px; height: 1000px;
        background: radial-gradient(circle, rgba(11,158,88,0.1) 0%, rgba(11,158,88,0) 65%);
        border-radius: 50%;
        filter: blur(100px);
        animation: float3 25s infinite ease-in-out;
    }
    .hero-glass-overlay {
        position: absolute;
        inset: 0;
        background: linear-gradient(180deg, rgba(255,255,255,0.2) 0%, rgba(255,255,255,0.9) 100%);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
    }
    
    @keyframes float1 {
        0%, 100% { transform: translate(0, 0) scale(1); }
        50% { transform: translate(60px, -40px) scale(1.1); }
    }
    @keyframes float2 {
        0%, 100% { transform: translate(0, 0) scale(1); }
        50% { transform: translate(-50px, 60px) scale(0.95); }
    }
    @keyframes float3 {
        0%, 100% { transform: translate(0, 0) scale(1); }
        50% { transform: translate(-40px, -80px) scale(1.05); }
    }

    /* Chat Bubble Styles Tightened */
    .msg-user-container { display: flex; align-items: flex-end; gap: 6px; align-self: flex-end; margin-bottom: 16px; opacity: 0; transform: translateY(10px); }
    .msg-user-bubble { background: #625df5; color: #fff; padding: 10px 14px; border-radius: 12px; border-bottom-right-radius: 4px; font-size: 13px; max-width: 220px; font-weight: 500; text-align: left; }
    .msg-user-avatar { width: 28px; height: 28px; border-radius: 50%; background: #e0e4f5; color: #625df5; display: flex; justify-content: center; align-items: center; }
    
    .msg-bot-container { display: flex; flex-direction: column; align-items: flex-start; gap: 6px; margin-bottom: 12px; opacity: 0; transform: translateY(10px); }
    .msg-bot-header { display: flex; align-items: center; gap: 6px; }
    .msg-bot-avatar { width: 24px; height: 24px; border-radius: 50%; background: url('https://i.pravatar.cc/100?img=11') center/cover; }
    .msg-bot-name { font-size: 12px; color: #444; }
    .msg-bot-bubble { background: #f4f5f7; color: #111; padding: 12px 14px; border-radius: 12px; border-top-left-radius: 4px; font-size: 13px; max-width: 260px; line-height: 1.4; text-align: left; }
    .msg-bot-bubble ul { margin: 6px 0 0 16px; padding: 0; }
    .msg-bot-bubble li { margin-bottom: 2px; }
    
    .typing-indicator { display: flex; gap: 4px; padding: 10px 14px; background: #f4f5f7; border-radius: 12px; border-top-left-radius: 4px; width: fit-content; opacity: 0; }
    .typing-indicator .dot { width: 5px; height: 5px; background: #888; border-radius: 50%; animation: type-dot 1.4s infinite ease-in-out both; }
    .typing-indicator .dot:nth-child(1) { animation-delay: -0.32s; }
    .typing-indicator .dot:nth-child(2) { animation-delay: -0.16s; }
    @keyframes type-dot { 0%, 80%, 100% { transform: scale(0); } 40% { transform: scale(1); } }
    
    /* Typewriter cursor */
    .typing-cursor { border-right: 2px solid #111; animation: blink 1s step-end infinite; }
    @keyframes blink { 50% { border-color: transparent; } }
  </style>
  <script>
    document.addEventListener("DOMContentLoaded", () => {
        gsap.registerPlugin(ScrollTrigger);
        
        let htl = gsap.timeline();
        
        // Initial hero intro
        htl.to(".gsap-fade-up", { opacity: 1, y: 0, duration: 0.8, stagger: 0.1, ease: "power3.out" })
           .to("#hero-main-web", { opacity: 1, y: 0, duration: 1, ease: "power4.out" }, "-=0.4")
           .to("#hero-bg-wa", { opacity: 1, x: 50, duration: 1.5, ease: "power3.out" }, "-=0.8")
           .to("#hero-bg-ig", { opacity: 1, x: -50, duration: 1.5, ease: "power3.out" }, "-=1.2");
           
        // Scroll Parallax for Background Mockups
        gsap.to("#hero-bg-wa", {
            scrollTrigger: { trigger: ".hero-v2", start: "top top", end: "bottom top", scrub: 1 },
            y: -80, rotation: -12, ease: "none"
        });
        gsap.to("#hero-bg-ig", {
            scrollTrigger: { trigger: ".hero-v2", start: "top top", end: "bottom top", scrub: 1 },
            y: -100, rotation: 12, ease: "none"
        });
           
        // Define industries data
        const industries = [
            {
                query: "ABOUT PRODUCT",
                botResponse: `I found <b>general market context</b> about <b>Habitiq</b>, including:
                              <ul>
                                <li>Market size and growth</li>
                                <li>Key players in India</li>
                              </ul>`
            },
            {
                query: "WHERE IS MY ORDER?",
                botResponse: `Your order <b>#8842</b> is out for delivery. It will arrive today between <b>4:00 PM and 6:00 PM</b> via FedEx.`
            },
            {
                query: "BOOK A DEMO",
                botResponse: `Great! I have available slots on <b>Tuesday</b>. Would you prefer morning or afternoon?`
            }
        ];
        
        const homeTypewriterEl = document.getElementById('home-typewriter');
        const homeSendBtn = document.getElementById('home-send-btn');
        const chatContentEl = document.getElementById('dynamic-chat-content');
        
        const screenHome = document.getElementById('chat-screen-home');
        const screenMsg = document.getElementById('chat-screen-msg');
        
        let currentIndustryIndex = 0;
        let isAnimating = false;
        let ctl = null;
        
        function resetToHomeScreen() {
            if(ctl) { ctl.kill(); ctl = null; }
            screenHome.style.opacity = 1;
            screenHome.style.zIndex = 2;
            screenMsg.style.opacity = 0;
            screenMsg.style.zIndex = 1;
            
            homeTypewriterEl.innerHTML = "Ask me anything";
            homeTypewriterEl.classList.remove('typing-cursor');
            homeTypewriterEl.style.color = "#888";
            homeSendBtn.style.background = "#f4f5f7";
            homeSendBtn.style.color = "#444";
            isAnimating = false;
        }
        
        function playIndustryScenario(index) {
            isAnimating = true;
            const data = industries[index % industries.length];
            
            resetToHomeScreen();
            isAnimating = true;
            
            homeTypewriterEl.innerHTML = "";
            homeTypewriterEl.classList.add('typing-cursor');
            homeTypewriterEl.style.color = "#111";
            
            chatContentEl.innerHTML = `
                <div class="msg-user-container" id="msg-u">
                   <div style="display:flex; flex-direction:column; align-items:flex-end; gap:4px;">
                     <span style="font-size:11px; color:#888; margin-right:6px;">You</span>
                     <div class="msg-user-bubble">${data.query}</div>
                   </div>
                   <div class="msg-user-avatar">
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                   </div>
                </div>
                
                <div class="msg-bot-container" id="msg-b">
                   <div class="msg-bot-header">
                      <div class="msg-bot-avatar"></div>
                      <span class="msg-bot-name">Product Guide</span>
                   </div>
                   <div class="typing-indicator" id="msg-t"><div class="dot"></div><div class="dot"></div><div class="dot"></div></div>
                   <div class="msg-bot-bubble" id="msg-r" style="display:none;">${data.botResponse}</div>
                </div>
            `;
            
            let queryText = data.query;
            ctl = gsap.timeline();
            
            // Wait 1s so user sees the home screen state
            ctl.to({}, { duration: 1 });
            
            // Type out query FAST
            ctl.to(homeTypewriterEl, { 
                duration: queryText.length * 0.03, 
                text: queryText,
                ease: "none",
                onUpdate: function() {
                    homeTypewriterEl.innerHTML = queryText.substring(0, Math.round(this.progress() * queryText.length));
                }
            });
            
            // Highlight send button
            ctl.call(() => { 
                homeTypewriterEl.classList.remove('typing-cursor');
                homeSendBtn.style.background = "#625df5";
                homeSendBtn.style.color = "#fff";
            }, null, "+=0.1");
            
            // Instant Crossfade to Messages Screen
            ctl.to(screenHome, { opacity: 0, duration: 0.3, ease: "power2.inOut" }, "+=0.2")
               .to(screenMsg, { opacity: 1, duration: 0.3, ease: "power2.inOut" }, "<")
               .call(() => {
                   screenHome.style.zIndex = 1;
                   screenMsg.style.zIndex = 2;
               });
               
            // Show user bubble pop in
            ctl.to("#msg-u", { opacity: 1, y: 0, duration: 0.3, ease: "back.out(1.2)" }, "+=0.1");
               
            // Show typing indicator
            ctl.to("#msg-b", { opacity: 1, y: 0, duration: 0.3, ease: "power3.out" }, "+=0.2")
               .to("#msg-t", { opacity: 1, duration: 0.1 });
               
            // Swap typing for response (FAST)
            ctl.call(() => {
                document.getElementById('msg-t').style.display = 'none';
                document.getElementById('msg-r').style.display = 'block';
            }, null, "+=0.8");
            
            // NO AUTO-FADEOUT! 
            // It stays on the chat indefinitely until the user scrolls away!
        }
        
        // Use IntersectionObserver to play animations ONLY when widget is in view
        // and reset/switch industries when it leaves view.
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    if (!isAnimating) {
                        playIndustryScenario(currentIndustryIndex);
                    }
                } else {
                    if (isAnimating) {
                        // Kill current animation timeline
                        if(ctl) { ctl.kill(); }
                        // Increment industry
                        currentIndustryIndex++;
                        // Reset instantly to home screen so it's ready for next scroll-in
                        resetToHomeScreen();
                    }
                }
            });
        }, { threshold: 0.2 });
        
        // Start observing after initial intro delay
        setTimeout(() => {
            observer.observe(document.getElementById('hero-main-web'));
        }, 2000);
    });
  </script>
"""

CUSTOM_FOUR_AGENTS = """
  <section class="section-v2" style="padding-top: 160px; max-width: 1200px;">
    <div style="text-align: center; margin-bottom: 80px;">
      <span class="gsap-fade-up" style="font-family: 'Geist Mono', monospace; font-size: 12px; color: var(--accent); letter-spacing: .2em; text-transform: uppercase;">FOUR AGENTS, ONE BRAIN</span>
      <h2 class="gsap-fade-up" style="font-family: 'Outfit'; font-size: clamp(40px, 5vw, 56px); margin: 16px 0 24px; color: var(--text-primary);">Four jobs. One memory.</h2>
      <p class="gsap-fade-up" style="font-size: 20px; color: var(--text-secondary); max-width: 700px; margin: 0 auto; line-height: 1.6;">Your support agent knows what your sales agent promised yesterday. That sounds obvious until you have used four separate tools that all forgot.</p>
    </div>

    <div class="bento-grid gsap-fade-up" style="grid-template-columns: repeat(2, 1fr); gap: 32px;">
      
      <!-- Sales Agent -->
      <div class="bento-card" style="padding: 48px; background: #fbfbfd; border: 1px solid var(--border-subtle); display: flex; flex-direction: column; justify-content: space-between; min-height: 440px; border-radius: 32px;">
        <div>
          <h3 style="font-family: 'Outfit'; font-size: 32px; margin-bottom: 16px; color: var(--text-primary);">Sales Agent</h3>
          <p style="color: var(--text-secondary); font-size: 16px; line-height: 1.6;">Checks what is actually in stock before it promises anything, then closes.</p>
        </div>
        <div class="micro-mockup" style="background: #EFEAE2; border-radius: 16px; padding: 16px; margin-top: 32px; border: 1px solid rgba(0,0,0,0.05);">
          <div class="chat-bubble in" style="color: #111;">Do you have this in large?</div>
          <div class="chat-bubble out" style="color: #111; margin-top: 8px;">Yes, two left! Added to cart.</div>
          <div class="receipt-pill" style="opacity: 1; transform: scale(1); margin: 16px auto 0; box-shadow: none; border: 1px solid rgba(11,158,88,0.2);"><span class="check">✓</span> <span>SHOPIFY</span></div>
        </div>
      </div>

      <!-- Lead Agent -->
      <div class="bento-card" style="padding: 48px; background: #fbfbfd; border: 1px solid var(--border-subtle); display: flex; flex-direction: column; justify-content: space-between; min-height: 440px; border-radius: 32px;">
        <div>
          <h3 style="font-family: 'Outfit'; font-size: 32px; margin-bottom: 16px; color: var(--text-primary);">Lead Agent</h3>
          <p style="color: var(--text-secondary); font-size: 16px; line-height: 1.6;">Finds out budget and timeline the way a good salesperson would, then writes it into your CRM.</p>
        </div>
        <div class="micro-mockup" style="background: #fff; border-radius: 16px; padding: 16px; margin-top: 32px; border: 1px solid var(--border-subtle);">
          <div style="font-family: 'Inter'; font-size: 12px; color: var(--text-tertiary); margin-bottom: 12px; text-transform: uppercase; letter-spacing: 1px;">HubSpot CRM</div>
          <div style="background: #f4f5f7; border-radius: 8px; padding: 16px; border-left: 3px solid #ff7a59;">
            <div style="font-weight: 600; color: #111; font-size: 14px;">New Lead: Sarah Jenkins</div>
            <div style="color: var(--text-secondary); font-size: 13px; margin-top: 6px;">Budget: $5k-$10k · Timeline: Q3</div>
          </div>
          <div class="receipt-pill" style="opacity: 1; transform: scale(1); margin: 16px auto 0; box-shadow: none; border: 1px solid rgba(11,158,88,0.2);"><span class="check">✓</span> <span>HUBSPOT</span></div>
        </div>
      </div>

      <!-- Meetings Agent -->
      <div class="bento-card" style="padding: 48px; background: #fbfbfd; border: 1px solid var(--border-subtle); display: flex; flex-direction: column; justify-content: space-between; min-height: 440px; border-radius: 32px;">
        <div>
          <h3 style="font-family: 'Outfit'; font-size: 32px; margin-bottom: 16px; color: var(--text-primary);">Meetings Agent</h3>
          <p style="color: var(--text-secondary); font-size: 16px; line-height: 1.6;">Offers times that are genuinely free, and puts the meeting in your calendar.</p>
        </div>
        <div class="micro-mockup" style="background: #fff; border-radius: 16px; padding: 16px; margin-top: 32px; border: 1px solid var(--border-subtle);">
          <div class="chat-bubble in ig-in" style="color: #111;">I want to book a site visit.</div>
          <div class="chat-bubble out ig-out" style="margin-top: 8px;">Saturday 11 AM works perfectly!</div>
          <div class="receipt-pill" style="opacity: 1; transform: scale(1); margin: 16px auto 0; box-shadow: none; border: 1px solid rgba(11,158,88,0.2);"><span class="check">✓</span> <span>CALENDAR</span></div>
        </div>
      </div>

      <!-- Support Agent -->
      <div class="bento-card" style="padding: 48px; background: #fbfbfd; border: 1px solid var(--border-subtle); display: flex; flex-direction: column; justify-content: space-between; min-height: 440px; border-radius: 32px;">
        <div>
          <h3 style="font-family: 'Outfit'; font-size: 32px; margin-bottom: 16px; color: var(--text-primary);">Support Agent</h3>
          <p style="color: var(--text-secondary); font-size: 16px; line-height: 1.6;">Tracks the order, explains the return policy, and only wakes you if something is actually wrong.</p>
        </div>
        <div class="micro-mockup" style="background: #fff; border-radius: 16px; padding: 16px; margin-top: 32px; border: 1px solid var(--border-subtle);">
          <div class="chat-bubble in ig-in" style="color: #111; border-radius: 4px;">Where is my order?</div>
          <div class="chat-bubble out ig-in" style="color: #111; margin-top: 8px; border-radius: 4px; border: 1px solid #efefef;">It is out for delivery today at 6PM!</div>
          <div class="receipt-pill" style="opacity: 1; transform: scale(1); margin: 16px auto 0; box-shadow: none; border: 1px solid rgba(11,158,88,0.2);"><span class="check">✓</span> <span>ZENDESK</span></div>
        </div>
      </div>

    </div>
  </section>
"""

CUSTOM_CHANNELS = """
<section class="section-v2" style="padding-top: 160px; max-width: 1200px;">
  <div style="text-align: center; margin-bottom: 80px;">
    <span class="gsap-fade-up" style="font-family: 'Geist Mono', monospace; font-size: 12px; color: var(--accent); letter-spacing: .2em; text-transform: uppercase;">EVERY CHANNEL</span>
    <h2 class="gsap-fade-up" style="font-family: 'Outfit'; font-size: clamp(40px, 5vw, 56px); margin: 16px 0 24px; color: var(--text-primary);">On Instagram it replies in public,<br>then finishes the sale in private.</h2>
    <p class="gsap-fade-up" style="font-size: 20px; color: var(--text-secondary); max-width: 700px; margin: 0 auto; line-height: 1.6;">A comment under a post and a WhatsApp message at midnight are not the same kind of conversation. Your agent treats them differently, because your customers do.</p>
  </div>

  <div class="bento-grid gsap-fade-up" style="grid-template-columns: repeat(3, 1fr); gap: 32px;">
    
    <!-- Instagram -->
    <div class="bento-card" style="padding: 40px; background: #fbfbfd; border: 1px solid var(--border-subtle); display: flex; flex-direction: column; min-height: 500px; border-radius: 32px;">
      <h3 style="font-family: 'Outfit'; font-size: 28px; margin-bottom: 8px; color: var(--text-primary); display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:24px; height:24px; border-radius:6px; background:linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888);"></span> Instagram
      </h3>
      <h4 style="font-size:18px; font-weight:600; margin-bottom:12px;">The comment nobody had time to answer.</h4>
      <p style="color: var(--text-secondary); font-size: 15px; line-height: 1.5; margin-bottom:32px;">Someone asks the price under your post. Your agent replies where everyone can see it, slides into the DM, and finishes the conversation there.</p>
      
      <div class="micro-mockup" style="background:#fff; border-radius:16px; padding:16px; border:1px solid var(--border-subtle); margin-top:auto;">
        <div style="display:flex; gap:12px; align-items:flex-start; margin-bottom:12px;">
          <div style="width:24px; height:24px; border-radius:50%; background:#e0e0e0; flex-shrink:0;"></div>
          <div style="font-size:13px; color:#111;"><span style="font-weight:600;">customer123</span> How much is this jacket?</div>
        </div>
        <div style="display:flex; gap:12px; align-items:flex-start; margin-left:36px; padding-left:12px; border-left:1px solid #efefef;">
          <div style="width:24px; height:24px; border-radius:50%; background:linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888); flex-shrink:0;"></div>
          <div style="font-size:13px; color:#111;"><span style="font-weight:600;">yourbrand</span> @customer123 Just sent you a DM with the pricing and a checkout link! ⚡️</div>
        </div>
      </div>
    </div>

    <!-- WhatsApp -->
    <div class="bento-card" style="padding: 40px; background: #fbfbfd; border: 1px solid var(--border-subtle); display: flex; flex-direction: column; min-height: 500px; border-radius: 32px;">
      <h3 style="font-family: 'Outfit'; font-size: 28px; margin-bottom: 8px; color: var(--text-primary); display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:24px; height:24px; border-radius:50%; background:#25D366;"></span> WhatsApp
      </h3>
      <h4 style="font-size:18px; font-weight:600; margin-bottom:12px;">Where your customers already spend their evening.</h4>
      <p style="color: var(--text-secondary); font-size: 15px; line-height: 1.5; margin-bottom:32px;">Booking links, payment links, delivery updates, all inside the app they already have open.</p>
      
      <div class="micro-mockup" style="background:#EFEAE2; border-radius:16px; padding:16px; border:1px solid rgba(0,0,0,0.05); margin-top:auto;">
        <div class="chat-bubble out" style="color: #111; margin-bottom:8px;">Your order #8842 has shipped! Track it here: <a href="#" style="color:#00a884; font-weight:600;">track.me/8842</a></div>
        <div class="chat-bubble in" style="color: #111; margin-bottom:8px;">Can I change the delivery address?</div>
        <div class="chat-bubble out" style="color: #111;">Sure, just send me the new address and I'll update it before the driver leaves.</div>
      </div>
    </div>

    <!-- Website -->
    <div class="bento-card" style="padding: 40px; background: #fbfbfd; border: 1px solid var(--border-subtle); display: flex; flex-direction: column; min-height: 500px; border-radius: 32px;">
      <h3 style="font-family: 'Outfit'; font-size: 28px; margin-bottom: 8px; color: var(--text-primary); display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:24px; height:24px; border-radius:6px; background:var(--accent);"></span> Website
      </h3>
      <h4 style="font-size:18px; font-weight:600; margin-bottom:12px;">It knows which page they are standing on.</h4>
      <p style="color: var(--text-secondary); font-size: 15px; line-height: 1.5; margin-bottom:32px;">Someone asks "does this come in blue" while looking at a specific jacket. Your agent knows which jacket.</p>
      
      <div class="micro-mockup" style="background:#f4f5f7; border-radius:16px; padding:16px; border:1px solid var(--border-subtle); margin-top:auto; position:relative; overflow:hidden;">
        <!-- Fake product page background -->
        <div style="position:absolute; top:0; left:0; width:100%; padding:16px; opacity:0.4;">
          <div style="width:100%; height:120px; background:#e0e4e8; border-radius:8px; margin-bottom:8px;"></div>
          <div style="width:60%; height:12px; background:#d0d4d8; border-radius:4px; margin-bottom:4px;"></div>
          <div style="width:40%; height:12px; background:#d0d4d8; border-radius:4px;"></div>
        </div>
        
        <!-- Chat widget overlay -->
        <div style="position:relative; z-index:2; background:#fff; border-radius:12px; box-shadow:0 10px 30px rgba(0,0,0,0.1); border:1px solid var(--border-subtle); margin-top:40px;">
          <div style="background:var(--accent); color:white; padding:12px 16px; border-radius:12px 12px 0 0; font-size:13px; font-weight:600; display:flex; justify-content:space-between;">
            Chat Support <span style="cursor:pointer;">×</span>
          </div>
          <div style="padding:16px; background:#f9fafb; display:flex; flex-direction:column; gap:8px; border-radius:0 0 12px 12px;">
            <div class="chat-bubble in" style="font-size:13px; align-self:flex-end; background:var(--accent); color:white; border-radius:12px 12px 0 12px; box-shadow:none;">Does this come in blue?</div>
            <div class="chat-bubble out" style="font-size:13px; align-self:flex-start; background:#fff; border:1px solid #eee; border-radius:12px 12px 12px 0; color:#111; box-shadow:none;">Yes, the 'Classic Jacket' is available in Navy Blue!</div>
          </div>
        </div>
      </div>
    </div>

  </div>
</section>
"""

CUSTOM_SETUP = """
<section class="section-v2 setup-section" style="padding-top: 160px; max-width: 1400px; margin:0 auto; display:flex; gap:64px; align-items:center;">
  <div style="flex:1;">
    <span class="gsap-fade-up" style="font-family: 'Geist Mono', monospace; font-size: 12px; color: var(--accent); letter-spacing: .2em; text-transform: uppercase; margin-bottom:16px; display:block;">LIVE IN AN AFTERNOON</span>
    <h2 class="gsap-fade-up" style="font-family: 'Outfit'; font-size: clamp(40px, 4vw, 56px); margin: 0 0 24px; color: var(--text-primary); line-height:1.1;">Paste your website link.<br>That is genuinely the hard part.</h2>
    <p class="gsap-fade-up" style="font-size: 18px; color: var(--text-secondary); margin-bottom: 48px; line-height: 1.6; max-width:500px;">Your agent reads your pages and works out what you sell. You check it, change the greeting so it sounds like you, and switch on the channels you want. Most people are finished before their coffee goes cold.</p>
    
    <div class="setup-steps" style="display:flex; flex-direction:column; gap:32px;">
      <div class="gsap-fade-up step-txt-1" style="display:flex; gap:16px; transition:0.3s;">
        <div class="step-num-1" style="width:32px; height:32px; border-radius:50%; background:var(--text-primary); border:1px solid var(--border-subtle); display:flex; align-items:center; justify-content:center; font-weight:700; color:var(--bg-surface); flex-shrink:0; transition:0.3s;">1</div>
        <div>
          <h4 style="font-size:18px; font-weight:700; margin-bottom:8px;">Teach it</h4>
          <p style="color:var(--text-secondary); font-size:15px; line-height:1.5; margin:0;">Paste the link. It reads your site and learns your products, your prices, and your policies.</p>
        </div>
      </div>
      <div class="gsap-fade-up step-txt-2" style="display:flex; gap:16px; opacity:0.4; transition:0.3s;">
        <div class="step-num-2" style="width:32px; height:32px; border-radius:50%; background:var(--bg-surface); border:1px solid var(--border-subtle); display:flex; align-items:center; justify-content:center; font-weight:700; color:var(--text-primary); flex-shrink:0; transition:0.3s;">2</div>
        <div>
          <h4 style="font-size:18px; font-weight:700; margin-bottom:8px;">Make it yours</h4>
          <p style="color:var(--text-secondary); font-size:15px; line-height:1.5; margin:0;">Pick the name, the colour, and the first thing it says. Keep changing the tone until it sounds like someone who works for you.</p>
        </div>
      </div>
      <div class="gsap-fade-up step-txt-3" style="display:flex; gap:16px; opacity:0.4; transition:0.3s;">
        <div class="step-num-3" style="width:32px; height:32px; border-radius:50%; background:var(--bg-surface); border:1px solid var(--border-subtle); display:flex; align-items:center; justify-content:center; font-weight:700; color:var(--text-primary); flex-shrink:0; transition:0.3s;">3</div>
        <div>
          <h4 style="font-size:18px; font-weight:700; margin-bottom:8px;">Connect it</h4>
          <p style="color:var(--text-secondary); font-size:15px; line-height:1.5; margin:0;">Shopify, your calendar, your CRM, your inbox. Each one you connect gives your agent something new it can actually do rather than just talk about.</p>
        </div>
      </div>
    </div>
  </div>
  
  <div style="flex:1; display:flex; justify-content:center; align-items:center; min-width:300px;">
    <!-- Dark Mode Setup Mockup container -->
    <div class="setup-mockup" style="opacity:0; transform:scale(0.9); width:100%; max-width:460px; height:500px; background:#111; border-radius:24px; border:1px solid #222; box-shadow: 0 24px 64px rgba(0,0,0,0.2); color:#fff; font-family:'Inter', sans-serif; position:relative; overflow:hidden;">
      
      <!-- STEP 1: Connect Website -->
      <div id="setup-step-1" style="position:absolute; inset:32px; display:flex; flex-direction:column; z-index:3;">
          <div style="display:flex; align-items:center; gap:16px; margin-bottom:12px;">
            <div style="width:40px; height:40px; border-radius:12px; background:#222; border:1px solid #333; display:flex; align-items:center; justify-content:center;">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
            </div>
            <h3 style="font-family:'Outfit'; font-size:24px; font-weight:700; margin:0;">Connect your website</h3>
          </div>
          <p style="color:#888; font-size:15px; margin-bottom:32px; line-height:1.5;">Enter your website URL so we can learn about your brand and content.</p>
          
          <div style="margin-bottom:24px;">
            <label style="display:block; font-size:14px; font-weight:500; margin-bottom:12px;">Website URL</label>
            <div style="width:100%; height:52px; background:#1f2228; border:1px solid #3a3f4a; border-radius:12px; padding:0 16px; display:flex; align-items:center; font-family:monospace; font-size:15px; color:#fff; position:relative; overflow:hidden;">
              <span id="typewriter-url"></span><span class="cursor" style="display:inline-block; width:2px; height:18px; background:#fff; margin-left:4px; animation:blink 1s infinite;"></span>
            </div>
            <p style="color:#666; font-size:13px; margin-top:12px;">We'll detect your logo, colors, and content automatically.</p>
          </div>
          
          <div id="mockup-success-state" style="opacity:0; height:0; overflow:hidden; display:flex; flex-direction:column; gap:12px;">
            <div style="background:#1f2228; border:1px solid #3a3f4a; border-radius:12px; padding:16px; display:flex; align-items:center; gap:12px;">
              <div style="width:24px; height:24px; border-radius:50%; background:#fff; color:#111; display:flex; align-items:center; justify-content:center; font-size:14px; font-weight:800;">✓</div>
              <div style="font-size:14px; font-weight:500;">Connected — branding fetched</div>
            </div>
            
            <div style="background:#1f2228; border:1px solid #3a3f4a; border-radius:12px; padding:16px; display:flex; align-items:center; justify-content:space-between;">
              <div>
                <div style="font-size:14px; font-weight:600; margin-bottom:4px;">2 pages found</div>
                <div style="font-size:12px; color:#888;">2 selected · Click to review and edit</div>
              </div>
              <button style="background:transparent; border:1px solid #3a3f4a; color:#fff; border-radius:8px; padding:6px 12px; font-size:13px; font-weight:500;">See all</button>
            </div>
          </div>
          
          <div style="display:flex; justify-content:space-between; align-items:center; margin-top:auto; border-top:1px solid #222; padding-top:24px;">
            <button style="background:transparent; border:1px solid #333; color:#fff; border-radius:8px; padding:12px 24px; font-size:14px; font-weight:500;">Back</button>
            <button id="mockup-proceed-btn" style="background:#333; border:none; color:#888; border-radius:8px; padding:12px 24px; font-size:14px; font-weight:600; transition:all 0.3s;">Connect</button>
          </div>
      </div>
      
      <!-- STEP 2: Make It Yours -->
      <div id="setup-step-2" style="position:absolute; inset:32px; display:flex; flex-direction:column; z-index:2; opacity:0; pointer-events:none;">
          <div style="display:flex; align-items:center; gap:16px; margin-bottom:12px;">
            <div style="width:40px; height:40px; border-radius:12px; background:#222; border:1px solid #333; display:flex; align-items:center; justify-content:center;">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><path d="M12 20h9"></path><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path></svg>
            </div>
            <h3 style="font-family:'Outfit'; font-size:24px; font-weight:700; margin:0;">Make it yours</h3>
          </div>
          <p style="color:#888; font-size:15px; margin-bottom:32px; line-height:1.5;">Customize your agent's personality and appearance.</p>
          
          <div style="margin-bottom:20px;">
            <label style="display:block; font-size:14px; font-weight:500; margin-bottom:8px;">Agent Name</label>
            <div style="width:100%; height:48px; background:#1f2228; border:1px solid #3a3f4a; border-radius:12px; padding:0 16px; display:flex; align-items:center; font-size:15px; color:#fff;">
              <span id="typewriter-name"></span><span class="cursor2" style="display:inline-block; width:2px; height:18px; background:#fff; margin-left:4px; opacity:0; animation:blink 1s infinite;"></span>
            </div>
          </div>
          
          <div style="margin-bottom:20px;">
            <label style="display:block; font-size:14px; font-weight:500; margin-bottom:8px;">Brand Color</label>
            <div style="display:flex; gap:12px;">
              <div class="color-swatch" style="width:36px; height:36px; border-radius:50%; background:#1A56DB; border:2px solid transparent;"></div>
              <div class="color-swatch" id="target-color" style="width:36px; height:36px; border-radius:50%; background:#0B9E58; border:2px solid transparent;"></div>
              <div class="color-swatch" style="width:36px; height:36px; border-radius:50%; background:#E63946; border:2px solid transparent;"></div>
              <!-- Simulated Cursor for Click Animation -->
              <div id="sim-cursor-1" style="position:absolute; width:20px; height:20px; background:rgba(255,255,255,0.8); border-radius:50%; pointer-events:none; opacity:0; z-index:10; top:200px; left:200px; box-shadow:0 0 10px rgba(0,0,0,0.2);"></div>
            </div>
          </div>
          
          <div style="display:flex; justify-content:space-between; align-items:center; margin-top:auto; border-top:1px solid #222; padding-top:24px;">
            <button style="background:transparent; border:1px solid #333; color:#fff; border-radius:8px; padding:12px 24px; font-size:14px; font-weight:500;">Back</button>
            <button id="mockup-proceed-btn-2" style="background:#fff; border:none; color:#111; border-radius:8px; padding:12px 24px; font-size:14px; font-weight:600; transition:all 0.3s;">Next Step</button>
          </div>
      </div>
      
      <!-- STEP 3: Connect It & Go Live -->
      <div id="setup-step-3" style="position:absolute; inset:32px; display:flex; flex-direction:column; z-index:1; opacity:0; pointer-events:none;">
          <div id="step-3-content" style="display:flex; flex-direction:column; height:100%;">
              <div style="display:flex; align-items:center; gap:16px; margin-bottom:12px;">
                <div style="width:40px; height:40px; border-radius:12px; background:#222; border:1px solid #333; display:flex; align-items:center; justify-content:center;">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                </div>
                <h3 style="font-family:'Outfit'; font-size:24px; font-weight:700; margin:0;">Connect Channels</h3>
              </div>
              <p style="color:#888; font-size:15px; margin-bottom:32px; line-height:1.5;">Where should your agent talk to customers?</p>
              
              <div style="display:flex; flex-direction:column; gap:16px;">
                <div style="background:#1f2228; border:1px solid #3a3f4a; border-radius:12px; padding:16px; display:flex; align-items:center; justify-content:space-between;">
                  <div style="display:flex; align-items:center; gap:12px;">
                     <span style="display:inline-block; width:24px; height:24px; border-radius:50%; background:#25D366;"></span> <span style="font-size:15px; font-weight:500;">WhatsApp</span>
                  </div>
                  <div class="toggle-track" id="toggle-wa" style="width:40px; height:24px; background:#333; border-radius:12px; position:relative; transition:0.3s;">
                     <div class="toggle-thumb" style="width:20px; height:20px; background:#888; border-radius:50%; position:absolute; top:2px; left:2px; transition:0.3s;"></div>
                  </div>
                </div>
                
                <div style="background:#1f2228; border:1px solid #3a3f4a; border-radius:12px; padding:16px; display:flex; align-items:center; justify-content:space-between;">
                  <div style="display:flex; align-items:center; gap:12px;">
                     <span style="display:inline-block; width:24px; height:24px; border-radius:6px; background:var(--accent);"></span> <span style="font-size:15px; font-weight:500;">Website Widget</span>
                  </div>
                  <div class="toggle-track" id="toggle-web" style="width:40px; height:24px; background:#333; border-radius:12px; position:relative; transition:0.3s;">
                     <div class="toggle-thumb" style="width:20px; height:20px; background:#888; border-radius:50%; position:absolute; top:2px; left:2px; transition:0.3s;"></div>
                  </div>
                </div>
              </div>
              
              <div id="sim-cursor-2" style="position:absolute; width:20px; height:20px; background:rgba(255,255,255,0.8); border-radius:50%; pointer-events:none; opacity:0; z-index:10; top:300px; left:200px; box-shadow:0 0 10px rgba(0,0,0,0.2);"></div>
              
              <div style="display:flex; justify-content:center; align-items:center; margin-top:auto; padding-top:24px;">
                <button id="mockup-go-live-btn" style="width:100%; background:linear-gradient(45deg, #1A56DB, #0B9E58); border:none; color:#fff; border-radius:12px; padding:16px; font-size:16px; font-weight:700; transition:all 0.3s;">Go Live ></button>
              </div>
          </div>
          
          <!-- SUCCESS SCREEN -->
          <div id="step-success-screen" style="position:absolute; inset:0; background:#111; display:flex; flex-direction:column; align-items:center; justify-content:center; opacity:0; pointer-events:none; z-index:20;">
              <div class="loader-circle" style="width:48px; height:48px; border:4px solid #333; border-top-color:#0B9E58; border-radius:50%; margin-bottom:24px; animation:spin 1s linear infinite;"></div>
              
              <div id="success-content" style="opacity:0; display:flex; flex-direction:column; align-items:center; position:absolute; inset:0; justify-content:center; background:#111;">
                <div id="success-confetti" style="font-size:64px; margin-bottom:16px; transform:scale(0);">&#x1F389;</div>
                <h2 style="font-family:'Outfit'; font-size:32px; font-weight:700; margin-bottom:12px; text-align:center; background:linear-gradient(45deg, #1A56DB, #0B9E58); -webkit-background-clip:text; -webkit-text-fill-color:transparent;">Congratulations!</h2>
                <p style="color:#888; text-align:center; line-height:1.5;">Your agent is live and talking to customers.</p>
              </div>
              
              <!-- Web Chat Bubble Pop -->
              <div id="demo-chat-bubble" style="position:absolute; bottom:-120px; right:0; background:#fff; border-radius:16px 16px 0 16px; padding:16px; color:#111; width:260px; box-shadow:0 10px 30px rgba(0,0,0,0.3); border:1px solid #efefef;">
                 <div style="font-size:13px; font-weight:700; color:var(--accent); margin-bottom:4px;">Sales Agent</div>
                 <div style="font-size:14px; line-height:1.4;">Hi! I'm live on your site. How can I help? &#x1F44B;</div>
              </div>
          </div>
      </div>
      
    </div>
  </div>
</section>
<style>
@keyframes spin { 100% { transform: rotate(360deg); } }
</style>
"""

CUSTOM_ONE_INBOX = """
<section class="section-v2 inbox-section" style="padding-top: 160px; max-width: 1400px; margin:0 auto; display:flex; gap:64px; align-items:center;">
  <div style="flex:1;">
    <span class="gsap-fade-up" style="font-family: 'Geist Mono', monospace; font-size: 12px; color: var(--accent); letter-spacing: .2em; text-transform: uppercase; margin-bottom:16px; display:block;">YOU STAY IN CONTROL</span>
    <h2 class="gsap-fade-up" style="font-family: 'Outfit'; font-size: clamp(40px, 4vw, 56px); margin: 0 0 24px; color: var(--text-primary); line-height:1.1;">It never sends a message you cannot read.</h2>
    <p class="gsap-fade-up" style="font-size: 18px; color: var(--text-secondary); margin-bottom: 24px; line-height: 1.6; max-width:500px;">Every conversation, from every channel, lands in one inbox. Jump in whenever you feel like it and your agent goes quiet on that thread until you are finished.</p>
    <p class="gsap-fade-up" style="font-size: 18px; color: var(--text-secondary); margin-bottom: 0; line-height: 1.6; max-width:500px;">You decide what it is allowed to answer. You decide where it has to stop. Every conversation is there to read. When it hands over, the whole history comes with it.</p>
  </div>
  
  <div style="flex:1.5; display:flex; justify-content:center; align-items:center; min-width:300px;">
    <!-- Inbox UI Mockup -->
    <div class="inbox-mockup" style="opacity:0; transform:scale(0.9); width:100%; max-width:800px; height:500px; background:#fff; border-radius:24px; border:1px solid var(--border-subtle); box-shadow: 0 32px 80px rgba(0,0,0,0.08); display:flex; overflow:hidden; font-family:'Inter', sans-serif;">
      
      <!-- Sidebar -->
      <div style="width:260px; background:#fbfbfd; border-right:1px solid var(--border-subtle); display:flex; flex-direction:column;">
         <div style="padding:24px; border-bottom:1px solid var(--border-subtle);">
            <div style="font-weight:700; font-size:18px; font-family:'Outfit'; color:#111;">Steps Inbox</div>
         </div>
         <div style="flex:1; overflow-y:auto; padding:12px;">
            <!-- WhatsApp Item -->
            <div id="sidebar-wa" style="padding:12px; background:#fff; border-radius:12px; border:1px solid var(--accent); box-shadow:0 4px 12px rgba(0,0,0,0.05); margin-bottom:8px; cursor:pointer; transition:0.3s;">
               <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
                  <div style="font-weight:600; font-size:14px; color:#111; display:flex; align-items:center; gap:6px;">
                     <span class="pulse-dot" style="display:inline-block; width:8px; height:8px; background:var(--accent); border-radius:50%;"></span> Sarah Jenkins
                  </div>
                  <div style="font-size:12px; color:#888;">Just now</div>
               </div>
               <div style="font-size:13px; color:#666; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">Can I speak to a human about this?</div>
               <div style="display:flex; gap:6px; margin-top:8px;">
                  <span class="tag-handover" style="background:#E9F8F0; color:#0B9E58; padding:2px 6px; border-radius:4px; font-size:10px; font-weight:700; opacity:0; transition:0.3s;">HANDOVER</span>
                  <span style="background:#f4f5f7; color:#666; padding:2px 6px; border-radius:4px; font-size:10px; font-weight:600;">WHATSAPP</span>
               </div>
            </div>
            
            <!-- Instagram Item -->
            <div id="sidebar-ig" style="padding:12px; background:transparent; border-radius:12px; border:1px solid transparent; margin-bottom:8px; opacity:0.6; cursor:pointer; transition:0.3s;">
               <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
                  <div style="font-weight:600; font-size:14px; color:#111;">Mike Davies</div>
                  <div style="font-size:12px; color:#888;">10:42 AM</div>
               </div>
               <div style="font-size:13px; color:#666; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">Thanks for the sizing info!</div>
               <div style="display:flex; gap:6px; margin-top:8px;">
                  <span style="background:#EBF3FF; color:var(--accent); padding:2px 6px; border-radius:4px; font-size:10px; font-weight:700;">AI HANDLED</span>
                  <span style="background:#f4f5f7; color:#666; padding:2px 6px; border-radius:4px; font-size:10px; font-weight:600;">INSTAGRAM</span>
               </div>
            </div>
            
            <!-- Web Chat Item -->
            <div id="sidebar-web" style="padding:12px; background:transparent; border-radius:12px; border:1px solid transparent; margin-bottom:8px; opacity:0.6; cursor:pointer; transition:0.3s;">
               <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
                  <div style="font-weight:600; font-size:14px; color:#111;">Alex Chen</div>
                  <div style="font-size:12px; color:#888;">09:15 AM</div>
               </div>
               <div style="font-size:13px; color:#666; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">What are the pricing plans?</div>
               <div style="display:flex; gap:6px; margin-top:8px;">
                  <span style="background:#EBF3FF; color:var(--accent); padding:2px 6px; border-radius:4px; font-size:10px; font-weight:700;">AI HANDLED</span>
                  <span style="background:#f4f5f7; color:#666; padding:2px 6px; border-radius:4px; font-size:10px; font-weight:600;">WEBSITE</span>
               </div>
            </div>
         </div>
      </div>
      
      <!-- Main Chat Area -->
      <div style="flex:1; display:flex; flex-direction:column; background:#fff; position:relative;">
         
         <!-- WHATSAPP CHAT -->
         <div id="chat-wa" style="position:absolute; inset:0; display:flex; flex-direction:column; background:#fff; z-index:3;">
             <!-- Chat Header -->
             <div style="padding:20px 24px; border-bottom:1px solid var(--border-subtle); display:flex; justify-content:space-between; align-items:center;">
                <div>
                   <div style="font-weight:700; font-size:16px; color:#111;">Sarah Jenkins</div>
                   <div style="font-size:13px; color:#666;">WhatsApp | Order #8821</div>
                </div>
                <div class="inbox-status" style="background:#EBF3FF; color:var(--accent); padding:6px 12px; border-radius:100px; font-size:12px; font-weight:600; display:flex; align-items:center; gap:6px; transition:0.3s;">
                   <span class="status-dot-h" style="display:inline-block; width:6px; height:6px; background:var(--accent); border-radius:50%;"></span> <span class="status-text">AI is reading...</span>
                </div>
             </div>
             
             <!-- Chat History -->
             <div class="chat-scroll-area" style="flex:1; padding:24px; overflow-y:auto; display:flex; flex-direction:column; gap:16px; background:#fbfbfd; scroll-behavior: smooth;">
                <div style="align-self:center; font-size:12px; color:#888; font-weight:500;">Today 10:15 AM</div>
                
                <div style="display:flex; gap:12px; max-width:85%;">
                   <div style="width:28px; height:28px; border-radius:50%; background:#e0e0e0; flex-shrink:0;"></div>
                   <div style="background:#fff; padding:12px 16px; border-radius:16px 16px 16px 0; border:1px solid var(--border-subtle); font-size:14px; color:#111; line-height:1.5;">Do you ship to Germany? And how long does it take?</div>
                </div>
                
                <div style="display:flex; gap:12px; max-width:85%; align-self:flex-end;">
                   <div style="background:#EBF3FF; padding:12px 16px; border-radius:16px 16px 0 16px; border:1px solid #d4e5ff; font-size:14px; color:#111; line-height:1.5; position:relative;">
                      <div style="position:absolute; top:-8px; right:12px; font-size:10px; font-weight:700; color:var(--accent); background:#fff; padding:0 4px; border-radius:4px;">AI AGENT</div>
                      Yes! We ship to Germany via DHL Express. It usually takes 2-3 business days. Shipping is free on orders over $150.
                   </div>
                </div>
                
                <div class="human-req" style="display:flex; gap:12px; max-width:85%;">
                   <div style="width:28px; height:28px; border-radius:50%; background:#e0e0e0; flex-shrink:0;"></div>
                   <div style="background:#fff; padding:12px 16px; border-radius:16px 16px 16px 0; border:1px solid var(--border-subtle); font-size:14px; color:#111; line-height:1.5;">Great. I have a custom tax exemption code for my business, can I speak to a human about applying it to this order?</div>
                </div>
                
                <div class="handover-banner" style="display:none; background:#E9F8F0; border:1px solid #c2ebd5; padding:12px; border-radius:12px; align-items:center; justify-content:center; gap:8px; margin:8px 0; opacity:0; transform:translateY(10px);">
                   <span style="font-size:16px;">&#x1F6D1;</span>
                   <span style="font-size:13px; font-weight:600; color:#0B9E58;">Agent automatically paused. Thread handed over to human.</span>
                </div>
                
                <div class="human-reply" style="display:none; gap:12px; max-width:85%; align-self:flex-end; opacity:0; transform:translateY(10px);">
                   <div style="background:var(--text-primary); padding:12px 16px; border-radius:16px 16px 0 16px; font-size:14px; color:#fff; line-height:1.5; position:relative;">
                      <div style="position:absolute; top:-8px; right:12px; font-size:10px; font-weight:700; color:var(--text-primary); background:#fff; padding:0 4px; border-radius:4px; border:1px solid var(--text-primary);">YOU</div>
                      <span id="typewriter-human"></span><span class="cursor-human" style="display:inline-block; width:2px; height:14px; background:#fff; margin-left:2px; animation:blink 1s infinite;"></span>
                   </div>
                </div>
                <div id="scroll-anchor" style="height:1px;"></div>
             </div>
             
             <!-- Chat Input -->
             <div style="padding:16px 24px; border-top:1px solid var(--border-subtle); background:#fff;">
                <div style="background:#f4f5f7; border:1px solid var(--border-subtle); border-radius:12px; padding:12px 16px; display:flex; align-items:center; justify-content:space-between;">
                   <div class="input-placeholder" style="color:#888; font-size:14px;">Reply to Sarah...</div>
                   <div style="color:#aaa; font-weight:600; font-size:12px;">Press Enter to send</div>
                </div>
             </div>
         </div>
         
         <!-- INSTAGRAM CHAT -->
         <div id="chat-ig" style="position:absolute; inset:0; display:flex; flex-direction:column; background:#fff; z-index:2; opacity:0;">
             <div style="padding:20px 24px; border-bottom:1px solid var(--border-subtle); display:flex; justify-content:space-between; align-items:center;">
                <div>
                   <div style="font-weight:700; font-size:16px; color:#111;">Mike Davies</div>
                   <div style="font-size:13px; color:#666;">Instagram DM</div>
                </div>
                <div style="background:#EBF3FF; color:var(--accent); padding:6px 12px; border-radius:100px; font-size:12px; font-weight:600; display:flex; align-items:center; gap:6px;">
                   <span style="display:inline-block; width:6px; height:6px; background:var(--accent); border-radius:50%;"></span> AI Handled
                </div>
             </div>
             <div style="flex:1; padding:24px; overflow-y:auto; display:flex; flex-direction:column; gap:16px; background:#fbfbfd;">
                <div style="align-self:center; font-size:12px; color:#888; font-weight:500;">Today 10:35 AM</div>
                <div style="display:flex; gap:12px; max-width:85%;">
                   <div style="width:28px; height:28px; border-radius:50%; background:#e0e0e0; flex-shrink:0;"></div>
                   <div style="background:#fff; padding:12px 16px; border-radius:16px 16px 16px 0; border:1px solid var(--border-subtle); font-size:14px; color:#111; line-height:1.5;">Do you have the oversized t-shirt in black? Size medium.</div>
                </div>
                <div style="display:flex; gap:12px; max-width:85%; align-self:flex-end;">
                   <div style="background:#EBF3FF; padding:12px 16px; border-radius:16px 16px 0 16px; border:1px solid #d4e5ff; font-size:14px; color:#111; line-height:1.5; position:relative;">
                      <div style="position:absolute; top:-8px; right:12px; font-size:10px; font-weight:700; color:var(--accent); background:#fff; padding:0 4px; border-radius:4px;">AI AGENT</div>
                      Yes! We have exactly 3 left in stock for the Oversized Black (Medium). Shall I hold one for you?
                   </div>
                </div>
                <div style="display:flex; gap:12px; max-width:85%;">
                   <div style="width:28px; height:28px; border-radius:50%; background:#e0e0e0; flex-shrink:0;"></div>
                   <div style="background:#fff; padding:12px 16px; border-radius:16px 16px 16px 0; border:1px solid var(--border-subtle); font-size:14px; color:#111; line-height:1.5;">Thanks for the sizing info! No holding needed, just purchased on the site.</div>
                </div>
             </div>
             <div style="padding:16px 24px; border-top:1px solid var(--border-subtle); background:#fff;">
                <div style="background:#f4f5f7; border:1px solid var(--border-subtle); border-radius:12px; padding:12px 16px; display:flex; align-items:center; justify-content:space-between;">
                   <div style="color:#888; font-size:14px;">Reply to Mike...</div>
                </div>
             </div>
         </div>
         
         <!-- WEBSITE CHAT -->
         <div id="chat-web" style="position:absolute; inset:0; display:flex; flex-direction:column; background:#fff; z-index:1; opacity:0;">
             <div style="padding:20px 24px; border-bottom:1px solid var(--border-subtle); display:flex; justify-content:space-between; align-items:center;">
                <div>
                   <div style="font-weight:700; font-size:16px; color:#111;">Alex Chen</div>
                   <div style="font-size:13px; color:#666;">Website Widget</div>
                </div>
                <div style="background:#EBF3FF; color:var(--accent); padding:6px 12px; border-radius:100px; font-size:12px; font-weight:600; display:flex; align-items:center; gap:6px;">
                   <span style="display:inline-block; width:6px; height:6px; background:var(--accent); border-radius:50%;"></span> AI Handled
                </div>
             </div>
             <div style="flex:1; padding:24px; overflow-y:auto; display:flex; flex-direction:column; gap:16px; background:#fbfbfd;">
                <div style="align-self:center; font-size:12px; color:#888; font-weight:500;">Today 09:10 AM</div>
                <div style="display:flex; gap:12px; max-width:85%;">
                   <div style="width:28px; height:28px; border-radius:50%; background:#e0e0e0; flex-shrink:0;"></div>
                   <div style="background:#fff; padding:12px 16px; border-radius:16px 16px 16px 0; border:1px solid var(--border-subtle); font-size:14px; color:#111; line-height:1.5;">What are the pricing plans?</div>
                </div>
                <div style="display:flex; gap:12px; max-width:85%; align-self:flex-end;">
                   <div style="background:#EBF3FF; padding:12px 16px; border-radius:16px 16px 0 16px; border:1px solid #d4e5ff; font-size:14px; color:#111; line-height:1.5; position:relative;">
                      <div style="position:absolute; top:-8px; right:12px; font-size:10px; font-weight:700; color:var(--accent); background:#fff; padding:0 4px; border-radius:4px;">AI AGENT</div>
                      Our plans start at $49/mo for the Starter tier which includes 1,000 AI conversations. We also have a Pro plan for $149/mo. Would you like to see a detailed feature comparison?
                   </div>
                </div>
                <div style="display:flex; gap:12px; max-width:85%;">
                   <div style="width:28px; height:28px; border-radius:50%; background:#e0e0e0; flex-shrink:0;"></div>
                   <div style="background:#fff; padding:12px 16px; border-radius:16px 16px 16px 0; border:1px solid var(--border-subtle); font-size:14px; color:#111; line-height:1.5;">That would be great, thanks.</div>
                </div>
             </div>
             <div style="padding:16px 24px; border-top:1px solid var(--border-subtle); background:#fff;">
                <div style="background:#f4f5f7; border:1px solid var(--border-subtle); border-radius:12px; padding:12px 16px; display:flex; align-items:center; justify-content:space-between;">
                   <div style="color:#888; font-size:14px;">Reply to Alex...</div>
                </div>
             </div>
         </div>
         
      </div>
      
    </div>
  </div>
</section>
<style>
@keyframes pulse { 0% { box-shadow: 0 0 0 0 rgba(26, 86, 219, 0.4); } 70% { box-shadow: 0 0 0 6px rgba(26, 86, 219, 0); } 100% { box-shadow: 0 0 0 0 rgba(26, 86, 219, 0); } }
.pulse-dot { animation: pulse 2s infinite; }
</style>
"""


CUSTOM_ANALYTICS = """
<section class="section-v2 analytics-section" style="padding-top: 160px; padding-bottom: 160px; max-width: 1400px; margin:0 auto; display:flex; gap:64px; align-items:center;">
  <div style="flex:1;">
    <span class="gsap-fade-up" style="font-family: 'Geist Mono', monospace; font-size: 12px; color: var(--accent); letter-spacing: .2em; text-transform: uppercase; margin-bottom:16px; display:block;">SEE WHAT IT DID</span>
    <h2 class="gsap-fade-up" style="font-family: 'Outfit'; font-size: clamp(40px, 4vw, 56px); margin: 0 0 24px; color: var(--text-primary); line-height:1.1;">A paragraph, not a dashboard.</h2>
    <p class="gsap-fade-up" style="font-size: 18px; color: var(--text-secondary); margin-bottom: 24px; line-height: 1.6; max-width:500px;">Most analytics tell you a number moved. Yours tells you that three people asked for something you do not stock yet.</p>
    <p class="gsap-fade-up" style="font-size: 13px; color: #888; margin-bottom: 0; line-height: 1.5; max-width:500px; border-left: 2px solid var(--border-subtle); padding-left: 12px;">*Every number on this page comes from a real account or is clearly marked as an example. We do not publish numbers we cannot show you.</p>
  </div>
  
  <div style="flex:1.2; display:flex; justify-content:center; align-items:center; min-width:300px; position:relative;">
    <!-- Background Glow -->
    <div style="position:absolute; width:100%; height:100%; background:radial-gradient(circle at center, rgba(26,86,219,0.1) 0%, transparent 70%); z-index:0; pointer-events:none;"></div>
    
    <!-- Analytics Paragraph Card -->
    <div class="analytics-card" style="opacity:0; transform:translateY(40px); width:100%; max-width:600px; background:#fff; border-radius:24px; border:1px solid var(--border-subtle); box-shadow: 0 32px 80px rgba(0,0,0,0.06); padding:48px; position:relative; z-index:1;">
       
       <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:24px; border-bottom:1px solid var(--border-subtle); padding-bottom:16px;">
          <div style="font-family:'Geist Mono', monospace; font-size:12px; color:#888; text-transform:uppercase; letter-spacing:0.1em;">The Weekly Summary</div>
          <div style="background:#f4f5f7; color:#666; font-size:11px; font-weight:600; padding:4px 8px; border-radius:4px;">EXAMPLE ACCOUNT</div>
       </div>
       
       <div style="font-family:'Outfit'; font-size:28px; color:#111; line-height:1.5; font-weight:400;">
          This week your agent handled 
          <span class="hl-stat hl-1" style="display:inline-block; font-weight:700; color:var(--accent); background:#EBF3FF; padding:0 8px; border-radius:8px; margin:0 4px; box-shadow:0 4px 12px rgba(26,86,219,0.15);"><span id="count-1">0</span></span> 
          conversations. It answered 
          <span class="hl-stat hl-2" style="display:inline-block; font-weight:700; color:#0B9E58; background:#E9F8F0; padding:0 8px; border-radius:8px; margin:0 4px; box-shadow:0 4px 12px rgba(11,158,88,0.15);"><span id="count-2">0</span></span> 
          on its own, booked 
          <span class="hl-stat hl-3" style="display:inline-block; font-weight:700; color:#8B5CF6; background:#F5F3FF; padding:0 8px; border-radius:8px; margin:0 4px; box-shadow:0 4px 12px rgba(139,92,246,0.15);"><span id="count-3">0</span></span> 
          meetings, and passed 
          <span class="hl-stat hl-4" style="display:inline-block; font-weight:700; color:#F59E0B; background:#FEF3C7; padding:0 8px; border-radius:8px; margin:0 4px; box-shadow:0 4px 12px rgba(245,158,11,0.15);"><span id="count-4">0</span></span> 
          to your team.
       </div>
       
       <div class="insight-reveal" style="opacity:0; transform:translateY(10px); margin-top:32px; padding:24px; background:#111; border-radius:16px; position:relative; overflow:hidden;">
          <div style="position:absolute; top:0; left:0; width:4px; height:100%; background:linear-gradient(to bottom, #F59E0B, #EA580C);"></div>
          <div style="display:flex; gap:16px; align-items:flex-start;">
             <div style="width:32px; height:32px; background:rgba(245,158,11,0.2); border-radius:8px; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#F59E0B" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 16v-4"></path><path d="M12 8h.01"></path></svg>
             </div>
             <div>
                <div style="color:#F59E0B; font-size:12px; font-weight:700; letter-spacing:0.05em; margin-bottom:4px; text-transform:uppercase;">Key Insight Generated</div>
                <div style="color:#fff; font-size:16px; line-height:1.5;">Three customers asked about a product you do not stock yet.</div>
             </div>
          </div>
       </div>
       
    </div>
  </div>
</section>
"""



CUSTOM_COPILOT = """
<section class="section-v2 copilot-section" style="padding-top: 160px; padding-bottom: 160px; max-width: 1400px; margin:0 auto; display:flex; gap:64px; align-items:center;">
  <div style="flex:1;">
    <span class="gsap-fade-up" style="font-family: 'Geist Mono', monospace; font-size: 12px; color: var(--accent); letter-spacing: .2em; text-transform: uppercase; margin-bottom:16px; display:block;">INTERNAL COPILOT</span>
    <h2 class="gsap-fade-up" style="font-family: 'Outfit'; font-size: clamp(40px, 4vw, 56px); margin: 0 0 24px; color: var(--text-primary); line-height:1.1;">The same brain, pointed inwards.</h2>
    <p class="gsap-fade-up" style="font-size: 18px; color: var(--text-secondary); margin-bottom: 24px; line-height: 1.6; max-width:500px;">Your team asks it where the leave policy lives, what you agreed with that client in March, which version of the deck is the current one.</p>
    <p class="gsap-fade-up" style="font-size: 18px; color: var(--text-secondary); margin-bottom: 32px; line-height: 1.6; max-width:500px;">It looks through everything you have connected, answers, and shows you exactly which document it got that from.</p>
    
    <a href="#" class="gsap-fade-up" style="display:inline-flex; align-items:center; gap:8px; color:var(--text-primary); font-weight:600; text-decoration:none; border-bottom:1px solid var(--text-primary); padding-bottom:4px;">
       See Internal Copilot
       <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14"></path><path d="M12 5l7 7-7 7"></path></svg>
    </a>
  </div>
  
  <div style="flex:1.2; display:flex; justify-content:center; align-items:center; min-width:300px; position:relative;">
    
    <!-- Copilot Mockup -->
    <div class="copilot-mockup" style="opacity:0; transform:scale(0.9); width:100%; max-width:640px; background:#1f2228; border-radius:24px; border:1px solid #3a3f4a; box-shadow: 0 32px 80px rgba(0,0,0,0.4); padding:32px; display:flex; flex-direction:column; gap:24px; font-family:'Inter', sans-serif;">
       
       <!-- Search Bar -->
       <div style="display:flex; align-items:center; gap:16px; background:#111; border:1px solid #333; border-radius:16px; padding:16px 24px;">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#666" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><path d="M21 21l-4.35-4.35"></path></svg>
          <div style="flex:1; color:#fff; font-size:16px; font-family:'Geist Mono', monospace;">
             <span id="cp-typewriter"></span><span class="cp-cursor" style="display:inline-block; width:2px; height:18px; background:var(--accent); margin-left:4px; animation:blink 1s infinite;"></span>
          </div>
          <div class="cp-enter" style="opacity:0; transform:scale(0.8); background:#333; color:#aaa; font-size:12px; font-weight:600; padding:4px 8px; border-radius:6px; border:1px solid #444;">ENTER</div>
       </div>
       
       <!-- Scanning Animation -->
       <div class="cp-scanning" style="height:0; overflow:hidden; opacity:0; display:flex; flex-direction:column; gap:12px;">
          <div style="display:flex; gap:12px; align-items:center;">
             <div class="cp-spinner" style="width:16px; height:16px; border:2px solid #333; border-top-color:var(--accent); border-radius:50%;"></div>
             <div style="color:#888; font-size:14px; font-family:'Geist Mono', monospace;">Searching internal knowledge base...</div>
          </div>
          <div style="display:flex; gap:8px;">
             <div class="cp-doc doc-1" style="opacity:0; transform:translateY(10px); background:#2A2D35; border:1px solid #3a3f4a; padding:6px 12px; border-radius:8px; font-size:12px; color:#aaa; display:flex; align-items:center; gap:6px;">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#DB4437" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg> Gmail
             </div>
             <div class="cp-doc doc-2" style="opacity:0; transform:translateY(10px); background:#2A2D35; border:1px solid #3a3f4a; padding:6px 12px; border-radius:8px; font-size:12px; color:#aaa; display:flex; align-items:center; gap:6px;">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#0F9D58" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg> Google Drive
             </div>
             <div class="cp-doc doc-3" style="opacity:0; transform:translateY(10px); background:#2A2D35; border:1px solid #3a3f4a; padding:6px 12px; border-radius:8px; font-size:12px; color:#aaa; display:flex; align-items:center; gap:6px;">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#4A154B" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg> Slack
             </div>
          </div>
       </div>
       
       <!-- Answer Result -->
       <div class="cp-result" style="height:0; overflow:hidden; opacity:0; display:flex; flex-direction:column; gap:16px;">
          <div style="background:#2A2D35; border:1px solid #3a3f4a; border-radius:16px; padding:24px; position:relative;">
             <div style="position:absolute; top:-12px; left:24px; background:linear-gradient(45deg, #1A56DB, #8B5CF6); padding:4px 12px; border-radius:100px; font-size:11px; font-weight:700; color:#fff; letter-spacing:0.05em;">ANSWER</div>
             <p style="color:#fff; font-size:15px; line-height:1.6; margin:0; margin-top:8px;">
                We agreed to a <strong style="color:var(--accent);">10% discount on the Enterprise tier</strong> for Acme Corp, starting April 1st. They also requested a custom SLA, which was approved by Legal.
             </p>
             
             <!-- Sources -->
             <div style="margin-top:20px; border-top:1px solid #3a3f4a; padding-top:16px;">
                <div style="font-size:12px; color:#888; font-weight:600; margin-bottom:12px;">SOURCES</div>
                <div style="display:flex; gap:12px; flex-wrap:wrap;">
                   <div style="background:#111; border:1px solid #333; padding:8px 12px; border-radius:8px; display:flex; align-items:center; gap:8px; cursor:pointer;">
                      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#0F9D58" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path></svg>
                      <div>
                         <div style="color:#ddd; font-size:13px; font-weight:500;">Acme_Contract_March.pdf</div>
                         <div style="color:#666; font-size:11px;">Google Drive &bull; Page 4</div>
                      </div>
                   </div>
                   <div style="background:#111; border:1px solid #333; padding:8px 12px; border-radius:8px; display:flex; align-items:center; gap:8px; cursor:pointer;">
                      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#4A154B" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect></svg>
                      <div>
                         <div style="color:#ddd; font-size:13px; font-weight:500;">#legal-approvals</div>
                         <div style="color:#666; font-size:11px;">Slack &bull; Mar 15</div>
                      </div>
                   </div>
                </div>
             </div>
          </div>
       </div>
       
    </div>
  </div>
</section>
"""



CUSTOM_FIT = """
<section class="section-v2 fit-section" style="padding-top: 160px; padding-bottom: 160px; max-width: 1400px; margin:0 auto; display:flex; gap:64px; align-items:center;">
  
  <div style="flex:1;">
    <span class="gsap-fade-up" style="font-family: 'Geist Mono', monospace; font-size: 12px; color: var(--accent); letter-spacing: .2em; text-transform: uppercase; margin-bottom:16px; display:block;">HONEST FIT</span>
    <h2 class="gsap-fade-up" style="font-family: 'Outfit'; font-size: clamp(40px, 4vw, 56px); margin: 0 0 24px; color: var(--text-primary); line-height:1.1;">You might not need this.</h2>
    <p class="gsap-fade-up" style="font-size: 18px; color: var(--text-secondary); margin-bottom: 24px; line-height: 1.6; max-width:500px;">Some businesses are better off without it, and it is cheaper for both of us if you work that out now rather than in month three.</p>
  </div>
  
  <div class="gsap-fade-up" style="flex:1.5; display:flex; flex-direction:column; gap:24px; min-width:300px;">
    
    <!-- Good Fit Card -->
    <div style="background:#fff; border:1px solid var(--border-subtle); border-radius:24px; padding:40px; box-shadow: 0 12px 40px rgba(0,0,0,0.04); display:flex; flex-direction:column; gap:24px; transition:0.3s; position:relative; overflow:hidden;" onmouseover="this.style.borderColor='#0B9E58'; this.style.boxShadow='0 12px 40px rgba(11,158,88,0.1)'" onmouseout="this.style.borderColor='var(--border-subtle)'; this.style.boxShadow='0 12px 40px rgba(0,0,0,0.04)'">
       <div style="position:absolute; top:0; left:0; width:6px; height:100%; background:#0B9E58;"></div>
       <div style="display:flex; align-items:center; gap:12px;">
          <div style="width:40px; height:40px; border-radius:12px; background:#E9F8F0; display:flex; align-items:center; justify-content:center;">
             <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#0B9E58" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
          </div>
          <h3 style="font-family:'Outfit'; font-size:24px; font-weight:600; margin:0; color:#111;">Worth trying if...</h3>
       </div>
       
       <div style="display:flex; flex-direction:column; gap:16px;">
          <div style="display:flex; gap:12px; align-items:flex-start;">
             <div style="color:#0B9E58; margin-top:2px;">•</div>
             <div style="font-size:16px; color:#555; line-height:1.5;">People are messaging you on WhatsApp, Instagram or your website in real numbers.</div>
          </div>
          <div style="display:flex; gap:12px; align-items:flex-start;">
             <div style="color:#0B9E58; margin-top:2px;">•</div>
             <div style="font-size:16px; color:#555; line-height:1.5;">You are losing sales because nobody replied fast enough.</div>
          </div>
          <div style="display:flex; gap:12px; align-items:flex-start;">
             <div style="color:#0B9E58; margin-top:2px;">•</div>
             <div style="font-size:16px; color:#555; line-height:1.5;">You answer the same handful of questions every day and have started to resent them.</div>
          </div>
          <div style="display:flex; gap:12px; align-items:flex-start;">
             <div style="color:#0B9E58; margin-top:2px;">•</div>
             <div style="font-size:16px; color:#555; line-height:1.5;">You want to decide what the AI is allowed to say.</div>
          </div>
       </div>
    </div>
    
    <!-- Bad Fit Card -->
    <div style="background:#fff; border:1px solid var(--border-subtle); border-radius:24px; padding:40px; box-shadow: 0 12px 40px rgba(0,0,0,0.04); display:flex; flex-direction:column; gap:24px; transition:0.3s; position:relative; overflow:hidden;" onmouseover="this.style.borderColor='#DB4437'; this.style.boxShadow='0 12px 40px rgba(219,68,55,0.1)'" onmouseout="this.style.borderColor='var(--border-subtle)'; this.style.boxShadow='0 12px 40px rgba(0,0,0,0.04)'">
       <div style="position:absolute; top:0; left:0; width:6px; height:100%; background:#DB4437;"></div>
       <div style="display:flex; align-items:center; gap:12px;">
          <div style="width:40px; height:40px; border-radius:12px; background:#FCE8E6; display:flex; align-items:center; justify-content:center;">
             <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#DB4437" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
          </div>
          <h3 style="font-family:'Outfit'; font-size:24px; font-weight:600; margin:0; color:#111;">Probably not, if...</h3>
       </div>
       
       <div style="display:flex; flex-direction:column; gap:16px;">
          <div style="display:flex; gap:12px; align-items:flex-start;">
             <div style="color:#DB4437; margin-top:2px;">•</div>
             <div style="font-size:16px; color:#555; line-height:1.5;">You want an AI running loose with nobody checking on it.</div>
          </div>
          <div style="display:flex; gap:12px; align-items:flex-start;">
             <div style="color:#DB4437; margin-top:2px;">•</div>
             <div style="font-size:16px; color:#555; line-height:1.5;">You are hoping to let your support team go.</div>
          </div>
          <div style="display:flex; gap:12px; align-items:flex-start;">
             <div style="color:#DB4437; margin-top:2px;">•</div>
             <div style="font-size:16px; color:#555; line-height:1.5;">You expect it to work properly without anyone setting it up.</div>
          </div>
       </div>
    </div>
    
  </div>
  
</section>
"""



CUSTOM_CTA = """
<section class="section-v2 cta-section" style="padding-top: 200px; padding-bottom: 200px; background: #0A0A0B; color: #fff; position: relative; overflow: hidden; text-align: center;">
  
  <!-- Drifting Receipts Background -->
  <div class="drifting-bg" style="position: absolute; top: 0; left: 0; width: 200%; height: 100%; display: flex; align-items: center; justify-content: flex-start; z-index: 0; opacity: 0.03; pointer-events: none;">
     <div class="receipt-track" style="display: flex; gap: 40px; font-family: 'Geist Mono', monospace; font-size: 80px; font-weight: 700; white-space: nowrap; text-transform: uppercase;">
        <span>CART UPDATED &bull; MEETING BOOKED &bull; LEAD CREATED &bull; ORDER TRACKED &bull; TICKET RESOLVED &bull;</span>
        <span>CART UPDATED &bull; MEETING BOOKED &bull; LEAD CREATED &bull; ORDER TRACKED &bull; TICKET RESOLVED &bull;</span>
        <span>CART UPDATED &bull; MEETING BOOKED &bull; LEAD CREATED &bull; ORDER TRACKED &bull; TICKET RESOLVED &bull;</span>
     </div>
  </div>
  
  <!-- Content -->
  <div style="position: relative; z-index: 1; max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; align-items: center;">
     
     <h2 class="gsap-fade-up" style="font-family: 'Outfit'; font-size: clamp(48px, 6vw, 80px); margin: 0 0 24px; color: #fff; line-height: 1.1; letter-spacing: -0.02em;">Somebody is typing right now.</h2>
     
     <p class="gsap-fade-up" style="font-size: 24px; color: #888; margin-bottom: 48px; line-height: 1.5; max-width: 600px;">
        Set it up this afternoon.<br>Find out what it did over breakfast.
     </p>
     
     <div class="gsap-fade-up" style="display: flex; gap: 16px; align-items: center; justify-content: center; margin-bottom: 24px; flex-wrap: wrap;">
        <a href="#" class="btn-primary" style="background: #fff; color: #111; padding: 18px 36px; border-radius: 100px; font-weight: 600; font-size: 16px; text-decoration: none; transition: 0.3s; border: 1px solid #fff;">
           Start free trial
        </a>
        <a href="#" class="btn-secondary" style="background: transparent; color: #fff; padding: 18px 36px; border-radius: 100px; font-weight: 600; font-size: 16px; text-decoration: none; transition: 0.3s; border: 1px solid rgba(255,255,255,0.2);">
           Book a demo
        </a>
     </div>
     
     <div class="gsap-fade-up" style="display: flex; gap: 16px; align-items: center; justify-content: center; color: #666; font-size: 14px; font-family: 'Geist Mono', monospace;">
        <span><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-right:6px; vertical-align:-2px;"><polyline points="20 6 9 17 4 12"></polyline></svg> No credit card</span>
        <span>&bull;</span>
        <span><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-right:6px; vertical-align:-2px;"><polyline points="20 6 9 17 4 12"></polyline></svg> Live in under an hour</span>
     </div>
     
  </div>
  
</section>
<style>
@keyframes drift {
    0% { transform: translateX(0); }
    100% { transform: translateX(-33.33%); }
}
.receipt-track {
    animation: drift 30s linear infinite;
}
.btn-primary:hover { background: #eee !important; transform: translateY(-2px); box-shadow: 0 10px 20px rgba(255,255,255,0.1); }
.btn-secondary:hover { background: rgba(255,255,255,0.1) !important; border-color: rgba(255,255,255,0.4) !important; transform: translateY(-2px); }
</style>
"""


CUSTOM_HOME_ACCORDION = """
  <section class="section-v2" style="background: var(--bg-surface-2);">
    <div style="text-align: center; margin-bottom: 64px;">
      <span style="font-family: 'Geist Mono', monospace; font-size: 12px; color: var(--text-secondary); letter-spacing: .2em; text-transform: uppercase;">BUILT AROUND YOUR BUSINESS</span>
      <h2 style="font-family: 'Outfit'; font-size: 48px; margin-top: 16px; color: var(--text-primary);">Made for the way your customers buy.</h2>
    </div>
    <div class="industries-accordion gsap-fade-up">
      <a href="./solutions/ecommerce/index.html" class="accordion-panel" style="background-image: url('https://images.unsplash.com/photo-1607082348824-0a96f2a4b9da?w=800&q=80'); text-decoration:none;">
        <div class="accordion-content"><h3 class="accordion-title">Ecommerce</h3><p class="accordion-desc">Checks live stock before it promises anything. Recovers the cart before the customer forgets.</p></div>
      </a>
      <a href="./solutions/saas/index.html" class="accordion-panel" style="background-image: url('https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&q=80'); text-decoration:none;">
        <div class="accordion-content"><h3 class="accordion-title">SaaS & Tech</h3><p class="accordion-desc">Answers integration questions from your own docs. Compares plans without pushing the expensive one.</p></div>
      </a>
      <a href="./solutions/healthcare/index.html" class="accordion-panel" style="background-image: url('https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=800&q=80'); text-decoration:none;">
        <div class="accordion-content"><h3 class="accordion-title">Healthcare & Wellness</h3><p class="accordion-desc">Shows which doctor is free. Books the appointment inside the conversation. Sends the reminder so the slot isn't wasted.</p></div>
      </a>
      <a href="./solutions/real-estate/index.html" class="accordion-panel" style="background-image: url('https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=800&q=80'); text-decoration:none;">
        <div class="accordion-content"><h3 class="accordion-title">Real Estate</h3><p class="accordion-desc">Qualifies the buyer before anyone picks up the phone. Books the site visit while they're still looking.</p></div>
      </a>
    </div>
  </section>
"""

def render_s05(kicker, h1, p):
    return f"""
    <section class="hero-v2">
        <div class="hero-bg-glow"></div>
        <div class="gsap-fade-up" style="color:var(--accent); font-weight:700; font-size:14px; letter-spacing:1px; margin-bottom:24px; text-transform:uppercase;">{kicker}</div>
        <h1 class="gsap-fade-up">{h1}</h1>
        <p class="gsap-fade-up">{p}</p>
        <div class="gsap-fade-up" style="display:flex; gap:16px; justify-content:center;">
            <button class="btn-primary">Start free trial</button>
            <button class="btn-outline">Book a demo</button>
        </div>
    </section>
    """

FOOTER = """
  <!-- S03 CTA Band -->
  <section class="cta-band">
    <h2>Somebody is typing right now.</h2>
    <div style="display:flex; justify-content:center; gap:16px;">
      <a href="{root_prefix}partners/apply/index.html"><button class="btn-primary">Start free trial</button></a>
      <button class="btn-outline">Book a demo</button>
    </div>
  </section>
  <footer class="footer">
    <div class="footer-container">
      <div class="footer-col" style="grid-column: span 2;">
        <div style="font-weight: 800; font-size: 20px; margin-bottom:16px;">StepsAI</div>
        <p style="color:var(--text-secondary); font-size:14px; max-width: 250px;">Your AI agent layer for every business. Answer, capture, and close at any hour.</p>
      </div>
      <div class="footer-col">
        <h4>Product</h4>
        <ul><li><a href="{root_prefix}product/ai-agents/index.html">AI Agents</a></li><li><a href="{root_prefix}pricing/index.html">Pricing</a></li></ul>
      </div>
      <div class="footer-col">
        <h4>Solutions</h4>
        <ul><li><a href="{root_prefix}solutions/ecommerce/index.html">E-Commerce</a></li><li><a href="{root_prefix}solutions/real-estate/index.html">Real Estate</a></li></ul>
      </div>
      <div class="footer-col">
        <h4>Company</h4>
        <ul><li><a href="{root_prefix}about/index.html">About</a></li><li><a href="{root_prefix}contact/index.html">Contact</a></li></ul>
      </div>
    </div>
  </footer>
  <script>
    gsap.registerPlugin(ScrollTrigger);
    gsap.to(".gsap-fade-up", { y: 0, opacity: 1, duration: 1, stagger: 0.15, ease: "power3.out" });
    gsap.utils.toArray('.gsap-scale-in').forEach(element => {
      gsap.to(element, { scrollTrigger: { trigger: element, start: "top 85%", toggleActions: "play none none reverse" }, scale: 1, opacity: 1, duration: 0.8, ease: "power3.out" });
    });
    const stepProgress = document.getElementById('stepLineProgress');
    if(stepProgress) { window.addEventListener('scroll', () => { const docHeight = document.documentElement.scrollHeight - window.innerHeight; const progress = (window.scrollY / docHeight) * 100; stepProgress.style.height = progress + "%"; }); }
    if(document.getElementById('screen-wa')) {
        let tl = gsap.timeline({ repeat: -1, repeatDelay: 2 });
        tl.to(".stp-t1", { display: "none", duration: 0.1 }, "+=1")
          .to(".stp-2", { display: "block", duration: 0.1 }).to(".stp-3", { opacity: 1, y: 0, duration: 0.4, ease: "back.out" }, "+=0.8")
          .to(".stp-t2", { display: "flex", duration: 0.1 }).to(".stp-t2", { display: "none", duration: 0.1 }, "+=1.2")
          .to(".stp-4", { display: "block", duration: 0.1 }).to(".stp-5", { opacity: 1, scale: 1, duration: 0.5, ease: "back.out(1.5)" }, "+=0.5")
          .to("#screen-wa", { opacity: 0, duration: 0.5, ease: "power2.inOut" }, "+=3").to("#screen-ig", { opacity: 1, zIndex: 3, duration: 0.5, ease: "power2.inOut" }, "<")
          .to(".stp-ig-t1", { display: "none", duration: 0.1 }, "+=1").to(".stp-ig-2", { display: "block", duration: 0.1 })
          .to(".stp-ig-3", { opacity: 1, y: 0, duration: 0.4, ease: "back.out" }, "+=0.8").to(".stp-ig-t2", { display: "flex", duration: 0.1 })
          .to(".stp-ig-t2", { display: "none", duration: 0.1 }, "+=1.2").to(".stp-ig-4", { display: "block", duration: 0.1 })
          .to(".stp-ig-5", { opacity: 1, scale: 1, duration: 0.5, ease: "back.out(1.5)" }, "+=0.5")
          .to("#screen-ig", { opacity: 0, duration: 0.5, ease: "power2.inOut" }, "+=3").to("#screen-wa", { opacity: 1, zIndex: 3, duration: 0.5, ease: "power2.inOut" }, "<")
          .set([".stp-2", ".stp-4", ".stp-ig-2", ".stp-ig-4", ".stp-t2", ".stp-ig-t2"], { display: "none" })
          .set([".stp-t1", ".stp-ig-t1"], { display: "flex" })
          .set([".stp-3", ".stp-5", ".stp-ig-3", ".stp-ig-5"], { opacity: 0, scale: 0.94, y: 10 });
    }
    
    // Setup Storytelling Animation
    let setupPlayed = false;
    ScrollTrigger.create({
      trigger: ".setup-section",
      start: "top 75%",
      onEnter: () => {
        if(setupPlayed) return;
        setupPlayed = true;
        let setupTl = gsap.timeline();
        
        // --- STEP 1 ---
        let urlText = "https://habitiq.app/";
        let el = document.getElementById("typewriter-url");
        if(el) {
            setupTl.to(".setup-mockup", { opacity: 1, scale: 1, duration: 0.8, ease: "power3.out" })
            .to({}, {duration: 0.2}) // tiny delay
            .add(() => {
              let i = 0;
              let interval = setInterval(() => {
                if(i < urlText.length) { el.textContent += urlText.charAt(i); i++; }
                else { clearInterval(interval); }
              }, 60);
            })
            .to({}, {duration: 1.8}) // wait after typing
            .to("#mockup-success-state", { height: "auto", opacity: 1, duration: 0.6, ease: "power2.out" })
            .to("#mockup-proceed-btn", { background: "#fff", color: "#111", duration: 0.3 }, "<")
            .add(() => { document.getElementById("mockup-proceed-btn").textContent = "Proceed"; }, "<")
            
            // Highlight step 1 text dim
            .to(".step-txt-1", { opacity: 0.4 }, "+=1")
            .to(".step-num-1", { background: "var(--bg-surface)", color: "var(--text-primary)" }, "<")
            
            // Transition to Step 2
            .to("#mockup-proceed-btn", { scale: 0.95, duration: 0.1 })
            .to("#mockup-proceed-btn", { scale: 1, duration: 0.1 })
            .to("#setup-step-1", { opacity: 0, x: -50, duration: 0.4 }, "+=0.2")
            .to("#setup-step-2", { opacity: 1, x: 0, zIndex: 10, duration: 0.4 }, "<")
            .fromTo("#setup-step-2", { x: 50 }, { x: 0, duration: 0.4 }, "<")
            
            // Highlight step 2 text
            .to(".step-txt-2", { opacity: 1 }, "<")
            .to(".step-num-2", { background: "var(--text-primary)", color: "var(--bg-surface)" }, "<")

            // --- STEP 2 ---
            .add(() => {
                let nameEl = document.getElementById("typewriter-name");
                let nameText = "StepsAI Sales Agent";
                let j = 0;
                let c = document.querySelector(".cursor2");
                if(c) c.style.opacity = 1;
                let nameInterval = setInterval(() => {
                if(j < nameText.length) { nameEl.textContent += nameText.charAt(j); j++; }
                else { clearInterval(nameInterval); }
                }, 50);
            })
            .to({}, {duration: 1.5})
            .to("#sim-cursor-1", { opacity: 1, top: "180px", left: "150px", duration: 0.5 }) 
            .to("#sim-cursor-1", { scale: 0.8, duration: 0.1 })
            .to("#target-color", { border: "2px solid #fff", scale: 1.1, duration: 0.2 })
            .to("#sim-cursor-1", { scale: 1, opacity: 0, duration: 0.2 })
            
            // Highlight step 2 text dim
            .to(".step-txt-2", { opacity: 0.4 }, "+=0.5")
            .to(".step-num-2", { background: "var(--bg-surface)", color: "var(--text-primary)" }, "<")

            // Transition to Step 3
            .to("#mockup-proceed-btn-2", { scale: 0.95, duration: 0.1 })
            .to("#mockup-proceed-btn-2", { scale: 1, duration: 0.1 })
            .to("#setup-step-2", { opacity: 0, x: -50, duration: 0.4 }, "+=0.2")
            .to("#setup-step-3", { opacity: 1, zIndex: 10, duration: 0.4 }, "<")
            .fromTo("#setup-step-3", { x: 50 }, { x: 0, duration: 0.4 }, "<")
            
            // Highlight step 3 text
            .to(".step-txt-3", { opacity: 1 }, "<")
            .to(".step-num-3", { background: "var(--text-primary)", color: "var(--bg-surface)" }, "<")

            // --- STEP 3 ---
            .to("#sim-cursor-2", { opacity: 1, top: "140px", left: "380px", duration: 0.5 }, "+=0.5")
            .to("#sim-cursor-2", { scale: 0.8, duration: 0.1 })
            .to("#toggle-wa", { background: "#0B9E58", duration: 0.2 })
            .to("#toggle-wa .toggle-thumb", { left: "18px", background: "#fff", duration: 0.2 }, "<")
            .to("#sim-cursor-2", { scale: 1, top: "220px", left: "380px", duration: 0.4 })
            .to("#sim-cursor-2", { scale: 0.8, duration: 0.1 })
            .to("#toggle-web", { background: "#0B9E58", duration: 0.2 })
            .to("#toggle-web .toggle-thumb", { left: "18px", background: "#fff", duration: 0.2 }, "<")
            .to("#sim-cursor-2", { scale: 1, opacity: 0, duration: 0.2 })

            // Click Go Live
            .to("#mockup-go-live-btn", { scale: 0.95, duration: 0.1 }, "+=0.5")
            .to("#mockup-go-live-btn", { scale: 1, duration: 0.1 })

            // 3 second Loading & Success Screen
            .to("#step-3-content", { opacity: 0, duration: 0.3 }, "+=0.2")
            .to("#step-success-screen", { opacity: 1, duration: 0.3 })
            .to({}, { duration: 2.5 }) // simulate 2.5s loading
            .to(".loader-circle", { opacity: 0, duration: 0.2 })
            .to("#success-content", { opacity: 1, duration: 0.3 })
            .to("#success-confetti", { scale: 1, rotation: 360, duration: 0.8, ease: "back.out(1.5)" }, "<")
            .to("#demo-chat-bubble", { bottom: "32px", duration: 0.6, ease: "back.out(1.2)" }, "+=0.5");
        }
      }
    });
    
    
    
    
    // Copilot Storytelling Animation
    let copilotPlayed = false;
    ScrollTrigger.create({
      trigger: ".copilot-section",
      start: "top 75%",
      onEnter: () => {
        if(copilotPlayed) return;
        copilotPlayed = true;
        let tl = gsap.timeline();
        
        // 1. Enter mockup
        tl.to(".copilot-mockup", { opacity: 1, scale: 1, duration: 0.8, ease: "power3.out" })
          .to({}, {duration: 0.4})
          
          // 2. Type question
          .add(() => {
              let text = "What did we agree with Acme in March?";
              let el = document.getElementById("cp-typewriter");
              let i = 0;
              let interval = setInterval(() => {
                if(i < text.length) {
                  if(el) el.textContent += text.charAt(i);
                  i++;
                } else {
                  clearInterval(interval);
                }
              }, 40);
          })
          .to({}, {duration: 1.8}) // Wait for typing
          
          // 3. Hit Enter
          .to(".cp-enter", { opacity: 1, scale: 1, duration: 0.2, ease: "back.out(2)" })
          .to(".cp-enter", { background: "var(--accent)", color: "#fff", duration: 0.1 })
          .to(".cp-enter", { background: "#333", color: "#aaa", duration: 0.2 }, "+=0.1")
          .add(() => { let c = document.querySelector(".cp-cursor"); if(c) c.style.display="none"; })
          
          // 4. Show scanning
          .to(".cp-scanning", { height: "auto", opacity: 1, duration: 0.4, ease: "power2.out" })
          .to(".doc-1", { opacity: 1, y: 0, duration: 0.3, ease: "back.out" }, "+=0.2")
          .to(".doc-2", { opacity: 1, y: 0, duration: 0.3, ease: "back.out" }, "+=0.2")
          .to(".doc-3", { opacity: 1, y: 0, duration: 0.3, ease: "back.out" }, "+=0.2")
          
          // Animate spinner
          .to(".cp-spinner", { rotation: 720, duration: 2.5, ease: "power1.inOut" }, "<")
          
          // 5. Show Result
          .to(".cp-scanning", { height: 0, opacity: 0, duration: 0.3, ease: "power2.in" })
          .to(".cp-result", { height: "auto", opacity: 1, duration: 0.6, ease: "power3.out" });
      }
    });

// Analytics Storytelling Animation
    let analyticsPlayed = false;
    ScrollTrigger.create({
      trigger: ".analytics-section",
      start: "top 75%",
      onEnter: () => {
        if(analyticsPlayed) return;
        analyticsPlayed = true;
        let tl = gsap.timeline();
        
        tl.to(".analytics-card", { opacity: 1, y: 0, duration: 0.8, ease: "power3.out" })
          .to({}, {duration: 0.4})
          
          // Animate counters
          .add(() => {
              let obj = { val1: 0, val2: 0, val3: 0, val4: 0 };
              gsap.to(obj, {
                  val1: 412, val2: 358, val3: 24, val4: 30,
                  duration: 2.5,
                  ease: "power2.out",
                  onUpdate: () => {
                      document.getElementById("count-1").innerText = Math.floor(obj.val1);
                      document.getElementById("count-2").innerText = Math.floor(obj.val2);
                      document.getElementById("count-3").innerText = Math.floor(obj.val3);
                      document.getElementById("count-4").innerText = Math.floor(obj.val4);
                  }
              });
          })
          
          // Slight pop on the highlight backgrounds during count
          .fromTo(".hl-1", {scale:0.95}, {scale:1, duration:0.5, ease:"back.out(2)"}, "<0.2")
          .fromTo(".hl-2", {scale:0.95}, {scale:1, duration:0.5, ease:"back.out(2)"}, "<0.3")
          .fromTo(".hl-3", {scale:0.95}, {scale:1, duration:0.5, ease:"back.out(2)"}, "<0.2")
          .fromTo(".hl-4", {scale:0.95}, {scale:1, duration:0.5, ease:"back.out(2)"}, "<0.2")
          
          .to({}, {duration: 1.5}) // Let the numbers finish
          
          // Reveal Insight
          .to(".insight-reveal", { opacity: 1, y: 0, duration: 0.6, ease: "back.out(1.2)" });
      }
    });

// Inbox Storytelling Animation
    let inboxPlayed = false;
    ScrollTrigger.create({
      trigger: ".inbox-section",
      start: "top 75%",
      onEnter: () => {
        if(inboxPlayed) return;
        inboxPlayed = true;
        let tl = gsap.timeline();
        
        // 1. Enter mockup
        tl.to(".inbox-mockup", { opacity: 1, scale: 1, duration: 0.8, ease: "power3.out" })
          .to({}, {duration: 0.5}) // reading the question
          
          // 2. Handover triggers (WhatsApp)
          .to(".handover-banner", { display: "flex", duration: 0.1 })
          .to(".handover-banner", { opacity: 1, y: 0, duration: 0.5, ease: "back.out" })
          
          // Change status pill
          .to(".inbox-status", { background: "#E9F8F0", color: "#0B9E58", duration: 0.3 }, "<")
          .to(".status-dot-h", { background: "#0B9E58", duration: 0.3 }, "<")
          .add(() => { 
             let st = document.querySelector(".status-text"); if(st) st.textContent = "You are in control";
             let pd = document.querySelector(".pulse-dot"); if(pd) pd.style.background = "#0B9E58";
             let th = document.querySelector(".tag-handover"); if(th) th.style.opacity = "1";
          }, "<")
          
          .to({}, {duration: 0.5}) // pause for user to read
          
          // Start typing human reply
          .to(".human-reply", { display: "flex", duration: 0.1 })
          .to(".human-reply", { opacity: 1, y: 0, duration: 0.4 })
          .add(() => {
              let text = "Hi Sarah! I can absolutely help with that. Please send the code here.";
              let el = document.getElementById("typewriter-human");
              let inputPh = document.querySelector(".input-placeholder");
              let i = 0;
              let scrollArea = document.querySelector(".chat-scroll-area");
              let interval = setInterval(() => {
                if(i < text.length) {
                  if(el) el.textContent += text.charAt(i);
                  if(inputPh) inputPh.textContent = "Reply to Sarah... " + text.substring(0, i + 1);
                  if(scrollArea) scrollArea.scrollTop = scrollArea.scrollHeight;
                  i++;
                } else {
                  clearInterval(interval);
                  let c = document.querySelector(".cursor-human"); if(c) c.style.display = "none";
                  if(inputPh) inputPh.textContent = "Reply to Sarah...";
                }
              }, 30);
          })
          
          .to({}, {duration: 3.5}) // Wait for typing to finish and let user read
          
          // 3. Switch to Instagram Chat
          .to("#sidebar-wa", { background: "transparent", borderColor: "transparent", opacity: 0.6, boxShadow: "none", duration: 0.3 })
          .to("#sidebar-ig", { background: "#fff", borderColor: "var(--accent)", opacity: 1, boxShadow: "0 4px 12px rgba(0,0,0,0.05)", duration: 0.3 }, "<")
          .to("#chat-wa", { opacity: 0, zIndex: 1, duration: 0.3 })
          .to("#chat-ig", { opacity: 1, zIndex: 3, duration: 0.3 }, "<")
          
          .to({}, {duration: 3.0}) // Let user read Instagram chat
          
          // 4. Switch to Website Chat
          .to("#sidebar-ig", { background: "transparent", borderColor: "transparent", opacity: 0.6, boxShadow: "none", duration: 0.3 })
          .to("#sidebar-web", { background: "#fff", borderColor: "var(--accent)", opacity: 1, boxShadow: "0 4px 12px rgba(0,0,0,0.05)", duration: 0.3 }, "<")
          .to("#chat-ig", { opacity: 0, zIndex: 1, duration: 0.3 })
          .to("#chat-web", { opacity: 1, zIndex: 3, duration: 0.3 }, "<");
      }
    });
</script>
</body>
</html>
"""

decks = [
    r"C:\Users\user\Downloads\StepsAI-Copy-Deck.md",
    r"C:\Users\user\Downloads\StepsAI-Copy-Deck-v2.md",
    r"C:\Users\user\Downloads\StepsAI-Copy-Deck-v3.md",
    r"C:\Users\user\Downloads\StepsAI-Copy-Deck-v4-FINAL.md"
]

all_content = ""
for d in decks:
    if os.path.exists(d):
        with open(d, 'r', encoding='utf-8') as f:
            all_content += f.read() + "\n\n"

all_content = re.sub(r'SECTION \d+\s*(?:—|-)\s*', '', all_content, flags=re.IGNORECASE)
pages = re.split(r'\n# PAGE \d+\s*(?:—|-)\s*', all_content)
pages = pages[1:] 

def parse_page(page_text):
    lines = page_text.strip().split('\n')
    header_line = lines[0]
    match = re.search(r'\(`?(/[^`\)]*)`?\)', header_line)
    if not match: return None
    route = match.group(1).strip('/')
    title = header_line.split('(')[0].strip()
    h1 = ""
    sub = []
    kicker = ""
    in_hero = False
    blocks = []
    current_block = {"title": "", "content": []}
    for line in lines[1:]:
        line = line.strip()
        if line.startswith('## Hero'):
            in_hero = True
            continue
        if line.startswith('## '):
            in_hero = False
            if current_block["title"] or current_block["content"]:
                blocks.append(current_block)
            current_block = {"title": line.replace('##', '').strip(), "content": []}
            continue
        if in_hero:
            if line.startswith('> #'): h1 = line.replace('> #', '').strip()
            elif line.startswith('> **'): kicker = line.replace('> **', '').replace('**', '').strip()
            elif line.startswith('>') and not '›' in line and not line.startswith('> `'): sub.append(line.replace('>', '').strip())
        else:
            if line:
                current_block["content"].append(line)
    if current_block["title"] or current_block["content"]:
        blocks.append(current_block)
    return {"route": route, "title": title, "h1": h1, "sub": " ".join(sub), "kicker": kicker, "blocks": blocks}

def get_nav(root_prefix):
    mega_css = """<style>.nav-dropdown-wrapper:hover .mega-menu { opacity: 1 !important; visibility: visible !important; transform: translateX(-50%) translateY(0) !important; }.sol-menu:hover .mega-menu { transform: translateX(0) translateY(0) !important; }.res-menu:hover .mega-menu { transform: translateX(0) translateY(0) !important; }</style>"""
    return mega_css + f"""
  <nav class="nav" id="mainNav">
    <div class="nav-container">
      <a href="{root_prefix}index.html" class="nav-logo-area">
        <div class="nav-logo-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="white"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg></div>
        <div class="nav-logo-text">StepsAI</div>
      </a>
      <div class="nav-tabs">
        <div class="nav-dropdown-wrapper">
          <a class="nav-tab">Product <span style="font-size: 10px; margin-left: 4px;">▼</span></a>
          <div class="mega-menu">
            <div class="mega-grid">
              <div class="mega-col"><div class="mega-col-title">PRODUCTS</div><a href="{root_prefix}product/ai-agents/index.html">AI Agents</a><a href="{root_prefix}product/copilot/index.html">Internal Copilot</a></div>
              <div class="mega-col"><div class="mega-col-title">WHAT IT DOES</div><a href="{root_prefix}features/sales-agent/index.html">Sales Agent</a><a href="{root_prefix}features/lead-agent/index.html">Lead Agent</a><a href="{root_prefix}features/meetings-agent/index.html">Meetings Agent</a><a href="{root_prefix}features/support-agent/index.html">Support Agent</a></div>
              <div class="mega-col"><div class="mega-col-title">PLATFORM</div><a href="{root_prefix}features/workflows/index.html">Workflows</a><a href="{root_prefix}features/inbox/index.html">One Inbox</a><a href="{root_prefix}features/analytics/index.html">Analytics</a><a href="{root_prefix}integrations/index.html">Integrations</a></div>
              <div class="mega-col"><div class="mega-col-title">CHANNELS</div><a href="{root_prefix}channels/website/index.html">Website</a><a href="{root_prefix}channels/whatsapp/index.html">WhatsApp</a><a href="{root_prefix}channels/instagram/index.html">Instagram</a><a href="{root_prefix}channels/standalone-page/index.html">Standalone Page</a></div>
            </div>
          </div>
        </div>
        <div class="nav-dropdown-wrapper sol-menu">
          <a class="nav-tab">Solutions <span style="font-size: 10px; margin-left: 4px;">▼</span></a>
          <div class="mega-menu" style="min-width: 400px; left: 0; transform: translateX(0) translateY(10px);">
            <div class="mega-grid" style="grid-template-columns: 1fr 1fr;">
              <div class="mega-col"><div class="mega-col-title">BY INDUSTRY</div><a href="{root_prefix}solutions/ecommerce/index.html">E-Commerce <span class="mega-badge">Flagship</span></a><a href="{root_prefix}solutions/saas/index.html">SaaS</a><a href="{root_prefix}solutions/healthcare/index.html">Healthcare</a><a href="{root_prefix}solutions/education/index.html">Education</a><a href="{root_prefix}solutions/real-estate/index.html">Real Estate</a></div>
              <div class="mega-col"><div class="mega-col-title">BY ROLE</div><a href="{root_prefix}use-cases/marketing-growth/index.html">Marketing & Growth</a><a href="{root_prefix}use-cases/sales/index.html">Sales</a><a href="{root_prefix}use-cases/support-cx/index.html">Support & CX</a><a href="{root_prefix}use-cases/operations/index.html">Operations</a></div>
            </div>
          </div>
        </div>
        <a href="{root_prefix}pricing/index.html" class="nav-tab">Pricing</a>
        <a href="{root_prefix}partners/index.html" class="nav-tab">Partner</a>
        <div class="nav-dropdown-wrapper res-menu">
          <a class="nav-tab">Resources <span style="font-size: 10px; margin-left: 4px;">▼</span></a>
          <div class="mega-menu" style="min-width: 300px; left: auto; right: 0; transform: translateX(0) translateY(10px);">
            <div class="mega-grid" style="grid-template-columns: 1fr 1fr;">
              <div class="mega-col"><div class="mega-col-title">LEARN</div><a href="{root_prefix}blog/index.html">Blog</a><a href="{root_prefix}resources/ai-guides/index.html">AI Guides</a><a href="{root_prefix}resources/case-studies/index.html">Case Studies</a></div>
              <div class="mega-col"><div class="mega-col-title">COMPANY</div><a href="{root_prefix}about/index.html">About</a><a href="{root_prefix}team/index.html">Team • Careers</a><a href="{root_prefix}note/index.html">Note • Contact</a></div>
            </div>
          </div>
        </div>
      </div>
      <div class="nav-right">
        <a href="{root_prefix}partners/apply/index.html"><button class="btn-primary">Start free trial</button></a>
      </div>
    </div>
  </nav>
"""

def parse_markdown_line(line):
    line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line)
    line = re.sub(r'!\[([^\]]*)\]\(([^\)]+)\)', r'<img src="\2" alt="\1" style="width: 100%; border-radius: 12px; margin: 16px 0; border: 1px solid var(--border-subtle); display: block;" />', line)
    return line

def get_micro_mockup(title):
    if "WhatsApp" in title or "Sales Agent" in title:
        return '<div class="micro-mockup"><div class="chat-bubble in">Hi, do you have this in large?</div><div class="chat-bubble out">Yes, two left! Added to cart.</div><div class="receipt-pill" style="opacity:1; transform:scale(1); margin:4px 0 0;"><span class="check">✓</span> <span>SHOPIFY</span></div></div>'
    elif "Instagram" in title or "Meetings Agent" in title:
        return '<div class="micro-mockup micro instagram"><div class="chat-bubble in ig-in">I want to book a visit.</div><div class="chat-bubble out ig-out">Saturday 11 AM works perfectly!</div><div class="receipt-pill" style="opacity:1; transform:scale(1); margin:4px 0 0;"><span class="check">✓</span> <span>CALENDAR</span></div></div>'
    elif "Website" in title or "Lead Agent" in title:
        return '<div class="micro-mockup micro website"><div class="chat-bubble in ig-in">What is the pricing?</div><div class="chat-bubble out ig-in">Plans start at $49. Whats your email?</div><div class="receipt-pill" style="opacity:1; transform:scale(1); margin:4px 0 0;"><span class="check">✓</span> <span>HUBSPOT</span></div></div>'
    elif "Support" in title:
        return '<div class="micro-mockup micro website"><div class="chat-bubble in ig-in">Where is my order?</div><div class="chat-bubble out ig-in">It is out for delivery today at 6PM!</div><div class="receipt-pill" style="opacity:1; transform:scale(1); margin:4px 0 0;"><span class="check">✓</span> <span>ZENDESK</span></div></div>'
    return ""

for p in pages:
    data = parse_page(p)
    if not data: continue
    
    # FOR THIS RUN: We only want to rebuild the Home Page to fix the Four Agents bug.
    if data["route"] != "":
        continue
        
    html_content = ""
    if data["route"] == "" and data["h1"]:
        html_content += CUSTOM_HOME_HERO
    elif data["h1"]:
        html_content += render_s05(data["kicker"], data["h1"], data["sub"])
    
    for block in data["blocks"]:
        if not block["title"] or "Hero" in block["title"]: continue
        
        if data["route"] == "" and "Industries" in block["title"]:
            html_content += CUSTOM_HOME_ACCORDION
            continue
            
        if data["route"] == "" and "Four Agents" in block["title"]:
            html_content += CUSTOM_FOUR_AGENTS
            continue
            
        if data["route"] == "" and "Channels" in block["title"]:
            html_content += CUSTOM_CHANNELS
            continue
            
        if data["route"] == "" and "Setup" in block["title"]:
            html_content += CUSTOM_SETUP
            continue
            
        if data["route"] == "" and "One Inbox" in block["title"]:
            html_content += CUSTOM_ONE_INBOX
            continue

        if data["route"] == "" and "Analytics" in block["title"]:
            html_content += CUSTOM_ANALYTICS
            continue

        if data["route"] == "" and "Internal Copilot" in block["title"]:
            html_content += CUSTOM_COPILOT
            continue

        if data["route"] == "" and "Who this is for" in block["title"]:
            html_content += CUSTOM_FIT
            continue

        if data["route"] == "" and "Closing CTA" in block["title"]:
            html_content += CUSTOM_CTA
            continue





            
        is_faq = "FAQ" in block["title"].upper()
        
        html_content += f'''
        <section class="section-v2" style="background: var(--bg-surface-2);">
            <h2 class="section-title-v2 gsap-fade-up">{block["title"]}</h2>
        '''
        
        if is_faq:
            # First, parse all Q&A pairs
            qa_pairs = []
            q = ""
            a = []
            for c in block["content"]:
                c_clean = c.replace('>', '').strip()
                if c_clean.startswith('**') and '?' in c_clean:
                    if q:
                        qa_pairs.append({"q": q, "a": ' '.join(a)})
                    q = c_clean.replace('**', '').strip()
                    a = []
                elif c_clean:
                    a.append(parse_markdown_line(c_clean))
            if q:
                qa_pairs.append({"q": q, "a": ' '.join(a)})
            
            # Now build the two-column HTML
            html_content += '<div class="faq-container gsap-fade-up" style="max-width: 1200px; margin: 0 auto; display: flex; gap: 64px; align-items: flex-start; position: relative;">'
            
            # Left column: Questions List
            html_content += '<div style="flex: 1; display: flex; flex-direction: column; gap: 8px;">'
            for idx, pair in enumerate(qa_pairs):
                # We use inline event handlers for a quick hover effect without relying on complex GSAP timelines here
                hover_script = f"document.querySelectorAll('.faq-answer').forEach(el => el.style.opacity = '0'); document.getElementById('faq-ans-{idx}').style.opacity = '1'; document.querySelectorAll('.faq-q-item').forEach(el => el.style.color = 'var(--text-secondary)'); this.style.color = 'var(--accent)';"
                
                initial_color = "var(--accent)" if idx == 0 else "var(--text-secondary)"
                html_content += f'''
                <div class="faq-q-item" onmouseover="{hover_script}" style="font-family: 'Outfit'; font-size: 24px; font-weight: 500; color: {initial_color}; padding: 24px 32px; cursor: pointer; transition: 0.3s; border-radius: 16px; border: 1px solid transparent;" onmouseenter="this.style.background='#fff'; this.style.borderColor='var(--border-subtle)'" onmouseleave="this.style.background='transparent'; this.style.borderColor='transparent'">
                    {pair["q"]}
                </div>
                '''
            html_content += '</div>'
            
            # Right column: Sticky Answer Area
            html_content += '<div style="flex: 1; position: sticky; top: 120px; background: #fff; padding: 48px; border-radius: 24px; border: 1px solid var(--border-subtle); box-shadow: 0 24px 60px rgba(0,0,0,0.04); min-height: 300px; display: flex; align-items: center; justify-content: center;">'
            html_content += '<div style="position: relative; width: 100%; height: 100%;">'
            for idx, pair in enumerate(qa_pairs):
                opacity = "1" if idx == 0 else "0"
                html_content += f'''
                <div id="faq-ans-{idx}" class="faq-answer" style="position: absolute; inset: 0; opacity: {opacity}; transition: opacity 0.4s ease; display: flex; flex-direction: column; justify-content: center;">
                    <div style="font-size: 14px; font-weight: 700; color: var(--accent); letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 16px;">ANSWER</div>
                    <p style="color: var(--text-primary); font-size: 20px; line-height: 1.6; margin: 0;">{pair["a"]}</p>
                </div>
                '''
            html_content += '</div></div>'
            html_content += '</div></section>'
            
        else:
            html_content += '<div class="bento-grid">'
            card_title = ""
            card_desc = []
            
            for c in block["content"]:
                c_clean = c.replace('>', '').strip()
                if not c_clean or c_clean.startswith('→') or c_clean.startswith('`['): continue
                
                if c_clean.startswith('### '):
                    if card_title or card_desc:
                        mockup_html = get_micro_mockup(card_title)
                        html_content += f'''
                        <div class="bento-card gsap-scale-in">
                            <h3 class="bento-title" style="font-size: 24px; margin-bottom: 16px;">{card_title}</h3>
                            <p class="bento-desc" style="font-size:16px;">{' '.join(card_desc)}</p>
                            {mockup_html}
                        </div>'''
                    card_title = c_clean.replace('### ', '')
                    card_desc = []
                else:
                    card_desc.append(parse_markdown_line(c_clean))
                    
            if card_title or card_desc:
                mockup_html = get_micro_mockup(card_title)
                html_content += f'''
                <div class="bento-card gsap-scale-in">
                    <h3 class="bento-title" style="font-size: 24px; margin-bottom: 16px;">{card_title}</h3>
                    <p class="bento-desc" style="font-size:16px;">{' '.join(card_desc)}</p>
                    {mockup_html}
                </div>'''
                
            html_content += '</div></section>'
    
    depth = len(data["route"].split('/')) if data["route"] else 0
    root_prefix = "../" * depth if depth > 0 else "./"
    
    head = GLOBAL_HEAD.replace("{title}", data["title"]).replace("{root_prefix}", root_prefix)
    footer = FOOTER.replace("{root_prefix}", root_prefix)
    
    full_html = head + get_nav(root_prefix) + html_content + footer
    
    if data["route"] == "":
        dir_path = ""
    else:
        dir_path = os.path.join(data["route"])
        os.makedirs(dir_path, exist_ok=True)
        
    with open(os.path.join(dir_path, "index.html"), "w", encoding="utf-8") as f:
        f.write(full_html)
    
print(f"V11 Compiler finished. Generated Four Agents layout on Home Page.")
