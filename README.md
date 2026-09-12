# Zero to Hero AI Course Book

An illustrated, interactive course book from **Class 1 to PhD**: school intuition, undergraduate CS-AI, **data skills (detailed Python, Excel/Sheets, Pandas, SQL, visualization, statistics, Power BI, capstone)**, machine learning, deep learning, LLMs, **AI Agents**, **Agentic AI**, research theory, alignment, and production practice.

Open `index.html` in a browser, or serve the folder:

```bash
python3 -m http.server 8080 --bind 0.0.0.0
```

Then visit the local URL shown by the server.

## What’s inside

- **Learning paths** (school / data / UG / industry / PhD) and a **complete syllabus**
- **School chapter** plus **37 numbered chapters** (38 teaching units with school)
- **Short notes** and **point notes** in every lesson
- **190+ MCQs** with instant check and chapter scoring
- **70+ practice questions** with model answers and self-marking
- **Final exam (38 questions: 30 core AI + 8 data skills)** with percentage, grade name, and result breakdown
- Progress is saved in the browser (`localStorage`)

## Chapter map

| ID | Topic | Level |
|----|--------|--------|
| paths | Class 1 → PhD learning paths | Start |
| syllabus | Complete AI syllabus | Start |
| sch1 | AI for school | Class 1–12 |
| ch1–3 | What / history / types of AI | School–UG |
| ch4–6 | Maths, Python, data | UG |
| **ch30** | **Python in depth (types, functions, OOP, files, errors)** | **Data** |
| **ch31** | **Excel & Google Sheets (formulas, cleaning, pivots, charts)** | **Data** |
| **ch32** | **Data analysis with Pandas & NumPy (EDA)** | **Data** |
| **ch33** | **SQL for data & AI (joins, CTEs, windows)** | **Data** |
| **ch34** | **Data visualization & storytelling** | **Data** |
| **ch35** | **Statistics for analysis (CIs, tests, A/B)** | **Data** |
| **ch36** | **Power BI & dashboards (model, DAX, publish)** | **Data** |
| **ch37** | **Capstone: end-to-end data project** | **Data** |
| ch17–18 | Search, games, logic, planning | UG classical |
| ch7–9 | ML fundamentals, supervised, unsupervised | UG |
| ch19–20 | Bayesian & causal AI; recsys, IR, knowledge graphs | UG / applied |
| ch10–11 | Neural nets; CNN / RNN / vision | DL |
| ch21 | Vision, speech, multimodal | DL |
| ch12–14 | NLP, Transformers & LLMs, generative AI | DL / gen |
| ch22 | Fine-tuning, PEFT, evals | Industry |
| **ch23** | **AI Agents** | **Agents** |
| **ch24** | **Agentic AI systems** | **Agents** |
| ch15, ch25 | RL; advanced RL / MARL / world models | Decisions |
| ch26 | GNNs, time series, AutoML, evolutionary, robotics | Survey |
| ch27–29 | Learning theory; XAI / alignment / privacy; systems & research methods | PhD |
| ch16 | Ethics, MLOps & career | Practice |
| notes / exam / results | Revision sheet, 38-Q exam, grades | Test |

## How scoring works

- Chapter button **Grade this chapter** scores that chapter’s MCQs.
- Practice questions are self-marked after you reveal the model answer.
- **Submit final exam** writes a grade: Apprentice → Practitioner → Advanced Practitioner → **AI Hero** (90%+).
- Use **Reset progress** in the sidebar for a clean retake.

## Files

```
index.html      Course book (all chapters)
css/style.css   Layout and textbook theme
js/app.js       Navigation, quizzes, exam grading
images/         Chapter illustrations
```
