#!/usr/bin/env python3
"""Phase 11: wire Ch59-62 (sidebar, nav, exam Q58-61, notes/syllabus/glossary/cheats/cover/README)."""
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

# sidebar F13-16
edit("src/_sidebar.html",
     '      <button class="toc-item" data-go="ch58"><span class="toc-num">F12</span> Recommenders deep-dive</button>\n',
     '      <button class="toc-item" data-go="ch58"><span class="toc-num">F12</span> Recommenders deep-dive</button>\n'
     '      <button class="toc-item" data-go="ch59"><span class="toc-num">F13</span> Injection defense lab</button>\n'
     '      <button class="toc-item" data-go="ch60"><span class="toc-num">F14</span> AI economics & jobs</button>\n'
     '      <button class="toc-item" data-go="ch61"><span class="toc-num">F15</span> Multimodal evals</button>\n'
     '      <button class="toc-item" data-go="ch62"><span class="toc-num">F16</span> Agent red-teaming</button>\n', 1, "sidebar-f")
edit("src/_sidebar.html", "Final exam (57 Q)", "Final exam (61 Q)", 1, "sidebar-exam")

# app.js PAGES + TITLES
edit("js/app.js", '"ch56","ch57","ch58",\n  "ch15"',
     '"ch56","ch57","ch58","ch59","ch60","ch61","ch62",\n  "ch15', 1, "pages")
edit("js/app.js", '  ch58: "Recommenders deep-dive",',
     '  ch58: "Recommenders deep-dive",\n  ch59: "Injection defense lab",\n  ch60: "AI economics & jobs",\n'
     '  ch61: "Multimodal evals",\n  ch62: "Agent red-teaming",', 1, "titles")

# nav (fragments: inherently unique)
edit("src/pages/ch58.html", '<button data-go="ch15">Reinforcement learning →</button>',
     '<button data-go="ch59">Injection defense →</button>', 1, "ch58-next")
edit("src/pages/ch15.html", '<button class="ghost" data-go="ch58">← Recommenders</button>',
     '<button class="ghost" data-go="ch62">← Agent red-teaming</button>', 1, "ch15-prev")

# cover
edit("src/pages/cover.html", '<div class="stat"><b>59</b><span>teaching chapters</span></div>',
     '<div class="stat"><b>63</b><span>teaching chapters</span></div>', 1, "cov-ch")
edit("src/pages/cover.html", '<div class="stat"><b>330+</b><span>scored MCQs</span></div>',
     '<div class="stat"><b>360+</b><span>scored MCQs</span></div>', 1, "cov-mcq")
edit("src/pages/cover.html", "robotics, science, recsys)",
     "robotics, science, recsys, injection lab, economics, multimodal evals, red-teaming)", 1, "cov-lede")
edit("src/pages/cover.html", '            <button data-go="ch58">Recsys (F12)</button>\n',
     '            <button data-go="ch58">Recsys (F12)</button>\n'
     '            <button data-go="ch59">Injection lab (F13)</button>\n'
     '            <button data-go="ch60">Economics (F14)</button>\n'
     '            <button data-go="ch61">MM evals (F15)</button>\n'
     '            <button data-go="ch62">Red-team (F16)</button>\n', 1, "cov-mini")
edit("src/pages/cover.html", "Final exam (57 Q)", "Final exam (61 Q)", 1, "cov-exam")

# how / paths / syllabus / notes
edit("src/pages/how.html", "57 mixed questions covering school through PhD topics",
     "61 mixed questions covering school through PhD topics", 1, "how-exam")
edit("src/pages/how.html", "हिंदी meanings of key terms (Ch 30–58)",
     "हिंदी meanings of key terms (Ch 30–62)", 1, "how-gloss")
edit("src/pages/paths.html", "frontier Ch 47–58 first", "frontier Ch 47–62 first", 1, "paths-ind")
edit("src/pages/paths.html", "frontier (Ch 47–58)", "frontier (Ch 47–62)", 1, "paths-zero")
edit("src/pages/syllabus.html",
     "<li>Frontier (Ch 47–58): AGI, advanced RAG, reasoning, edge, VLMs, voice, video, federated, quantum, robotics, AI-for-science, recsys</li>",
     "<li>Frontier (Ch 47–62): AGI, RAG+, reasoning, edge, VLMs, voice, video, federated, quantum, robotics, science, recsys, injection defence, economics, MM-evals, red-teaming</li>",
     1, "syl")
edit("src/pages/notes.html", "(Ch 47–58)</h4>", "(Ch 47–62)</h4>", 1, "notes-h")
edit("src/pages/notes.html",
     "<li>Science (Ch 57): surrogate → search → validate; prospective bar; recsys (Ch 58): towers + debias.</li>",
     "<li>Science (Ch 57): surrogate → search → validate; prospective bar; recsys (Ch 58): towers + debias.</li>\n"
     "              <li>Security (Ch 59, 62): hierarchy + spotlight + least-privilege + egress; red-team 4 surfaces.</li>\n"
     "              <li>Economics (Ch 60): tasks≠jobs, J-curve, judgment×leverage; MM-evals (Ch 61): L1–L4 + κ.</li>",
     1, "notes")

# cheats +4
cp = ROOT / "src/pages/cheats.html"
cs = cp.read_text()
m = re.search(r'(<div class="cheat-card"><h4>Ch 58 · Rec</h4><ul>.*?</ul></div>)', cs, re.S)
if not m:
    fails.append("cheats :: ch58 card not found")
else:
    cp.write_text(cs.replace(m.group(1), m.group(1) + """
            <div class="cheat-card"><h4>Ch 59 · Inject</h4><ul>
              <li>Tools out = untrusted</li>
              <li>Hierarchy never flips</li>
              <li>Spotlight + dual-LLM</li>
              <li>Egress + secret scans</li>
              <li>ASR suite in CI</li>
            </ul></div>
            <div class="cheat-card"><h4>Ch 60 · Econ</h4><ul>
              <li>Tasks ≠ jobs</li>
              <li>J-curve redesign</li>
              <li>Judgment × leverage</li>
              <li>Sell outcomes</li>
              <li>Public receipts</li>
            </ul></div>
            <div class="cheat-card"><h4>Ch 61 · MME</h4><ul>
              <li>MMMU/POPE/RefCOCO</li>
              <li>L1–L4 stack</li>
              <li>IoU ≥ 0.5, sliced</li>
              <li>Rubrics + blind + κ</li>
              <li>Golden = your data</li>
            </ul></div>
            <div class="cheat-card"><h4>Ch 62 · RedT</h4><ul>
              <li>4 surfaces × goals</li>
              <li>30–60 scenarios</li>
              <li>Traces = deliverable</li>
              <li>Sandbox + kill switch</li>
              <li>Incident → new test</li>
            </ul></div>""", 1))
edit("src/pages/cheats.html", "One card per chapter (Ch 30–58).",
     "One card per chapter (Ch 30–62).", 1, "cheats-lede")

# glossary +1 table (104 → 112)
edit("src/pages/glossary.html", "Every key term from Ch 30–58 with its हिंदी meaning in one line.",
     "Every key term from Ch 30–62 with its हिंदी meaning in one line.", 1, "gloss-lede")
edit("src/pages/glossary.html",
     """            <tr><td>Bandit</td><td>बैंडिट</td><td>नई चीज़ें आज़माओ, अच्छी को बढ़ाओ</td></tr>
          </tbody></table>""",
     """            <tr><td>Bandit</td><td>बैंडिट</td><td>नई चीज़ें आज़माओ, अच्छी को बढ़ाओ</td></tr>
          </tbody></table>
          <h3>Ch 59–62 · Security, economics, evals</h3>
          <table><thead><tr><th>English</th><th>हिंदी</th><th>आसान मतलब</th></tr></thead><tbody>
            <tr><td>Prompt injection</td><td>प्रॉम्प्ट-घुसपैठ</td><td>धोखे से model को ग़लत काम कराना</td></tr>
            <tr><td>Jailbreak</td><td>जेलब्रेक</td><td>मना किए काम के लिए तरकीब से मनाना</td></tr>
            <tr><td>Privilege hierarchy</td><td>अधिकार-क्रम</td><td>system &gt; developer &gt; user &gt; tool</td></tr>
            <tr><td>Egress check</td><td>निकास-जाँच</td><td>बाहर जाते data/पते की रोक-जाँच</td></tr>
            <tr><td>J-curve</td><td>J-वक्र</td><td>पहले गिरावट, फिर तेज़ फ़ायदा (बदलाव के बाद)</td></tr>
            <tr><td>IoU</td><td>IoU (अतिव्यापन)</td><td>box कितना सही — 0.5+ पास</td></tr>
            <tr><td>Red team</td><td>रेड टीम</td><td>जानबूझकर हमला करके कमज़ोरी खोजना</td></tr>
            <tr><td>Sandbox</td><td>सैंडबॉक्स</td><td>सीमित सुरक्षित खेल-मैदान (allowlist + kill switch)</td></tr>
          </tbody></table>""", 1, "gloss-table")
edit("src/pages/glossary.html", "<p>104 terms, 8 per chapter group.",
     "<p>112 terms, 8 per chapter group.", 1, "gloss-count")

# exam Q58-61
edit("src/pages/exam.html", "<h2>Final exam · 57 questions</h2>",
     "<h2>Final exam · 61 questions</h2>", 1, "exam-h2")
edit("src/pages/exam.html",
     "(57 total: Q1–30 core AI + Q31–39 data + Q40–45 eng & production + Q46–57 frontier)",
     "(61 total: Q1–30 core AI + Q31–39 data + Q40–45 eng & production + Q46–61 frontier)",
     1, "exam-scoring")
Q = """
          <div class="mcq" data-answer="c">
            <p class="q">58. The non-negotiable privilege order for agent inputs is:</p>
            <div class="opts">
              <button class="opt" data-opt="a" onclick="selectOpt(this)">A. Tool output outranks everything</button>
              <button class="opt" data-opt="b" onclick="selectOpt(this)">B. Longest text wins</button>
              <button class="opt" data-opt="c" onclick="selectOpt(this)">C. system &gt; developer &gt; user &gt; tool output</button>
              <button class="opt" data-opt="d" onclick="selectOpt(this)">D. User outranks system</button>
            </div>
            <div class="mcq-actions"><button class="btn" onclick="checkOne(this)">Check</button><span class="score-chip"></span></div>
            <div class="explain">Documents never outrank instructions.</div>
          </div>
          <div class="mcq" data-answer="a">
            <p class="q">59. The productivity J-curve implies AI gains accrue to those who:</p>
            <div class="opts">
              <button class="opt" data-opt="a" onclick="selectOpt(this)">A. Redesign workflows (through a dip) rather than garnishing old ones</button>
              <button class="opt" data-opt="b" onclick="selectOpt(this)">B. Buy the most tools fastest</button>
              <button class="opt" data-opt="c" onclick="selectOpt(this)">C. Avoid all change</button>
              <button class="opt" data-opt="d" onclick="selectOpt(this)">D. Ban AI at work</button>
            </div>
            <div class="mcq-actions"><button class="btn" onclick="checkOne(this)">Check</button><span class="score-chip"></span></div>
            <div class="explain">Reorganisation first, compounding later.</div>
          </div>
          <div class="mcq" data-answer="d">
            <p class="q">60. Low inter-rater agreement (κ) in a human eval of VLMs tells you to:</p>
            <div class="opts">
              <button class="opt" data-opt="a" onclick="selectOpt(this)">A. Ship immediately</button>
              <button class="opt" data-opt="b" onclick="selectOpt(this)">B. Delete the models</button>
              <button class="opt" data-opt="c" onclick="selectOpt(this)">C. Add more parameters</button>
              <button class="opt" data-opt="d" onclick="selectOpt(this)">D. Fix the rubric and calibrate raters before trusting any scores</button>
            </div>
            <div class="mcq-actions"><button class="btn" onclick="checkOne(this)">Check</button><span class="score-chip"></span></div>
            <div class="explain">Disagreement measures the test, not the models.</div>
          </div>
          <div class="mcq" data-answer="b">
            <p class="q">61. After an agent security incident, the correct first sequence is:</p>
            <div class="opts">
              <button class="opt" data-opt="a" onclick="selectOpt(this)">A. Delete logs and hope</button>
              <button class="opt" data-opt="b" onclick="selectOpt(this)">B. Freeze the agent → preserve traces → assess blast radius → rotate credentials</button>
              <button class="opt" data-opt="c" onclick="selectOpt(this)">C. Ship new features</button>
              <button class="opt" data-opt="d" onclick="selectOpt(this)">D. Blame the intern</button>
            </div>
            <div class="mcq-actions"><button class="btn" onclick="checkOne(this)">Check</button><span class="score-chip"></span></div>
            <div class="explain">Then notify, post-mortem, and add the scenario to the suite.</div>
          </div>
"""
edit("src/pages/exam.html",
     '          <p style="margin-top:22px">You can check questions one-by-one for study, or submit the whole exam for an official grade.</p>',
     Q + '          <p style="margin-top:22px">You can check questions one-by-one for study, or submit the whole exam for an official grade.</p>',
     1, "exam-qs")

# results
edit("src/pages/results.html", "Take the 57-question final exam, then come back here.",
     "Take the 61-question final exam, then come back here.", 1, "res-blurb")
edit("src/pages/results.html", '<strong id="resTotal">57</strong> correct',
     '<strong id="resTotal">61</strong> correct', 1, "res-total")

# README
edit("README.md", "**58 numbered chapters** (59 teaching units with school)",
     "**62 numbered chapters** (63 teaching units with school)", 1, "rm-count")
edit("README.md", "**330+ MCQs**", "**360+ MCQs**", 1, "rm-mcq")
edit("README.md", "**Final exam (57 questions: 30 core AI + 9 data + 6 eng & production + 12 frontier)**",
     "**Final exam (61 questions: 30 core AI + 9 data + 6 eng & production + 16 frontier)**", 1, "rm-exam")
edit("README.md", "| **ch58** | **Recommenders deep-dive (two-tower, bandits)** | **Frontier** |",
     "| **ch58** | **Recommenders deep-dive (two-tower, bandits)** | **Frontier** |\n"
     "| **ch59** | **Prompt-injection defense lab (hierarchy, red suites)** | **Frontier** |\n"
     "| **ch60** | **AI economics & jobs (J-curve, freelance playbook)** | **Frontier** |\n"
     "| **ch61** | **Multimodal evals (MMMU, POPE, rubrics)** | **Frontier** |\n"
     "| **ch62** | **Agent red-teaming playbook (sandbox, forensics)** | **Frontier** |", 1, "rm-rows")
edit("README.md", "glossary, 57-Q exam, grades", "glossary, 61-Q exam, grades", 1, "rm-exam-row")
edit("README.md", "(104 terms)", "(112 terms)", 1, "rm-gloss")

print("FAILURES:" if fails else "ALL OK")
for f in fails:
    print(" ", f)
sys.exit(1 if fails else 0)
