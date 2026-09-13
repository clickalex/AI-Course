/* Datasets playground — built-in tables + answer checking. 100% client-side (GitHub Pages safe). */

const DATASETS = {
  sales: {
    title: "sales — 10 orders",
    cols: ["order_id", "customer_id", "region", "amount", "status", "date"],
    rows: [
      ["o1", "c1", "North", 1200, "delivered", "2025-01-05"],
      ["o2", "c2", "West", 1800, "delivered", "2025-01-06"],
      ["o3", "c3", "West", 400, "refunded", "2025-01-07"],
      ["o4", "c1", "East", 900, "delivered", "2025-01-08"],
      ["o5", "c2", "North", 2500, "delivered", "2025-02-02"],
      ["o6", "c4", "West", 2200, "delivered", "2025-02-03"],
      ["o7", "c5", "East", 300, "refunded", "2025-02-04"],
      ["o8", "c3", "South", 1500, "delivered", "2025-02-05"],
      ["o9", "c4", "West", 700, "delivered", "2025-02-06"],
      ["o10", "c6", "North", 1100, "refunded", "2025-02-07"]
    ]
  },
  customers: {
    title: "customers — 6 customers (c7 never ordered)",
    cols: ["customer_id", "name", "city", "signup"],
    rows: [
      ["c1", "Asha", "Mumbai", "2024-05-01"],
      ["c2", "Rohan", "Delhi", "2024-06-12"],
      ["c3", "Meera", "Goa", "2024-07-20"],
      ["c4", "Arjun", "Mumbai", "2024-09-02"],
      ["c5", "Kabir", "Delhi", "2024-11-15"],
      ["c7", "Vera", "Goa", "2025-01-10"]
    ]
  },
  employees: {
    title: "employees — 8 staff (for Excel practice)",
    cols: ["name", "dept", "salary", "city"],
    rows: [
      ["Asha", "Sales", 60000, "Mumbai"],
      ["Rohan", "Engg", 90000, "Delhi"],
      ["Meera", "Engg", 95000, "Goa"],
      ["Arjun", "Sales", 55000, "Mumbai"],
      ["Kabir", "Support", 45000, "Delhi"],
      ["Vera", "Engg", 92000, "Goa"],
      ["Dev", "Support", 47000, "Mumbai"],
      ["Tara", "Sales", 62000, "Delhi"]
    ]
  }
};

function renderDatasets() {
  Object.keys(DATASETS).forEach(key => {
    const host = document.getElementById("ds-" + key);
    if (!host) return;
    const ds = DATASETS[key];
    let h = '<table><thead><tr>' + ds.cols.map(c => '<th>' + c + '</th>').join("") + '</tr></thead><tbody>';
    ds.rows.forEach(r => {
      h += '<tr>' + r.map(v => '<td>' + v + '</td>').join("") + '</tr>';
    });
    host.innerHTML = '<h4>' + ds.title + '</h4>' + h + '</tbody></table>';
  });
}

function norm(s) {
  return (s || "").toLowerCase().replace(/["'`\[\]]/g, "").replace(/\s+/g, " ");
}

function checkChallenge(btn) {
  const box = btn.closest(".practice");
  const need = (box.dataset.need || "").split("|").map(s => s.trim().toLowerCase()).filter(Boolean);
  const text = norm(box.querySelector("textarea").value);
  const chip = box.querySelector(".score-chip");
  const hint = box.querySelector(".challenge-hint");
  if (!text.trim()) {
    chip.textContent = "Type something first";
    chip.className = "score-chip bad";
    hint.textContent = "";
    return;
  }
  const missing = need.filter(n => text.indexOf(n) === -1);
  if (missing.length === 0) {
    chip.textContent = "Looks right!";
    chip.className = "score-chip ok";
    hint.textContent = "Nice — compare with the model answer below, then self-mark.";
  } else {
    chip.textContent = (need.length - missing.length) + "/" + need.length + " pieces found";
    chip.className = "score-chip bad";
    hint.textContent = (box.dataset.hint || "Compare with the model answer.") + " (Missing: " + missing.slice(0, 3).join(", ") + ")";
  }
}

window.addEventListener("DOMContentLoaded", renderDatasets);
