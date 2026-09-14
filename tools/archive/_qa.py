#!/usr/bin/env python3
"""QA pass: stray bytes, favicon, 404, SEO/OG meta, cover stats, Continue button, focus styles."""
import pathlib, sys

ROOT = pathlib.Path("/home/user/AI-Course")
fails = []

def edit(path, old, new, expect=1, label=""):
    p = ROOT / path
    s = p.read_text()
    n = s.count(old)
    if n != expect:
        fails.append(f"{path} :: {label}: found {n}, expected {expect}")
        return
    p.write_text(s.replace(old, new, expect))

# 1. stray "ml>" after </html> on every page
edit("src/_foot.html", "</html>\nml>\n", "</html>\n", 1, "stray-ml")

# 2. head: SEO/OG/theme/favicon (single contiguous insert)
edit("src/_head.html", '  <title>Zero to Hero AI Course Book</title>\n',
     '  <title>Zero to Hero AI Course Book</title>\n'
     '  <meta name="description" content="Zero to Hero AI Course Book — free illustrated interactive course from Class 1 to PhD: data skills, ML, LLMs, agents, frontier GenAI, interview prep and scored exams." />\n'
     '  <meta name="theme-color" content="#0c1b2e" />\n'
     '  <meta property="og:type" content="website" />\n'
     '  <meta property="og:title" content="Zero to Hero AI Course Book" />\n'
     '  <meta property="og:description" content="Free illustrated interactive AI course: Class 1 to PhD, with diagrams, MCQs, practice labs and scored exams." />\n'
     '  <link rel="icon" href="favicon.svg" type="image/svg+xml" />\n', 1, "head-meta")

# 3. build.py: per-page og:title
edit("build.py",
     '''    title = TITLES.get(pid, pid)
    h = head.replace("<title>Zero to Hero AI Course Book</title>",
                     f"<title>{title} · Zero to Hero AI</title>", 1)''',
     '''    title = TITLES.get(pid, pid)
    h = head.replace("<title>Zero to Hero AI Course Book</title>",
                     f"<title>{title} · Zero to Hero AI</title>", 1)
    h = h.replace('<meta property="og:title" content="Zero to Hero AI Course Book" />',
                  f'<meta property="og:title" content="{title} · Zero to Hero AI" />', 1)''',
     1, "build-og")

# 4. cover: true stats + continue placeholder
edit("src/pages/cover.html",
     '''            <div class="stat"><b>70+</b><span>practice questions</span></div>
            <div class="stat"><b>45</b><span>final exam questions</span></div>''',
     '''            <div class="stat"><b>190+</b><span>practice questions</span></div>
            <div class="stat"><b>61</b><span>final exam questions</span></div>''',
     1, "cover-stats")
edit("src/pages/cover.html", "          <h3>Jump in by level</h3>",
     '          <div id="continueWrap"></div>\n          <h3>Jump in by level</h3>', 1, "cover-continue")

# 5. app.js: Continue-where-you-left-off
edit("js/app.js", 'window.addEventListener("DOMContentLoaded", () => {\n  const hash',
     '''function renderContinue() {
  const w = document.getElementById("continueWrap");
  if (!w) return;
  const st = storage.get();
  const last = st.page;
  if (!last || last === "cover" || !PAGES.includes(last)) return;
  const b = document.createElement("button");
  b.className = "btn navy";
  b.textContent = "Continue: " + (TITLES[last] || last) + " →";
  b.addEventListener("click", () => go(last));
  w.appendChild(b);
}
window.addEventListener("DOMContentLoaded", () => {
  const hash''', 1, "app-fn")
edit("js/app.js", "  markSeen(currentPage());\n  renderInterview();",
     "  markSeen(currentPage());\n  renderContinue();\n  renderInterview();", 1, "app-hook")

# 6. css: keyboard focus visibility
cp = ROOT / "css/style.css"
cs = cp.read_text()
add = "\nbutton:focus-visible, a:focus-visible { outline: 3px solid #0f766e; outline-offset: 2px; }\n#continueWrap .btn { font-size: 17px; margin-bottom: 6px; }\n"
if "focus-visible" in cs:
    fails.append("css :: focus-visible already present")
else:
    cp.write_text(cs + add)

# 7. new files
(ROOT / "favicon.svg").write_text(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
    '<rect width="64" height="64" rx="14" fill="#0c1b2e"/>'
    '<circle cx="47" cy="17" r="6" fill="#5eead4"/>'
    '<text x="27" y="43" font-size="27" text-anchor="middle" fill="#faf7f2" '
    'font-family="sans-serif" font-weight="bold">AI</text></svg>\n')
(ROOT / "404.html").write_text(
    '<!DOCTYPE html>\n<html lang="en">\n<head>\n'
    '  <meta charset="UTF-8" />\n'
    '  <meta name="viewport" content="width=device-width, initial-scale=1" />\n'
    '  <title>Page not found · Zero to Hero AI</title>\n'
    '  <meta name="description" content="That page drifted off into latent space. Head back to the Zero to Hero AI Course Book." />\n'
    '  <link rel="icon" href="favicon.svg" type="image/svg+xml" />\n'
    '  <link rel="stylesheet" href="css/style.css" />\n</head>\n<body>\n'
    '  <main class="main" style="margin:12vh auto;max-width:640px;text-align:center;padding:0 20px">\n'
    '    <div class="kicker">404 · lost in latent space</div>\n'
    '    <h2>That page doesn&apos;t exist (yet)</h2>\n'
    '    <p class="lede">Head back to the cover and keep learning.</p>\n'
    '    <p><button class="btn navy" onclick="location.href=\'index.html\'">← Back to the book</button></p>\n'
    '  </main>\n</body>\n</html>\n')

print("FAILURES:" if fails else "QA OK")
for f in fails:
    print(" ", f)
sys.exit(1 if fails else 0)
