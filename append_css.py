import os

css_append = """
/* MEGA MENU */
.nav-dropdown-wrapper {
  position: relative;
  height: 100%;
  display: flex;
  align-items: center;
}
.mega-menu {
  position: absolute;
  top: calc(100% + 10px);
  left: 50%;
  transform: translateX(-50%) translateY(10px);
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: 16px;
  padding: 32px;
  box-shadow: var(--shadow-lg);
  opacity: 0;
  visibility: hidden;
  transition: all 0.2s var(--ease);
  min-width: 600px;
}
.nav-dropdown-wrapper:hover .mega-menu {
  opacity: 1;
  visibility: visible;
  transform: translateX(-50%) translateY(0);
}
.mega-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 32px;
}
.mega-col {
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.mega-col-title {
  font-size: 13px;
  font-weight: 700;
  color: var(--text-tertiary);
  letter-spacing: 0.5px;
  margin-bottom: 8px;
  font-family: 'Outfit', sans-serif;
  text-transform: uppercase;
}
.mega-menu a {
  font-size: 15px;
  font-weight: 600;
  color: var(--text-primary);
  transition: color 0.2s;
  display: inline-flex;
  align-items: center;
}
.mega-menu a:hover {
  color: var(--accent);
}
.mega-badge {
  background: var(--accent-tint);
  color: var(--accent-deep);
  font-size: 11px;
  padding: 2px 8px;
  border-radius: 4px;
  margin-left: 8px;
  font-weight: 700;
}
"""

css_path = r"c:\Users\user\Downloads\HOME STAEP AI\assets\css\style.css"
if os.path.exists(css_path):
    with open(css_path, 'r', encoding='utf-8') as f:
        content = f.read()
    if "/* MEGA MENU */" not in content:
        with open(css_path, 'a', encoding='utf-8') as f:
            f.write(css_append)
        print("Mega menu CSS appended.")
    else:
        print("Mega menu CSS already exists.")
