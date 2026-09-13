"""Batch 3b: captioned SVG snapshots for 30 chapters (ch34-39, ch41-43, ch45, ch47-66).
Same builders/idiom as _snapshots3.py, plus vrbars (vertical bars), poly
(line chart with optional confidence band), and arrowed strip (pipelines).
Inserts each figure immediately before the chapter's quiz-block."""
import pathlib

MONO = 'font-family="JetBrains Mono, monospace"'
BG, PN, ST, PL, CM = "#0f172a", "#1e293b", "#64748b", "#e2e8f0", "#94a3b8"
GN, AM, RD, PR, SK = "#4ade80", "#fbbf24", "#f87171", "#5eead4", "#7dd3fc"


def W(title, h=176):
    return (f'<svg viewBox="0 0 640 {h + 20}" role="img" aria-label="{title}">'
            f'<rect x="10" y="10" width="620" height="{h}" rx="10" fill="{BG}" '
            f'stroke="{ST}" stroke-width="1.5"/>'
            f'<rect x="10" y="10" width="620" height="34" rx="10" fill="{PN}"/>'
            f'<rect x="10" y="30" width="620" height="14" fill="{PN}"/>'
            f'<circle cx="30" cy="27" r="5" fill="#f87171"/><circle cx="48" cy="27" '
            f'r="5" fill="#fbbf24"/><circle cx="66" cy="27" r="5" fill="#4ade80"/>'
            f'<text x="320" y="30" text-anchor="middle" {MONO} font-size="13" '
            f'fill="#cbd5e1">{title}</text></svg>').replace("</svg>", "")


def TL(y, spans):
    t = "".join(f'<tspan fill="{c}">{x}</tspan>' for c, x in spans)
    return f'<text x="34" y="{y}" {MONO} font-size="12" fill="{PL}">{t}</text>'


def term(title, lines):
    h = 52 + 22 * len(lines)
    o = [W(title, h)]
    for i, spans in enumerate(lines):
        o.append("              " + TL(70 + 22 * i, spans))
    return ("\n".join(o), h + 20)


def chat(title, turns):
    o, y = [W(title, 52 + 30 * len(turns) + 26)], 74
    for who, msg in [(t[0], t[1]) for t in turns]:
        tag = ("AI", GN) if who == "ai" else (("YOU", SK) if who == "you"
              else (("TOOL", AM) if who == "tool" else (who.upper(), ST)))
        o.append(f'              <text x="34" y="{y}" {MONO} font-size="12">'
                 f'<tspan fill="{tag[1]}">[{tag[0]}]</tspan>'
                 f'<tspan fill="{PL}"> {msg}</tspan></text>')
        y += 30
    return ("\n".join(o), 52 + 30 * len(turns) + 26 + 20)


def table(title, head, rows, foot=None, hl=None):
    n = len(rows)
    h = 74 + 24 * n + (26 if foot else 0)
    o = [W(title, h)]
    o.append(f'              <text x="34" y="68" {MONO} font-size="12" '
             f'fill="{CM}">{head}</text>')
    o.append(f'              <line x1="34" y1="78" x2="606" y2="78" stroke="{ST}"/>')
    y = 100
    for i, r in enumerate(rows):
        if hl is not None and i == hl:
            o.append(f'              <rect x="26" y="{y - 15}" width="588" '
                     f'height="21" rx="4" fill="#1e293b"/>')
        o.append(f'              <text x="34" y="{y}" {MONO} font-size="12" '
                 f'fill="{PL}">{r}</text>')
        y += 24
    if foot:
        o.append("              " + TL(y + 2, foot))
    return ("\n".join(o), h + 20)


def strip(title, cells, foot=None, arrows=False):
    n = len(cells)
    h = 178 + (26 if foot else 0)
    gw = 580 // n
    o = [W(title, h)]
    for i, (g, lab) in enumerate(cells):
        x = 30 + i * gw
        o.append(f'              <rect x="{x}" y="58" width="{gw - 12}" height="84" '
                 f'rx="8" fill="{PN}" stroke="{ST}"/>'
                 f'<text x="{x + (gw - 12) // 2}" y="94" text-anchor="middle" '
                 f'font-size="26">{g}</text>'
                 f'<text x="{x + (gw - 12) // 2}" y="126" text-anchor="middle" '
                 f'{MONO} font-size="12" fill="{PL}">{lab}</text>')
        if arrows and i < n - 1:
            o.append(f'              <text x="{x + gw - 6}" y="108" text-anchor="middle" '
                     f'font-size="16" fill="{PR}">\u2192</text>')
    if foot:
        o.append("              " + TL(168, foot))
    return ("\n".join(o), h + 20)


def vrbars(title, vals, labels=None, foot=None, bw=34, color="#0ea5e9"):
    n = len(vals)
    h = 208 + (28 if foot else 0)
    gw = 520 // n
    mx = max(vals)
    o = [W(title, h)]
    o.append(f'              <line x1="60" y1="168" x2="590" y2="168" stroke="{ST}"/>')
    for i, v in enumerate(vals):
        bh = max(3, round(104 * v / mx))
        x = 60 + i * gw + (gw - bw) // 2
        o.append(f'              <rect x="{x}" y="{168 - bh}" width="{bw}" '
                 f'height="{bh}" rx="3" fill="{color}"/>')
        if labels:
            o.append(f'              <text x="{x + bw // 2}" y="188" text-anchor="middle" '
                     f'{MONO} font-size="11" fill="{CM}">{labels[i]}</text>')
    if foot:
        o.append("              " + TL(212, foot))
    return ("\n".join(o), h + 20)


def poly(title, pts, xlabels, foot, band=None, color="#5eead4"):
    m = len(pts)
    X = lambda i: 70 + i * (520 / (m - 1))
    Y = lambda v: 180 - v * 120
    o = [W(title, 226)]
    o.append(f'              <line x1="70" y1="180" x2="590" y2="180" stroke="{ST}"/>'
             f'<line x1="70" y1="60" x2="70" y2="180" stroke="{ST}"/>')
    if band:
        lo = " ".join(f"{X(i):.0f},{Y(v[0]):.0f}" for i, v in enumerate(band))
        hi = " ".join(f"{X(i):.0f},{Y(v[1]):.0f}" for i, v in
                      reversed(list(enumerate(band))))
        o.append(f'              <polygon points="{lo} {hi}" fill="#0ea5e9" opacity="0.25"/>')
    o.append('              <polyline points="' +
             " ".join(f"{X(i):.0f},{Y(v):.0f}" for i, v in enumerate(pts)) +
             f'" fill="none" stroke="{color}" stroke-width="3"/>')
    for i, v in enumerate(pts):
        o.append(f'              <circle cx="{X(i):.0f}" cy="{Y(v):.0f}" r="4" fill="{color}"/>')
    for i, lab in enumerate(xlabels):
        o.append(f'              <text x="{X(i):.0f}" y="198" text-anchor="middle" '
                 f'{MONO} font-size="11" fill="{CM}">{lab}</text>')
    o.append("              " + TL(220, foot))
    return ("\n".join(o), 246)


def fig(svg, caption):
    inner, h = svg
    return (f'<figure class="diagram">\n            <div class="diagram-art">\n              '
            f'{inner}\n              </svg>\n            </div>\n            '
            f'<figcaption>{caption}</figcaption>\n          </figure>\n          ')


QZ = '<div class="quiz-block">'  # inline-style files: no newline after tag


def insert_before(path, anchor, html):
    p = pathlib.Path(path)
    s = p.read_text()
    assert s.count(anchor) == 1, (path, s.count(anchor))
    p.write_text(s.replace(anchor, html + anchor, 1))


S = lambda n, t: f"Snapshot {n}.1 \u2014 {t}."  # noqa: E731

insert_before("src/pages/ch34.html", QZ, fig(vrbars(
    "refunds by city \u2014 July \u20b9k",
    [482, 419, 524], ["Jaipur", "Indore", "Bhopal"],
    [(GN, "Bhopal leads \u2713 "), (PL, "y-axis starts at 0 (honest!)")]),
    S(34, "city bars, zero baseline, no truncation tricks")))

insert_before("src/pages/ch35.html", QZ, fig(table(
    "A/B result \u2014 ship or not?",
    "grp&#160;&#160;&#160;n&#160;&#160;&#160;&#160;&#160;conv",
    ["A&#160;&#160;&#160;&#160;&#160;5000&#160;&#160;4.1%", "B&#160;&#160;&#160;&#160;&#160;5000&#160;&#160;4.9% \u2605"],
    [(GN, "p=0.03 &lt; 0.05 \u2713 "), (PL, "pre-registered \u2192 ship B")], hl=1),
    S(35, "B wins, p = 0.03, pre-registered: ship it")))

insert_before("src/pages/ch36.html", QZ, fig(table(
    "store dashboard \u2014 July",
    "kpi&#160;&#160;&#160;&#160;&#160;&#160;&#160;value",
    ["revenue&#160;&#160;&#160;\u20b98.1M \u25b212%", "orders&#160;&#160;&#160;&#160;12.4k \u25b28%",
     "RLS&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;seller-scoped \u2713"],
    [(CM, "one definition of revenue, sliced by role")]),
    S(36, "one revenue definition, RLS-scoped, refresh stamped")))

insert_before("src/pages/ch37.html", QZ, fig(term("capstone \u2014 tree", [
    [(PR, "$ "), (PL, "tree refund-spike -L 2")],
    [(PL, "\u251c\u2500\u2500 data/raw/orders.jsonl")],
    [(PL, "\u251c\u2500\u2500 notebooks/eda.ipynb")],
    [(GN, "\u251c\u2500\u2500 memo.md  "), (PL, "\u2190 the deliverable \u2713")],
    [(PL, "\u2514\u2500\u2500 dashboard.pbix")]]),
    S(37, "capstone tree: raw data, notebook, memo, dashboard")))

insert_before("src/pages/ch38.html", QZ, fig(table(
    "pick your fighter",
    "tool&#160;&#160;&#160;&#160;&#160;best-at",
    ["Excel&#160;&#160;&#160;&#160;ad-hoc, solo", "PBI&#160;&#160;&#160;&#160;&#160;&#160;MS shops, cheap",
     "Tableau&#160;&#160;exec polish", "Looker&#160;&#160;&#160;git + governance"],
    [(CM, "match tool to team, not hype \u2713")]),
    S(38, "BI shootout: match the tool to the team")))

insert_before("src/pages/ch39.html", QZ, fig(strip(
    "nightly_elt \u2014 04:12",
    [("\U0001f4e5", "extract"), ("\U0001f527", "dbt"), ("\u2705", "quality"),
     ("\U0001f680", "serve")],
    [(GN, "all green \u2713 "), (PL, "raw \u2192 modeled \u2192 tested \u2192 served")],
    arrows=True),
    S(39, "nightly ELT: extract, model, test, serve \u2014 all green")))

insert_before("src/pages/ch41.html", QZ, fig(term("ship it", [
    [(PR, "$ "), (PL, "git log --graph --oneline -4")],
    [(PL, "* 9f2c1a Add LEFT JOIN query \u2713 CI green")],
    [(PL, "* 7b3d0e Fix fanout (dedupe keys)")],
    [(PR, "$ "), (PL, "git status")],
    [(GN, "clean \u2713 "), (CM, "\u2014 small PRs, green CI, ship it")]]),
    S(41, "small PRs, green CI, clean tree \u2014 ship it")))

insert_before("src/pages/ch42.html", QZ, fig(chat("support RAG \u2014 cited", [
    ("you", "How do I return shoes?"),
    ("ai", "30-day window, tags on [1]. Orders \u2192 Return [2]."),
    ("tool", "cited policy#returns \u00b7 faith 0.94 \u2713")]),
    S(42, "grounded answer with citations, faithfulness 0.94")))

insert_before("src/pages/ch43.html", QZ, fig(table(
    "prod health \u2014 SLOs",
    "signal&#160;&#160;value",
    ["p99&#160;&#160;&#160;&#160;&#160;240ms \u2713", "err&#160;&#160;&#160;&#160;&#160;0.2% \u2713",
     "drift&#160;&#160;&#160;0.31 watch"],
    [(AM, "drift watchlisted "), (CM, "\u2014 all else green")]),
    S(43, "SLO board: p99, errors green, drift watchlisted")))

insert_before("src/pages/ch45.html", QZ, fig(poly(
    "demand forecast + 80% band",
    [0.35, 0.42, 0.50, 0.62, 0.78], ["M1", "M2", "M3", "M4", "M5"],
    [(GN, "holiday spike inside 80% band \u2713")],
    band=[(0.33, 0.37), (0.39, 0.45), (0.44, 0.56), (0.52, 0.72), (0.64, 0.92)],
    color="#0ea5e9"),
    S(45, "forecast with widening band: the spike lands inside")))

insert_before("src/pages/ch47.html", QZ, fig(table(
    "frontier scoreboard",
    "bench&#160;&#160;score",
    ["ARC&#160;&#160;&#160;&#160;&#160;71%", "SWE-b&#160;&#160;&#160;54%", "GPQA&#160;&#160;&#160;&#160;62%"],
    [(CM, "moving fast \u2014 date your claims \u2713")]),
    S(47, "frontier scoreboard: ARC, SWE-bench, GPQA \u2014 dated")))

insert_before("src/pages/ch48.html", QZ, fig(term("hybrid trace", [
    [(PR, "$ "), (PL, 'ask "refund window for shoes?"')],
    [(PL, "dense 8 + sparse 8 \u2192 rerank \u2192 top 3")],
    [(GN, "answer + 3 citations \u2713 "), (CM, "faith 0.96")]]),
    S(48, "hybrid retrieval trace: dense + sparse, reranked, cited")))

insert_before("src/pages/ch49.html", QZ, fig(chat("think aloud \u2014 math", [
    ("think", "3 apples + 5 more\u20263+5 = 8."),
    ("ai", "Answer: \\boxed{8} \u2713 (steps shown)")]),
    S(49, "auditable CoT: steps shown, boxed answer")))

insert_before("src/pages/ch50.html", QZ, fig(table(
    "cloud vs edge",
    "where&#160;&#160;lat&#160;&#160;&#160;&#160;cost",
    ["cloud&#160;&#160;380ms&#160;&#160;\u20b9\u20b9", "edge&#160;&#160;&#160;24ms&#160;&#160;&#160;\u20b9 \u2713"],
    [(GN, "24ms wins realtime \u2713")], hl=1),
    S(50, "cloud 380 ms vs edge 24 ms: realtime wins")))

insert_before("src/pages/ch51.html", QZ, fig(chat("grounded VQA", [
    ("you", "[shelf photo] how many red boxes?"),
    ("ai", "3 red boxes \u2713 [0.12,0.40,\u2026] grounded")]),
    S(51, "grounded VQA: count plus bounding box")))

insert_before("src/pages/ch52.html", QZ, fig(vrbars(
    "call \u2014 live transcript",
    [0.30, 0.50, 0.80, 0.60, 0.40, 0.70, 0.90, 0.50, 0.35, 0.60, 0.75, 0.45,
     0.30, 0.55, 0.85, 0.65, 0.40, 0.50, 0.70, 0.45, 0.30, 0.60, 0.50, 0.35],
    foot=[(PL, '"refund chahiye" '), (GN, "\u00b7 barge-in at 0:42 \u2713")], bw=12),
    S(52, "live waveform with barge-in at 0:42")))

insert_before("src/pages/ch53.html", QZ, fig(strip(
    "storyboard \u2014 24fps",
    [("\U0001f305", "f1"), ("\U0001f35b", "f2"), ("\U0001f3d9\ufe0f", "f3"),
     ("\U0001f303", "f4")],
    [(GN, "C2PA signed \u2713 "), (PL, "prompt locked")]),
    S(53, "locked storyboard frames, C2PA-signed")))

insert_before("src/pages/ch54.html", QZ, fig(table(
    "federated rounds",
    "rnd&#160;&#160;clients&#160;&#160;acc",
    ["1&#160;&#160;&#160;&#160;40&#160;&#160;&#160;&#160;&#160;&#160;&#160;0.71", "5&#160;&#160;&#160;&#160;38&#160;&#160;&#160;&#160;&#160;&#160;&#160;0.84",
     "10&#160;&#160;&#160;41&#160;&#160;&#160;&#160;&#160;&#160;&#160;0.89 \u2713"],
    [(GN, "raw data never left devices \u2713")], hl=2),
    S(54, "federated rounds: accuracy climbs, data stays put")))

insert_before("src/pages/ch55.html", QZ, fig(term("Bell pair", [
    [(PR, "$ "), (PL, "qc.run(shots=1000)")],
    [(PL, '{"00": 498, "11": 502}')],
    [(GN, "entangled \u2713 "), (CM, "(correlated, not agreed)")]]),
    S(55, "Bell pair: 00/11 split, correlated not agreed")))

insert_before("src/pages/ch56.html", QZ, fig(term("VLA rollout", [
    [(PR, "$ "), (PL, 'rollout --task "fold towel"')],
    [(PL, "obs \u2192 tokens \u2192 [grasp, lift, fold]")],
    [(GN, "7/10 success \u2713 "), (CM, "sim2real gap logged")]]),
    S(56, "VLA rollout: observe, tokenize, act \u2014 7/10")))

insert_before("src/pages/ch57.html", QZ, fig(table(
    "surrogate vs sim",
    "model&#160;&#160;s/run&#160;&#160;err",
    ["sim&#160;&#160;&#160;&#160;3600&#160;&#160;&#160;&#160;0%", "surr&#160;&#160;&#160;0.4&#160;&#160;&#160;&#160;&#160;&#160;2% \u2605"],
    [(GN, "9000x faster \u2713 "), (CM, "honest error bars attached")], hl=1),
    S(57, "surrogate: 9000x faster at 2% error")))

insert_before("src/pages/ch58.html", QZ, fig(table(
    "ranked + explore",
    "item&#160;&#160;&#160;&#160;&#160;&#160;&#160;score&#160;&#160;why",
    ["Dune&#160;&#160;&#160;&#160;&#160;&#160;0.97&#160;&#160;&#160;exploit",
     "Hyperion&#160;&#160;0.81&#160;&#160;&#160;explore \u2605"],
    [(PL, "\u03b5-greedy 10% \u2713 "), (CM, "serendipity on purpose")]),
    S(58, "ranked slate with an epsilon-greedy explorer")))

insert_before("src/pages/ch59.html", QZ, fig(term("red suite", [
    [(PR, "$ "), (PL, "pytest red_suite/ -q")],
    [(PL, "48 passed \u00b7 2 failed")],
    [(AM, "FAIL indirect-email-07 "), (PL, "\u2192 patch + rerun")],
    [(GN, "ASR 4% \u2192 &lt;1% target \u2713 "), (CM, "suite gates deploys")]]),
    S(59, "red-team suite: 48 pass, failures gate the deploy")))

insert_before("src/pages/ch60.html", QZ, fig(poly(
    "the J-curve",
    [0.62, 0.55, 0.45, 0.38, 0.42, 0.55, 0.72, 0.88],
    ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8"],
    [(GN, "the dip is the price \u2713 "), (PL, "redesign, then compound")],
    color="#fbbf24"),
    S(60, "the J-curve: dip deep, redesign, then compound")))

insert_before("src/pages/ch61.html", QZ, fig(table(
    "VLM report card",
    "bench&#160;&#160;score",
    ["MMMU&#160;&#160;&#160;&#160;58%", "POPE&#160;&#160;&#160;&#160;91%", "IoU&#160;&#160;&#160;&#160;&#160;&#160;0.62"],
    [(GN, "\u03ba=0.81 \u2713 "), (PL, "raters agree \u2014 ship it")]),
    S(61, "VLM report card with rater agreement kappa 0.81")))

insert_before("src/pages/ch62.html", QZ, fig(term("trace review", [
    [(PR, "$ "), (PL, "review traces/agent-4417.log")],
    [(GN, "tool:read_email \u2713 "), (PL, "\u00b7 "),
     (RD, "tool:refund $50k \u2717 BLOCKED")],
    [(GN, "contained \u2713 "),
     (CM, "injection attempt logged + quarantined")]]),
    S(62, "trace review: read allowed, refund blocked, contained")))

insert_before("src/pages/ch63.html", QZ, fig(term("PR #412 \u2014 agent fix", [
    [(CM, "  def total(rows):")],
    [(RD, '-     return sum(r[1] for r in rows)')],
    [(GN, '+     return sum(r["amt"] for r in rows)')],
    [(GN, "pytest 12 passed \u00b7 CI green \u2713 "), (CM, "merge?")]]),
    S(63, "agent diff: fragile index to named key, CI green")))

insert_before("src/pages/ch64.html", QZ, fig(term("flywheel", [
    [(PR, "$ "), (PL, "flywheel --gen 20x --verify strict")],
    [(PL, "kept 34% \u00b7 tail-acc 0.81 \u2713")],
    [(GN, "diversity stable \u2713 "), (CM, "no collapse this generation")]]),
    S(64, "data flywheel: keep a third, verify strict, no collapse")))

insert_before("src/pages/ch65.html", QZ, fig(table(
    "fertility = money",
    "lang&#160;&#160;&#160;&#160;&#160;tok/wd",
    ["EN&#160;&#160;&#160;&#160;&#160;&#160;&#160;1.3", "HI-Deva&#160;&#160;3.1", "HI-roman&#160;4.6"],
    [(CM, "same meaning, 3.5x tokens \u2014 budget it \u2713")]),
    S(65, "tokenizer fertility: same meaning, 3.5x the tokens")))

insert_before("src/pages/ch66.html", QZ, fig(term("refinery", [
    [(PR, "$ "), (PL, "refine --in crawl-100GB")],
    [(PL, "kept 8.2% \u00b7 dedup -31% \u00b7 evals quarantined \u2713")],
    [(GN, "licenses 100% known \u2713 "), (CM, "datasheet written")]]),
    S(66, "data refinery: keep 8%, dedup, license, datasheet")))

print("ALL OK")
