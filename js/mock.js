/* Mock interview mode — timed random draws from the Interview Q&A bank (no duplication: reads #interview DOM). */

let MOCK = null;

function mockBank() {
  return [...document.querySelectorAll("#interview .practice")].map(el => ({
    pid: el.dataset.pid,
    q: el.querySelector(".q").textContent.trim(),
    ans: el.querySelector(".answer").innerHTML,
    star: el.querySelector(".q").textContent.includes("★")
  }));
}

function mockShowBest() {
  let best = null;
  try { best = JSON.parse(localStorage.getItem("zh-mock-best") || "null"); } catch (e) {}
  const el = document.getElementById("mockBest");
  if (el) el.textContent = best ? `${best.got}/${best.n} (${best.pct}%)` : "—";
}

function startMock() {
  const n = parseInt(document.getElementById("mockCount").value, 10);
  const secs = parseInt(document.getElementById("mockSecs").value, 10);
  const pool = document.getElementById("mockPool").value;
  let bank = mockBank();
  if (pool === "star") bank = bank.filter(q => q.star);
  if (!bank.length) return;
  // shuffle, take n (or all if fewer)
  for (let i = bank.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [bank[i], bank[j]] = [bank[j], bank[i]];
  }
  if (MOCK && MOCK.timer) clearInterval(MOCK.timer);
  MOCK = { list: bank.slice(0, Math.min(n, bank.length)), i: 0, secs, left: secs, results: [], timer: null, revealed: false };
  document.getElementById("mockSetup").style.display = "none";
  document.getElementById("mockSetupBtn").style.display = "none";
  document.getElementById("mockFinal").style.display = "none";
  document.getElementById("mockStage").style.display = "";
  renderMockQ();
}

function renderMockQ() {
  const m = MOCK;
  const item = m.list[m.i];
  m.left = m.secs;
  m.revealed = false;
  document.getElementById("mockProg").textContent = `Q ${m.i + 1}/${m.list.length}`;
  document.getElementById("mockQ").textContent = item.q;
  document.getElementById("mockAns").style.display = "none";
  document.getElementById("mockAns").innerHTML = "";
  document.getElementById("mockMark").style.display = "none";
  document.getElementById("mockRevealBtn").style.display = "";
  updateMockTimer();
  if (m.timer) clearInterval(m.timer);
  m.timer = setInterval(() => {
    // stop if user navigated away
    if (!document.getElementById("mock").classList.contains("active")) {
      clearInterval(MOCK.timer); MOCK.timer = null; return;
    }
    MOCK.left -= 0.25;
    if (MOCK.left <= 0) { MOCK.left = 0; updateMockTimer(); revealMockAns(true); return; }
    updateMockTimer();
  }, 250);
}

function updateMockTimer() {
  const m = MOCK;
  const frac = Math.max(0, m.left / m.secs);
  const bar = document.getElementById("mockTimeBar");
  bar.style.width = (frac * 100).toFixed(1) + "%";
  bar.style.background = frac < 0.2 ? "#be123c" : (frac < 0.5 ? "#b45309" : "#0f766e");
  document.getElementById("mockTimeText").textContent = `${Math.ceil(m.left)}s left`;
}

function revealMockAns(auto) {
  const m = MOCK;
  if (!m || m.revealed) return;
  m.revealed = true;
  if (m.timer) { clearInterval(m.timer); m.timer = null; }
  const box = document.getElementById("mockAns");
  box.innerHTML = (auto ? "<p><em>⏰ Time’s up — model answer revealed. Mark yourself honestly.</em></p>" : "") + m.list[m.i].ans;
  box.style.display = "";
  document.getElementById("mockRevealBtn").style.display = "none";
  document.getElementById("mockMark").style.display = "";
}

function markMock(ok) {
  const m = MOCK;
  if (!m || !m.revealed) return;
  m.results.push({ item: m.list[m.i], ok });
  m.i += 1;
  if (m.i >= m.list.length) finishMock();
  else renderMockQ();
}

function quitMock() {
  if (MOCK && MOCK.timer) { clearInterval(MOCK.timer); MOCK.timer = null; }
  if (MOCK && MOCK.results.length) finishMock();
  else resetMock();
}

function finishMock() {
  const m = MOCK;
  if (m.timer) { clearInterval(m.timer); m.timer = null; }
  const got = m.results.filter(r => r.ok).length;
  const n = m.results.length;
  const pct = n ? Math.round((got / n) * 100) : 0;
  document.getElementById("mockStage").style.display = "none";
  document.getElementById("mockFinal").style.display = "";
  document.getElementById("mockScore").textContent = `${got}/${n}`;
  document.getElementById("mockPct").textContent = `${pct}%`;
  document.getElementById("mockVerdict").textContent =
    pct >= 80 ? "Interview-ready. Book the real thing." :
    pct >= 60 ? "Close — drill the missed ones in the bank and retry." :
    "Keep studying the bank first, then come back for pressure training.";
  const rev = document.getElementById("mockReview");
  rev.innerHTML = "";
  m.results.forEach(r => {
    const div = document.createElement("div");
    div.className = "practice";
    div.innerHTML = `<p class="q">${r.ok ? "✅" : "❌"} ${r.item.q}</p>`;
    rev.appendChild(div);
  });
  try {
    const prev = JSON.parse(localStorage.getItem("zh-mock-best") || "null");
    if (!prev || pct > prev.pct || (pct === prev.pct && n > prev.n)) {
      localStorage.setItem("zh-mock-best", JSON.stringify({ got, n, pct }));
    }
  } catch (e) {}
  mockShowBest();
}

function resetMock() {
  if (MOCK && MOCK.timer) { clearInterval(MOCK.timer); MOCK.timer = null; }
  MOCK = null;
  document.getElementById("mockStage").style.display = "none";
  document.getElementById("mockFinal").style.display = "none";
  document.getElementById("mockSetup").style.display = "";
  document.getElementById("mockSetupBtn").style.display = "";
  mockShowBest();
}

document.addEventListener("DOMContentLoaded", mockShowBest);
