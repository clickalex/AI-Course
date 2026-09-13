/* Interview Q&A bank data — shared by interview.html (render) and mock.js (draws). */
const INTERVIEW = [
 {
  "pid": "iq1",
  "q": "★ Q1. List vs tuple vs dict vs set — when do you use each?",
  "ans": "<p>List: ordered, mutable sequences. Tuple: ordered, immutable — dict keys, fixed records, safe returns. Dict: key→value lookups O(1). Set: unique membership + dedupe/intersection. Say the trade-off aloud: mutability, ordering, hashing.</p>",
  "cat": "Python &amp; SQL"
 },
 {
  "pid": "iq2",
  "q": "★ Q2. Second-highest salary per department in SQL — write it and explain.",
  "ans": "<p><code>SELECT dept, MAX(salary) FROM emp WHERE salary &lt; (SELECT MAX(salary) …) GROUP BY dept</code> — or robustly: <code>DENSE_RANK() OVER (PARTITION BY dept ORDER BY salary DESC)</code> then filter rank = 2 (handles ties). Mention NULL handling and testing on edge cases.</p>",
  "cat": "Python &amp; SQL"
 },
 {
  "pid": "iq3",
  "q": "Q3. Your pandas groupby is slow on 10M rows. What do you do?",
  "ans": "<p>Filter columns/rows early, set efficient dtypes (category, int32), avoid apply (vectorise), aggregate before merging, consider Polars/DuckDB or chunked processing. Profile first (<code>%%timeit</code>, line_profiler) — never optimise blind.</p>",
  "cat": "Python &amp; SQL"
 },
 {
  "pid": "iq4",
  "q": "Q4. LEFT JOIN doubled your row count. Explain and fix.",
  "ans": "<p>Fanout: the right table has duplicate keys. Diagnose with <code>GROUP BY key HAVING COUNT(*) &gt; 1</code>. Fix: dedupe the right side (which row wins?), or aggregate before joining, or use <code>validate=\"many_to_one\"</code> in pandas to fail loudly next time.</p>",
  "cat": "Python &amp; SQL"
 },
 {
  "pid": "iq5",
  "q": "★ Q5. Your model has 99% accuracy and is useless. Explain.",
  "ans": "<p>Class imbalance: 99% negatives means “always predict negative” scores 99%. Report precision/recall/F1/AUC-PR per class, use stratified splits, try class weights or resampling, and pick the metric that matches the business cost (missed fraud vs false alarm).</p>",
  "cat": "ML fundamentals"
 },
 {
  "pid": "iq6",
  "q": "★ Q6. Overfitting vs underfitting — how do you detect and fix each?",
  "ans": "<p>Overfit: train ≪ validation error — fix with more data, regularization, simpler model, early stopping, cross-validation. Underfit: both errors high — bigger model, more/better features, longer training, lower regularization. Draw the learning curves while talking.</p>",
  "cat": "ML fundamentals"
 },
 {
  "pid": "iq7",
  "q": "Q7. What is data leakage? Give two real examples.",
  "ans": "<p>Future/target info sneaking into features: (1) fitting a scaler on the full dataset before splitting; (2) a “days_since_signup” feature computed at prediction time with future data, or training on rows that include the outcome timestamp. Fix: strict time splits, fit preprocessors on train only, audit feature availability dates.</p>",
  "cat": "ML fundamentals"
 },
 {
  "pid": "iq8",
  "q": "Q8. Random forest vs gradient boosting (XGBoost/LightGBM) — trade-offs?",
  "ans": "<p>RF: bagged parallel trees, robust, few knobs, great baseline. Boosting: sequential error-correction, usually higher accuracy on tabular data, but more tuning + overfit risk + slower training. Default: boosting for competitions/leaderboards, RF for a fast reliable baseline.</p>",
  "cat": "ML fundamentals"
 },
 {
  "pid": "iq9",
  "q": "★ Q9. Explain backpropagation in one minute.",
  "ans": "<p>Forward pass computes loss; backprop applies the chain rule layer-by-layer to get each weight’s gradient (∂L/∂w); the optimizer steps weights downhill (w − η∇L). Repeat over batches. Vanishing gradients in deep nets motivated ReLU, residuals, normalization.</p>",
  "cat": "Deep learning &amp; NLP"
 },
 {
  "pid": "iq10",
  "q": "★ Q10. How does self-attention work? Why did transformers win?",
  "ans": "<p>Attention(Q,K,V) = softmax(QKᵀ/√d)V: every token queries all others, weighting by relevance — capturing long-range context in parallel (unlike RNNs), fully GPU-friendly, and scalable (scaling laws). Cost: O(n²) in sequence length, hence context limits and efficient variants.</p>",
  "cat": "Deep learning &amp; NLP"
 },
 {
  "pid": "iq11",
  "q": "Q11. CNN vs Vision Transformer — when does each win?",
  "ans": "<p>CNNs: built-in locality/translation bias, data-efficient, great on small datasets and edge devices. ViTs: global attention, win with large data + compute + pretraining. Default today: pretrained ViT/backbone + fine-tune; CNN when data or latency budget is tight.</p>",
  "cat": "Deep learning &amp; NLP"
 },
 {
  "pid": "iq12",
  "q": "Q12. What causes hallucinations, and how do you reduce them?",
  "ans": "<p>Next-token prediction optimizes fluency, not truth; gaps get filled confidently. Reduce with: RAG grounding + citations, abstention when retrieval is thin, lower temperature for factual tasks, structured output + verification, evals on faithfulness. Never present unverified LLM output as fact.</p>",
  "cat": "Deep learning &amp; NLP"
 },
 {
  "pid": "iq13",
  "q": "★ Q13. Design a RAG system for 100k company docs. Walk me through it.",
  "ans": "<p>Parse (keep tables), chunk 300–800 tokens with overlap + metadata (date, tenant), embed, hybrid dense+BM25 index with reranker. At query: retrieve top-k, filter by tenant/date, generate with citations, abstain if thin. Eval: recall@k, faithfulness, golden set. Ops: incremental re-indexing, freshness dates in answers, cost/token dashboards.</p>",
  "cat": "LLMs, RAG &amp; agents"
 },
 {
  "pid": "iq14",
  "q": "★ Q14. Fine-tuning vs RAG vs prompt engineering — how do you choose?",
  "ans": "<p>Prompting: cheapest, no training — start here. RAG: knowledge changes often or needs citations — add retrieval. Fine-tuning (LoRA): need style/format/behavior baked in or offline use — needs clean data + evals. Often combine: fine-tuned model over RAG. Always compare against the simpler option first.</p>",
  "cat": "LLMs, RAG &amp; agents"
 },
 {
  "pid": "iq15",
  "q": "Q15. What is prompt injection and how do you defend?",
  "ans": "<p>Untrusted content (docs, webpages, user text) overriding instructions — “ignore previous instructions…”. Defences: privilege hierarchy (system &gt; developer &gt; user &gt; tool), least-privilege tools, human approval for side effects, input/output filtering, eval with adversarial suites. Treat all tool output as untrusted.</p>",
  "cat": "LLMs, RAG &amp; agents"
 },
 {
  "pid": "iq16",
  "q": "Q16. How do you evaluate an LLM feature before launch?",
  "ans": "<p>Golden set (typical + edge + unanswerable + adversarial) with expected answers/citations; retrieval metrics (recall@k); faithfulness checks; human spot-checks; A/B with task-success metrics (not vibes); red-team for safety/jailbreaks/PII. Block deploy on regression; monitor live with sampled reviews.</p>",
  "cat": "LLMs, RAG &amp; agents"
 },
 {
  "pid": "iq17",
  "q": "★ Q17. Your model decayed in production. How do you detect and fix it?",
  "ans": "<p>Detect: monitor feature drift (PSI/KS), prediction distribution, delayed-label accuracy, and the business KPI. Fix: alert → diagnose (data vs concept drift) → retrain on fresh clean labels → shadow → canary with auto-rollback. Prevent: retraining schedule, versioned data+model, rollback runbook.</p>",
  "cat": "MLOps &amp; production"
 },
 {
  "pid": "iq18",
  "q": "Q18. Training-serving skew — what is it and how do you prevent it?",
  "ans": "<p>Features computed differently in training vs serving (different code, time windows, defaults). Prevent with one shared feature pipeline used by both, contract tests on schemas, logging served features to compare distributions, and shadow mode before full rollout.</p>",
  "cat": "MLOps &amp; production"
 },
 {
  "pid": "iq19",
  "q": "Q19. How do you deploy a model safely? (CI/CD for ML)",
  "ans": "<p>Version data+code+params+env (MLflow); gate on data validation + slice evals + behavioural tests; shadow on live traffic; canary 5%→50%→100% with auto-rollback on metric dips; one-click rollback; dashboards on latency, errors, drift, business KPI. Deploy is a pipeline, never a laptop.</p>",
  "cat": "MLOps &amp; production"
 },
 {
  "pid": "iq20",
  "q": "Q20. Docker image vs container, and why pin versions?",
  "ans": "<p>Image = frozen template (code+libs+OS layers); container = running instance (one→many). Pin tags+digests because :latest is a moving target — unreproducible deploys and uncertain rollbacks. Also: non-root users, health checks, secrets from a manager, resource limits.</p>",
  "cat": "MLOps &amp; production"
 },
 {
  "pid": "iq21",
  "q": "★ Q21. “Tell me about yourself.” (2-minute structure)",
  "ans": "<p>Present → past → future in 2 minutes: who you are now (role, 1-line specialty), 2 proof points with numbers (project, impact), why this role/company next. End with a question hook. Practise until it sounds conversational, not memorised.</p>",
  "cat": "Behavioral &amp; HR"
 },
 {
  "pid": "iq22",
  "q": "Q22. “Describe a project that failed. What did you do?”",
  "ans": "<p>Use STAR: Situation (one line), Task (your responsibility), Action (what YOU did — detected, communicated early, pivoted), Result + lesson (process you changed: checklists, evals, smaller bets). Pick a real failure; the lesson is the point, not the failure.</p>",
  "cat": "Behavioral &amp; HR"
 },
 {
  "pid": "iq23",
  "q": "Q23. “How do you explain a model to a non-technical stakeholder?”",
  "ans": "<p>Lead with the decision, not the method: what changes, expected impact, risks/uncertainty in plain numbers. One visual max. Analogies over equations (“like spell-check for fraud”). Offer the technical appendix, don’t present it. Check understanding by asking what they’d decide.</p>",
  "cat": "Behavioral &amp; HR"
 },
 {
  "pid": "iq24",
  "q": "Q24. “Why should we hire you for this ML role?”",
  "ans": "<p>Map 3 of their stated needs to your proof: need → evidence → result (numbers). Mention the full loop (data → model → deploy → monitor) and one differentiator (evals, communication, ownership). Close: “That’s the impact I’d bring in the first 90 days.”</p>",
  "cat": "Behavioral &amp; HR"
 }
];
