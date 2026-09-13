/* Zero to Hero AI Course — navigation, quizzes, scoring */

const PAGES = [
  "cover","how","paths","syllabus","sch1",
  "ch1","ch2","ch3","ch4","ch5","ch6",
  "ch30","ch31","ch32","ch33","ch34","ch35","ch36","ch37","ch38","ch39","ch40","ch41","ch45",
  "ch17","ch18",
  "ch7","ch8","ch9",
  "ch19","ch20",
  "ch10","ch11","ch21",
  "ch12","ch13","ch14","ch22",
  "ch23","ch24","ch42","ch44","ch43","ch46","ch47","ch48","ch49","ch50","ch51","ch52","ch53","ch54","ch55","ch56","ch57","ch58","ch59","ch60","ch61","ch62",
  "ch15","ch25","ch26",
  "ch27","ch28","ch29","ch16",
  "notes","glossary","cheats","playground","interview","design","gate","mock","exam","results"
];

const TITLES = {
  cover: "Cover",
  how: "How to use this book",
  paths: "Learning paths (Class 1 → PhD)",
  syllabus: "Complete syllabus",
  sch1: "AI for school",
  ch1: "What is AI?",
  ch2: "History of AI",
  ch3: "Types of AI",
  ch4: "Mathematics for AI",
  ch5: "Python for AI",
  ch6: "Data & Features",
  ch7: "ML Fundamentals",
  ch8: "Supervised Learning",
  ch9: "Unsupervised Learning",
  ch10: "Neural Networks",
  ch11: "Deep Learning",
  ch12: "NLP",
  ch13: "Transformers & LLMs",
  ch14: "Generative AI",
  ch15: "Reinforcement Learning",
  ch16: "Ethics, MLOps & Career",
  ch17: "Search, games & classical AI",
  ch18: "Logic, knowledge & planning",
  ch19: "Bayesian ML & causality",
  ch20: "Recommenders, search & knowledge graphs",
  ch21: "Vision, speech & multimodal",
  ch22: "Fine-tuning, PEFT & evals",
  ch23: "AI Agents",
  ch24: "Agentic AI systems",
  ch25: "Advanced RL & world models",
  ch26: "Graphs, time series, AutoML & robotics",
  ch27: "Learning theory (PhD)",
  ch28: "XAI, alignment, adversarial & privacy",
  ch29: "Systems, hardware & research methods",
  ch30: "Python in depth",
  ch31: "Excel & Sheets",
  ch32: "Pandas & NumPy",
  ch33: "SQL for data & AI",
  ch34: "Visualization & story",
  ch35: "Statistics for analysis",
  ch36: "Power BI & dashboards",
  ch37: "Capstone data project",
  ch38: "BI tools compared",
  ch39: "Data engineering & big data",
  ch40: "APIs & web scraping",
  ch41: "Git & collaboration",
  ch42: "Prompt eng, RAG & evals",
  ch43: "MLOps in production",
  ch44: "Cloud, Docker & GPUs",
  ch45: "Time series & forecasting",
  ch46: "Transformers lab",
  ch47: "AGI: benchmarks & safety",
  ch48: "Advanced RAG",
  ch49: "Reasoning models",
  ch50: "Small models & edge AI",
  ch51: "Vision-language models",
  ch52: "Voice agents & speech",
  ch53: "Video generation",
  ch54: "Federated learning",
  ch55: "Quantum ML primer",
  ch56: "Robotics & VLA",
  ch57: "AI for science",
  ch58: "Recommenders deep-dive",
  ch59: "Injection defense lab",
  ch60: "AI economics & jobs",
  ch61: "Multimodal evals",
  ch62: "Agent red-teaming",
  glossary: "Hindi glossary (data skills)",
  cheats: "Cheat-sheet cards",
  playground: "Datasets playground",
  interview: "Interview Q&A bank",
  design: "System design walkthroughs",
  gate: "GATE / UG question bank",
  mock: "Mock interview mode",
  notes: "Revision short notes",
  exam: "Final exam",
  results: "Your results"
};

const storage = {
  get() {
    try { return JSON.parse(localStorage.getItem("zh-ai-course") || "{}"); }
    catch { return {}; }
  },
  set(data) { localStorage.setItem("zh-ai-course", JSON.stringify(data)); }
};

function isLesson(id) {
  return id.startsWith("ch") || id.startsWith("sch");
}

function pageFile(id) {
  return id === "cover" ? "index.html" : id + ".html";
}
function currentPage() {
  const f = location.pathname.split("/").pop() || "index.html";
  if (f === "index.html" || f === "" || f === "/") return "cover";
  return f.replace(/\.html$/, "");
}
function markSeen(id) {
  const st = storage.get();
  st.page = id;
  if (isLesson(id) || id === "notes" || id === "exam" || id === "syllabus" || id === "paths") {
    st.seen = st.seen || {};
    st.seen[id] = true;
  }
  storage.set(st);
}
function go(id) {
  if ("speechSynthesis" in window) { try { speechSynthesis.cancel(); } catch (e) {} }
  if (!PAGES.includes(id)) id = "cover";
  markSeen(id);
  if (id === currentPage()) { window.scrollTo(0, 0); closeMenu(); return; }
  window.location.href = pageFile(id);
}

function openMenu() {
  document.getElementById("sidebar").classList.add("open");
  document.getElementById("backdrop").classList.add("show");
}
function closeMenu() {
  document.getElementById("sidebar").classList.remove("open");
  document.getElementById("backdrop").classList.remove("show");
}

function updateProgress() {
  const st = storage.get();
  const chapters = PAGES.filter(isLesson);
  const seen = chapters.filter(c => st.seen && st.seen[c]).length;
  const pct = Math.round((seen / chapters.length) * 100);
  const bar = document.getElementById("progressBar");
  const lab = document.getElementById("progressLabel");
  if (bar) bar.style.width = pct + "%";
  if (lab) lab.textContent = pct + "% read";
}

function selectOpt(btn) {
  const mcq = btn.closest(".mcq");
  if (mcq.classList.contains("graded")) return;
  mcq.querySelectorAll(".opt").forEach(o => o.classList.remove("selected"));
  btn.classList.add("selected");
}

function gradeMcq(mcq) {
  const answer = mcq.dataset.answer;
  const selected = mcq.querySelector(".opt.selected");
  if (!selected) {
    mcq.querySelector(".hint-pick")?.remove();
    const h = document.createElement("div");
    h.className = "hint-pick";
    h.style.cssText = "color:#be123c;font-size:14px;margin-top:8px;";
    h.textContent = "Pick an option first.";
    mcq.querySelector(".mcq-actions").before(h);
    return false;
  }
  mcq.querySelector(".hint-pick")?.remove();
  mcq.classList.add("graded");
  mcq.querySelectorAll(".opt").forEach(o => {
    if (o.dataset.opt === answer) o.classList.add("correct");
    if (o.classList.contains("selected") && o.dataset.opt !== answer) o.classList.add("wrong");
  });
  const ok = selected.dataset.opt === answer;
  const chip = mcq.querySelector(".score-chip");
  if (chip) {
    chip.textContent = ok ? "Correct" : "Incorrect";
    chip.className = "score-chip " + (ok ? "ok" : "bad");
  }
  return ok;
}

function checkOne(btn) {
  gradeMcq(btn.closest(".mcq"));
}

function checkChapter(chapterId) {
  const root = document.getElementById(chapterId);
  const mcqs = [...root.querySelectorAll(".mcq")];
  let correct = 0;
  mcqs.forEach(m => {
    const r = gradeMcq(m);
    if (r) correct += 1;
  });
  const answered = mcqs.filter(m => m.querySelector(".opt.selected")).length;
  const box = root.querySelector(".chapter-score");
  if (box) {
    box.classList.add("show");
    const pct = mcqs.length ? Math.round((correct / mcqs.length) * 100) : 0;
    box.innerHTML = `<strong>Chapter result:</strong> ${correct} / ${mcqs.length} correct (${pct}%). ${answered < mcqs.length ? "Some questions were skipped." : "All questions attempted."}`;
  }
  const st = storage.get();
  st.chapter = st.chapter || {};
  st.chapter[chapterId] = { correct, total: mcqs.length };
  storage.set(st);
}

function revealAnswer(btn) {
  const p = btn.closest(".practice");
  p.querySelector(".answer").classList.add("show");
  btn.textContent = "Answer shown";
  btn.disabled = true;
}

function markPractice(btn, val) {
  const wrap = btn.parentElement;
  wrap.querySelectorAll("button").forEach(b => b.classList.remove("on-yes", "on-no"));
  btn.classList.add(val === "yes" ? "on-yes" : "on-no");
  const id = btn.closest(".practice").dataset.pid;
  const st = storage.get();
  st.practice = st.practice || {};
  st.practice[id] = val;
  storage.set(st);
}

function gradeExam() {
  const root = document.getElementById("exam");
  const mcqs = [...root.querySelectorAll(".mcq")];
  let correct = 0;
  let skipped = 0;
  mcqs.forEach(m => {
    if (!m.querySelector(".opt.selected")) skipped += 1;
    if (gradeMcq(m)) correct += 1;
  });
  const total = mcqs.length;
  const pct = Math.round((correct / total) * 100);
  let grade, blurb;
  if (pct >= 90) { grade = "AI Hero"; blurb = "Outstanding. You connect school-level intuition to data skills, agents, theory, and production — a full-stack picture of AI."; }
  else if (pct >= 75) { grade = "Advanced Practitioner"; blurb = "Very solid. Review missed items (often agents, theory, SQL/stats, or classical search), then you are ready for projects and papers."; }
  else if (pct >= 60) { grade = "AI Practitioner"; blurb = "Good working knowledge. Revisit the short notes for weaker levels (esp. data skills Ch 30–41 + 45) and retry the exam."; }
  else if (pct >= 40) { grade = "Apprentice"; blurb = "Foundations are forming. Focus on Ch 4, 7, 10, 13, 23–24 plus data skills Ch 30–41 + 45, then take the exam again."; }
  else { grade = "Keep going"; blurb = "This field rewards repetition. Read the point notes, redo chapter MCQs, then return to the final exam."; }

  const st = storage.get();
  st.exam = { correct, total, pct, grade, blurb, skipped };
  storage.set(st);

  go("results");
}

function renderResults() {
  if (!document.getElementById("gradeRing")) return;
  const st = storage.get();
  const ex = st.exam;
  if (!ex) return; // keep the default "not yet graded" state
  document.getElementById("resCorrect").textContent = ex.correct;
  document.getElementById("resTotal").textContent = ex.total;
  document.getElementById("resPct").textContent = ex.pct + "%";
  document.getElementById("resGrade").textContent = ex.grade;
  document.getElementById("resBlurb").textContent = ex.blurb;
  document.getElementById("gradeRing").style.setProperty("--p", ex.pct + "%");
  const ch = st.chapter || {};
  const rows = Object.keys(ch).sort((a,b) => a.localeCompare(b, undefined, {numeric:true})).map(k => {
    const c = ch[k];
    return `<tr><td>${TITLES[k] || k}</td><td>${c.correct}/${c.total}</td><td>${Math.round(c.correct / c.total * 100)}%</td></tr>`;
  }).join("") || `<tr><td colspan="3">No chapter quizzes submitted yet.</td></tr>`;
  document.getElementById("chapterResultsBody").innerHTML = rows;
}

function resetAll() {
  if (!confirm("Reset all quiz answers, progress and exam score?")) return;
  localStorage.removeItem("zh-ai-course");
  document.querySelectorAll(".mcq").forEach(m => {
    m.classList.remove("graded");
    m.querySelectorAll(".opt").forEach(o => o.classList.remove("selected", "correct", "wrong"));
    const chip = m.querySelector(".score-chip");
    if (chip) { chip.textContent = ""; chip.className = "score-chip"; }
  });
  document.querySelectorAll(".answer").forEach(a => a.classList.remove("show"));
  document.querySelectorAll(".practice .btn").forEach(b => { b.disabled = false; if (b.textContent === "Answer shown") b.textContent = "Show model answer"; });
  document.querySelectorAll(".self-mark button").forEach(b => b.classList.remove("on-yes", "on-no"));
  document.querySelectorAll(".chapter-score").forEach(b => { b.classList.remove("show"); b.innerHTML = ""; });
  updateProgress();
  go("cover");
}

document.addEventListener("click", (e) => {
  const goBtn = e.target.closest("[data-go]");
  if (goBtn) {
    e.preventDefault();
    go(goBtn.dataset.go);
  }
});

document.addEventListener("keydown", (e) => {
  if (e.altKey || e.ctrlKey || e.metaKey) return;
  const tag = (e.target && e.target.tagName) || "";
  if (/INPUT|TEXTAREA|SELECT/.test(tag)) return;
  const st = storage.get();
  const i = PAGES.indexOf(st.page || "cover");
  if (i < 0) return;
  if (e.key === "ArrowRight" && i < PAGES.length - 1) go(PAGES[i + 1]);
  if (e.key === "ArrowLeft" && i > 0) go(PAGES[i - 1]);
});

window.addEventListener("hashchange", () => {
  const id = location.hash.replace("#", "");
  if (PAGES.includes(id)) go(id);
});

function renderInterview() {
  const shells = [...document.querySelectorAll(".practice-block[id^='iqCat']")];
  if (!shells.length || typeof INTERVIEW === "undefined") return;
  const order = [...new Set(INTERVIEW.map(q => q.cat))];
  shells.forEach((sh, i) => {
    const list = INTERVIEW.filter(q => q.cat === order[i]);
    sh.innerHTML = list.map(q => `
            <div class="practice" data-pid="${q.pid}"><p class="q">${q.q}</p>
              <button class="btn" onclick="revealAnswer(this)">Show model answer</button>
              <div class="answer">${q.ans}</div>
              <div class="self-mark"><span>Self-mark:</span><button onclick="markPractice(this,'yes')">I got it</button><button onclick="markPractice(this,'no')">Missed it</button></div>
            </div>`).join("");
  });
}
function applyPracticeMarks() {
  const st = storage.get();
  const marks = st.practice || {};
  document.querySelectorAll(".practice[data-pid]").forEach(p => {
    const v = marks[p.dataset.pid];
    if (!v) return;
    const btns = p.querySelectorAll(".self-mark button");
    btns.forEach(b => b.classList.remove("on-yes", "on-no"));
    const el = btns[v === "yes" ? 0 : 1];
    if (el) el.classList.add(v === "yes" ? "on-yes" : "on-no");
  });
}
window.addEventListener("DOMContentLoaded", () => {
  const hash = location.hash.replace("#", "");
  if (PAGES.includes(hash) && hash !== currentPage()) { go(hash); return; } // legacy #deep-links
  markSeen(currentPage());
  renderInterview();
  applyPracticeMarks();
  renderResults();
  updateProgress();
});

window.addEventListener("beforeprint", () => {
  document.querySelectorAll("details").forEach(d => {
    if (!d.open) { d.dataset.wasClosed = "1"; d.open = true; }
  });
});
window.addEventListener("afterprint", () => {
  document.querySelectorAll('details[data-was-closed="1"]').forEach(d => {
    d.open = false;
    delete d.dataset.wasClosed;
  });
});

/* 🔊 Listen buttons on every Short-notes box (browser TTS, offline-safe, static-safe) */
let listenCurrent = null;
function resetListenButtons() {
  document.querySelectorAll(".listen-btn").forEach(b => { b.textContent = "🔊 Listen"; });
  listenCurrent = null;
}
function toggleSpeak(btn, scopeEl) {
  const synth = window.speechSynthesis;
  const wasCurrent = listenCurrent === btn;
  synth.cancel();
  resetListenButtons();
  if (wasCurrent) return;
  const text = [...scopeEl.querySelectorAll("p")].map(p => p.innerText).join(" ");
  const u = new SpeechSynthesisUtterance(text);
  u.rate = 1;
  u.onend = resetListenButtons;
  u.onerror = resetListenButtons;
  listenCurrent = btn;
  btn.textContent = "⏹ Stop";
  synth.speak(u);
}
function initListenButtons() {
  if (!("speechSynthesis" in window)) return;
  document.querySelectorAll(".page .note").forEach(n => {
    const h = n.querySelector("h4");
    if (!h || !/short notes/i.test(h.textContent)) return;
    if (n.querySelector(".listen-btn")) return;
    const b = document.createElement("button");
    b.className = "btn listen-btn";
    b.textContent = "🔊 Listen";
    b.title = "Read these short notes aloud";
    b.addEventListener("click", () => toggleSpeak(b, n));
    h.after(b);
  });
}
window.addEventListener("DOMContentLoaded", initListenButtons);
