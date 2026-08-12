# -*- coding: utf-8 -*-
import os
import re

CUSTOM_CHANNELS = """
    <section class="section-v2 channels-section" style="padding-top: 120px; padding-bottom: 120px; position: relative; overflow: hidden; background: #fff;">
      
      <div style="text-align: center; margin-bottom: 80px; position: relative; z-index: 1;">
        <span class="gsap-fade-up" style="font-family: 'Geist Mono', monospace; font-size: 12px; color: var(--accent); letter-spacing: .2em; text-transform: uppercase;">EVERY CHANNEL</span>
        <h2 class="gsap-fade-up" style="font-family: 'Outfit'; font-size: clamp(40px, 4vw, 56px); margin: 16px auto 24px; color: var(--text-primary); max-width: 900px; line-height: 1.1;">On Instagram it replies in public, then finishes the sale in private.</h2>
        <p class="gsap-fade-up" style="font-size: 20px; color: var(--text-secondary); max-width: 700px; margin: 0 auto; line-height: 1.6;">A comment under a post and a WhatsApp message at midnight are not the same kind of conversation. Your agent treats them differently, because your customers do.</p>
      </div>
  
      <div class="bento-grid gsap-fade-up" style="grid-template-columns: repeat(3, 1fr); gap: 32px; max-width: 1300px; margin: 0 auto; position: relative; z-index: 1;">
        
        <!-- Instagram Card -->
        <div class="bento-card" style="padding: 40px; background: linear-gradient(145deg, rgba(255, 235, 245, 0.9) 0%, rgba(255, 255, 255, 0.8) 100%); backdrop-filter: blur(20px); border: 1px solid var(--border-subtle); display: flex; flex-direction: column; justify-content: space-between; min-height: 520px; border-radius: 32px; box-shadow: 0 24px 64px rgba(0,0,0,0.03);">
          <div>
            <div style="font-family: 'Inter'; font-size: 14px; font-weight: 700; background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 12px; display: inline-block;">INSTAGRAM</div>
            <h3 style="font-family: 'Outfit'; font-size: 28px; margin-bottom: 16px; color: var(--text-primary); line-height: 1.2;">The comment nobody had time to answer.</h3>
            <p style="color: var(--text-secondary); font-size: 16px; line-height: 1.6;">Someone asks the price under your post. Your agent replies where everyone can see it, slides into the DM, and finishes the conversation there.</p>
          </div>
          <div class="micro-mockup ig-mockup" style="background: #fafafa; border-radius: 16px; padding: 20px; margin-top: 32px; border: 1px solid rgba(0,0,0,0.05); position: relative; overflow: hidden; display: flex; flex-direction: column; gap: 12px;">
            <div class="ig-comment" style="display: flex; gap: 12px; opacity: 0; transform: translateY(10px);">
                <div style="width: 24px; height: 24px; border-radius: 50%; background: #ddd; flex-shrink: 0;"></div>
                <div>
                    <div style="font-size: 12px; font-weight: 600; color: #111;">user123</div>
                    <div style="font-size: 13px; color: #444; margin-top: 2px;">How much is this?</div>
                </div>
            </div>
            <div class="ig-reply" style="display: flex; gap: 12px; padding-left: 36px; opacity: 0; transform: translateY(10px);">
                <div style="width: 24px; height: 24px; border-radius: 50%; background: linear-gradient(45deg, #1A56DB, #0B9E58); flex-shrink: 0;"></div>
                <div>
                    <div style="font-size: 12px; font-weight: 600; color: #111;">yourbrand <span style="color:#0B9E58;">&#10003;</span></div>
                    <div style="font-size: 13px; color: #444; margin-top: 2px;">Hey! Just sent you a DM with the details and a link to buy 😊</div>
                </div>
            </div>
            <div class="ig-dm" style="background: #fff; border: 1px solid #eee; border-radius: 16px; padding: 12px; margin-top: 8px; opacity: 0; transform: translateY(10px); box-shadow: 0 8px 24px rgba(0,0,0,0.05);">
                <div style="font-size: 11px; color: #888; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px; text-align: center;">Direct Message</div>
                <div style="background: #efefef; color: #111; padding: 10px 12px; border-radius: 16px; border-bottom-left-radius: 4px; font-size: 13px; display: inline-block;">It is $49. Would you like the link?</div>
            </div>
          </div>
        </div>
  
        <!-- WhatsApp Card -->
        <div class="bento-card" style="padding: 40px; background: linear-gradient(145deg, rgba(235, 255, 240, 0.9) 0%, rgba(255, 255, 255, 0.8) 100%); backdrop-filter: blur(20px); border: 1px solid var(--border-subtle); display: flex; flex-direction: column; justify-content: space-between; min-height: 520px; border-radius: 32px; box-shadow: 0 24px 64px rgba(0,0,0,0.03);">
          <div>
            <div style="font-family: 'Inter'; font-size: 14px; font-weight: 700; color: #25D366; margin-bottom: 12px;">WHATSAPP</div>
            <h3 style="font-family: 'Outfit'; font-size: 28px; margin-bottom: 16px; color: var(--text-primary); line-height: 1.2;">Where your customers already spend their evening.</h3>
            <p style="color: var(--text-secondary); font-size: 16px; line-height: 1.6;">Booking links, payment links, delivery updates, all inside the app they already have open.</p>
          </div>
          <div class="micro-mockup wa-mockup" style="background: #E5DDD5; border-radius: 16px; padding: 16px; margin-top: 32px; border: 1px solid rgba(0,0,0,0.05); position: relative; overflow: hidden; display: flex; flex-direction: column; gap: 8px;">
            <div style="text-align: center; font-size: 11px; color: #555; background: rgba(255,255,255,0.6); padding: 4px 8px; border-radius: 8px; margin: 0 auto 8px; width: max-content;">Today</div>
            <div class="wa-msg-1" style="background: #fff; color: #111; padding: 10px 14px; border-radius: 12px; border-top-left-radius: 0; align-self: flex-start; max-width: 85%; font-size: 13px; opacity: 0; transform: translateY(10px); box-shadow: 0 1px 1px rgba(0,0,0,0.05);">When will my order arrive?</div>
            <div class="wa-msg-2" style="background: #DCF8C6; color: #111; padding: 10px 14px; border-radius: 12px; border-top-right-radius: 0; align-self: flex-end; max-width: 85%; font-size: 13px; opacity: 0; transform: translateY(10px); box-shadow: 0 1px 1px rgba(0,0,0,0.05);">It's out for delivery! Track it here: <br><a href="#" style="color: #0367D3; text-decoration: none;">track.link/892</a></div>
          </div>
        </div>
        
        <!-- Website Card -->
        <div class="bento-card" style="padding: 40px; background: linear-gradient(145deg, rgba(235, 245, 255, 0.9) 0%, rgba(255, 255, 255, 0.8) 100%); backdrop-filter: blur(20px); border: 1px solid var(--border-subtle); display: flex; flex-direction: column; justify-content: space-between; min-height: 520px; border-radius: 32px; box-shadow: 0 24px 64px rgba(0,0,0,0.03);">
          <div>
            <div style="font-family: 'Inter'; font-size: 14px; font-weight: 700; color: #0367D3; margin-bottom: 12px;">WEBSITE</div>
            <h3 style="font-family: 'Outfit'; font-size: 28px; margin-bottom: 16px; color: var(--text-primary); line-height: 1.2;">It knows which page they are standing on.</h3>
            <p style="color: var(--text-secondary); font-size: 16px; line-height: 1.6;">Someone asks "does this come in blue" while looking at a specific jacket. Your agent knows which jacket.</p>
          </div>
          <div class="micro-mockup web-mockup" style="background: #fafafa; border-radius: 16px; padding: 0; margin-top: 32px; border: 1px solid rgba(0,0,0,0.05); position: relative; overflow: hidden; height: 180px;">
             <!-- Fake Website BG -->
             <div style="padding: 20px;">
                <div style="width: 60%; height: 80px; background: #eee; border-radius: 8px; margin-bottom: 12px;"></div>
                <div style="width: 80%; height: 12px; background: #eee; border-radius: 4px; margin-bottom: 8px;"></div>
                <div style="width: 40%; height: 12px; background: #eee; border-radius: 4px;"></div>
             </div>
             <!-- Chat Widget -->
             <div class="web-widget" style="position: absolute; bottom: 16px; right: 16px; background: #fff; width: 200px; border-radius: 16px; border-bottom-right-radius: 4px; box-shadow: 0 12px 32px rgba(0,0,0,0.1); border: 1px solid #eaeaea; opacity: 0; transform: translateY(20px) scale(0.9); transform-origin: bottom right;">
                <div style="background: #111; color: #fff; padding: 12px; border-top-left-radius: 16px; border-top-right-radius: 16px; font-size: 12px; font-weight: 600;">Chat with us</div>
                <div style="padding: 12px; font-size: 12px;">
                   <div style="background: #f4f5f7; padding: 8px 12px; border-radius: 12px; border-bottom-left-radius: 4px; display: inline-block; margin-bottom: 8px;">Does this come in blue?</div>
                   <div style="background: #0B9E58; color: #fff; padding: 8px 12px; border-radius: 12px; border-bottom-right-radius: 4px; display: inline-block; align-self: flex-end; float: right;">Yes, the Denim Jacket comes in Navy Blue!</div>
                </div>
             </div>
          </div>
        </div>

      </div>
    </section>
"""

CUSTOM_WORKFLOWS = """
    <style>
      .wf-row { background: var(--bg-surface); padding: 32px; border-radius: 24px; border: 1px solid var(--border-subtle); margin-bottom: 24px; box-shadow: 0 4px 24px rgba(0,0,0,0.02); }
      .wf-title { font-family: 'Outfit'; font-size: 24px; font-weight: 700; color: var(--text-primary); margin-bottom: 24px; display: flex; align-items: center; justify-content: space-between; }
      .wf-path { display: flex; align-items: center; justify-content: space-between; position: relative; padding: 20px 0; }
      .wf-line { position: absolute; top: 50%; left: 0; right: 0; height: 2px; background: #eee; z-index: 0; transform: translateY(-50%); }
      .wf-line-active { position: absolute; top: 50%; left: 0; width: 0; height: 2px; background: #0B9E58; z-index: 1; transform: translateY(-50%); }
      .wf-node { position: relative; z-index: 2; background: #fff; border: 2px solid #eee; padding: 8px 16px; border-radius: 100px; font-size: 13px; font-weight: 600; color: #555; transition: 0.3s; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
      .wf-node.active { border-color: #0B9E58; color: #0B9E58; background: #f0fdf4; box-shadow: 0 0 16px rgba(11,158,88,0.2); }
      .wf-pulse { position: absolute; top: 50%; left: 0; width: 8px; height: 8px; background: #0B9E58; border-radius: 50%; z-index: 3; transform: translate(-50%, -50%); opacity: 0; box-shadow: 0 0 12px #0B9E58; }
      @media (max-width: 900px) {
        .wf-path { flex-direction: column; align-items: flex-start; gap: 24px; padding: 0; }
        .wf-line, .wf-line-active, .wf-pulse { display: none; }
        .wf-node { width: 100%; border-radius: 12px; }
      }
    </style>
    <section class="section-v2 workflows-section" style="padding-top: 120px; padding-bottom: 120px; background: #fafafa;">
      
      <div style="text-align: center; margin-bottom: 80px; position: relative; z-index: 1;">
        <span class="gsap-fade-up" style="font-family: 'Geist Mono', monospace; font-size: 12px; color: var(--accent); letter-spacing: .2em; text-transform: uppercase;">AUTOMATED WORKFLOWS</span>
        <h2 class="gsap-fade-up" style="font-family: 'Outfit'; font-size: clamp(40px, 4vw, 56px); margin: 16px auto 24px; color: var(--text-primary); max-width: 900px; line-height: 1.1;">Most sales do not die from a no. They die from silence.</h2>
        <p class="gsap-fade-up" style="font-size: 20px; color: var(--text-secondary); max-width: 700px; margin: 0 auto; line-height: 1.6;">Somebody fills a cart and then their food arrives. A lead asks one question and disappears for a week. Your agent notices the gap, waits the right amount of time, and starts the conversation up again.</p>
      </div>
  
      <div class="gsap-fade-up" style="max-width: 1000px; margin: 0 auto; position: relative; z-index: 1;">
        
        <!-- Workflow 1 -->
        <div class="wf-row">
            <div class="wf-title">Recover Carts <span style="font-size: 14px; background: #eee; padding: 4px 12px; border-radius: 100px; font-weight: 500; color: #666;">Default</span></div>
            <div class="wf-path wf-path-1">
                <div class="wf-line"></div>
                <div class="wf-line-active wf-line-active-1"></div>
                <div class="wf-pulse wf-pulse-1"></div>
                
                <div class="wf-node wf-n1-1">Cart left behind</div>
                <div class="wf-node wf-n1-2">Wait 30 minutes</div>
                <div class="wf-node wf-n1-3">Send WhatsApp message</div>
                <div class="wf-node wf-n1-4">Share checkout link</div>
                <div class="wf-node wf-n1-5" style="background: #111; color: #fff; border-color: #111;">Checkout Reopened</div>
            </div>
        </div>

        <!-- Workflow 2 -->
        <div class="wf-row">
            <div class="wf-title">Follow up leads</div>
            <div class="wf-path wf-path-2">
                <div class="wf-line"></div>
                <div class="wf-line-active wf-line-active-2"></div>
                <div class="wf-pulse wf-pulse-2"></div>
                
                <div class="wf-node wf-n2-1">New lead captured</div>
                <div class="wf-node wf-n2-2">Save to CRM</div>
                <div class="wf-node wf-n2-3">Send a short follow-up</div>
                <div class="wf-node wf-n2-4">Offer free times</div>
                <div class="wf-node wf-n2-5" style="background: #111; color: #fff; border-color: #111;">Follow-up Sent</div>
            </div>
        </div>

        <!-- Workflow 3 -->
        <div class="wf-row">
            <div class="wf-title">Remind customers</div>
            <div class="wf-path wf-path-3">
                <div class="wf-line"></div>
                <div class="wf-line-active wf-line-active-3"></div>
                <div class="wf-pulse wf-pulse-3"></div>
                
                <div class="wf-node wf-n3-1">Meeting booked</div>
                <div class="wf-node wf-n3-2">Wait until day before</div>
                <div class="wf-node wf-n3-3">Send the reminder</div>
                <div class="wf-node wf-n3-4">Let them confirm</div>
                <div class="wf-node wf-n3-5" style="background: #111; color: #fff; border-color: #111;">Reminder Sent</div>
            </div>
        </div>

        <!-- Workflow 4 -->
        <div class="wf-row">
            <div class="wf-title">Re-engage</div>
            <div class="wf-path wf-path-4">
                <div class="wf-line"></div>
                <div class="wf-line-active wf-line-active-4"></div>
                <div class="wf-pulse wf-pulse-4"></div>
                
                <div class="wf-node wf-n4-1">Quiet for 30 days</div>
                <div class="wf-node wf-n4-2">Work out which group</div>
                <div class="wf-node wf-n4-3">Send relevant message</div>
                <div class="wf-node wf-n4-4">Handle the replies</div>
                <div class="wf-node wf-n4-5" style="background: #111; color: #fff; border-color: #111;">Campaign Live</div>
            </div>
        </div>

      </div>
    </section>
"""

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
    .gsap-fade-up {{ opacity: 0; transform: translateY(40px); }}
    .gsap-scale-in {{ opacity: 0; transform: scale(0.9); }}
    
    .hero-v2 {{ min-height: 80vh; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 160px 32px 80px; position: relative; overflow: hidden; }}
    .hero-v2.split-hero {{ flex-direction: row; text-align: left; max-width: 1300px; margin: 0 auto; gap: 64px; }}
    @media (max-width: 1000px) {{ .hero-v2.split-hero {{ flex-direction: column; text-align: center; }} }}
    
    .hero-bg-glow {{ position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 80vw; height: 80vw; background: radial-gradient(circle, var(--accent-tint) 0%, rgba(251,252,254,0) 70%); z-index: -1; }}
    .hero-v2 h1 {{ font-size: clamp(48px, 6vw, 80px); line-height: 1.05; letter-spacing: -2px; font-family: 'Outfit', sans-serif; }}
    .hero-v2 p {{ font-size: 20px; color: var(--text-secondary); max-width: 720px; line-height: 1.6; }}
    
    .section-v2 {{ padding: 112px 32px; max-width: 1400px; margin: 0 auto; }}
    .section-title-v2 {{ font-size: clamp(36px, 4vw, 54px); letter-spacing: -1px; margin-bottom: 80px; font-family: 'Outfit', sans-serif; text-align: center;}}
    
    .bento-grid {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px; grid-auto-flow: dense; }}
    .bento-card {{ background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 24px; padding: 48px; position: relative; overflow: hidden; display: flex; flex-direction: column; transition: transform 0.5s cubic-bezier(.16,1,.3,1), border-color 0.5s, box-shadow 0.5s; box-shadow: var(--shadow); }}
    .bento-card:hover {{ transform: translateY(-8px); border-color: var(--accent); box-shadow: var(--shadow-lg); }}
    .bento-title {{ font-size: 32px; font-weight: 700; margin-bottom: 16px; font-family: 'Outfit', sans-serif; color: var(--text-primary);}}
    .bento-desc {{ color: var(--text-secondary); font-size: 16px; line-height: 1.6; }}
    @media (max-width: 992px) {{ .bento-grid {{ grid-template-columns: 1fr; }} }}
    
    .industries-accordion {{ max-width: 1200px; margin: 0 auto; display: flex; gap: 16px; height: 500px; }}
    .accordion-panel {{ position: relative; flex: 1; border-radius: 24px; overflow: hidden; background-size: cover; background-position: center; transition: flex 0.6s cubic-bezier(0.16, 1, 0.3, 1); cursor: pointer; }}
    .accordion-panel::after {{ content: ''; position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0) 100%); transition: opacity 0.4s; }}
    .accordion-panel:hover {{ flex: 3; }}
    .accordion-content {{ position: absolute; bottom: 0; left: 0; width: 100%; padding: 32px; color: white; z-index: 2; display: flex; flex-direction: column; justify-content: flex-end; }}
    .accordion-title {{ font-family: 'Outfit', sans-serif; font-size: 28px; font-weight: 700; margin: 0; white-space: nowrap; }}
    .accordion-desc {{ font-size: 16px; color: rgba(255,255,255,0.8); margin-top: 12px; line-height: 1.5; opacity: 0; transform: translateY(10px); transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); }}
    .accordion-panel:hover .accordion-desc {{ opacity: 1; transform: translateY(0); transition-delay: 0.1s; }}
    
    .step-line-container {{ position: fixed; top: 0; left: 40px; width: 6px; height: 100%; z-index: 0; pointer-events: none; }}
    .step-line {{ width: 2px; height: 100%; background: var(--line); position: absolute; left: 2px; }}
    .step-line-progress {{ width: 2px; height: 0%; background: var(--accent); position: absolute; left: 2px; transition: height 0.1s linear; }}
    
    .phone-mockup {{ width: 340px; height: 640px; background: #fff; border-radius: 48px; box-shadow: 0 32px 80px rgba(0,0,0,0.15), inset 0 0 0 10px #e0e4e8, inset 0 0 0 12px #f4f5f7; position: relative; overflow: hidden; display: flex; flex-direction: column; flex-shrink:0; }}
    .phone-notch {{ position: absolute; top: 10px; left: 50%; transform: translateX(-50%); width: 120px; height: 28px; background: #e0e4e8; border-radius: 14px; z-index: 10; }}
    .mockup-screen {{ position: absolute; inset: 12px; border-radius: 36px; overflow: hidden; display: flex; flex-direction: column; background:#fff; z-index:1; opacity:0; }}
    .mockup-header {{ height: 80px; padding: 40px 16px 12px; display: flex; align-items: center; gap: 12px; font-family: 'Inter', sans-serif; }}
    .mockup-header.whatsapp {{ background: #008069; color: white; }}
    .mockup-header.instagram {{ background: #fff; color: #111; border-bottom: 1px solid #efefef; }}
    .mockup-body {{ flex: 1; padding: 16px; display: flex; flex-direction: column; gap: 12px; background: #EFEAE2; font-family: 'Inter', sans-serif; }}
    .mockup-body.instagram {{ background: #fff; }}
    .chat-bubble {{ max-width: 85%; padding: 12px 14px; border-radius: 12px; font-size: 14px; line-height: 1.4; position: relative; }}
    .chat-bubble.in {{ align-self: flex-start; background: #fff; border-top-left-radius: 4px; box-shadow: 0 1px 2px rgba(0,0,0,0.05); color:#111; }}
    .chat-bubble.out {{ align-self: flex-end; background: #D9FDD3; border-top-right-radius: 4px; box-shadow: 0 1px 2px rgba(0,0,0,0.05); color:#111; }}
    .chat-bubble.ig-in {{ background: #efefef; border-radius: 18px; color:#111; }}
    .chat-bubble.ig-out {{ background: linear-gradient(135deg, #4F5BD5, #962FBF); color: white; border-radius: 18px; }}
    .chat-time {{ font-size: 10px; color: rgba(0,0,0,0.4); float: right; margin: 8px 0 -4px 8px; }}
    .chat-time.out {{ color: rgba(0,0,0,0.5); }}
    .receipt-pill {{ display: inline-flex; align-items: center; justify-content:center; gap: 8px; background: #E9F8F0; border-radius: 8px; padding: 8px 16px; font-family: 'Geist Mono', monospace; font-size: 11px; font-weight: 500; color: #0C1322; letter-spacing: 0.12em; text-transform: uppercase; margin-top: 16px; align-self:center; opacity: 0; transform: scale(0.94); box-shadow:0 4px 12px rgba(11,158,88,0.15); }}
    .receipt-pill .check {{ color: #0B9E58; font-size: 14px; font-weight: 800; }}
    .receipt-pill span {{ color: #46536B; }}
    
    .micro-mockup {{ transition: 0.3s; transform: translateY(10px); }}
    .bento-card:hover .micro-mockup {{ transform: translateY(0); box-shadow: 0 20px 40px rgba(0,0,0,0.08) !important; }}
    
    .typing {{ display:flex; gap:4px; padding:16px 20px; align-items:center; }}
    .dot {{ width:6px; height:6px; background:rgba(0,0,0,0.3); border-radius:50%; animation: type 1.4s infinite ease-in-out both; }}
    .dot:nth-child(1) {{ animation-delay: -0.32s; }}
    .dot:nth-child(2) {{ animation-delay: -0.16s; }}
    @keyframes type {{ 0%, 80%, 100% {{ transform: scale(0); }} 40% {{ transform: scale(1); }} }}
  </style>
</head>
<body>
  <div class="step-line-container">
    <div class="step-line"></div>
    <div class="step-line-progress" id="stepLineProgress"></div>
  </div>
"""

CUSTOM_HOME_HERO = """
  <!-- S01 Landing Hero - Animated Mockup -->
  <section class="hero-v2 split-hero">
    <div class="hero-bg-glow"></div>
    <div style="flex:1;">
      <span class="kicker gsap-fade-up" style="font-family: 'Geist Mono', monospace; font-size: 11px; font-weight: 500; color: var(--accent); letter-spacing: .24em; text-transform: uppercase; margin-bottom: 24px; display:block;">AI AGENT FOR SALES & SUPPORT</span>
      <h1 class="gsap-fade-up" style="margin-bottom: 24px;">It answers.<br>Then it acts.</h1>
      <p class="gsap-fade-up" style="margin-bottom: 48px;">StepsAI answers customer questions on WhatsApp, Instagram and your website. Then it books the meeting, saves the lead, or updates the order. Nobody on your team has to be awake for it.</p>
      <div class="hero-actions gsap-fade-up" style="display:flex; gap:16px;">
        <a href="./partners/apply/index.html"><button class="btn-primary" style="padding: 16px 32px; font-size: 18px;">Start free trial</button></a>
        <button class="btn-outline" style="padding: 16px 32px; font-size: 18px;">Book a demo</button>
      </div>
      <div class="gsap-fade-up" style="margin-top:24px; font-size:14px; color:var(--text-tertiary);">Works with Shopify, HubSpot, Calendly and your inbox.</div>
    </div>
    <div class="hero-mockup-wrapper gsap-scale-in" style="flex:1; display:flex; justify-content:center; align-items:center;">
      <div class="phone-mockup">
        <div class="phone-notch"></div>
        <div class="mockup-screen" id="screen-wa" style="opacity:1; z-index:2;">
          <div class="mockup-header whatsapp">
            <div style="width:36px; height:36px; border-radius:50%; background:#fff; display:flex; align-items:center; justify-content:center; color:#008069; font-weight:800; font-size:18px;">S</div>
            <div style="line-height:1.2; font-weight:600; font-size:15px;">StepsAI<br><span style="font-size:12px; font-weight:400; opacity:0.8;">Online</span></div>
          </div>
          <div class="mockup-body">
            <div class="chat-bubble in stp-1">Do you have the linen shirt in medium? <span class="chat-time">10:42 PM</span></div>
            <div class="chat-bubble out typing stp-t1"><div class="dot"></div><div class="dot"></div><div class="dot"></div></div>
            <div class="chat-bubble out stp-2" style="display:none;">Yes, two left in medium. Want me to hold one? <span class="chat-time out">10:42 PM</span></div>
            <div class="chat-bubble in stp-3" style="opacity:0; transform:translateY(10px);">Yes please <span class="chat-time">10:43 PM</span></div>
            <div class="chat-bubble out typing stp-t2" style="display:none;"><div class="dot"></div><div class="dot"></div><div class="dot"></div></div>
            <div class="chat-bubble out stp-4" style="display:none;">Reserved and added to your cart.<br><b style="display:block; margin-top:8px; padding-top:8px; border-top:1px solid rgba(0,0,0,0.1);">Linen Shirt · Medium · ₹2,400</b> <span class="chat-time out">10:43 PM</span></div>
            <div class="receipt-pill stp-5"><span class="check">✓</span> <span>SHOPIFY</span> · CART UPDATED</div>
          </div>
        </div>
        <div class="mockup-screen" id="screen-ig" style="opacity:0; z-index:1;">
          <div class="mockup-header instagram">
            <div style="width:36px; height:36px; border-radius:50%; background:linear-gradient(135deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%); padding:2px; display:flex; align-items:center; justify-content:center;"><div style="width:100%; height:100%; background:#fff; border-radius:50%;"></div></div>
            <div style="line-height:1.2; font-weight:600; font-size:15px; color:#111;">StepsAI Real Estate<br><span style="font-size:12px; font-weight:400; color:#888;">StepsAI Real Estate</span></div>
          </div>
          <div class="mockup-body instagram">
            <div class="chat-bubble in ig-in stp-ig-1">Is the 3BHK still available? <span class="chat-time">9:15 PM</span></div>
            <div class="chat-bubble out ig-out typing stp-ig-t1"><div class="dot" style="background:rgba(255,255,255,0.5);"></div><div class="dot" style="background:rgba(255,255,255,0.5);"></div><div class="dot" style="background:rgba(255,255,255,0.5);"></div></div>
            <div class="chat-bubble out ig-out stp-ig-2" style="display:none;">It is. Want to see it this weekend? <span class="chat-time out" style="color:rgba(255,255,255,0.7);">9:15 PM</span></div>
            <div class="chat-bubble in ig-in stp-ig-3" style="opacity:0; transform:translateY(10px);">Saturday works <span class="chat-time">9:16 PM</span></div>
            <div class="chat-bubble out ig-out typing stp-ig-t2" style="display:none;"><div class="dot" style="background:rgba(255,255,255,0.5);"></div><div class="dot" style="background:rgba(255,255,255,0.5);"></div><div class="dot" style="background:rgba(255,255,255,0.5);"></div></div>
            <div class="chat-bubble out ig-out stp-ig-4" style="display:none;">Booked for Saturday 11 AM. Sending the address.<br><div style="display:flex; gap:8px; margin-top:8px;"><span style="background:rgba(255,255,255,0.2); padding:4px 8px; border-radius:8px; font-size:12px;">Sat 11:00</span><span style="background:rgba(255,255,255,0.2); padding:4px 8px; border-radius:8px; font-size:12px;">Sat 4:00</span></div><span class="chat-time out" style="color:rgba(255,255,255,0.7);">9:16 PM</span></div>
            <div class="receipt-pill stp-ig-5"><span class="check">✓</span> <span>CALENDAR</span> · VISIT BOOKED</div>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

CUSTOM_FOUR_AGENTS = """
    <section class="section-v2 four-agents-section" style="padding-top: 160px; padding-bottom: 120px; position: relative; overflow: hidden;">
      <!-- Animated Background Mesh (Inspired by Logo Colors: Red #D04859 and Blue #5B6DB0) -->
      <div class="mesh-bg" style="position: absolute; top: -50%; left: -50%; width: 200%; height: 200%; z-index: 0; background: radial-gradient(circle at 50% 50%, rgba(208, 72, 89, 0.06) 0%, transparent 40%), radial-gradient(circle at 80% 20%, rgba(91, 109, 176, 0.06) 0%, transparent 40%), radial-gradient(circle at 20% 80%, rgba(208, 72, 89, 0.04) 0%, transparent 40%); filter: blur(60px); pointer-events: none; opacity:0;"></div>
      
      <div style="text-align: center; margin-bottom: 80px; position: relative; z-index: 1;">
        <span class="gsap-fade-up" style="font-family: 'Geist Mono', monospace; font-size: 12px; color: var(--accent); letter-spacing: .2em; text-transform: uppercase;">FOUR AGENTS, ONE BRAIN</span>
        <h2 class="gsap-fade-up" style="font-family: 'Outfit'; font-size: clamp(40px, 5vw, 56px); margin: 16px 0 24px; color: var(--text-primary);">Four jobs. One memory.</h2>
        <p class="gsap-fade-up" style="font-size: 20px; color: var(--text-secondary); max-width: 700px; margin: 0 auto; line-height: 1.6;">Your support agent knows what your sales agent promised yesterday. That sounds obvious until you have used four separate tools that all forgot.</p>
      </div>
  
      <div class="bento-grid gsap-fade-up" style="grid-template-columns: repeat(2, 1fr); gap: 32px; max-width: 1200px; margin: 0 auto; position: relative; z-index: 1;">
        
        <!-- Sales Agent -->
        <div class="bento-card" style="padding: 48px; background: linear-gradient(145deg, rgba(255, 245, 235, 0.95) 0%, rgba(255, 255, 255, 0.8) 100%); backdrop-filter: blur(20px); border: 1px solid var(--border-subtle); display: flex; flex-direction: column; justify-content: space-between; min-height: 480px; border-radius: 32px; box-shadow: 0 24px 64px rgba(0,0,0,0.03);">
          <div>
            <h3 style="font-family: 'Outfit'; font-size: 32px; margin-bottom: 16px; color: var(--text-primary);">Sales Agent</h3>
            <p style="color: var(--text-secondary); font-size: 16px; line-height: 1.6;">Checks what is actually in stock before it promises anything, then closes.</p>
          </div>
          <div class="micro-mockup sales-mockup" style="background: #EFEAE2; border-radius: 16px; padding: 24px; margin-top: 32px; border: 1px solid rgba(0,0,0,0.05); position: relative; overflow: hidden; display: flex; flex-direction: column; gap: 12px;">
            <div class="sales-msg-1" style="background: #fff; color: #111; padding: 12px 16px; border-radius: 16px; border-bottom-left-radius: 4px; align-self: flex-start; max-width: 90%; font-size: 14px; opacity: 0; transform: translateY(10px); box-shadow: 0 4px 12px rgba(0,0,0,0.05);">Do you have this in large?</div>
            <div class="sales-typing" style="align-self: flex-start; background: #e5dfd6; padding: 8px 16px; border-radius: 16px; opacity: 0; display: flex; gap: 4px; align-items: center; transform: scale(0.9); transform-origin: left bottom;"><span class="dot" style="width:6px;height:6px;background:#aaa;border-radius:50%;display:inline-block;"></span><span class="dot" style="width:6px;height:6px;background:#aaa;border-radius:50%;display:inline-block;"></span><span class="dot" style="width:6px;height:6px;background:#aaa;border-radius:50%;display:inline-block;"></span></div>
            <div class="sales-msg-2" style="background: #DDF3D5; color: #155724; padding: 12px 16px; border-radius: 16px; border-bottom-right-radius: 4px; align-self: flex-end; max-width: 90%; font-size: 14px; opacity: 0; transform: translateY(10px); box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
               <span id="sales-tw"></span><span class="sales-cursor" style="display:inline-block; width:2px; height:14px; background:#155724; margin-left:2px; animation:blink 1s infinite;"></span>
            </div>
            <div class="receipt-pill sales-receipt" style="opacity: 0; transform: scale(0.9); margin: 8px auto 0; background: #fff; padding: 8px 16px; border-radius: 100px; display: flex; align-items: center; gap: 8px; font-size: 12px; font-weight: 600; color: #111; border: 1px solid rgba(11,158,88,0.2); box-shadow: 0 8px 24px rgba(11,158,88,0.1);"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#0B9E58" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg> <span>SHOPIFY</span></div>
          </div>
        </div>
  
        <!-- Lead Agent -->
        <div class="bento-card" style="padding: 48px; background: linear-gradient(145deg, rgba(249, 240, 255, 0.95) 0%, rgba(255, 255, 255, 0.8) 100%); backdrop-filter: blur(20px); border: 1px solid var(--border-subtle); display: flex; flex-direction: column; justify-content: space-between; min-height: 480px; border-radius: 32px; box-shadow: 0 24px 64px rgba(0,0,0,0.03);">
          <div>
            <h3 style="font-family: 'Outfit'; font-size: 32px; margin-bottom: 16px; color: var(--text-primary);">Lead Agent</h3>
            <p style="color: var(--text-secondary); font-size: 16px; line-height: 1.6;">Finds out budget and timeline the way a good salesperson would, then writes it into your CRM.</p>
          </div>
          <div class="micro-mockup lead-mockup" style="background: #fafafa; border-radius: 16px; padding: 24px; margin-top: 32px; border: 1px solid var(--border-subtle); position: relative; overflow: hidden;">
            <div style="font-family: 'Inter'; font-size: 12px; color: var(--text-tertiary); margin-bottom: 12px; text-transform: uppercase; letter-spacing: 1px;">HubSpot CRM</div>
            <div class="lead-hs-card" style="background: #fff; border-radius: 8px; padding: 16px; border-left: 4px solid #ff7a59; box-shadow: 0 4px 12px rgba(0,0,0,0.05); opacity: 0; transform: translateX(20px);">
              <div style="font-weight: 600; color: #111; font-size: 14px;">New Lead: <span id="lead-name-tw" style="color:#ff7a59;"></span><span class="lead-cursor-1" style="display:inline-block; width:2px; height:12px; background:#ff7a59; margin-left:2px; animation:blink 1s infinite;"></span></div>
              <div style="color: var(--text-secondary); font-size: 13px; margin-top: 8px; display: flex; flex-direction: column; gap: 4px;">
                 <div class="lead-budget" style="opacity:0; transform:translateX(10px);">Budget: <strong style="color:#111;">$5k-$10k</strong></div>
                 <div class="lead-timeline" style="opacity:0; transform:translateX(10px);">Timeline: <strong style="color:#111;">Q3</strong></div>
              </div>
            </div>
            <div class="receipt-pill lead-receipt" style="opacity: 0; transform: scale(0.9); margin: 24px auto 0; background: #fff; padding: 8px 16px; border-radius: 100px; display: flex; align-items: center; justify-content: center; gap: 8px; font-size: 12px; font-weight: 600; color: #111; border: 1px solid rgba(255,122,89,0.3); box-shadow: 0 8px 24px rgba(255,122,89,0.15); width: max-content;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#ff7a59" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg> <span>HUBSPOT</span></div>
          </div>
        </div>
  
        <!-- Meetings Agent -->
        <div class="bento-card" style="padding: 48px; background: linear-gradient(145deg, rgba(239, 245, 255, 0.95) 0%, rgba(255, 255, 255, 0.8) 100%); backdrop-filter: blur(20px); border: 1px solid var(--border-subtle); display: flex; flex-direction: column; justify-content: space-between; min-height: 480px; border-radius: 32px; box-shadow: 0 24px 64px rgba(0,0,0,0.03);">
          <div>
            <h3 style="font-family: 'Outfit'; font-size: 32px; margin-bottom: 16px; color: var(--text-primary);">Meetings Agent</h3>
            <p style="color: var(--text-secondary); font-size: 16px; line-height: 1.6;">Offers times that are genuinely free, and puts the meeting in your calendar.</p>
          </div>
          <div class="micro-mockup meet-mockup" style="background: #F9FAFB; border-radius: 16px; padding: 24px; margin-top: 32px; border: 1px solid var(--border-subtle); position: relative; overflow: hidden; display: flex; flex-direction: column; gap: 12px;">
            <div class="meet-msg-1" style="background: #E5E7EB; color: #111; padding: 12px 16px; border-radius: 16px; border-bottom-left-radius: 4px; align-self: flex-start; max-width: 90%; font-size: 14px; opacity: 0; transform: translateY(10px); box-shadow: 0 4px 12px rgba(0,0,0,0.05);">I want to book a site visit.</div>
            
            <div class="meet-cal-card" style="background: #fff; border-radius: 12px; border: 1px solid #eee; padding: 12px; box-shadow: 0 8px 24px rgba(0,0,0,0.05); align-self: center; width: 100%; opacity: 0; transform: translateY(10px);">
               <div style="font-size: 11px; color: #888; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px;">Pick a time</div>
               <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
                  <div style="border: 1px solid #eee; padding: 8px; border-radius: 6px; font-size: 12px; text-align: center; color: #666;">Friday 2 PM</div>
                  <div class="meet-slot-target" style="border: 1px solid #eee; padding: 8px; border-radius: 6px; font-size: 12px; text-align: center; color: #666; position: relative;">Saturday 11 AM
                     <div class="meet-slot-pulse" style="position: absolute; top:0; left:0; right:0; bottom:0; background: rgba(139,92,246,0.3); border-radius: 6px; opacity: 0; transform: scale(1);"></div>
                  </div>
               </div>
            </div>

            <div class="meet-msg-2" style="background: #8B5CF6; color: #fff; padding: 12px 16px; border-radius: 16px; border-bottom-right-radius: 4px; align-self: flex-end; max-width: 90%; font-size: 14px; opacity: 0; transform: translateY(10px); box-shadow: 0 4px 12px rgba(139,92,246,0.2);">Saturday 11 AM works perfectly!</div>
            <div class="receipt-pill meet-receipt" style="opacity: 0; transform: scale(0.9); margin: 8px auto 0; background: #fff; padding: 8px 16px; border-radius: 100px; display: flex; align-items: center; justify-content: center; gap: 8px; font-size: 12px; font-weight: 600; color: #111; border: 1px solid rgba(139,92,246,0.3); box-shadow: 0 8px 24px rgba(139,92,246,0.15); width: max-content;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#8B5CF6" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg> <span>CALENDAR</span></div>
          </div>
        </div>
  
        <!-- Support Agent -->
        <div class="bento-card" style="padding: 48px; background: linear-gradient(145deg, rgba(236, 251, 249, 0.95) 0%, rgba(255, 255, 255, 0.8) 100%); backdrop-filter: blur(20px); border: 1px solid var(--border-subtle); display: flex; flex-direction: column; justify-content: space-between; min-height: 480px; border-radius: 32px; box-shadow: 0 24px 64px rgba(0,0,0,0.03);">
          <div>
            <h3 style="font-family: 'Outfit'; font-size: 32px; margin-bottom: 16px; color: var(--text-primary);">Support Agent</h3>
            <p style="color: var(--text-secondary); font-size: 16px; line-height: 1.6;">Tracks the order, explains the return policy, and only wakes you if something is actually wrong.</p>
          </div>
          <div class="micro-mockup supp-mockup" style="background: #fafafa; border-radius: 16px; padding: 24px; margin-top: 32px; border: 1px solid var(--border-subtle); position: relative; overflow: hidden; display: flex; flex-direction: column; gap: 12px;">
            <div class="supp-msg-1" style="background: #fff; color: #111; padding: 12px 16px; border-radius: 16px; border-bottom-left-radius: 4px; align-self: flex-start; max-width: 90%; font-size: 14px; opacity: 0; transform: translateY(10px); box-shadow: 0 4px 12px rgba(0,0,0,0.05); border: 1px solid #eee;">Where is my order?</div>
            
            <div class="supp-zd-card" style="background: #fff; border-radius: 12px; padding: 16px; border: 1px solid #eee; border-left: 4px solid #00363D; opacity: 0; transform: translateX(-20px); align-self: center; width: 100%; display: flex; align-items: center; justify-content: space-between;">
               <div>
                  <div style="font-size: 12px; color: #666;">Order #8924</div>
                  <div class="supp-status" style="font-weight: 600; color: #111; font-size: 14px; margin-top: 4px;">Processing...</div>
               </div>
               <div class="supp-icon" style="background: #f4f5f7; padding: 8px; border-radius: 50%;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#666" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg></div>
            </div>

            <div class="supp-msg-2" style="background: #f4f5f7; color: #111; padding: 12px 16px; border-radius: 16px; border-bottom-right-radius: 4px; align-self: flex-end; max-width: 90%; font-size: 14px; opacity: 0; transform: translateY(10px); box-shadow: 0 4px 12px rgba(0,0,0,0.05); border: 1px solid #efefef;">It is out for delivery today at 6PM!</div>
            
            <div class="receipt-pill supp-receipt" style="opacity: 0; transform: scale(0.9); margin: 8px auto 0; background: #fff; padding: 8px 16px; border-radius: 100px; display: flex; align-items: center; justify-content: center; gap: 8px; font-size: 12px; font-weight: 600; color: #111; border: 1px solid rgba(0,54,61,0.3); box-shadow: 0 8px 24px rgba(0,54,61,0.15); width: max-content;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#00363D" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg> <span>ZENDESK</span></div>
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
  
  <div style="flex:1; display:flex; justify-content:center; align-items:center; min-width:300px; position:relative; padding: 60px;">
    <!-- Dark Gradient Backdrop for Mockup -->
    <div style="position:absolute; top:0; left:0; width:100%; height:100%; background: linear-gradient(135deg, #060B16 0%, #12264E 100%); border-radius: 40px; z-index: 0;"></div>
    
    <!-- Subtle Inner Glow for Extra Depth -->
    <div style="position:absolute; top:50%; left:50%; transform:translate(-50%, -50%); width:80%; height:80%; background: radial-gradient(circle at center, rgba(61, 116, 236, 0.4) 0%, transparent 70%); filter: blur(60px); z-index: 1; pointer-events: none;"></div>
    
    <!-- Dark Mode Setup Mockup container -->
    <div class="setup-mockup gsap-scale-in" style="width:100%; max-width:460px; height:500px; background:#111; border-radius:24px; border:1px solid #222; box-shadow: 0 24px 64px rgba(0,0,0,0.2); color:#fff; font-family:'Inter', sans-serif; position:relative; overflow:hidden; z-index:2;">
      
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
                <button id="mockup-go-live-btn" style="width:100%; background:linear-gradient(45deg, #1A56DB, #0B9E58); border:none; color:#fff; border-radius:12px; padding:16px; font-size:16px; font-weight:700; transition:all 0.3s;">Go Live 🚀</button>
              </div>
          </div>
          
          <!-- SUCCESS SCREEN -->
          <div id="step-success-screen" style="position:absolute; inset:0; background:#111; display:flex; flex-direction:column; align-items:center; justify-content:center; opacity:0; pointer-events:none; z-index:20;">
              <div class="loader-circle" style="width:48px; height:48px; border:4px solid #333; border-top-color:#0B9E58; border-radius:50%; margin-bottom:24px; animation:spin 1s linear infinite;"></div>
              
              <div id="success-content" style="opacity:0; display:flex; flex-direction:column; align-items:center; position:absolute; inset:0; justify-content:center; background:#111;">
                <div id="success-confetti" style="font-size:64px; margin-bottom:16px; transform:scale(0);">🎉</div>
                <h2 style="font-family:'Outfit'; font-size:32px; font-weight:700; margin-bottom:12px; text-align:center; background:linear-gradient(45deg, #1A56DB, #0B9E58); -webkit-background-clip:text; -webkit-text-fill-color:transparent;">Congratulations!</h2>
                <p style="color:#888; text-align:center; line-height:1.5;">Your agent is live and talking to customers.</p>
              </div>
              
              <!-- Web Chat Bubble Pop -->
              <div id="demo-chat-bubble" style="position:absolute; bottom:-120px; right:0; background:#fff; border-radius:16px 16px 0 16px; padding:16px; color:#111; width:260px; box-shadow:0 10px 30px rgba(0,0,0,0.3); border:1px solid #efefef;">
                 <div style="font-size:13px; font-weight:700; color:var(--accent); margin-bottom:4px;">Sales Agent</div>
                 <div style="font-size:14px; line-height:1.4;">Hi! I'm live on your site. How can I help? 👋</div>
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
  
  <div style="flex:1.5; display:flex; justify-content:center; align-items:center; min-width:300px; position:relative; padding: 60px;">
    <!-- Dark Gradient Backdrop for Mockup -->
    <div style="position:absolute; top:0; left:0; width:100%; height:100%; background: linear-gradient(135deg, #060B16 0%, #12264E 100%); border-radius: 40px; z-index: 0;"></div>
    
    <!-- Subtle Inner Glow for Extra Depth -->
    <div style="position:absolute; top:50%; left:50%; transform:translate(-50%, -50%); width:80%; height:80%; background: radial-gradient(circle at center, rgba(61, 116, 236, 0.4) 0%, transparent 70%); filter: blur(60px); z-index: 1; pointer-events: none;"></div>
    
    <!-- Inbox UI Mockup -->
    <div class="inbox-mockup" style="opacity:0; transform:scale(0.9); width:100%; max-width:800px; height:500px; background:#fff; border-radius:24px; border:1px solid rgba(255,255,255,0.1); box-shadow: 0 32px 80px rgba(0,0,0,0.4); display:flex; overflow:hidden; font-family:'Inter', sans-serif; position:relative; z-index:2;">
      
      <!-- Sidebar -->
      <div style="width:260px; background:#fbfbfd; border-right:1px solid var(--border-subtle); display:flex; flex-direction:column;">
         <div style="padding:24px; border-bottom:1px solid var(--border-subtle);">
            <div style="font-weight:700; font-size:18px; font-family:'Outfit'; color:#111;">Steps Inbox</div>
         </div>
         <div style="flex:1; overflow-y:auto; padding:12px;">
            <div style="padding:12px; background:#fff; border-radius:12px; border:1px solid var(--accent); box-shadow:0 4px 12px rgba(0,0,0,0.05); margin-bottom:8px; cursor:pointer;">
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
            
            <div style="padding:12px; background:transparent; border-radius:12px; border:1px solid transparent; margin-bottom:8px; opacity:0.6;">
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
         </div>
      </div>
      
      <!-- Main Chat Area -->
      <div style="flex:1; display:flex; flex-direction:column; background:#fff;">
         <!-- Chat Header -->
         <div style="padding:20px 24px; border-bottom:1px solid var(--border-subtle); display:flex; justify-content:space-between; align-items:center;">
            <div>
               <div style="font-weight:700; font-size:16px; color:#111;">Sarah Jenkins</div>
               <div style="font-size:13px; color:#666;">WhatsApp &bull; Order #8821</div>
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
                  Yes! We ship to Germany via DHL Express. It usually takes 2-3 business days. Shipping is free on orders over €150.
               </div>
            </div>
            
            <div class="human-req" style="display:flex; gap:12px; max-width:85%;">
               <div style="width:28px; height:28px; border-radius:50%; background:#e0e0e0; flex-shrink:0;"></div>
               <div style="background:#fff; padding:12px 16px; border-radius:16px 16px 16px 0; border:1px solid var(--border-subtle); font-size:14px; color:#111; line-height:1.5;">Great. I have a custom tax exemption code for my business, can I speak to a human about applying it to this order?</div>
            </div>
            
            <div class="handover-banner" style="display:none; background:#E9F8F0; border:1px solid #c2ebd5; padding:12px; border-radius:12px; align-items:center; justify-content:center; gap:8px; margin:8px 0; opacity:0; transform:translateY(10px);">
               <span style="font-size:16px;">🛑</span>
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
      
    </div>
  </div>
  
  <div style="flex:1;">
    <span class="gsap-fade-up" style="font-family: 'Geist Mono', monospace; font-size: 12px; color: var(--accent); letter-spacing: .2em; text-transform: uppercase; margin-bottom:16px; display:block;">YOU STAY IN CONTROL</span>
    <h2 class="gsap-fade-up" style="font-family: 'Outfit'; font-size: clamp(40px, 4vw, 56px); margin: 0 0 24px; color: var(--text-primary); line-height:1.1;">It never sends a message you cannot read.</h2>
    <p class="gsap-fade-up" style="font-size: 18px; color: var(--text-secondary); margin-bottom: 24px; line-height: 1.6; max-width:500px;">Every conversation, from every channel, lands in one inbox. Jump in whenever you feel like it and your agent goes quiet on that thread until you are finished.</p>
    <p class="gsap-fade-up" style="font-size: 18px; color: var(--text-secondary); margin-bottom: 0; line-height: 1.6; max-width:500px;">You decide what it is allowed to answer. You decide where it has to stop. Every conversation is there to read. When it hands over, the whole history comes with it.</p>
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
  <div style="flex:1.2; display:flex; justify-content:center; align-items:center; min-width:300px; position:relative; padding: 60px;">
    <!-- Dark Gradient Backdrop for Mockup -->
    <div style="position:absolute; top:0; left:0; width:100%; height:100%; background: linear-gradient(135deg, #060B16 0%, #12264E 100%); border-radius: 40px; z-index: 0;"></div>
    
    <!-- Subtle Inner Glow for Extra Depth -->
    <div style="position:absolute; top:50%; left:50%; transform:translate(-50%, -50%); width:80%; height:80%; background: radial-gradient(circle at center, rgba(61, 116, 236, 0.4) 0%, transparent 70%); filter: blur(60px); z-index: 1; pointer-events: none;"></div>
    
    <!-- Copilot Mockup -->
    <div class="copilot-mockup" style="opacity:0; transform:scale(0.9); width:100%; max-width:640px; background:#1f2228; border-radius:24px; border:1px solid #3a3f4a; box-shadow: 0 32px 80px rgba(0,0,0,0.4); padding:32px; display:flex; flex-direction:column; gap:24px; font-family:'Inter', sans-serif; position:relative; z-index:2;">
       
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
          <div style="background:#2A2D35; border:1px solid #3a3f4a; border-radius:16px; padding:24px; position:relative; margin-top:12px;">
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
</section>
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
      start: "top 60%",
      onEnter: () => {
        if(setupPlayed) return;
        setupPlayed = true;
        let setupTl = gsap.timeline({
          repeat: -1,
          repeatDelay: 2,
          onRepeat: () => {
            let urlEl = document.getElementById("typewriter-url");
            if (urlEl) urlEl.textContent = "";
            let btn = document.getElementById("mockup-proceed-btn");
            if (btn) btn.textContent = "Connect";
            let nameEl = document.getElementById("typewriter-name");
            if (nameEl) nameEl.textContent = "";
          }
        });
        
        // --- STEP 1 ---
        let urlText = "https://habitiq.app/";
        let el = document.getElementById("typewriter-url");
        if(el) {
            setupTl.to({}, {duration: 0.5}) // delay
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


    // Inbox Storytelling Animation
    let inboxPlayed = false;
    ScrollTrigger.create({
      trigger: ".inbox-section",
      start: "top 75%",
      onEnter: () => {
        if(inboxPlayed) return;
        inboxPlayed = true;
        let tl = gsap.timeline({
          repeat: -1,
          repeatDelay: 2,
          onRepeat: () => {
             let st = document.querySelector(".status-text"); if(st) st.textContent = "AI is reading...";
             let pd = document.querySelector(".pulse-dot"); if(pd) pd.style.background = "var(--accent)";
             let th = document.querySelector(".tag-handover"); if(th) th.style.opacity = "0";
             let el = document.getElementById("typewriter-human"); if(el) el.textContent = "";
             let inputPh = document.querySelector(".input-placeholder"); if(inputPh) inputPh.style.opacity = "1";
          }
        });
        
        tl.to(".inbox-mockup", { opacity: 1, scale: 1, duration: 0.8, ease: "power3.out" })
          .to({}, {duration: 0.8}) // reading the question
          
          // Handover triggers
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
          
          .to({}, {duration: 1.0}) // pause for user to read
          
          // Start typing human reply
          .to(".human-reply", { display: "flex", duration: 0.1 })
          .to(".human-reply", { opacity: 1, y: 0, duration: 0.4 })
          .add(() => {
              let text = "Hi Sarah! I can absolutely help with that. Please send the code here.";
              let el = document.getElementById("typewriter-human");
              let inputPh = document.querySelector(".input-placeholder");
              let i = 0;
              
              // Scroll to bottom
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
              }, 40);
          });
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
        let tl = gsap.timeline({
          repeat: -1,
          repeatDelay: 2
        });
        
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


    // Copilot Storytelling Animation
    let copilotPlayed = false;
    ScrollTrigger.create({
      trigger: ".copilot-section",
      start: "top 75%",
      onEnter: () => {
        if(copilotPlayed) return;
        copilotPlayed = true;
        let tl = gsap.timeline({
          repeat: -1,
          repeatDelay: 2,
          onRepeat: () => {
            let el = document.getElementById("cp-typewriter"); if (el) el.textContent = "";
            let c = document.querySelector(".cp-cursor"); if (c) c.style.display = "inline-block";
          }
        });
        
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


    // --- Animated Mesh Gradient Background ---
    gsap.to(".mesh-bg", {
      opacity: 1,
      duration: 2,
      scrollTrigger: { trigger: ".four-agents-section", start: "top 60%" }
    });
    
    // Rotate the mesh gradient slowly
    gsap.to(".mesh-bg", {
      rotation: 360,
      duration: 40,
      repeat: -1,
      ease: "linear",
      transformOrigin: "center center"
    });

    // --- 1. Sales Agent Animation ---
    let salesTl = gsap.timeline({ repeat: -1, repeatDelay: 2, 
      onRepeat: () => {
         let el = document.getElementById("sales-tw"); if(el) el.textContent = "";
      }
    });
    salesTl.to(".sales-msg-1", { opacity: 1, y: 0, duration: 0.4, ease: "power2.out" })
           .to({}, {duration: 0.5})
           .to(".sales-typing", { opacity: 1, scale: 1, duration: 0.2 })
           .to(".sales-typing .dot", { y: -3, duration: 0.2, stagger: 0.1, yoyo: true, repeat: 3 })
           .to(".sales-typing", { opacity: 0, scale: 0.9, duration: 0.2 })
           .to(".sales-msg-2", { opacity: 1, y: 0, duration: 0.4, ease: "power2.out" })
           .add(() => {
              let text = "Yes, two left! Added to cart.";
              let el = document.getElementById("sales-tw");
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
           .to({}, {duration: 1.5})
           .to(".sales-receipt", { opacity: 1, scale: 1, duration: 0.5, ease: "back.out(2)" });

    // --- 2. Lead Agent Animation ---
    let leadTl = gsap.timeline({ repeat: -1, repeatDelay: 2,
      onRepeat: () => {
         let el = document.getElementById("lead-name-tw"); if(el) el.textContent = "";
      }
    });
    leadTl.to(".lead-hs-card", { opacity: 1, x: 0, duration: 0.6, ease: "power3.out" })
          .add(() => {
              let text = "Sarah Jenkins";
              let el = document.getElementById("lead-name-tw");
              let i = 0;
              let interval = setInterval(() => {
                if(i < text.length) {
                  if(el) el.textContent += text.charAt(i);
                  i++;
                } else {
                  clearInterval(interval);
                }
              }, 60);
          })
          .to({}, {duration: 1.2})
          .to(".lead-budget", { opacity: 1, x: 0, duration: 0.3 })
          .to(".lead-timeline", { opacity: 1, x: 0, duration: 0.3 }, "+=0.2")
          .to({}, {duration: 0.5})
          .to(".lead-receipt", { opacity: 1, scale: 1, duration: 0.5, ease: "back.out(2)" });

    // --- 3. Meetings Agent Animation ---
    let meetTl = gsap.timeline({ repeat: -1, repeatDelay: 2,
      onRepeat: () => {
         let el = document.querySelector(".meet-slot-target");
         if(el) {
            el.style.background = "none";
            el.style.color = "#666";
            el.style.borderColor = "#eee";
            el.style.fontWeight = "normal";
         }
      }
    });
    meetTl.to(".meet-msg-1", { opacity: 1, y: 0, duration: 0.4, ease: "power2.out" })
          .to({}, {duration: 0.5})
          .to(".meet-cal-card", { opacity: 1, y: 0, duration: 0.5, ease: "power2.out" })
          .to({}, {duration: 0.5})
          .add(() => {
             let el = document.querySelector(".meet-slot-target");
             if(el) {
                el.style.background = "rgba(139,92,246,0.1)";
                el.style.color = "#8B5CF6";
                el.style.borderColor = "#8B5CF6";
                el.style.fontWeight = "600";
             }
          })
          .to(".meet-slot-pulse", { opacity: 1, scale: 1.5, duration: 0.4, ease: "power2.out" })
          .to(".meet-slot-pulse", { opacity: 0, duration: 0.2 })
          .to({}, {duration: 0.4})
          .to(".meet-msg-2", { opacity: 1, y: 0, duration: 0.4, ease: "power2.out" })
          .to({}, {duration: 0.5})
          .to(".meet-receipt", { opacity: 1, scale: 1, duration: 0.5, ease: "back.out(2)" });

    // --- 4. Support Agent Animation ---
    let suppTl = gsap.timeline({ repeat: -1, repeatDelay: 2,
      onRepeat: () => {
         let st = document.querySelector(".supp-status"); if(st) { st.textContent = "Processing..."; st.style.color = "#111"; }
         let ic = document.querySelector(".supp-icon svg"); if(ic) { ic.innerHTML = '<path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>'; ic.style.stroke = "#666"; }
         let bg = document.querySelector(".supp-icon"); if(bg) bg.style.background = "#f4f5f7";
         let cd = document.querySelector(".supp-zd-card"); if(cd) cd.style.borderLeftColor = "#00363D";
      }
    });
    suppTl.to(".supp-msg-1", { opacity: 1, y: 0, duration: 0.4, ease: "power2.out" })
          .to({}, {duration: 0.5})
          .to(".supp-zd-card", { opacity: 1, x: 0, duration: 0.5, ease: "power2.out" })
          .to({}, {duration: 0.8})
          // Status change
          .add(() => {
             let st = document.querySelector(".supp-status"); if(st) { st.textContent = "Out for Delivery"; st.style.color = "#0B9E58"; }
             let ic = document.querySelector(".supp-icon svg"); if(ic) { ic.innerHTML = '<polyline points="20 6 9 17 4 12"></polyline>'; ic.style.stroke = "#0B9E58"; }
             let bg = document.querySelector(".supp-icon"); if(bg) bg.style.background = "#E9F8F0";
          })
          .to(".supp-zd-card", { borderLeftColor: "#0B9E58", duration: 0.3 })
          .to({}, {duration: 0.8})
          .to(".supp-msg-2", { opacity: 1, y: 0, duration: 0.4, ease: "power2.out" })
          .to({}, {duration: 0.5})
          .to(".supp-receipt", { opacity: 1, scale: 1, duration: 0.5, ease: "back.out(2)" });


    // --- Channels Section Animations ---
    
    // IG Animation
    let igTl = gsap.timeline({ repeat: -1, repeatDelay: 3 });
    igTl.to(".ig-comment", { opacity: 1, y: 0, duration: 0.4, ease: "power2.out" })
        .to({}, {duration: 0.8})
        .to(".ig-reply", { opacity: 1, y: 0, duration: 0.4, ease: "power2.out" })
        .to({}, {duration: 0.8})
        .to(".ig-dm", { opacity: 1, y: 0, duration: 0.5, ease: "back.out(1.5)" })
        .to({}, {duration: 2});

    // WA Animation
    let waTl = gsap.timeline({ repeat: -1, repeatDelay: 3 });
    waTl.to(".wa-msg-1", { opacity: 1, y: 0, duration: 0.4, ease: "power2.out" })
        .to({}, {duration: 0.8})
        .to(".wa-msg-2", { opacity: 1, y: 0, duration: 0.5, ease: "back.out(1.5)" })
        .to({}, {duration: 2});

    // Web Animation
    let webTl = gsap.timeline({ repeat: -1, repeatDelay: 3 });
    webTl.to(".web-widget", { opacity: 1, y: 0, scale: 1, duration: 0.6, ease: "back.out(1.2)" })
         .to({}, {duration: 3});


    // --- Workflows Section Animations ---
    function animateWorkflow(pathIndex) {
        let tl = gsap.timeline({ repeat: -1, repeatDelay: 2 });
        let pulse = `.wf-pulse-${pathIndex}`;
        let lineActive = `.wf-line-active-${pathIndex}`;
        
        tl.set(pulse, { left: "0%", opacity: 1 })
          .set(lineActive, { width: "0%" })
          .call(() => { let el = document.querySelector(`.wf-n${pathIndex}-1`); if(el) el.classList.add('active'); })
          
          .to(pulse, { left: "25%", duration: 1, ease: "power1.inOut" })
          .to(lineActive, { width: "25%", duration: 1, ease: "power1.inOut" }, "<")
          .call(() => { let el = document.querySelector(`.wf-n${pathIndex}-2`); if(el) el.classList.add('active'); })
          
          .to(pulse, { left: "50%", duration: 1, ease: "power1.inOut" })
          .to(lineActive, { width: "50%", duration: 1, ease: "power1.inOut" }, "<")
          .call(() => { let el = document.querySelector(`.wf-n${pathIndex}-3`); if(el) el.classList.add('active'); })
          
          .to(pulse, { left: "75%", duration: 1, ease: "power1.inOut" })
          .to(lineActive, { width: "75%", duration: 1, ease: "power1.inOut" }, "<")
          .call(() => { let el = document.querySelector(`.wf-n${pathIndex}-4`); if(el) el.classList.add('active'); })
          
          .to(pulse, { left: "100%", duration: 1, ease: "power1.inOut" })
          .to(lineActive, { width: "100%", duration: 1, ease: "power1.inOut" }, "<")
          .to(pulse, { opacity: 0, duration: 0.2 })
          
          // Cleanup at end
          .to({}, {duration: 1})
          .call(() => {
              document.querySelectorAll(`.wf-n${pathIndex}-1, .wf-n${pathIndex}-2, .wf-n${pathIndex}-3, .wf-n${pathIndex}-4`).forEach(el => el.classList.remove('active'));
          });
          
        return tl;
    }
    
    // Create ScrollTrigger to start animations when section is visible
    ScrollTrigger.create({
        trigger: ".workflows-section",
        start: "top 60%",
        onEnter: () => {
            setTimeout(() => animateWorkflow(1), 0);
            setTimeout(() => animateWorkflow(2), 500);
            setTimeout(() => animateWorkflow(3), 1000);
            setTimeout(() => animateWorkflow(4), 1500);
        },
        once: true
    });

  </script>
</body>
</html>
"""

decks = [
    r"C:/Users/user/Downloads/StepsAI-Copy-Deck.md",
    r"C:/Users/user/Downloads/StepsAI-Copy-Deck-v2.md",
    r"C:/Users/user/Downloads/StepsAI-Copy-Deck-v3.md",
    r"C:/Users/user/Downloads/StepsAI-Copy-Deck-v4-FINAL.md"
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
    line = re.sub(r'\*\*(.*?)\*\*', r'<strong></strong>', line)
    line = re.sub(r'!\[([^\]]*)\]\(([^\)]+)\)', r'<img src="" alt="" style="width: 100%; border-radius: 12px; margin: 16px 0; border: 1px solid var(--border-subtle); display: block;" />', line)
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
            
        if data["route"] == "" and "Setup" in block["title"]:
            try: html_content += CUSTOM_SETUP
            except NameError: pass
            continue
            
        if data["route"] == "" and "One Inbox" in block["title"]:
            try: html_content += CUSTOM_ONE_INBOX
            except NameError: pass
            continue
            
        if data["route"] == "" and "Analytics" in block["title"]:
            try: html_content += CUSTOM_ANALYTICS
            except NameError: pass
            continue
            
        if data["route"] == "" and "Channels" in block["title"]:
            try: html_content += CUSTOM_CHANNELS
            except NameError: pass
            continue

        if data["route"] == "" and "Workflows" in block["title"]:
            try: html_content += CUSTOM_WORKFLOWS
            except NameError: pass
            continue

        if data["route"] == "" and "Internal Copilot" in block["title"]:
            try: html_content += CUSTOM_COPILOT
            except NameError: pass
            continue
            
        
        is_faq = "FAQ" in block["title"].upper()
        
        if is_faq:
            html_content += '''
            <style>
              .faq-split-section { display: flex; gap: 80px; align-items: flex-start; max-width: 1200px; margin: 0 auto; padding: 120px 32px; }
              .faq-left { flex: 1; position: sticky; top: 120px; }
              .faq-right { flex: 1.5; display: flex; flex-direction: column; border-top: 1px solid #eaeaea; }
              .faq-item { border-bottom: 1px solid #eaeaea; overflow: hidden; }
              .faq-question { padding: 24px 0; display: flex; justify-content: space-between; align-items: center; cursor: pointer; font-family: 'Inter', sans-serif; font-size: 18px; font-weight: 700; color: #111; user-select: none; }
              .faq-icon { font-size: 24px; font-weight: 300; color: #111; transition: transform 0.3s ease; }
              .faq-item.active .faq-icon { transform: rotate(45deg); }
              .faq-answer { max-height: 0; overflow: hidden; transition: max-height 0.3s ease, padding 0.3s ease; font-size: 16px; color: #666; line-height: 1.6; padding: 0 0; }
              .faq-item.active .faq-answer { max-height: 500px; padding: 0 0 24px 0; }
              @media (max-width: 900px) {
                 .faq-split-section { flex-direction: column; gap: 40px; padding: 80px 24px; }
                 .faq-left { position: static; }
              }
            </style>
            <section class="section-v2" style="background: #ffffff; padding: 0;">
               <div class="faq-split-section">
                 <div class="faq-left gsap-fade-up">
                    <h2 style="font-family: 'Outfit'; font-size: clamp(40px, 5vw, 56px); font-weight: 800; color: #111; margin-bottom: 24px; line-height: 1.1; letter-spacing: -0.02em;">You should have questions.</h2>
                    <p style="font-size: 18px; color: #666; line-height: 1.6; margin-bottom: 32px; font-family: 'Inter', sans-serif;">The most useful homepage FAQs reduce purchase anxiety.<br>They should not become an SEO keyword dump.</p>
                    <a href="#" style="color: #0B9E58; font-weight: 600; text-decoration: none; font-size: 16px; display: inline-flex; align-items: center; gap: 8px; font-family: 'Inter', sans-serif;">Still unsure? Talk to a human <span style="font-size: 18px;">&rarr;</span></a>
                 </div>
                 <div class="faq-right gsap-fade-up">
            '''
            q = ""
            a = []
            for c in block["content"]:
                c_clean = c.replace('>', '').strip()
                if c_clean.startswith('**') and '?' in c_clean:
                    if q:
                        html_content += f'''
                        <div class="faq-item" onclick="this.classList.toggle('active')">
                            <div class="faq-question">{q} <span class="faq-icon">+</span></div>
                            <div class="faq-answer">{chr(10).join(a)}</div>
                        </div>'''
                    q = c_clean.replace('**', '').strip()
                    a = []
                elif c_clean:
                    a.append(parse_markdown_line(c_clean))
            if q:
                html_content += f'''
                <div class="faq-item" onclick="this.classList.toggle('active')">
                    <div class="faq-question">{q} <span class="faq-icon">+</span></div>
                    <div class="faq-answer">{chr(10).join(a)}</div>
                </div>'''
            html_content += '''
                 </div>
               </div>
            </section>
            '''

            
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
    
    head = GLOBAL_HEAD.format(title=data["title"], root_prefix=root_prefix)
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
