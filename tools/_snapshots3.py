#!/usr/bin/env python3
"""Snapshots batch 3a: sch1 + ch1-ch4 + ch6-ch29 (29 figures, data-driven)."""
import pathlib, sys

ROOT = pathlib.Path("/home/user/AI-Course")
fails = []
MONO = 'font-family="JetBrains Mono, monospace"'
KW, FN, ST, CM, PL, GN, PR, HD, AM, RD, SK = (
    "#5eead4", "#7dd3fc", "#fcd34d", "#64748b", "#e2e8f0",
    "#34d399", "#5eead4", "#94a3b8", "#fbbf24", "#f87171", "#7dd3fc")

def W(title, h, w=620, x=10, y=10):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#0f172a" stroke="#334155"/>'
        f'<circle cx="{x+22}" cy="{y+19}" r="6" fill="#f87171"/>'
        f'<circle cx="{x+40}" cy="{y+19}" r="6" fill="#fbbf24"/>'
        f'<circle cx="{x+58}" cy="{y+19}" r="6" fill="#34d399"/>'
        f'<text x="{x+w//2}" y="{y+23}" text-anchor="middle" {MONO} font-size="12" fill="#94a3b8">{title}</text>'
        f'<line x1="{x}" y1="{y+36}" x2="{x+w}" y2="{y+36}" stroke="#1e293b"/>')

def TL(y, spans, x=34, fs=12):
    inner = "".join(f'<tspan fill="{c}">{t}</tspan>' for c, t in spans)
    return f'<text x="{x}" y="{y}" {MONO} font-size="{fs}" fill="#e2e8f0">{inner}</text>'

def term(title, lines):
    h = 60 + 20 * len(lines)
    o = [W(title, h)]
    for i, sp in enumerate(lines):
        o.append("              " + TL(70 + 20 * i, sp))
    return ("\n".join(o), h + 20)

def chat(title, msgs):
    return term(title, [[(c, n + ": "), (PL, t)] for c, n, t in msgs])

def table(title, head, rows, foot=None):
    n = len(rows)
    h = 118 + 24 * n + (30 if foot else 6)
    o = [W(title, h),
         '              <rect x="34" y="58" width="572" height="26" fill="#1e293b"/>',
         "              " + TL(76, [(HD, head)])]
    for i, r in enumerate(rows):
        y = 110 + 24 * i
        o.append(f'              <line x1="34" y1="{y+8}" x2="606" y2="{y+8}" stroke="#1e293b"/>')
        o.append("              " + TL(y, [(PL, r)], x=48))
    if foot:
        o.append("              " + TL(110 + 24 * (n - 1) + 32, foot))
    return ("\n".join(o), h + 20)

def bars(title, items, foot=None):
    n = len(items)
    h = 76 + 30 * n + (30 if foot else 6)
    o = [W(title, h)]
    for i, (lab, pct, col, val) in enumerate(items):
        y = 70 + 30 * i
        w = round(280 * pct / 100)
        o.append("              " + TL(y, [(PL, lab)], x=34))
        o.append(f'              <rect x="200" y="{y-13}" width="{w}" height="16" rx="4" fill="{col}"/>')
        o.append("              " + TL(y, [(PL, val)], x=200 + w + 10))
    if foot:
        o.append("              " + TL(70 + 30 * (n - 1) + 30, foot))
    return ("\n".join(o), h + 20)

def scatter(title, pts, foot):
    o = [W(title, 216),
         '              <line x1="60" y1="190" x2="590" y2="190" stroke="#334155"/>',
         '              <line x1="60" y1="60" x2="60" y2="190" stroke="#334155"/>']
    for x, y, c in pts:
        o.append(f'              <circle cx="{60+x*520:.0f}" cy="{190-y*130:.0f}" r="6" fill="{c}"/>')
    o.append("              " + TL(212, foot))
    return ("\n".join(o), 236)

def strip(title, cells, foot=None):
    n = len(cells)
    gw = (572 - 12 * (n - 1)) // n
    h = 200 + (30 if foot else 0)
    o = [W(title, h)]
    for i, (g, lab) in enumerate(cells):
        x = 34 + i * (gw + 12)
        o.append(f'              <rect x="{x}" y="58" width="{gw}" height="110" rx="10" fill="#1e293b" stroke="#334155"/>')
        o.append(f'              <text x="{x+gw//2}" y="114" text-anchor="middle" font-size="36">{g}</text>')
        o.append(f'              <text x="{x+gw//2}" y="152" text-anchor="middle" {MONO} font-size="12" fill="#94a3b8">{lab}</text>')
    if foot:
        o.append("              " + TL(196, foot))
    return ("\n".join(o), h + 20)

def insert_before(path, anchor, figure_html, label):
    p = ROOT / path
    s = p.read_text()
    if s.count(anchor) != 1:
        fails.append(f"{path} :: {label}: anchor found {s.count(anchor)}x, expected 1")
        return
    p.write_text(s.replace(anchor, figure_html + anchor, 1))

def fig(svg, caption):
    inner, h = svg
    return (f'          <div class="diagram">\n            <svg viewBox="0 0 640 {h}" width="640" height="{h}">\n'
            + inner + '\n            </svg>\n'
            + f'            <div class="diagram-title">{caption}</div>\n          </div>\n')

QZ = '<div class="quiz-block">'

insert_before("src/pages/sch1.html", QZ, fig(chat("ai-buddy — Class 5", [
    (SK, "you", "Is my calculator AI?"),
    (GN, "ai", "No — fixed rules. AI learns patterns from examples!"),
    (SK, "you", "Is YouTube search AI?"),
    (GN, "ai", "Yes! It ranks by learning what people click. ✓")]),
    "Snapshot S1.1 — The one-line test: fixed rules (calculator) versus learned patterns (search)."), "sch1")

insert_before("src/pages/ch1.html", QZ, fig(chat("what-is-ai — ask anything", [
    (SK, "you", "Define AI in one line."),
    (GN, "ai", "Machines doing tasks that need judgment: see, read, decide."),
    (SK, "you", "One everyday example?"),
    (GN, "ai", "Spam filters — they LEARN junk from millions of mails.")]),
    "Snapshot 1.1 — AI in one line, plus the example hiding in your inbox."), "ch1")

insert_before("src/pages/ch2.html", QZ, fig(term("git log — ai-history", [
    [(PR, "$ "), (PL, "git log --oneline ai-history")],
    [(CM, "a1b2c3d "), (PL, "1956 Dartmouth: the term 'AI' is born")],
    [(CM, "e4f5g6h "), (PL, "1997 Deep Blue beats Kasparov")],
    [(CM, "i7j8k9l "), (PL, "2012 AlexNet ignites deep learning")],
    [(CM, "m1n2o3p "), (PL, "2017 Attention is all you need")],
    [(GN, "q4r5s6t "), (PL, "2022 ChatGPT: AI goes mainstream ✓")]]),
    "Snapshot 2.1 — Seventy years of AI as a commit log. Winters included."), "ch2")

insert_before("src/pages/ch3.html", QZ, fig(table("model cards — scope check",
    "system        scope    status",
    ["spam filter   narrow   shipped ✓",
     "chess engine  narrow   shipped ✓",
     "chatbot       broad    here-ish",
     "AGI           general  research"],
    [(CM, "narrow = solved slices · general = the moonshot")]),
    "Snapshot 3.1 — Narrow AI ships products; general AI ships papers."), "ch3")

insert_before("src/pages/ch4.html", QZ, fig(term("python — shapes first", [
    [(PR, ">>> "), (PL, "import numpy as np")],
    [(PR, ">>> "), (PL, "W = np.zeros((4, 3)); x = np.zeros(3)")],
    [(PR, ">>> "), (PL, "(W @ x).shape")],
    [(GN, "(4,)  ✓ "), (CM, "inner dims agree (3 == 3)")]]),
    "Snapshot 4.1 — Half of ML debugging is shape-checking. This is the habit."), "ch4")

insert_before("src/pages/ch6.html", QZ, fig(table("df.describe() — know thy data",
    "col      mean    min     max",
    ["age      34.2    18      71",
     "income   58k     12k     210k",
     "churn    0.21    0       1"],
    [(GN, "3 cols · 0 nulls ✓ "), (CM, "— ranges first, models later")]),
    "Snapshot 6.1 — Describe before you model: ranges, nulls, surprises."), "ch6")

insert_before("src/pages/ch7.html", QZ, fig(term("split — no leakage", [
    [(PR, "$ "), (PL, "python split.py --test 0.2 --seed 42")],
    [(GN, "train 8000 · test 2000 "), (CM, "stratify=label ✓")],
    [(PR, "$ "), (PL, "python leak_check.py")],
    [(GN, "0 shared ids ✓ "), (CM, "— test set stays virgin")]]),
    "Snapshot 7.1 — Split once, stratify, and prove zero leakage."), "ch7")

insert_before("src/pages/ch8.html", QZ, fig(table("confusion matrix — errors have addresses",
    "             pred-N  pred-P",
    ["actual-N     1820    96",
     "actual-P     140     944"],
    [(PL, "accuracy 0.92 · recall 0.87 "), (CM, "— read the off-diagonal")]),
    "Snapshot 8.1 — Accuracy hides sins; the matrix shows where they live."), "ch8")

insert_before("src/pages/ch9.html", QZ, fig(scatter("k-means, k=3",
    [(0.18,0.72,PR),(0.24,0.65,PR),(0.15,0.60,PR),(0.22,0.78,PR),
     (0.52,0.45,AM),(0.58,0.52,AM),(0.48,0.40,AM),(0.56,0.38,AM),
     (0.78,0.74,SK),(0.84,0.68,SK),(0.75,0.62,SK),(0.82,0.80,SK)],
    [(GN, "k=3 ✓ "), (PL, "inertia 412 → 88 — elbow found, clusters separated")]),
    "Snapshot 9.1 — No labels given, three groups found. The elbow says k=3."), "ch9")

insert_before("src/pages/ch10.html", QZ, fig(table("training log — loss must fall",
    "epoch  loss   acc",
    ["1      0.69   0.51",
     "5      0.31   0.88",
     "10     0.12   0.96"],
    [(GN, "learning ✓ "), (CM, "loss ↓, accuracy ↑ — the only graph that matters")]),
    "Snapshot 10.1 — Ten epochs: from coin-flip to 96%. Loss falling is learning."), "ch10")

insert_before("src/pages/ch11.html", QZ, fig(table("model summary — tiny CNN",
    "layer    out        params",
    ["conv1    28x28x16   160",
     "pool1    14x14x16   0",
     "fc1      128        401k",
     "fc2      10         1.3k"],
    [(PL, "total 403k params "), (CM, "— count before you train")]),
    "Snapshot 11.1 — 403k knobs, mostly in one layer. Summaries reveal hogs."), "ch11")

insert_before("src/pages/ch12.html", QZ, fig(term("tokens — text becomes numbers", [
    [(PR, "$ "), (PL, "python tok.py")],
    [(PL, "tokens: ['cats', 'love', 'naps']")],
    [(PL, "ids:    [ 4821,  2390,  9117 ]")],
    [(GN, "3 words → 3 ids ✓ "), (CM, "(vocab 50k)")]]),
    "Snapshot 12.1 — Words in, integers out. Everything downstream is arithmetic."), "ch12")

insert_before("src/pages/ch13.html", QZ, fig(term("one endpoint, any question", [
    [(PR, "$ "), (PL, 'curl api.llm/v1/chat -d \'{"q": "capital of MP?"}\'')],
    [(GN, '{"answer": "Bhopal"'), (PL, ', "tokens": 9, "ms": 210}')],
    [(CM, "✓ knowledge + reasoning behind a single POST")]]),
    "Snapshot 13.1 — LLMs as infrastructure: ask anything over HTTP."), "ch13")

insert_before("src/pages/ch14.html", QZ, fig(strip("generate — 'thali at sunset'",
    [("🍛", "v1"), ("🌅", "v2"), ("🍛", "v3 ★"), ("🌅", "v4")],
    [(GN, "seed 42 · "), (PL, "4 options, human picks v3 ✓")]),
    "Snapshot 14.1 — Prompt once, get four candidates, curate like an editor."), "ch14")

insert_before("src/pages/ch15.html", QZ, fig(table("episodes — explore, then exploit",
    "ep    reward  epsilon",
    ["1     -42     1.00",
     "50    +18     0.40",
     "200   +96     0.05"],
    [(GN, "reward climbs ✓ "), (CM, "curiosity annealed into skill")]),
    "Snapshot 15.1 — From flailing (-42) to mastery (+96): epsilon does the growing."), "ch15")

insert_before("src/pages/ch16.html", QZ, fig(term("pre-deploy review — ethics as checklist", [
    [(GN, "[x] "), (PL, "bias sliced by group")],
    [(GN, "[x] "), (PL, "privacy: PII scrubbed")],
    [(AM, "[ ] "), (PL, "red-team sign-off  ← blocker")],
    [(GN, "verdict: HOLD ✓ "), (CM, "— process working as designed")]]),
    "Snapshot 16.1 — Values compile to checklists. This one correctly says HOLD."), "ch16")

insert_before("src/pages/ch17.html", QZ, fig(term("A* — optimal path", [
    [(PR, "$ "), (PL, "python astar.py --from S --to G")],
    [(PL, "open: S → A(2) → C(5) → G(7)")],
    [(GN, "path S → A → C → G · cost 7 ✓ "), (CM, "admissible = optimal")]]),
    "Snapshot 17.1 — A* expands 4 nodes and proves optimality. Greedy can't."), "ch17")

insert_before("src/pages/ch18.html", QZ, fig(term("knowledge base — ask it", [
    [(PR, "?- "), (PL, "flies(X).")],
    [(GN, "X = sparrow ;  X = eagle.")],
    [(PR, "?- "), (PL, "flies(penguin).")],
    [(AM, "false. "), (CM, "✓ exceptions are knowledge too")]]),
    "Snapshot 18.1 — Logic programming: assert facts, query truths, respect penguins."), "ch18")

insert_before("src/pages/ch19.html", QZ, fig(table("update beliefs — Bayes",
    "hyp      prior  like   post",
    ["fair     0.90   0.50   0.47",
     "biased   0.10   0.95   0.53"],
    [(GN, "10% → 53% ✓ "), (CM, "evidence moved us, prior tempered us")]),
    "Snapshot 19.1 — One surprising streak moves biased from 10% to 53%."), "ch19")

insert_before("src/pages/ch20.html", QZ, fig(table("top-5 for you — ranked",
    "rank  item          score",
    ["1     Dune          0.97",
     "2     Foundation    0.93",
     "3     Neuromancer   0.88"],
    [(CM, "dot(user, item) + a pinch of serendipity")]),
    "Snapshot 20.1 — Your taste as a vector, books as vectors, dot products decide."), "ch20")

insert_before("src/pages/ch21.html", QZ, fig(chat("multimodal — see + read + speak", [
    (SK, "you", "[photo of a dog] what's happening?"),
    (GN, "ai", "A beagle catching a frisbee (0.98). Hindi caption?"),
    (SK, "you", "haan, Hindi me batao"),
    (GN, "ai", "एक बीगल फ्रिस्बी पकड़ रहा है ✓")]),
    "Snapshot 21.1 — One model sees the photo and answers in your language."), "ch21")

insert_before("src/pages/ch22.html", QZ, fig(term("LoRA — cheap adaptation", [
    [(PR, "$ "), (PL, "python train_lora.py --r 16 --epochs 3")],
    [(PL, "trainable: 4.2M / 7B "), (CM, "(0.06% of weights)")],
    [(GN, "eval 0.61 → 0.83 ✓ "), (CM, "one GPU, lunch break, done")]]),
    "Snapshot 22.1 — 0.06% of weights move, eval jumps 22 points."), "ch22")

insert_before("src/pages/ch23.html", QZ, fig(chat("ReAct trace — think, act, observe", [
    (GN, "think", "Need today's rice price. Search first."),
    (AM, "act", "search(rice price mandi) → ₹3,240/quintal"),
    (GN, "think", "Got a number + source. Answer now."),
    (SK, "ai", "₹3,240/quintal (mandi report, today) ✓")]),
    "Snapshot 23.1 — The agent loop in four lines: think, act, observe, answer."), "ch23")

insert_before("src/pages/ch24.html", QZ, fig(chat("crew — planner, worker, critic", [
    (GN, "planner", "Plan: fetch → clean → chart."),
    (SK, "worker", "Fetched 12k rows, cleaned, chart ready."),
    (AM, "critic", "Y-axis starts at 0? Fix and resubmit."),
    (SK, "worker", "Fixed. Chart approved ✓")]),
    "Snapshot 24.1 — Three roles, one loop: plan, do, critique, ship."), "ch24")

insert_before("src/pages/ch25.html", QZ, fig(table("MARL scoreboard — self-play",
    "agent   wins  elo",
    ["blue-3  61%   1480",
     "red-7   55%   1412",
     "blue-1  48%   1355"],
    [(CM, "yesterday's champ is today's sparring partner")]),
    "Snapshot 25.1 — Agents level up by beating their own past selves."), "ch25")

insert_before("src/pages/ch26.html", QZ, fig(table("AutoML trials — machines tune machines",
    "trial  model   acc   time",
    ["7      xgb     0.91  42s",
     "12     lgbm    0.92  38s ★",
     "19     mlp     0.89  210s"],
    [(GN, "promote trial 12 ✓ "), (CM, "best acc, cheapest to serve")]),
    "Snapshot 26.1 — Twenty trials overnight, one winner by morning."), "ch26")

insert_before("src/pages/ch27.html", QZ, fig(term("bounds — fear, quantified", [
    [(PR, "$ "), (PL, "python bound.py --n 10000 --vc 500")],
    [(PL, "train err: 0.08")],
    [(GN, "test err:  0.11  "), (CM, "(bound said ≤ 0.19 ✓)")],
    [(CM, "gap explained, not feared")]]),
    "Snapshot 27.1 — Theory promised ≤0.19; reality delivered 0.11. Trust, verify."), "ch27")

insert_before("src/pages/ch28.html", QZ, fig(bars("why declined? — SHAP-ish",
    [("income 32k", 85, RD, "+0.31"),
     ("late ×3", 70, AM, "+0.22"),
     ("age 24", 25, GN, "-0.04")],
    [(CM, "top driver: income · A/C 98•••44 ✓ masked")]),
    "Snapshot 28.1 — The model shows its work; PII stays masked."), "ch28")

insert_before("src/pages/ch29.html", QZ, fig(table("GPU price/perf — rent smart",
    "gpu     tok/s  $/hr",
    ["T4      41     0.35",
     "A10     96     0.75 ★",
     "H100    410    2.10"],
    [(GN, "★ best perf/$ here ✓ "), (CM, "right-size, then scale")]),
    "Snapshot 29.1 — The H100 is fastest; the A10 wins this workload's wallet."), "ch29")

print("FAILURES:" if fails else "ALL OK")
for f in fails:
    print(" ", f)
sys.exit(1 if fails else 0)
