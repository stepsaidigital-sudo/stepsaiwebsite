import os

pages = [
    '/pricing/', '/product/ai-agents/', '/product/copilot/',
    '/solutions/ecommerce/', '/solutions/saas/', '/solutions/healthcare/',
    '/solutions/education/', '/solutions/real-estate/',
    '/use-cases/marketing-growth/', '/use-cases/sales/', '/use-cases/support-cx/', '/use-cases/operations/',
    '/channels/', '/channels/website/', '/channels/whatsapp/', '/channels/instagram/', '/channels/standalone-page/',
    '/features/', '/features/sales-agent/', '/features/lead-agent/', '/features/meetings-agent/', '/features/support-agent/',
    '/features/workflows/', '/features/inbox/', '/features/analytics/',
    '/integrations/', '/partners/', '/partners/apply/',
    '/about/', '/note/', '/team/', '/careers/', '/contact/', '/blog/',
    '/resources/ai-guides/', '/resources/case-studies/',
    '/privacy-policy/', '/terms-of-service/', '/404/'
]

# Shared Base CSS and Nav structure
shared_head = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>StepsAI - {title}</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Outfit:wght@500;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    :root {
      --primary: #2563EB; 
      --bg-color: #FAFAFA;
      --text-main: #0F172A;
      --text-muted: #64748B;
      --border-light: #E2E8F0;
    }
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { background-color: var(--bg-color); color: var(--text-main); font-family: 'Inter', sans-serif; line-height: 1.6; }
    h1, h2, h3 { font-family: 'Outfit', sans-serif; }
    a { text-decoration: none; color: inherit; }
    
    .nav { position: fixed; top: 0; left: 0; width: 100%; z-index: 1000; background: rgba(255,255,255,0.9); backdrop-filter: blur(10px); border-bottom: 1px solid rgba(0,0,0,0.05); }
    .nav-container { max-width: 1300px; margin: 0 auto; padding: 16px 32px; display: flex; align-items: center; justify-content: space-between; }
    .nav-logo-area { display: flex; align-items: center; gap: 10px; font-weight: 800; font-size: 20px; }
    .nav-logo-icon { width: 30px; height: 30px; background: var(--primary); border-radius: 8px; color: white; display: flex; align-items: center; justify-content: center; }
    .nav-tabs { display: flex; gap: 28px; }
    .nav-tab { color: #334155; font-size: 14px; font-weight: 600; cursor: pointer; }
    .nav-tab:hover { color: var(--text-main); }
    .nav-right { display: flex; align-items: center; gap: 20px; }
    .btn-outline { border: 1px solid var(--border-light); background: white; padding: 8px 16px; border-radius: 8px; font-size: 14px; font-weight: 600; cursor: pointer; }
    .btn-primary { background: var(--primary); color: white; padding: 10px 20px; border-radius: 8px; font-size: 14px; font-weight: 600; border: none; cursor: pointer; }
    
    .page-hero { padding: 160px 24px 80px; text-align: center; background: white; border-bottom: 1px solid var(--border-light); }
    .page-hero h1 { font-size: 48px; margin-bottom: 16px; letter-spacing: -1px; }
    .page-hero p { font-size: 18px; color: var(--text-muted); max-width: 600px; margin: 0 auto; }
    
    .container { max-width: 1200px; margin: 80px auto; padding: 0 24px; min-height: 40vh; }
    
    .footer { background: white; padding: 64px 0 32px; border-top: 1px solid var(--border-light); text-align: center; color: var(--text-muted); font-size: 14px;}
  </style>
</head>
<body>
  <nav class="nav">
    <div class="nav-container">
      <a href="/" class="nav-logo-area">
        <div class="nav-logo-icon">S</div>
        <div>StepsAI</div>
      </a>
      <div class="nav-tabs">
        <div class="nav-tab">Product ▾</div>
        <div class="nav-tab">Solutions ▾</div>
        <a href="/pricing/" class="nav-tab">Pricing</a>
        <a href="/partners/" class="nav-tab">Partner</a>
        <div class="nav-tab">Resources ▾</div>
      </div>
      <div class="nav-right">
        <a href="#" style="color:#334155; font-size:14px; font-weight:600;">Sign in</a>
        <button class="btn-primary">Start free trial</button>
      </div>
    </div>
  </nav>

  <section class="page-hero">
    <h1>{title}</h1>
    <p>This is the newly generated {title} page, built strictly to the StepsAI documentation.</p>
  </section>

  <div class="container">
    <h2>Page content goes here</h2>
    <p>Sections for {title} will be constructed here according to Addendum E.</p>
  </div>

  <footer class="footer">
    Your AI agent layer for every business
  </footer>
</body>
</html>
"""

base_dir = r"C:\Users\user\Downloads\HOME STAEP AI"

for page in pages:
    if page == '/404/':
        dir_path = os.path.join(base_dir, "404")
    else:
        # Remove leading/trailing slashes
        clean_path = page.strip('/')
        dir_path = os.path.join(base_dir, clean_path.replace('/', os.sep))
    
    os.makedirs(dir_path, exist_ok=True)
    
    file_path = os.path.join(dir_path, 'index.html')
    
    # Generate a nice title
    parts = [p.replace('-', ' ').title() for p in page.strip('/').split('/') if p]
    title = " - ".join(parts) if parts else "Page"
    
    if page == '/404/':
        title = "404 Not Found"
        
    html = shared_head.replace('{title}', title)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)

print(f"Successfully generated {len(pages)} subpages.")
