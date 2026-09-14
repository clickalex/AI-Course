#!/usr/bin/env python3
"""Add SVG snapshot figures (code editors, terminals, browsers, DB grids) to ch67-ch74."""
import pathlib, sys

ROOT = pathlib.Path("/home/user/AI-Course")
fails = []

MONO = 'font-family="JetBrains Mono, monospace"'
DOTS = ('<circle cx="32" cy="29" r="6" fill="#f87171"/>'
        '<circle cx="50" cy="29" r="6" fill="#fbbf24"/>'
        '<circle cx="68" cy="29" r="6" fill="#34d399"/>')

def window_top(title, w=620, x=10):
    return (f'<rect x="{x}" y="10" width="{w}" height="%%H%%" rx="10" fill="#0f172a" stroke="#334155"/>'
            + DOTS.replace('cx="32"', f'cx="{x+22}"').replace('cx="50"', f'cx="{x+40}"').replace('cx="68"', f'cx="{x+58}"')
            + f'<text x="{x+w//2}" y="33" text-anchor="middle" {MONO} font-size="12" fill="#94a3b8">{title}</text>'
            + f'<line x1="{x}" y1="46" x2="{x+w}" y2="46" stroke="#1e293b"/>')

def code_line(n, y, num, spans, x=64):
    inner = "".join(f'<tspan fill="{c}">{t}</tspan>' for c, t in spans)
    return (f'<text x="30" y="{y}" {MONO} font-size="12" fill="#475569">{num}</text>'
            f'<text x="{x}" y="{y}" {MONO} font-size="12" fill="#e2e8f0">{inner}</text>')

def term_line(y, spans, x=34):
    inner = "".join(f'<tspan fill="{c}">{t}</tspan>' for c, t in spans)
    return f'<text x="{x}" y="{y}" {MONO} font-size="12" fill="#e2e8f0">{inner}</text>'

KW, FN, ST, CM, PL, GN, PR = "#5eead4", "#7dd3fc", "#fcd34d", "#64748b", "#e2e8f0", "#34d399", "#5eead4"

def insert(path, anchor, figure_html, label):
    p = ROOT / path
    s = p.read_text()
    if s.count(anchor) != 1:
        fails.append(f"{path} :: {label}: anchor found {s.count(anchor)}x, expected 1")
        return
    p.write_text(s.replace(anchor, anchor + figure_html, 1))

def fig(svg, caption):
    return f'\n          <div class="diagram">\n            <svg viewBox="0 0 640 {svg[1]}" width="640" height="{svg[1]}">\n{svg[0]}            </svg>\n            <div class="diagram-title">{caption}</div>\n          </div>'

# ---------- ch67: editor with binary search + run output ----------
s67 = [window_top("binary_search.py — editor").replace("%%H%%", "280")]
lines67 = [
    (1, [(KW, "def "), (FN, "binary_search"), (PL, "(a, x):")]),
    (2, [(PL, "    lo, hi = 0, len(a) - 1")]),
    (3, [(KW, "    while "), (PL, "lo &lt;= hi:")]),
    (4, [(PL, "        mid = (lo + hi) // 2")]),
    (5, [(KW, "        if "), (PL, "a[mid] == x:")]),
    (6, [(KW, "            return "), (PL, "mid")]),
    (7, [(CM, "        # ... (halve the range)")]),
    (8, [(PL, "result = "), (FN, "binary_search"), (PL, "([1,3,5,7], 5)")]),
    (9, [(FN, "print"), (PL, "(result)  "), (CM, "# → 2")]),
]
for i, (n, sp) in enumerate(lines67):
    s67.append("              " + code_line(n, 70 + 20 * i, n, sp))
s67.append('              <line x1="10" y1="258" x2="630" y2="258" stroke="#1e293b"/>')
s67.append("              " + term_line(278, [(PR, "▶ run  "), (GN, '"2"  ·  5 steps, not 1,000,000  ✓"'.replace('"', ""))]))
SVG67 = ("\n".join(s67), 300)

# ---------- ch68: editor + terminal stacked ----------
s68 = [window_top("fib.py — editor").replace("%%H%%", "168")]
lines68 = [
    (1, [(ST, "@lru_cache"), (PL, "(maxsize=None)")]),
    (2, [(KW, "def "), (FN, "fib"), (PL, "(n):")]),
    (3, [(KW, "    if "), (PL, "n &lt; 2:  "), (KW, "return "), (PL, "n")]),
    (4, [(KW, "    return "), (FN, "fib"), (PL, "(n-1) + "), (FN, "fib"), (PL, "(n-2)")]),
]
for i, (n, sp) in enumerate(lines68):
    s68.append("              " + code_line(n, 70 + 20 * i, n, sp))
s68.append(window_top("terminal — zsh", x=10).replace("%%H%%", "86").replace('y="10"', 'y="188"')
           .replace('cy="29"', 'cy="207"').replace('y="33"', 'y="211"').replace('y1="46" y2="46"', 'y="224"')
           .replace('<line x1="10" y1="46" x2="630" y2="46"', '<line x1="10" y1="224" x2="630" y2="224"'))
s68.append("              " + term_line(248, [(PR, "$ "), (PL, "python fib.py")]).replace('x="34"', 'x="34"'))
s68.append("              " + term_line(268, [(GN, "fib(30) = 832040"), (PL, "   (0.0003s — cached, not 2³⁰ calls)")]))
SVG68 = ("\n".join(s68), 296)

# ---------- ch69: browser with FastAPI docs ----------
s69 = [window_top("127.0.0.1:8000/docs — Thali API", w=620).replace("%%H%%", "232")]
s69.append('              <rect x="150" y="58" width="340" height="30" rx="15" fill="#1e293b"/>'
           '<text x="320" y="78" text-anchor="middle" font-family="Source Sans 3" font-size="12" fill="#94a3b8">🔒 127.0.0.1:8000/docs</text>')
s69.append('              <rect x="34" y="102" width="52" height="24" rx="6" fill="#166534"/>'
           '<text x="60" y="119" text-anchor="middle" font-family="Source Sans 3" font-size="12" fill="#fff">POST</text>'
           f'<text x="96" y="119" {MONO} font-size="13" fill="#e2e8f0">/predict</text>'
           '<rect x="470" y="100" width="136" height="28" rx="8" fill="#0f766e"/>'
           '<text x="538" y="119" text-anchor="middle" font-family="Source Sans 3" font-size="12" fill="#fff">Try it out ▸</text>')
s69.append('              <rect x="34" y="140" width="572" height="66" rx="8" fill="#020617" stroke="#1e293b"/>')
s69.append("              " + term_line(164, [(GN, "200 OK  "), (PL, '{ "label": "positive" }')]))
s69.append("              " + term_line(188, [(CM, "Request took 84 ms · model loaded once at startup")]))
SVG69 = ("\n".join(s69), 252)

# ---------- ch70: terminal with tmux + nvidia-smi ----------
s70 = [window_top("user@gpu: ~/project — tmux").replace("%%H%%", "216")]
s70.append("              " + term_line(70, [(PR, "$ "), (PL, "tmux new -s train")]))
s70.append("              " + term_line(90, [(CM, "[detached — survives closed laptops]")]))
s70.append("              " + term_line(110, [(PR, "$ "), (PL, "nvidia-smi --query-gpu=name,memory.used --format=csv")]))
s70.append("              " + term_line(130, [(PL, "name, memory.used [MiB]")]))
s70.append("              " + term_line(150, [(GN, "RTX 4090, 8421 MiB / 24576 MiB")]))
s70.append("              " + term_line(170, [(PR, "$ "), (PL, "tail -f logs/train.log  "), (CM, "# loss falling ✓")]))
s70.append('              <rect x="10" y="188" width="620" height="26" rx="0" fill="#166534"/>'
           '<text x="24" y="206" font-family="JetBrains Mono, monospace" font-size="12" fill="#fff">[train]  0:bash*  1:logs  ·  GPU 34%  ·  12:04</text>')
SVG70 = ("\n".join(s70), 234)

# ---------- ch71: SQL editor + results grid ----------
s71 = [window_top("DuckDB — refunds").replace("%%H%%", "232")]
s71.append("              " + term_line(68, [(CM, "-- top-3 refunds per city, ranked")]))
s71.append("              " + term_line(88, [(KW, "SELECT "), (PL, "city, month, revenue, "), (FN, "RANK"), (PL, "() OVER (...)")]))
s71.append('              <rect x="34" y="102" width="572" height="26" fill="#1e293b"/>'
           '<text x="48" y="120" font-family="JetBrains Mono, monospace" font-size="12" fill="#94a3b8">city     month      revenue   rev_rank</text>')
rows71 = [("Jaipur", "2026-07", "₹48,200", "1"), ("Jaipur", "2026-07", "₹41,900", "2"), ("Indore", "2026-07", "₹52,400", "1")]
for i, (c, m, r, k) in enumerate(rows71):
    y = 146 + 24 * i
    s71.append(f'              <line x1="34" y1="{y+8}" x2="606" y2="{y+8}" stroke="#1e293b"/>'
               f'<text x="48" y="{y}" {MONO} font-size="12" fill="#e2e8f0">{c:<9}{m}  {r:>9}   {k}</text>')
s71.append("              " + term_line(232, [(GN, "3 rows"), (PL, " · 41 ms  "), (CM, "(indexed: city, month, amount)")]))
SVG71 = ("\n".join(s71), 252)

# ---------- ch72: psql + redis-cli side by side ----------
s72 = [window_top("psql — docs", w=300, x=10).replace("%%H%%", "190")]
s72.append("              " + term_line(70, [(KW, "SELECT "), (PL, "id, dist")], x=24))
s72.append("              " + term_line(90, [(KW, "FROM "), (PL, "docs "), (KW, "WHERE "), (PL, "tenant=7")], x=24))
s72.append("              " + term_line(110, [(KW, "ORDER BY "), (PL, "emb &lt;-&gt; $1 "), (KW, "LIMIT "), (PL, "2;")], x=24))
s72.append("              " + term_line(140, [(GN, "101"), (PL, " | refund rules  | 0.18")], x=24))
s72.append("              " + term_line(160, [(GN, "207"), (PL, " | return window | 0.24")], x=24))
s72.append("              " + term_line(184, [(CM, "(2 rows · tenant-scoped ✓)")], x=24))
s72.append(window_top("redis-cli", w=300, x=330).replace("%%H%%", "190"))
s72.append("              " + term_line(70, [(PR, "&gt; "), (PL, "GET llm:9f2c")], x=344))
s72.append("              " + term_line(100, [(ST, '"label: positive"'), (GN, "  ← hit!")], x=344))
s72.append("              " + term_line(130, [(PL, "0.4 ms · saved one LLM call")], x=344))
s72.append("              " + term_line(160, [(PR, "&gt; "), (PL, "TTL llm:9f2c")], x=344))
s72.append("              " + term_line(184, [(GN, "3120"), (CM, "  (expires in 52 min)")], x=344))
SVG72 = ("\n".join(s72), 210)

# ---------- ch73: editor + pytest ----------
s73 = [window_top("topk.py — editor").replace("%%H%%", "148")]
lines73 = [
    (1, [(KW, "import "), (PL, "heapq")]),
    (2, [(KW, "def "), (FN, "top_k"), (PL, "(stream, k):")]),
    (3, [(PL, "    h = []  "), (CM, "# bounded min-heap")]),
    (4, [(KW, "    for "), (PL, "x "), (KW, "in "), (PL, "stream: push, pop if big")]),
]
for i, (n, sp) in enumerate(lines73):
    s73.append("              " + code_line(n, 70 + 20 * i, n, sp))
s73.append(window_top("terminal — pytest", x=10).replace("%%H%%", "86").replace('y="10"', 'y="168"')
           .replace('cy="29"', 'cy="187"').replace('y="33"', 'y="191"')
           .replace('<line x1="10" y1="46" x2="630" y2="46"', '<line x1="10" y1="204" x2="630" y2="204"'))
s73.append("              " + term_line(228, [(PR, "$ "), (PL, "pytest -q")]))
s73.append("              " + term_line(248, [(GN, "....  4 passed in 0.02s ✓")]))
SVG73 = ("\n".join(s73), 274)

# ---------- ch74: kubectl terminal ----------
s74 = [window_top("user@cloud: ~/ml — kubectl").replace("%%H%%", "216")]
s74.append("              " + term_line(70, [(PR, "$ "), (PL, "kubectl get pods")]))
s74.append("              " + term_line(94, [(CM, "NAME            READY   STATUS    GPU")]))
s74.append("              " + term_line(114, [(PL, "api-7d9f-2x4qj  1/1     Running   1")]))
s74.append("              " + term_line(134, [(PL, "train-bert-v3   0/1     Running   1")]))
s74.append("              " + term_line(158, [(PR, "$ "), (PL, "kubectl logs -f job/train-bert-v3")]))
s74.append("              " + term_line(178, [(GN, "epoch 3/10  loss=0.41  lr=2e-5  ✓ falling")]))
s74.append("              " + term_line(198, [(CM, "# quota used: 2/4 team GPUs")]))
SVG74 = ("\n".join(s74), 236)

insert("src/pages/ch67.html",
       "        else:\n            hi = mid - 1\n    return -1</code></pre>",
       fig(SVG67, "Snapshot 67.1 — Binary search in the editor: 5 probes to find 5 in a sorted list. The run line shows the payoff — log n, not n."),
       "ch67-snap")
insert("src/pages/ch68.html",
       "    return fib(n - 1) + fib(n - 2)   # shrink step</code></pre>",
       fig(SVG68, "Snapshot 68.1 — One decorator (@lru_cache) turns an exponential disaster into instant answers. The terminal proves it: fib(30) in under a millisecond."),
       "ch68-snap")
insert("src/pages/ch69.html",
       """-d '{"text": "loved the thali, will return!"}'</code></pre>""",
       fig(SVG69, "Snapshot 69.1 — FastAPI’s free Swagger UI at /docs: every endpoint documented and clickable. Green POST, “Try it out”, instant 200 response."),
       "ch69-snap")
insert("src/pages/ch70.html",
       'find . -name "*.ckpt" -size +1G   # where did my disk go?</code></pre>',
       fig(SVG70, "Snapshot 70.1 — A tmux session that outlives your Wi-Fi, nvidia-smi showing a healthy GPU, and logs being followed live. The green bar is tmux."),
       "ch70-snap")
insert("src/pages/ch71.html",
       "FROM monthly;</code></pre>",
       fig(SVG71, "Snapshot 71.1 — Window-function results: per-city ranks computed without collapsing a single row. 3 rows back in 41 ms on an indexed table."),
       "ch71-snap")
insert("src/pages/ch72.html",
       "LIMIT 5;</code></pre>",
       fig(SVG72, "Snapshot 72.1 — Left: tenant-scoped vector search in psql (similarity + filters together). Right: the same question answered from Redis in 0.4 ms — one LLM call saved."),
       "ch72-snap")
insert("src/pages/ch73.html",
       "biggest = -heapq.heappop(h)          # 9</code></pre>",
       fig(SVG73, "Snapshot 73.1 — Top-K via a bounded heap, then pytest confirming 4 passing tests in 0.02 s. Small code, fast proof."),
       "ch73-snap")
insert("src/pages/ch74.html",
       "kubectl top pods                          # CPU/RAM per pod</code></pre>",
       fig(SVG74, "Snapshot 74.1 — kubectl get pods: API serving on 1 GPU, training running on another. Logs stream with -f; the quota comment keeps teams honest."),
       "ch74-snap")

print("FAILURES:" if fails else "ALL OK")
for f in fails:
    print(" ", f)
sys.exit(1 if fails else 0)
