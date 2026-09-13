#!/usr/bin/env python3
"""Add SVG snapshot figures to ch5, ch30-33, ch40, ch44, ch46 (batch 2)."""
import pathlib, sys

ROOT = pathlib.Path("/home/user/AI-Course")
fails = []

MONO = 'font-family="JetBrains Mono, monospace"'
SANS = 'font-family="Source Sans 3"'

def dots(x):
    return (f'<circle cx="{x+22}" cy="29" r="6" fill="#f87171"/>'
            f'<circle cx="{x+40}" cy="29" r="6" fill="#fbbf24"/>'
            f'<circle cx="{x+58}" cy="29" r="6" fill="#34d399"/>')

def window_top(title, w=620, x=10, y=10, h=200, bg="#0f172a", tfill="#94a3b8"):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="#334155"/>'
            + dots(x).replace('cy="29"', f'cy="{y+19}"')
            + f'<text x="{x+w//2}" y="{y+23}" text-anchor="middle" {MONO} font-size="12" fill="{tfill}">{title}</text>'
            + f'<line x1="{x}" y1="{y+36}" x2="{x+w}" y2="{y+36}" stroke="#1e293b"/>')

def tline(y, spans, x=34, fs=12):
    inner = "".join(f'<tspan fill="{c}">{t}</tspan>' for c, t in spans)
    return f'<text x="{x}" y="{y}" {MONO} font-size="{fs}" fill="#e2e8f0">{inner}</text>'

def cline(n, y, num, spans, x=64):
    inner = "".join(f'<tspan fill="{c}">{t}</tspan>' for c, t in spans)
    return (f'<text x="30" y="{y}" {MONO} font-size="12" fill="#475569">{num}</text>'
            f'<text x="{x}" y="{y}" {MONO} font-size="12" fill="#e2e8f0">{inner}</text>')

KW, FN, ST, CM, PL, GN, PR = "#5eead4", "#7dd3fc", "#fcd34d", "#64748b", "#e2e8f0", "#34d399", "#5eead4"

def insert(path, anchor, figure_html, label):
    p = ROOT / path
    s = p.read_text()
    if s.count(anchor) != 1:
        fails.append(f"{path} :: {label}: anchor found {s.count(anchor)}x, expected 1")
        return
    p.write_text(s.replace(anchor, anchor + figure_html, 1))

def fig(svg_inner, h, caption):
    return (f'\n          <div class="diagram">\n            <svg viewBox="0 0 640 {h}" width="640" height="{h}">\n'
            + svg_inner + '            </svg>\n'
            + f'            <div class="diagram-title">{caption}</div>\n          </div>')

# ---------- ch5: sklearn editor + accuracy ----------
s5 = [window_top("sklearn_digits.py — editor", h=168)]
for i, (n, sp) in enumerate([
    (1, [(KW, "from "), (PL, "sklearn.linear_model "), (KW, "import "), (PL, "LogisticRegression")]),
    (2, [(PL, "Xtr, Xte, ytr, yte = "), (FN, "train_test_split"), (PL, "(X, y, test_size=0.2)")]),
    (3, [(PL, "model = "), (FN, "LogisticRegression"), (PL, "(max_iter=1000)")]),
    (4, [(PL, "model."), (FN, "fit"), (PL, "(Xtr, ytr)  "), (CM, "# learn")]),
    (5, [(PL, "pred = model."), (FN, "predict"), (PL, "(Xte)")]),
]):
    s5.append("              " + cline(n, 70 + 20 * i, n, sp))
s5.append(window_top("terminal", y=188, h=66))
s5.append("              " + tline(232, [(GN, "Accuracy: 0.94 ✓"), (CM, "   (stratified split, seed 42 — reproducible)")]))
SVG5 = ("\n".join(s5), 274)

# ---------- ch30: venv setup terminal ----------
s30 = [window_top("user@laptop: ~/thali — setup", h=196)]
s30.append("              " + tline(70, [(PR, "$ "), (PL, "python -m venv .venv &amp;&amp; source .venv/bin/activate")]))
s30.append("              " + tline(90, [(PR, "$ "), (PL, "pip install -r requirements.txt")]))
s30.append("              " + tline(110, [(GN, "✓ "), (PL, "numpy pandas scikit-learn matplotlib (4 pinned)")]))
s30.append("              " + tline(130, [(PR, "$ "), (PL, "jupyter nbconvert --execute analysis.ipynb --to notebook")]))
s30.append("              " + tline(150, [(GN, "All 18 cells ran top-to-bottom ✓"), (CM, "  (no luck-based ordering)")]))
s30.append("              " + tline(170, [(CM, "# system python untouched — one project, one world")]))
SVG30 = ("\n".join(s30), 216)

# ---------- ch31: light spreadsheet snapshot ----------
s31 = [window_top("Customers.xlsx — Excel", h=252, bg="#ffffff", tfill="#475569")]
s31.append('              <text x="34" y="78" font-family="Georgia, serif" font-style="italic" font-size="14" fill="#64748b">fx</text>'
           '<rect x="58" y="60" width="548" height="28" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>'
           f'<text x="70" y="79" {MONO} font-size="12" fill="#0c1b2e">=XLOOKUP([@ID],Customers[ID],Customers[City],"—")</text>')
gx, gy, cw, chh = 60, 104, 104, 24
cols = ["ID", "Age", "KYC", "City", "Status"]
rows = [["C-101", "24", "Yes", "Jaipur", "Eligible"],
        ["C-102", "17", "Yes", "Indore", "Review"],
        ["C-103", "31", "No", "Bhopal", "Review"]]
for j, c in enumerate(cols):
    s31.append(f'              <rect x="{gx+cw*j}" y="{gy}" width="{cw}" height="{chh}" fill="#dcfce7" stroke="#94a3b8"/>'
               f'<text x="{gx+cw*j+10}" y="{gy+17}" {MONO} font-size="12" fill="#166534">{c}</text>')
    s31.append(f'              <text x="{gx+cw*j+44}" y="{gy-8}" {MONO} font-size="11" fill="#94a3b8">{"ABCDE"[j]}</text>')
for i, r in enumerate(rows):
    for j, v in enumerate(r):
        fill = "#166534" if v == "Eligible" else "#b45309" if v == "Review" else "#0c1b2e"
        s31.append(f'              <rect x="{gx+cw*j}" y="{gy+chh*(i+1)}" width="{cw}" height="{chh}" fill="#ffffff" stroke="#e2e8f0"/>'
                   f'<text x="{gx+cw*j+10}" y="{gy+chh*(i+1)+17}" {MONO} font-size="12" fill="{fill}">{v}</text>')
    s31.append(f'              <text x="42" y="{gy+chh*(i+1)+17}" {MONO} font-size="11" fill="#94a3b8">{i+2}</text>')
s31.append("              " + tline(238, [(GN, "Table: Customers ✓"), (PL, "  "), (CM, "3 rows · Status = IF(AND(Age>=18,KYC=Yes))")]).replace('fill="#e2e8f0"', 'fill="#0c1b2e"').replace("#e2e8f0\">  ", "#64748b\">  "))
SVG31 = ("\n".join(s31), 272)

# ---------- ch32: groupby editor + DataFrame output ----------
s32 = [window_top("monthly_sales.py — editor", h=128)]
for i, (n, sp) in enumerate([
    (1, [(PL, "monthly = (df."), (FN, "assign"), (PL, "(ym=df["), (ST, '"date"'), (PL, "].dt.to_period("), (ST, '"M"'), (PL, ")))")]),
    (2, [(PL, "             ."), (FN, "groupby"), (PL, "(["), (ST, '"region","ym"'), (PL, "])["), (ST, '"amount"'), (PL, "]")]),
    (3, [(PL, "             ."), (FN, "agg"), (PL, "(total="), (ST, '"sum"'), (PL, ", orders="), (ST, '"count"'), (PL, ")))")]),
]):
    s32.append("              " + cline(n, 70 + 20 * i, n, sp))
s32.append(window_top("output — monthly.head()", y=148, h=106))
s32.append("              " + tline(192, [(CM, "  region    ym      total    orders")]))
s32.append("              " + tline(212, [(PL, "0 West   2026-06   812400    1210")]))
s32.append("              " + tline(232, [(GN, "✓ "), (PL, "one row per group — no loops harmed")]))
SVG32 = ("\n".join(s32), 274)

# ---------- ch33: LEFT JOIN psql ----------
s33 = [window_top("psql — shop", h=212)]
s33.append("              " + tline(70, [(KW, "SELECT "), (PL, "c.customer_id, "), (FN, "COALESCE"), (PL, "("), (FN, "SUM"), (PL, "(o.amount),0)")]))
s33.append("              " + tline(90, [(KW, "FROM "), (PL, "customers c "), (KW, "LEFT JOIN "), (PL, "orders o "), (KW, "USING "), (PL, "(customer_id)")]))
s33.append('              <rect x="34" y="104" width="572" height="24" fill="#1e293b"/>'
           f'<text x="48" y="121" {MONO} font-size="12" fill="#94a3b8">customer_id  city     total</text>')
for i, (r, hot) in enumerate([("C-101       Jaipur   48200", False), ("C-102       Indore   41900", False), ("C-103       Bhopal       0", True)]):
    y = 147 + 24 * i
    s33.append(f'              <line x1="34" y1="{y+7}" x2="606" y2="{y+7}" stroke="#1e293b"/>'
               f'<text x="48" y="{y}" {MONO} font-size="12" fill="#e2e8f0">{r}</text>'
               + (f'<text x="470" y="{y}" {MONO} font-size="12" fill="#34d399">← kept by LEFT JOIN</text>' if hot else ''))
SVG33 = ("\n".join(s33), 232)

# ---------- ch40: API pull terminal ----------
s40 = [window_top("user@laptop: ~/shop — pull", h=196)]
s40.append("              " + tline(70, [(PR, "$ "), (PL, "curl 'api.shop.com/v1/orders?cursor=abc'")]))
s40.append("              " + tline(90, [(PL, '{"orders": [{"id": 881}],  '), (ST, '"next_cursor": "def456"'), (PL, "}")]))
s40.append("              " + tline(110, [(GN, "200 OK"), (PL, " → saved "), (FN, "raw/orders_p3.jsonl"), (CM, "  (raw first!)")]))
s40.append("              " + tline(130, [(PR, "$ "), (PL, "curl 'api.shop.com/v1/orders?cursor=def'")]))
s40.append("              " + tline(150, [(ST, "429 Too Many Requests"), (PL, " → sleep 2s, retry ✓")]))
s40.append("              " + tline(170, [(CM, "# polite: 1 rps, backoff, robots.txt respected")]))
SVG40 = ("\n".join(s40), 216)

# ---------- ch44: Dockerfile + docker run split ----------
s44 = [window_top("Dockerfile", w=300, x=10, h=190)]
for i, (n, sp) in enumerate([
    (1, [(KW, "FROM "), (PL, "python:3.12-slim")]),
    (2, [(KW, "WORKDIR "), (PL, "/app")]),
    (3, [(KW, "RUN "), (PL, "pip install -r req.txt")]),
    (4, [(KW, "USER "), (PL, "appuser  "), (CM, "# non-root")]),
    (5, [(KW, "CMD "), (PL, '["uvicorn", "app:api"]')]),
]):
    s44.append("              " + cline(n, 70 + 20 * i, n, sp, x=44).replace('x="30"', 'x="24"'))
s44.append(window_top("terminal — docker", w=300, x=330, h=190))
s44.append("              " + tline(70, [(PR, "$ "), (PL, "docker build -t thali:1.4 .")], x=344))
s44.append("              " + tline(90, [(GN, "✓ "), (PL, "312 MB · pinned · non-root")], x=344))
s44.append("              " + tline(120, [(PR, "$ "), (PL, "docker run --gpus all thali:1.4")], x=344))
s44.append("              " + tline(140, [(GN, "API up on :8000 ✓"), (CM, "  (cloud VM)")], x=344))
s44.append("              " + tline(170, [(CM, "# auto-shutdown 22:00 — GPUs sleep")], x=344))
SVG44 = ("\n".join(s44), 210)

# ---------- ch46: chat template + generation ----------
s46 = [window_top("try_qwen.py — editor", h=128)]
for i, (n, sp) in enumerate([
    (1, [(PL, "msgs = [{"), (ST, '"role": "user"'), (PL, ", "), (ST, '"content": "Summarise…"'), (PL, "}]")]),
    (2, [(PL, "ids = tok."), (FN, "apply_chat_template"), (PL, "(msgs)  "), (CM, "# template!")]),
    (3, [(PL, "out = model."), (FN, "generate"), (PL, "(ids, max_new_tokens=40)")]),
]):
    s46.append("              " + cline(n, 70 + 20 * i, n, sp))
s46.append(window_top("output — generate", y=148, h=86))
s46.append("              " + tline(192, [(GN, ">> "), (PL, "Refunds spiked 3x after the sale; top cause: size swaps.")]))
s46.append("              " + tline(212, [(CM, "40 tokens · temp 0.3 — now evaluate before serving (Ch 61)")]))
SVG46 = ("\n".join(s46), 254)

insert("src/pages/ch5.html", "print(accuracy_score(y_test, pred))</code></pre>",
       fig(*SVG5, "Snapshot 5.1 — The scikit-learn five-liner: split, fit, predict, score. Reproducible seed, stratified split, honest 0.94."),
       "ch5-snap")
insert("src/pages/ch30.html", "matplotlib==3.8.4</code></pre>",
       fig(*SVG30, "Snapshot 30.1 — Professional setup in four commands: isolated venv, pinned deps, and a notebook proven to run top-to-bottom."),
       "ch30-snap")
insert("src/pages/ch31.html", '=VALUE(SUBSTITUTE([@Amt],"₹","")) // ₹1,200 → 1200 (then Format → Number)</code></pre>',
       fig(*SVG31, "Snapshot 31.1 — A real Excel Table: structured refs in the formula bar, XLOOKUP pulling cities, Status flagging Review rows for humans."),
       "ch31-snap")
insert("src/pages/ch32.html", 'print(m["customer_id"].isna().sum(), "orders with no customer match")</code></pre>',
       fig(*SVG32, "Snapshot 32.1 — Split–apply–combine in three lines: assign a month key, group by region × month, aggregate. One row per group, zero loops."),
       "ch32-snap")
insert("src/pages/ch33.html", "GROUP BY c.customer_id, c.city;</code></pre>",
       fig(*SVG33, "Snapshot 33.1 — LEFT JOIN keeps customer C-103 with total 0 instead of dropping her. COALESCE turns the NULL into an honest zero."),
       "ch33-snap")
insert("src/pages/ch40.html",
       "            <div class=\"diagram-title\">Diagram 40.1 — The polite pull loop. Raw first, parse later — APIs change field names without asking you.</div>\n          </div>",
       fig(*SVG40, "Snapshot 40.1 — The polite pull in action: page with cursors, save raw JSONL first, and back off gracefully when the API says 429."),
       "ch40-snap")
insert("src/pages/ch44.html", 'CMD ["uvicorn", "app:api", "--host", "0.0.0.0"]</code></pre>',
       fig(*SVG44, "Snapshot 44.1 — Left: a small, pinned, non-root Dockerfile. Right: built once (312 MB), run anywhere with GPUs, asleep by 22:00."),
       "ch44-snap")
insert("src/pages/ch46.html", "print(tok.decode(out[0][ids.shape[1]:]))</code></pre>",
       fig(*SVG46, "Snapshot 46.1 — Chat template applied, 40 tokens generated at temp 0.3. Next step per the chapter: evaluate, then serve."),
       "ch46-snap")

print("FAILURES:" if fails else "ALL OK")
for f in fails:
    print(" ", f)
sys.exit(1 if fails else 0)
