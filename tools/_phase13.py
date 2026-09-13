#!/usr/bin/env python3
"""Phase 13: wire Ch67-70 (Applied A5-A8: DSA I-II, serving, terminal)."""
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

# sidebar A5-A8 (+ exam label)
edit("src/_sidebar.html",
     '      <button class="toc-item" data-go="ch46"><span class="toc-num">A4</span> Transformers lab</button>\n',
     '      <button class="toc-item" data-go="ch46"><span class="toc-num">A4</span> Transformers lab</button>\n'
     '      <button class="toc-item" data-go="ch67"><span class="toc-num">A5</span> DSA I: Big-O & hashing</button>\n'
     '      <button class="toc-item" data-go="ch68"><span class="toc-num">A6</span> DSA II: trees, graphs, DP</button>\n'
     '      <button class="toc-item" data-go="ch69"><span class="toc-num">A7</span> Serve & demo your model</button>\n'
     '      <button class="toc-item" data-go="ch70"><span class="toc-num">A8</span> Terminal survival</button>\n', 1, "sidebar-a")
edit("src/_sidebar.html", "Final exam (65 Q)", "Final exam (69 Q)", 1, "sidebar-exam")

# app.js PAGES + TITLES
edit("js/app.js", '"ch43","ch46","ch47"',
     '"ch43","ch46","ch67","ch68","ch69","ch70","ch47"', 1, "pages")
edit("js/app.js", '  ch46: "Transformers lab",',
     '  ch46: "Transformers lab",\n  ch67: "DSA I: Big-O & hashing",\n  ch68: "DSA II: trees, graphs, DP",\n'
     '  ch69: "Serve & demo your model",\n  ch70: "Terminal survival",', 1, "titles")

# nav (insert between ch46 and ch47)
edit("src/pages/ch46.html", '<button data-go="ch47">AGI →</button>',
     '<button data-go="ch67">DSA I →</button>', 1, "ch46-next")
edit("src/pages/ch47.html", '<button class="ghost" data-go="ch46">← Transformers lab</button>',
     '<button class="ghost" data-go="ch70">← Terminal survival</button>', 1, "ch47-prev")

# cover
edit("src/pages/cover.html", '<div class="stat"><b>67</b><span>teaching chapters</span></div>',
     '<div class="stat"><b>71</b><span>teaching chapters</span></div>', 1, "cov-ch")
edit("src/pages/cover.html", '<div class="stat"><b>380+</b><span>scored MCQs</span></div>',
     '<div class="stat"><b>400+</b><span>scored MCQs</span></div>', 1, "cov-mcq")
edit("src/pages/cover.html", '<div class="stat"><b>200+</b><span>practice questions</span></div>',
     '<div class="stat"><b>220+</b><span>practice questions</span></div>', 1, "cov-prac")
edit("src/pages/cover.html", '<div class="stat"><b>65</b><span>final exam questions</span></div>',
     '<div class="stat"><b>69</b><span>final exam questions</span></div>', 1, "cov-exam-n")
edit("src/pages/cover.html", "industry practice, transformers lab, interview prep",
     "industry practice, transformers lab, DSA I–II, model serving, terminal survival, interview prep", 1, "cov-lede")
edit("src/pages/cover.html", '            <button data-go="ch46">Transformers lab (A4)</button>\n',
     '            <button data-go="ch46">Transformers lab (A4)</button>\n'
     '            <button data-go="ch67">DSA I (A5)</button>\n'
     '            <button data-go="ch68">DSA II (A6)</button>\n'
     '            <button data-go="ch69">Serving (A7)</button>\n'
     '            <button data-go="ch70">Terminal (A8)</button>\n', 1, "cov-mini")
edit("src/pages/cover.html", "Final exam (65 Q)", "Final exam (69 Q)", 1, "cov-exam")

# how / paths / syllabus / notes
edit("src/pages/how.html", "65 mixed questions covering school through PhD topics",
     "69 mixed questions covering school through PhD topics", 1, "how-exam")
edit("src/pages/how.html", "हिंदी meanings of key terms (Ch 30–66)",
     "हिंदी meanings of key terms (Ch 30–70)", 1, "how-gloss")
edit("src/pages/paths.html", "applied Ch 42–44 + Ch 46 and frontier Ch 47–66 first",
     "applied Ch 42–44 + Ch 46 + Ch 67–70 and frontier Ch 47–66 first", 1, "paths-ind")
edit("src/pages/paths.html", "applied production (Ch 42–44 + Ch 46) → frontier (Ch 47–66)",
     "applied production (Ch 42–44 + Ch 46 + Ch 67–70) → frontier (Ch 47–66)", 1, "paths-zero")
edit("src/pages/syllabus.html",
     "<li>Applied production (Ch 42–44): prompt patterns, RAG + evals, Docker, cloud GPUs, MLOps lifecycle, canary deploys</li>",
     "<li>Applied production (Ch 42–44, 46, 67–70): prompt patterns, RAG + evals, Docker, cloud GPUs, MLOps lifecycle, transformers lab, DSA I–II, model serving + demos, terminal survival</li>",
     1, "syl")
edit("src/pages/notes.html", "Applied production: RAG, cloud, MLOps (Ch 42–44, 46)",
     "Applied production: RAG, cloud, MLOps, coding (Ch 42–44, 46, 67–70)", 1, "notes-h")
edit("src/pages/notes.html",
     "<li>Transformers lab (Ch 46): template versioned; LoRA r8–64; golden+red evals; serve quantised.</li>",
     "<li>Transformers lab (Ch 46): template versioned; LoRA r8–64; golden+red evals; serve quantised.</li>\n"
     "              <li>DSA (Ch 67–68): Big-O aloud; bisect/two-pointers/hash; BFS/DFS + visited; DP = remember.</li>\n"
     "              <li>Ship it (Ch 69–70): FastAPI load-once + Pydantic; one venv per project; tmux; nvidia-smi.</li>",
     1, "notes")

# cheats +4 (append after Ch 66 card; numeric order)
cp = ROOT / "src/pages/cheats.html"
cs = cp.read_text()
m = re.search(r'(<div class="cheat-card"><h4>Ch 66 · TData</h4><ul>.*?</ul></div>)', cs, re.S)
if not m:
    fails.append("cheats :: ch66 card not found")
else:
    cp.write_text(cs.replace(m.group(1), m.group(1) + """
            <div class="cheat-card"><h4>Ch 67 · DSA1</h4><ul>
              <li>O: 1, log n, n, n log n</li>
              <li>Sorted = bisect</li>
              <li>Pairs = two pointers</li>
              <li>Seen = hash map</li>
              <li>deque, join, set</li>
            </ul></div>
            <div class="cheat-card"><h4>Ch 68 · DSA2</h4><ul>
              <li>Base + shrink</li>
              <li>lru_cache = DP</li>
              <li>BFS shortest/queue</li>
              <li>Visited set always</li>
              <li>Topo-sort deps</li>
            </ul></div>
            <div class="cheat-card"><h4>Ch 69 · Serve</h4><ul>
              <li>Load model once</li>
              <li>Pydantic limits</li>
              <li>curl, then UI</li>
              <li>Spaces cheap-first</li>
              <li>Log predictions</li>
            </ul></div>
            <div class="cheat-card"><h4>Ch 70 · Term</h4><ul>
              <li>grep, tail -f</li>
              <li>One env per proj</li>
              <li>SSH keys</li>
              <li>tmux sessions</li>
              <li>nvidia-smi, rsync</li>
            </ul></div>""", 1))
edit("src/pages/cheats.html", "One card per chapter (Ch 30–66).",
     "One card per chapter (Ch 30–70).", 1, "cheats-lede")

# glossary +1 table (120 → 128)
edit("src/pages/glossary.html", "Every key term from Ch 30–66 with its",
     "Every key term from Ch 30–70 with its", 1, "gloss-lede")
edit("src/pages/glossary.html",
     """            <tr><td>Provenance</td><td>उद्गम-रिकॉर्ड</td><td>data कहाँ से, किस लाइसेंस पर</td></tr>
          </tbody></table>""",
     """            <tr><td>Provenance</td><td>उद्गम-रिकॉर्ड</td><td>data कहाँ से, किस लाइसेंस पर</td></tr>
          </tbody></table>
          <h3>Ch 67–70 · DSA, serving, terminal</h3>
          <table><thead><tr><th>English</th><th>हिंदी</th><th>आसान मतलब</th></tr></thead><tbody>
            <tr><td>Big-O</td><td>बिग-O</td><td>input बढ़ने पर चाल की रफ़्तार (लागत का अंदाज़ा)</td></tr>
            <tr><td>Hash map</td><td>हैश-नक्शा</td><td>तुरंत खोज वाली सूची (dict/set)</td></tr>
            <tr><td>Recursion</td><td>रिकर्शन</td><td>खुद को छोटे हिस्से पर दोहराना</td></tr>
            <tr><td>Binary tree</td><td>बाइनरी-पेड़</td><td>हर गाँठ से दो शाखाएँ</td></tr>
            <tr><td>BFS / DFS</td><td>BFS/DFS</td><td>graph घूमना — परत-दर-परत / गहराई तक</td></tr>
            <tr><td>Endpoint</td><td>एंडपॉइंट</td><td>API का पता (जैसे /predict)</td></tr>
            <tr><td>Virtualenv</td><td>वर्चुअल-वातावरण</td><td>हर project का अलग Python-संसार</td></tr>
            <tr><td>tmux</td><td>tmux</td><td>टूटे बिना चलता terminal-सत्र (server पर अमर)</td></tr>
          </tbody></table>""", 1, "gloss-table")
edit("src/pages/glossary.html", "<p>120 terms, 8 per chapter group.",
     "<p>128 terms, 8 per chapter group.", 1, "gloss-count")

# exam Q66-69
edit("src/pages/exam.html", "<h2>Final exam · 65 questions</h2>",
     "<h2>Final exam · 69 questions</h2>", 1, "exam-h2")
edit("src/pages/exam.html",
     "(65 total: Q1–30 core AI + Q31–39 data + Q40–45 eng & production + Q46–65 frontier)",
     "(69 total: Q1–30 core AI + Q31–39 data + Q40–45 eng & production + Q46–65 frontier + Q66–69 applied coding)",
     1, "exam-scoring")
Q = """
          <div class="mcq" data-answer="b">
            <p class="q">66. Binary search needs sorted input and runs in:</p>
            <div class="opts">
              <button class="opt" data-opt="a" onclick="selectOpt(this)">A. O(n²)</button>
              <button class="opt" data-opt="b" onclick="selectOpt(this)">B. O(log n) by halving the range each step</button>
              <button class="opt" data-opt="c" onclick="selectOpt(this)">C. O(n!)</button>
              <button class="opt" data-opt="d" onclick="selectOpt(this)">D. O(1) always</button>
            </div>
            <div class="mcq-actions"><button class="btn" onclick="checkOne(this)">Check</button><span class="score-chip"></span></div>
            <div class="explain">Halving wins.</div>
          </div>
          <div class="mcq" data-answer="d">
            <p class="q">67. Shortest path in an unweighted graph is found with:</p>
            <div class="opts">
              <button class="opt" data-opt="a" onclick="selectOpt(this)">A. DFS</button>
              <button class="opt" data-opt="b" onclick="selectOpt(this)">B. Quicksort</button>
              <button class="opt" data-opt="c" onclick="selectOpt(this)">C. Binary search</button>
              <button class="opt" data-opt="d" onclick="selectOpt(this)">D. BFS with a queue + visited set</button>
            </div>
            <div class="mcq-actions"><button class="btn" onclick="checkOne(this)">Check</button><span class="score-chip"></span></div>
            <div class="explain">BFS explores in distance order.</div>
          </div>
          <div class="mcq" data-answer="a">
            <p class="q">68. In a FastAPI app, the model should be loaded:</p>
            <div class="opts">
              <button class="opt" data-opt="a" onclick="selectOpt(this)">A. Once at startup, shared by all requests</button>
              <button class="opt" data-opt="b" onclick="selectOpt(this)">B. Inside every request</button>
              <button class="opt" data-opt="c" onclick="selectOpt(this)">C. In the browser</button>
              <button class="opt" data-opt="d" onclick="selectOpt(this)">D. Never — models load themselves</button>
            </div>
            <div class="mcq-actions"><button class="btn" onclick="checkOne(this)">Check</button><span class="score-chip"></span></div>
            <div class="explain">Per-request loading wastes seconds.</div>
          </div>
          <div class="mcq" data-answer="c">
            <p class="q">69. One virtualenv per project exists because:</p>
            <div class="opts">
              <button class="opt" data-opt="a" onclick="selectOpt(this)">A. Venvs speed up code</button>
              <button class="opt" data-opt="b" onclick="selectOpt(this)">B. Python bills per project</button>
              <button class="opt" data-opt="c" onclick="selectOpt(this)">C. Projects need conflicting versions — isolation keeps them reproducible</button>
              <button class="opt" data-opt="d" onclick="selectOpt(this)">D. Disks are too empty</button>
            </div>
            <div class="mcq-actions"><button class="btn" onclick="checkOne(this)">Check</button><span class="score-chip"></span></div>
            <div class="explain">Isolate or perish.</div>
          </div>
"""
edit("src/pages/exam.html",
     '          <p style="margin-top:22px">You can check questions one-by-one for study, or submit the whole exam for an official grade.</p>',
     Q + '          <p style="margin-top:22px">You can check questions one-by-one for study, or submit the whole exam for an official grade.</p>',
     1, "exam-qs")

# results
edit("src/pages/results.html", "Take the 65-question final exam, then come back here.",
     "Take the 69-question final exam, then come back here.", 1, "res-blurb")
edit("src/pages/results.html", '<strong id="resTotal">65</strong> correct',
     '<strong id="resTotal">69</strong> correct', 1, "res-total")

# README
edit("README.md", "**66 numbered chapters** (67 teaching units with school)",
     "**70 numbered chapters** (71 teaching units with school)", 1, "rm-count")
edit("README.md", "**380+ MCQs**", "**400+ MCQs**", 1, "rm-mcq")
edit("README.md", "**Final exam (65 questions: 30 core AI + 9 data + 6 eng & production + 20 frontier)**",
     "**Final exam (69 questions: 30 core AI + 9 data + 10 eng & production + 20 frontier)**", 1, "rm-exam")
edit("README.md", "| **ch46** | **Transformers lab (tokenizers, LoRA, vLLM serving)** | **Applied** |",
     "| **ch46** | **Transformers lab (tokenizers, LoRA, vLLM serving)** | **Applied** |\n"
     "| **ch67** | **DSA I: Big-O, arrays, hashing (binary search, pointers)** | **Applied** |\n"
     "| **ch68** | **DSA II: recursion, trees, graphs, DP (BFS, Dijkstra)** | **Applied** |\n"
     "| **ch69** | **Serve & demo your model (FastAPI, Streamlit, Gradio)** | **Applied** |\n"
     "| **ch70** | **Terminal & environments survival (bash, venv, tmux)** | **Applied** |", 1, "rm-rows")
edit("README.md", "glossary, 65-Q exam, grades", "glossary, 69-Q exam, grades", 1, "rm-exam-row")
edit("README.md", "(120 terms)", "(128 terms)", 1, "rm-gloss")

print("FAILURES:" if fails else "ALL OK")
for f in fails:
    print(" ", f)
sys.exit(1 if fails else 0)
