#!/usr/bin/env python3
"""Phase 12: wire Ch63-66 (sidebar, nav, exam Q62-65, notes/syllabus/glossary/cheats/cover/README)."""
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

# sidebar F17-20 (+ exam label)
edit("src/_sidebar.html",
     '      <button class="toc-item" data-go="ch62"><span class="toc-num">F16</span> Agent red-teaming</button>\n',
     '      <button class="toc-item" data-go="ch62"><span class="toc-num">F16</span> Agent red-teaming</button>\n'
     '      <button class="toc-item" data-go="ch63"><span class="toc-num">F17</span> Coding agents</button>\n'
     '      <button class="toc-item" data-go="ch64"><span class="toc-num">F18</span> Synthetic data</button>\n'
     '      <button class="toc-item" data-go="ch65"><span class="toc-num">F19</span> Indic languages</button>\n'
     '      <button class="toc-item" data-go="ch66"><span class="toc-num">F20</span> Training data</button>\n', 1, "sidebar-f")
edit("src/_sidebar.html", "Final exam (61 Q)", "Final exam (65 Q)", 1, "sidebar-exam")

# app.js PAGES + TITLES (quotes symmetric on both sides)
edit("js/app.js", '"ch61","ch62",\n  "ch15"',
     '"ch61","ch62","ch63","ch64","ch65","ch66",\n  "ch15"', 1, "pages")
edit("js/app.js", '  ch62: "Agent red-teaming",',
     '  ch62: "Agent red-teaming",\n  ch63: "Coding agents",\n  ch64: "Synthetic data",\n'
     '  ch65: "Indic languages",\n  ch66: "Training data",', 1, "titles")

# nav
edit("src/pages/ch62.html", '<button data-go="ch15">Reinforcement learning →</button>',
     '<button data-go="ch63">Coding agents →</button>', 1, "ch62-next")
edit("src/pages/ch15.html", '<button class="ghost" data-go="ch62">← Agent red-teaming</button>',
     '<button class="ghost" data-go="ch66">← Training data</button>', 1, "ch15-prev")

# cover
edit("src/pages/cover.html", '<div class="stat"><b>63</b><span>teaching chapters</span></div>',
     '<div class="stat"><b>67</b><span>teaching chapters</span></div>', 1, "cov-ch")
edit("src/pages/cover.html", '<div class="stat"><b>360+</b><span>scored MCQs</span></div>',
     '<div class="stat"><b>380+</b><span>scored MCQs</span></div>', 1, "cov-mcq")
edit("src/pages/cover.html", '<div class="stat"><b>190+</b><span>practice questions</span></div>',
     '<div class="stat"><b>200+</b><span>practice questions</span></div>', 1, "cov-prac")
edit("src/pages/cover.html", '<div class="stat"><b>61</b><span>final exam questions</span></div>',
     '<div class="stat"><b>65</b><span>final exam questions</span></div>', 1, "cov-exam-n")
edit("src/pages/cover.html", "multimodal evals, red-teaming)",
     "multimodal evals, red-teaming, coding agents, synthetic data, Indic languages, training data)", 1, "cov-lede")
edit("src/pages/cover.html", '            <button data-go="ch62">Red-team (F16)</button>\n',
     '            <button data-go="ch62">Red-team (F16)</button>\n'
     '            <button data-go="ch63">Code agents (F17)</button>\n'
     '            <button data-go="ch64">Synth data (F18)</button>\n'
     '            <button data-go="ch65">Indic langs (F19)</button>\n'
     '            <button data-go="ch66">Train data (F20)</button>\n', 1, "cov-mini")
edit("src/pages/cover.html", "Final exam (61 Q)", "Final exam (65 Q)", 1, "cov-exam")

# how / paths / syllabus / notes
edit("src/pages/how.html", "61 mixed questions covering school through PhD topics",
     "65 mixed questions covering school through PhD topics", 1, "how-exam")
edit("src/pages/how.html", "हिंदी meanings of key terms (Ch 30–62)",
     "हिंदी meanings of key terms (Ch 30–66)", 1, "how-gloss")
edit("src/pages/paths.html", "frontier Ch 47–62 first", "frontier Ch 47–66 first", 1, "paths-ind")
edit("src/pages/paths.html", "frontier (Ch 47–62)", "frontier (Ch 47–66)", 1, "paths-zero")
edit("src/pages/syllabus.html",
     "<li>Frontier (Ch 47–62): AGI, RAG+, reasoning, edge, VLMs, voice, video, federated, quantum, robotics, science, recsys, injection defence, economics, MM-evals, red-teaming</li>",
     "<li>Frontier (Ch 47–66): AGI, RAG+, reasoning, edge, VLMs, voice, video, federated, quantum, robotics, science, recsys, injection defence, economics, MM-evals, red-teaming, code agents, synth data, Indic, training data</li>",
     1, "syl")
edit("src/pages/notes.html", "(Ch 47–62)</h4>", "(Ch 47–66)</h4>", 1, "notes-h")
edit("src/pages/notes.html",
     "<li>Economics (Ch 60): tasks≠jobs, J-curve, judgment×leverage; MM-evals (Ch 61): L1–L4 + κ.</li>",
     "<li>Economics (Ch 60): tasks≠jobs, J-curve, judgment×leverage; MM-evals (Ch 61): L1–L4 + κ.</li>\n"
     "              <li>Code agents (Ch 63): tests = spec, repo context, sandbox + human gates.</li>\n"
     "              <li>Data (Ch 64–66): verify synthetic, mind fertility, dedup + licence per row.</li>",
     1, "notes")

# cheats +4
cp = ROOT / "src/pages/cheats.html"
cs = cp.read_text()
m = re.search(r'(<div class="cheat-card"><h4>Ch 62 · RedT</h4><ul>.*?</ul></div>)', cs, re.S)
if not m:
    fails.append("cheats :: ch62 card not found")
else:
    cp.write_text(cs.replace(m.group(1), m.group(1) + """
            <div class="cheat-card"><h4>Ch 63 · Code</h4><ul>
              <li>Tests = spec</li>
              <li>Repo context indexed</li>
              <li>Small patches + CI</li>
              <li>Sandbox + human gates</li>
              <li>Traces on every PR</li>
            </ul></div>
            <div class="cheat-card"><h4>Ch 64 · Synth</h4><ul>
              <li>Seeds anchor truth</li>
              <li>Verify ladder</li>
              <li>Real data every mix</li>
              <li>Dedup vs evals</li>
              <li>Log licences</li>
            </ul></div>
            <div class="cheat-card"><h4>Ch 65 · Indic</h4><ul>
              <li>Fertility = cost</li>
              <li>Test roman + mixes</li>
              <li>Translationese lies</li>
              <li>Native judges + κ</li>
              <li>Adapt small &gt; big</li>
            </ul></div>
            <div class="cheat-card"><h4>Ch 66 · TData</h4><ul>
              <li>Extraction first</li>
              <li>Fuzzy dedup</li>
              <li>Quarantine evals</li>
              <li>Licence per row</li>
              <li>Datasheets always</li>
            </ul></div>""", 1))
edit("src/pages/cheats.html", "One card per chapter (Ch 30–62).",
     "One card per chapter (Ch 30–66).", 1, "cheats-lede")

# glossary +1 table (112 → 120)
edit("src/pages/glossary.html", "Every key term from Ch 30–62 with its",
     "Every key term from Ch 30–66 with its", 1, "gloss-lede")
edit("src/pages/glossary.html",
     """            <tr><td>Sandbox</td><td>सैंडबॉक्स</td><td>सीमित सुरक्षित खेल-मैदान (allowlist + kill switch)</td></tr>
          </tbody></table>""",
     """            <tr><td>Sandbox</td><td>सैंडबॉक्स</td><td>सीमित सुरक्षित खेल-मैदान (allowlist + kill switch)</td></tr>
          </tbody></table>
          <h3>Ch 63–66 · Code agents, data, languages</h3>
          <table><thead><tr><th>English</th><th>हिंदी</th><th>आसान मतलब</th></tr></thead><tbody>
            <tr><td>SWE-bench</td><td>SWE-बेंच</td><td>असली GitHub मुद्दों पर कोड-एजेंट की परीक्षा</td></tr>
            <tr><td>Distillation</td><td>डिस्टिलेशन</td><td>बड़े model से छोटा-सस्ता model बनाना</td></tr>
            <tr><td>Model collapse</td><td>मॉडल-संकुचन</td><td>नक़ली data दोहराने से विविधता मरना</td></tr>
            <tr><td>Fertility</td><td>फर्टिलिटी</td><td>एक शब्द पर कितने टोकन (लागत/संदर्भ)</td></tr>
            <tr><td>Code-switching</td><td>कोड-मिक्सिंग</td><td>वाक्य में भाषा बदलना (Hinglish)</td></tr>
            <tr><td>Translationese</td><td>अनुवादिया-भाषा</td><td>अनुवाद-जैसी बनावटी भाषा (मूल्यांकन-भ्रम)</td></tr>
            <tr><td>Dedup</td><td>डुप्लिकेट-सफ़ाई</td><td>दोहरी सामग्री हटाना (exact + fuzzy)</td></tr>
            <tr><td>Provenance</td><td>उद्गम-रिकॉर्ड</td><td>data कहाँ से, किस लाइसेंस पर</td></tr>
          </tbody></table>""", 1, "gloss-table")
edit("src/pages/glossary.html", "<p>112 terms, 8 per chapter group.",
     "<p>120 terms, 8 per chapter group.", 1, "gloss-count")

# exam Q62-65
edit("src/pages/exam.html", "<h2>Final exam · 61 questions</h2>",
     "<h2>Final exam · 65 questions</h2>", 1, "exam-h2")
edit("src/pages/exam.html",
     "(61 total: Q1–30 core AI + Q31–39 data + Q40–45 eng & production + Q46–61 frontier)",
     "(65 total: Q1–30 core AI + Q31–39 data + Q40–45 eng & production + Q46–65 frontier)",
     1, "exam-scoring")
Q = """
          <div class="mcq" data-answer="b">
            <p class="q">62. A coding agent's task is verifiably done when:</p>
            <div class="opts">
              <button class="opt" data-opt="a" onclick="selectOpt(this)">A. It writes a long summary</button>
              <button class="opt" data-opt="b" onclick="selectOpt(this)">B. Fail-to-pass tests pass with no regressions</button>
              <button class="opt" data-opt="c" onclick="selectOpt(this)">C. The diff exceeds 1000 lines</button>
              <button class="opt" data-opt="d" onclick="selectOpt(this)">D. It says "trust me"</button>
            </div>
            <div class="mcq-actions"><button class="btn" onclick="checkOne(this)">Check</button><span class="score-chip"></span></div>
            <div class="explain">Tests are the spec.</div>
          </div>
          <div class="mcq" data-answer="a">
            <p class="q">63. Training each generation purely on the previous generation's synthetic outputs causes:</p>
            <div class="opts">
              <button class="opt" data-opt="a" onclick="selectOpt(this)">A. Model collapse — tails vanish, outputs converge to the bland mean</button>
              <button class="opt" data-opt="b" onclick="selectOpt(this)">B. Infinite intelligence growth</button>
              <button class="opt" data-opt="c" onclick="selectOpt(this)">C. Free GPUs</button>
              <button class="opt" data-opt="d" onclick="selectOpt(this)">D. Nothing at all</button>
            </div>
            <div class="mcq-actions"><button class="btn" onclick="checkOne(this)">Check</button><span class="score-chip"></span></div>
            <div class="explain">Keep real data in every mix.</div>
          </div>
          <div class="mcq" data-answer="d">
            <p class="q">64. High tokenizer fertility for a language directly increases:</p>
            <div class="opts">
              <button class="opt" data-opt="a" onclick="selectOpt(this)">A. Model kindness</button>
              <button class="opt" data-opt="b" onclick="selectOpt(this)">B. Font size</button>
              <button class="opt" data-opt="c" onclick="selectOpt(this)">C. Test accuracy automatically</button>
              <button class="opt" data-opt="d" onclick="selectOpt(this)">D. Cost, latency, and effective-context pressure per word</button>
            </div>
            <div class="mcq-actions"><button class="btn" onclick="checkOne(this)">Check</button><span class="score-chip"></span></div>
            <div class="explain">Tokenization is an uneven tax.</div>
          </div>
          <div class="mcq" data-answer="c">
            <p class="q">65. Eval decontamination (removing benchmark items from training) matters because:</p>
            <div class="opts">
              <button class="opt" data-opt="a" onclick="selectOpt(this)">A. Benchmarks are heavy</button>
              <button class="opt" data-opt="b" onclick="selectOpt(this)">B. GPUs overheat on evals</button>
              <button class="opt" data-opt="c" onclick="selectOpt(this)">C. Leaked evals make leaderboards fiction instead of measurement</button>
              <button class="opt" data-opt="d" onclick="selectOpt(this)">D. Evals are copyrighted by exams</button>
            </div>
            <div class="mcq-actions"><button class="btn" onclick="checkOne(this)">Check</button><span class="score-chip"></span></div>
            <div class="explain">Quarantine evals before the first run.</div>
          </div>
"""
edit("src/pages/exam.html",
     '          <p style="margin-top:22px">You can check questions one-by-one for study, or submit the whole exam for an official grade.</p>',
     Q + '          <p style="margin-top:22px">You can check questions one-by-one for study, or submit the whole exam for an official grade.</p>',
     1, "exam-qs")

# results
edit("src/pages/results.html", "Take the 61-question final exam, then come back here.",
     "Take the 65-question final exam, then come back here.", 1, "res-blurb")
edit("src/pages/results.html", '<strong id="resTotal">61</strong> correct',
     '<strong id="resTotal">65</strong> correct', 1, "res-total")

# README
edit("README.md", "**62 numbered chapters** (63 teaching units with school)",
     "**66 numbered chapters** (67 teaching units with school)", 1, "rm-count")
edit("README.md", "**360+ MCQs**", "**380+ MCQs**", 1, "rm-mcq")
edit("README.md", "**Final exam (61 questions: 30 core AI + 9 data + 6 eng & production + 16 frontier)**",
     "**Final exam (65 questions: 30 core AI + 9 data + 6 eng & production + 20 frontier)**", 1, "rm-exam")
edit("README.md", "| **ch62** | **Agent red-teaming playbook (sandbox, forensics)** | **Frontier** |",
     "| **ch62** | **Agent red-teaming playbook (sandbox, forensics)** | **Frontier** |\n"
     "| **ch63** | **Coding agents & repo-level AI (SWE-bench, guardrails)** | **Frontier** |\n"
     "| **ch64** | **Synthetic data & distillation (flywheel, collapse)** | **Frontier** |\n"
     "| **ch65** | **Indic & low-resource languages (fertility, native evals)** | **Frontier** |\n"
     "| **ch66** | **Training-data engineering (dedup, licensing, provenance)** | **Frontier** |", 1, "rm-rows")
edit("README.md", "glossary, 61-Q exam, grades", "glossary, 65-Q exam, grades", 1, "rm-exam-row")
edit("README.md", "(112 terms)", "(120 terms)", 1, "rm-gloss")

print("FAILURES:" if fails else "ALL OK")
for f in fails:
    print(" ", f)
sys.exit(1 if fails else 0)
