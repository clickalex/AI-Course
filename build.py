#!/usr/bin/env python3
"""Build the static site: src/pages/<id>.html + templates -> one .html file per page.

Usage:  python3 build.py
Single sources of truth: PAGES + TITLES in js/app.js, sidebar in src/_sidebar.html.
Output: index.html (cover) + <id>.html for every other page. All committed for Pages.
"""
import re, pathlib, sys

ROOT = pathlib.Path("/home/user/AI-Course")
fails = []

app = (ROOT / "js" / "app.js").read_text()
PAGES = [p.strip() for p in
         re.search(r'const PAGES = \[(.*?)\];', app, re.S).group(1)
         .replace('"', '').replace('\n', '').split(',') if p.strip()]
TITLES = dict(re.findall(r'^  (\w+): "((?:[^"\\]|\\.)*)",?\s*$', app, re.M))

head = (ROOT / "src" / "_head.html").read_text()
sidebar_tpl = (ROOT / "src" / "_sidebar.html").read_text()
mainopen = (ROOT / "src" / "_mainopen.html").read_text()
foot = (ROOT / "src" / "_foot.html").read_text()

# sidebar order must equal PAGES
toc = re.findall(r'toc-item" data-go="([^"]+)"', sidebar_tpl)
if toc != PAGES:
    fails.append(f"sidebar order != PAGES (sidebar {len(toc)}, PAGES {len(PAGES)})")
    for a, b in zip(toc, PAGES):
        if a != b:
            fails.append(f"  first diff: sidebar={a} PAGES={b}")
            break

missing_t = [p for p in PAGES if p not in TITLES]
if missing_t:
    fails.append(f"TITLES missing: {missing_t}")

built = []
for pid in PAGES:
    frag = ROOT / "src" / "pages" / f"{pid}.html"
    if not frag.exists():
        fails.append(f"missing fragment: {frag}")
        continue
    art = frag.read_text()
    art = art.replace('class="page active"', 'class="page"')
    art = art.replace('class="page"', 'class="page active"', 1)
    sb = sidebar_tpl.replace(
        f'<button class="toc-item" data-go="{pid}">',
        f'<button class="toc-item active" data-go="{pid}">', 1)
    if sb.count('toc-item active') != 1:
        fails.append(f"sidebar active mark failed for {pid}")
        continue
    title = TITLES.get(pid, pid)
    h = head.replace("<title>Zero to Hero AI Course Book</title>",
                     f"<title>{title} · Zero to Hero AI</title>", 1)
    out = h + sb + "\n" + mainopen + art + "\n" + foot
    dest = ROOT / ("index.html" if pid == "cover" else f"{pid}.html")
    dest.write_text(out)
    built.append(dest.name)

# validate all data-go targets resolve
for name in built:
    t = (ROOT / name).read_text()
    for g in set(re.findall(r'data-go="([^"]+)"', t)):
        if g not in PAGES:
            fails.append(f"{name}: dead data-go={g}")

print(f"built {len(built)} files")
if fails:
    print("FAILURES:")
    for f in fails:
        print(" ", f)
    sys.exit(1)
print("BUILD OK")
