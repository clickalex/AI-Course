#!/usr/bin/env python3
"""One-time split: index.html -> src/_head.html, src/_sidebar.html, src/_mainopen.html,
src/pages/<id>.html, src/_foot.html + js/interview-data.js (interview practices extracted)."""
import re, json, pathlib

ROOT = pathlib.Path("/home/user/AI-Course")
s = (ROOT / "index.html").read_text()
(ROOT / "src" / "pages").mkdir(parents=True, exist_ok=True)

# --- split shell ---
app_open = '<div class="app">\n'
aside_open = '<aside class="sidebar" id="sidebar">'
aside_close = '</aside>'
main_open = '<main class="main">'

i_app = s.index(app_open) + len(app_open)
i_aside = s.index(aside_open)
i_aside_end = s.index(aside_close) + len(aside_close)
i_main = s.index(main_open)
i_mainline_end = s.index("\n", i_main) + 1
# print-head div follows main open
m_ph = re.search(r'<div class="print-head">.*?</div>\n', s[i_mainline_end:])
assert m_ph, "print-head not found"
i_content = i_mainline_end + m_ph.end()
i_main_close = s.index("</main>")

head = s[:i_app]
sidebar = s[i_aside:i_aside_end]
mainopen = s[i_main:i_content]
body = s[i_content:i_main_close]
foot = s[i_main_close:]

(ROOT / "src" / "_head.html").write_text(head)
(ROOT / "src" / "_sidebar.html").write_text(sidebar)
(ROOT / "src" / "_mainopen.html").write_text(mainopen)
(ROOT / "src" / "_foot.html").write_text(foot)

# --- articles ---
arts = re.findall(r'(<article class="page[^"]*" id="([^"]+)">.*?</article>)', body, re.S)
print("articles found:", len(arts))
ids = []
for html, aid in arts:
    ids.append(aid)
    (ROOT / "src" / "pages" / f"{aid}.html").write_text(html.strip() + "\n")
assert len(ids) == len(set(ids)), "dup ids!"
print("pages written:", len(ids))

# --- interview: extract practices to JS data, leave empty shells ---
iv_path = ROOT / "src" / "pages" / "interview.html"
iv = iv_path.read_text()
prac_re = re.compile(
    r'<div class="practice" data-pid="(iq\d+)"><p class="q">(.*?)</p>\s*'
    r'<button class="btn" onclick="revealAnswer\(this\)">.*?</button>\s*'
    r'<div class="answer">(.*?)</div>\s*'
    r'<div class="self-mark">.*?</div>\s*</div>', re.S)
# category = nearest preceding <h3>
h3s = [(m.start(), m.group(1)) for m in re.finditer(r'<h3>(.*?)</h3>', iv)]
practices = []
for m in prac_re.finditer(iv):
    cat = "General"
    for pos, txt in h3s:
        if pos < m.start():
            cat = txt
    practices.append({"pid": m.group(1), "q": m.group(2).strip(),
                      "ans": m.group(3).strip(), "cat": cat})
print("interview practices:", len(practices))
assert len(practices) == 24, f"expected 24, got {len(practices)}"
(ROOT / "js" / "interview-data.js").write_text(
    "/* Interview Q&A bank data — shared by interview.html (render) and mock.js (draws). */\n"
    "const INTERVIEW = " + json.dumps(practices, ensure_ascii=False, indent=1) + ";\n")
iv2, n = prac_re.subn("", iv)
assert n == 24
# number the emptied practice-block shells
shells = iv2.count('<div class="practice-block">')
assert shells == 6, f"expected 6 shells, got {shells}"
for k in range(6):
    iv2 = iv2.replace('<div class="practice-block">', f'<div class="practice-block" id="iqCat{k}">', 1)
iv_path.write_text(iv2)
print("interview shells: 6, data written to js/interview-data.js")
print("SPLIT DONE")
