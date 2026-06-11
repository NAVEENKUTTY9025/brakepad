import os

files_to_update = [
    "about.html",
    "blog.html",
    "contact.html",
    "faq.html",
    "home2.html",
    "index.html",
    "service.html"
]

css_desktop_to_add = """
    .login-btn-secondary {
      background: transparent;
      color: var(--nav-text);
      padding: 0.6rem 1.5rem;
      border-radius: 999px;
      font-weight: 700;
      text-decoration: none;
      font-size: 0.85rem;
      transition: 0.3s;
      white-space: nowrap;
      font-family: 'Oswald', sans-serif;
      border: 2px solid rgba(255,255,255,0.2);
    }
    .login-btn-secondary:hover { border-color: var(--accent); color: var(--accent); transform: translateY(-2px); }"""

css_mobile_to_add = """
    .mobile-login-btn-secondary {
      display: inline-block;
      margin: 1rem 1.5rem;
      background: transparent;
      color: var(--nav-text);
      padding: 0.75rem 1.5rem;
      border-radius: 999px;
      border: 2px solid rgba(255,255,255,0.2);
      text-decoration: none;
      font-weight: 700;
      text-align: center;
    }"""

desktop_css_target = ".login-btn:hover { background: #E0B800; transform: translateY(-2px); box-shadow: 0 6px 20px rgba(255,212,40,0.4); }"
mobile_css_target = "    .mobile-theme-rtl {"

for filename in files_to_update:
    filepath = os.path.join("e:\\GROWW projects\\ROTAR", filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if ".login-btn-secondary {" not in content:
            content = content.replace(desktop_css_target, desktop_css_target + css_desktop_to_add)
            
        if ".mobile-login-btn-secondary {" not in content:
            content = content.replace(mobile_css_target, css_mobile_to_add[1:] + "\n" + mobile_css_target)

        content = content.replace('<a href="login.html" class="login-btn">Sign In</a>', '<a href="login.html" class="login-btn-secondary">Sign In</a>')
        content = content.replace('<a href="login.html" class="mobile-login-btn">Sign In</a>', '<a href="login.html" class="mobile-login-btn-secondary">Sign In</a>')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")
    else:
        print(f"File not found: {filepath}")
