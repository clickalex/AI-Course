#!/usr/bin/env python3
"""Phase 14: wire Ch71-74 (D14-15: SQL II + AI DBs; A9-10: DSA III + K8s)."""
import re, pathlib, sys

ROOT = pathlib.Path("/home/user/AI-Course")
fails = []

def edit(path, old, new, expect=1, label=""):
    p = ROOT / path
    s = p.read_text()
    n = s.count(old)
    if n != expect:
        fails.append(f"{path} :: {label or old[:50]}: found {n}, expected {expect}")
        return
    p.write_text(s.replace(old, new, expect))

# sidebar D14/D15 + A9/A10 (+ exam label)
edit("src/_sidebar.html",
     '      <button class="toc-item" data-go="ch45"><span class="toc-num">D13</span> Time series</button>\n',
     '      <button class="toc-item" data-go="ch45"><span class="toc-num">D13</span> Time series</button>\n'
     '      <button class="toc-item" data-go="ch71"><span class="toc-num">D14</span> Advanced SQL</button>\n'
     '      <button class="toc-item" data-go="ch72"><span class="toc-num">D15</span> AI databases</button>\n', 1, "sidebar-d")
edit("src/_sidebar.html",
     '      <button class="toc-item" data-go="ch70"><span class="toc-num">A8</span> Terminal survival</button>\n',
     '      <button class="toc-item" data-go="ch70"><span class="toc-num">A8</span> Terminal survival</button>\n'
     '      <button class="toc-item" data-go="ch73"><span class="toc-num">A9</span> DSA III: heaps, tries</button>\n'
     '      <button class="toc-item" data-go="ch74"><span class="toc-num">A10</span> Kubernetes for ML</button>\n', 1, "sidebar-a")
edit("src/_sidebar.html", "Final exam (69 Q)", "Final exam (73 Q)", 1, "sidebar-exam")

# app.js PAGES + TITLES
edit("js/app.js", '"ch40","ch41","ch45",\n  "ch17"',
     '"ch40","ch41","ch45","ch71","ch72",\n  "ch17"', 1, "pages-d")
edit("js/app.js", '"ch69","ch70","ch47"',
     '"ch69","ch70","ch73","ch74","ch47"', 1, "pages-a")
edit("js/app.js", '  ch45: "Time series & forecasting",',
     '  ch45: "Time series & forecasting",\n  ch71: "Advanced SQL",\n  ch72: "AI databases",', 1, "titles-d")
edit("js/app.js", '  ch70: "Terminal survival",',
     '  ch70: "Terminal survival",\n  ch73: "DSA III: heaps, tries",\n  ch74: "Kubernetes for ML",', 1, "titles-a")

# nav (two insertions)
edit("src/pages/ch45.html", '<button data-go="ch17">Search & games →</button>',
     '<button data-go="ch71">Advanced SQL →</button>', 1, "ch45-next")
edit("src/pages/ch17.html", '<button class="ghost" data-go="ch45">← Time series</button>',
     '<button class="ghost" data-go="ch72">← AI databases</button>', 1, "ch17-prev")
edit("src/pages/ch70.html", '<button data-go="ch47">AGI →</button>',
     '<button data-go="ch73">DSA III →</button>', 1, "ch70-next")
edit("src/pages/ch47.html", '<button class="ghost" data-go="ch70">← Terminal survival</button>',
     '<button class="ghost" data-go="ch74">← Kubernetes for ML</button>', 1, "ch47-prev")

# cover
edit("src/pages/cover.html", '<div class="stat"><b>71</b><span>teaching chapters</span></div>',
     '<div class="stat"><b>75</b><span>teaching chapters</span></div>', 1, "cov-ch")
edit("src/pages/cover.html", '<div class="stat"><b>400+</b><span>scored MCQs</span></div>',
     '<div class="stat"><b>420+</b><span>scored MCQs</span></div>', 1, "cov-mcq")
edit("src/pages/cover.html", '<div class="stat"><b>220+</b><span>practice questions</span></div>',
     '<div class="stat"><b>230+</b><span>practice questions</span></div>', 1, "cov-prac")
edit("src/pages/cover.html", '<div class="stat"><b>69</b><span>final exam questions</span></div>',
     '<div class="stat"><b>73</b><span>final exam questions</span></div>', 1, "cov-exam-n")
edit("src/pages/cover.html", "data skills (Python, Excel, SQL, stats, BI)",
     "data skills (Python, Excel, SQL I–II, stats, BI, databases)", 1, "cov-lede-d")
edit("src/pages/cover.html", "DSA I–II, model serving, terminal survival, interview prep",
     "DSA I–III, model serving, terminal survival, Kubernetes, interview prep", 1, "cov-lede-a")
edit("src/pages/cover.html", '            <button data-go="ch45">Time series (D13)</button>\n',
     '            <button data-go="ch45">Time series (D13)</button>\n'
     '            <button data-go="ch71">Adv SQL (D14)</button>\n'
     '            <button data-go="ch72">AI DBs (D15)</button>\n', 1, "cov-mini-d")
edit("src/pages/cover.html", '            <button data-go="ch70">Terminal (A8)</button>\n',
     '            <button data-go="ch70">Terminal (A8)</button>\n'
     '            <button data-go="ch73">DSA III (A9)</button>\n'
     '            <button data-go="ch74">K8s (A10)</button>\n', 1, "cov-mini-a")
edit("src/pages/cover.html", "Final exam (69 Q)", "Final exam (73 Q)", 1, "cov-exam")

# how / paths / syllabus / notes
edit("src/pages/how.html", "69 mixed questions covering school through PhD topics",
     "73 mixed questions covering school through PhD topics", 1, "how-exam")
edit("src/pages/how.html", "हिंदी meanings of key terms (Ch 30–70)",
     "हिंदी meanings of key terms (Ch 30–74)", 1, "how-gloss")
edit("src/pages/paths.html", "data skills Ch 30–41 + Ch 45",
     "data skills Ch 30–41 + Ch 45 + Ch 71–72", 2, "paths-data")
edit("src/pages/paths.html", "applied Ch 42–44 + Ch 46 + Ch 67–70 and frontier",
     "applied Ch 42–44 + Ch 46 + Ch 67–70 + Ch 73–74 and frontier", 1, "paths-ind")
edit("src/pages/paths.html", "applied production (Ch 42–44 + Ch 46 + Ch 67–70) → frontier",
     "applied production (Ch 42–44 + Ch 46 + Ch 67–70 + Ch 73–74) → frontier", 1, "paths-zero")
edit("src/pages/syllabus.html", "Data skills · Python → Git (Ch 30–41, 45)",
     "Data skills · Python → AI DBs (Ch 30–41, 45, 71–72)", 1, "syl-d-sum")
edit("src/pages/syllabus.html",
     "<li>Time series (Ch 45): decomposition, ARIMA/ETS/Prophet, lag features, rolling backtests, intervals</li>",
     "<li>Time series (Ch 45): decomposition, ARIMA/ETS/Prophet, lag features, rolling backtests, intervals</li>\n"
     "<li>Advanced SQL (Ch 71): windows, RANK/LAG, staged CTEs, EXPLAIN, indexing, dbt</li>\n"
     "<li>AI databases (Ch 72): Postgres+pgvector, Redis caching, vector DBs, tenant isolation</li>",
     1, "syl-d-rows")
edit("src/pages/syllabus.html",
     "<li>Applied production (Ch 42–44, 46, 67–70): prompt patterns, RAG + evals, Docker, cloud GPUs, MLOps lifecycle, transformers lab, DSA I–II, model serving + demos, terminal survival</li>",
     "<li>Applied production (Ch 42–44, 46, 67–70, 73–74): prompt patterns, RAG + evals, Docker, cloud GPUs, MLOps lifecycle, transformers lab, DSA I–III, model serving + demos, terminal survival, Kubernetes for ML</li>",
     1, "syl-a")
edit("src/pages/notes.html", "Data engineering, APIs & git (Ch 39–41, 45)",
     "Data engineering, APIs, git + SQL II (Ch 39–41, 45, 71–72)", 1, "notes-d-h")
edit("src/pages/notes.html",
     "<li>Time series (Ch 45): trend+seasonal+noise; time splits only; beat naive; quote intervals.</li>",
     "<li>Time series (Ch 45): trend+seasonal+noise; time splits only; beat naive; quote intervals.</li>\n"
     "              <li>SQL II + DBs (Ch 71–72): windows + staged CTEs; Postgres→Redis→vector DB; tenant filters.</li>",
     1, "notes-d")
edit("src/pages/notes.html", "Applied production: RAG, cloud, MLOps, coding (Ch 42–44, 46, 67–70)",
     "Applied production: RAG, cloud, MLOps, coding (Ch 42–44, 46, 67–70, 73–74)", 1, "notes-a-h")
edit("src/pages/notes.html",
     "<li>Ship it (Ch 69–70): FastAPI load-once + Pydantic; one venv per project; tmux; nvidia-smi.</li>",
     "<li>Ship it (Ch 69–70): FastAPI load-once + Pydantic; one venv per project; tmux; nvidia-smi.</li>\n"
     "              <li>DSA III + K8s (Ch 73–74): heaps/tries/DSU/intervals; Jobs train, Deployments serve; quotas.</li>",
     1, "notes-a")

# cheats +4 (append after Ch 70 card; numeric order)
cp = ROOT / "src/pages/cheats.html"
cs = cp.read_text()
m = re.search(r'(<div class="cheat-card"><h4>Ch 70 · Term</h4><ul>.*?</ul></div>)', cs, re.S)
if not m:
    fails.append("cheats :: ch70 card not found")
else:
    cp.write_text(cs.replace(m.group(1), m.group(1) + """
            <div class="cheat-card"><h4>Ch 71 · SQL2</h4><ul>
              <li>PARTITION·ORDER·FRAME</li>
              <li>CTEs stage logic</li>
              <li>LAG beats self-joins</li>
              <li>EXPLAIN, then index</li>
              <li>Ties, TZ, NULLs</li>
            </ul></div>
            <div class="cheat-card"><h4>Ch 72 · AIDB</h4><ul>
              <li>Postgres first</li>
              <li>Filter → vectors</li>
              <li>Cache = derived</li>
              <li>Version embeddings</li>
              <li>Tenant-test all</li>
            </ul></div>
            <div class="cheat-card"><h4>Ch 73 · DSA3</h4><ul>
              <li>Top-K = heap</li>
              <li>Prefix = trie</li>
              <li>Connected = DSU</li>
              <li>Overlap = sort+sweep</li>
              <li>Choose, undo</li>
            </ul></div>
            <div class="cheat-card"><h4>Ch 74 · K8s</h4><ul>
              <li>Jobs train</li>
              <li>Deploys serve</li>
              <li>GPU req + quota</li>
              <li>describe events</li>
              <li>Pin images</li>
            </ul></div>""", 1))
edit("src/pages/cheats.html", "One card per chapter (Ch 30–70).",
     "One card per chapter (Ch 30–74).", 1, "cheats-lede")

# glossary +1 table (128 → 136)
edit("src/pages/glossary.html", "Every key term from Ch 30–70 with its",
     "Every key term from Ch 30–74 with its", 1, "gloss-lede")
edit("src/pages/glossary.html",
     """            <tr><td>tmux</td><td>tmux</td><td>टूटे बिना चलता terminal-सत्र (server पर अमर)</td></tr>
          </tbody></table>""",
     """            <tr><td>tmux</td><td>tmux</td><td>टूटे बिना चलता terminal-सत्र (server पर अमर)</td></tr>
          </tbody></table>
          <h3>Ch 71–74 · SQL II, databases, DSA III, K8s</h3>
          <table><thead><tr><th>English</th><th>हिंदी</th><th>आसान मतलब</th></tr></thead><tbody>
            <tr><td>Window function</td><td>विंडो-फंक्शन</td><td>पंक्तियाँ रखकर रैंक/जोड़ निकालना</td></tr>
            <tr><td>CTE</td><td>CTE (अस्थायी-चरण)</td><td>पढ़ने लायक चरणबद्ध query (WITH)</td></tr>
            <tr><td>Vector DB</td><td>वेक्टर-DB</td><td>अर्थ से खोजने वाला भंडार (RAG)</td></tr>
            <tr><td>Cache</td><td>कैश</td><td>तुरंत मिलने वाली नक़ल (Redis)</td></tr>
            <tr><td>Heap</td><td>हीप</td><td>सबसे छोटा/बड़ा ऊपर रखने वाली संरचना</td></tr>
            <tr><td>Trie</td><td>ट्राई</td><td>उपसर्ग-साझा पेड़ (autocomplete)</td></tr>
            <tr><td>Union-find</td><td>यूनियन-फाइंड</td><td>जुड़े समूह पहचानना (लगभग तुरंत)</td></tr>
            <tr><td>Pod</td><td>पॉड</td><td>K8s की सबसे छोटी इकाई (container-समूह)</td></tr>
          </tbody></table>""", 1, "gloss-table")
edit("src/pages/glossary.html", "<p>128 terms, 8 per chapter group.",
     "<p>136 terms, 8 per chapter group.", 1, "gloss-count")

# exam Q70-73
edit("src/pages/exam.html", "<h2>Final exam · 69 questions</h2>",
     "<h2>Final exam · 73 questions</h2>", 1, "exam-h2")
edit("src/pages/exam.html",
     "(69 total: Q1–30 core AI + Q31–39 data + Q40–45 eng & production + Q46–65 frontier + Q66–69 applied coding)",
     "(73 total: Q1–30 core AI + Q31–39 data + Q40–45 eng & production + Q46–65 frontier + Q66–69 applied coding + Q70–73 SQL-II, DBs, DSA-III, K8s)",
     1, "exam-scoring")
Q = """
          <div class="mcq" data-answer="c">
            <p class="q">70. RANK() OVER (PARTITION BY city ORDER BY revenue DESC) gives you:</p>
            <div class="opts">
              <button class="opt" data-opt="a" onclick="selectOpt(this)">A. Deleted rows</button>
              <button class="opt" data-opt="b" onclick="selectOpt(this)">B. One row per city</button>
              <button class="opt" data-opt="c" onclick="selectOpt(this)">C. Per-city revenue ranks with ties sharing a rank (1,1,3…)</button>
              <button class="opt" data-opt="d" onclick="selectOpt(this)">D. Random numbers</button>
            </div>
            <div class="mcq-actions"><button class="btn" onclick="checkOne(this)">Check</button><span class="score-chip"></span></div>
            <div class="explain">Windows rank without collapsing.</div>
          </div>
          <div class="mcq" data-answer="a">
            <p class="q">71. Upgrading an embedding model forces a re-embed (backfill) because:</p>
            <div class="opts">
              <button class="opt" data-opt="a" onclick="selectOpt(this)">A. Old and new vectors live in different spaces — distances become garbage</button>
              <button class="opt" data-opt="b" onclick="selectOpt(this)">B. Postgres requires it</button>
              <button class="opt" data-opt="c" onclick="selectOpt(this)">C. Redis deletes them</button>
              <button class="opt" data-opt="d" onclick="selectOpt(this)">D. Vectors expire weekly</button>
            </div>
            <div class="mcq-actions"><button class="btn" onclick="checkOne(this)">Check</button><span class="score-chip"></span></div>
            <div class="explain">Version + dual-read + backfill.</div>
          </div>
          <div class="mcq" data-answer="d">
            <p class="q">72. “Everyone connected to user X” over 10M pairs is best served by:</p>
            <div class="opts">
              <button class="opt" data-opt="a" onclick="selectOpt(this)">A. Binary search</button>
              <button class="opt" data-opt="b" onclick="selectOpt(this)">B. Bubble sort</button>
              <button class="opt" data-opt="c" onclick="selectOpt(this)">C. A trie</button>
              <button class="opt" data-opt="d" onclick="selectOpt(this)">D. Union-find — near-constant per op with path compression</button>
            </div>
            <div class="mcq-actions"><button class="btn" onclick="checkOne(this)">Check</button><span class="score-chip"></span></div>
            <div class="explain">Connected → DSU.</div>
          </div>
          <div class="mcq" data-answer="b">
            <p class="q">73. A GPU pod stuck in Pending is diagnosed first with:</p>
            <div class="opts">
              <button class="opt" data-opt="a" onclick="selectOpt(this)">A. Deleting the cluster</button>
              <button class="opt" data-opt="b" onclick="selectOpt(this)">B. kubectl describe pod — the Events reveal the scheduler's reason</button>
              <button class="opt" data-opt="c" onclick="selectOpt(this)">C. Rebooting the laptop</button>
              <button class="opt" data-opt="d" onclick="selectOpt(this)">D. Applying twice</button>
            </div>
            <div class="mcq-actions"><button class="btn" onclick="checkOne(this)">Check</button><span class="score-chip"></span></div>
            <div class="explain">Events explain Pending.</div>
          </div>
"""
edit("src/pages/exam.html",
     '          <p style="margin-top:22px">You can check questions one-by-one for study, or submit the whole exam for an official grade.</p>',
     Q + '          <p style="margin-top:22px">You can check questions one-by-one for study, or submit the whole exam for an official grade.</p>',
     1, "exam-qs")

# results
edit("src/pages/results.html", "Take the 69-question final exam, then come back here.",
     "Take the 73-question final exam, then come back here.", 1, "res-blurb")
edit("src/pages/results.html", '<strong id="resTotal">69</strong> correct',
     '<strong id="resTotal">73</strong> correct', 1, "res-total")

# README
edit("README.md", "**70 numbered chapters** (71 teaching units with school)",
     "**74 numbered chapters** (75 teaching units with school)", 1, "rm-count")
edit("README.md", "**400+ MCQs**", "**420+ MCQs**", 1, "rm-mcq")
edit("README.md", "**Final exam (69 questions: 30 core AI + 9 data + 10 eng & production + 20 frontier)**",
     "**Final exam (73 questions: 30 core AI + 11 data + 12 eng & production + 20 frontier)**", 1, "rm-exam")
edit("README.md", "| **ch45** | **Time series & forecasting (ARIMA, Prophet, backtests)** | **Data** |",
     "| **ch45** | **Time series & forecasting (ARIMA, Prophet, backtests)** | **Data** |\n"
     "| **ch71** | **Advanced SQL (windows, CTEs, EXPLAIN, dbt)** | **Data** |\n"
     "| **ch72** | **Databases for AI apps (pgvector, Redis, vector DBs)** | **Data** |", 1, "rm-rows-d")
edit("README.md", "| **ch70** | **Terminal & environments survival (bash, venv, tmux)** | **Applied** |",
     "| **ch70** | **Terminal & environments survival (bash, venv, tmux)** | **Applied** |\n"
     "| **ch73** | **DSA III: heaps, tries, union-find, intervals** | **Applied** |\n"
     "| **ch74** | **Kubernetes for ML (Jobs, GPUs, quotas, autoscale)** | **Applied** |", 1, "rm-rows-a")
edit("README.md", "glossary, 69-Q exam, grades", "glossary, 73-Q exam, grades", 1, "rm-exam-row")
edit("README.md", "(128 terms)", "(136 terms)", 1, "rm-gloss")

print("FAILURES:" if fails else "ALL OK")
for f in fails:
    print(" ", f)
sys.exit(1 if fails else 0)
