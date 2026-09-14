# Tools

## Active

- **`build.py`** — the static-site generator. Run it from the repository root
  (`python3 tools/build.py`). It combines the shared partials in
  `src/templates/` with the page fragments in `src/pages/`, using the `PAGES`
  and `TITLES` tables in `js/app.js` as the single source of truth, and writes
  `index.html` plus one file per page into `pages/`. It fails loudly on order
  mismatches, dead navigation links or wrong asset prefixes.

## `archive/`

Historical, one-off content-generation scripts kept for provenance
(`_phase11`–`_phase14`, `_snapshots`–`_snapshots4`, `_qa`, `split`). They are
**not** part of the build and are not meant to be re-run — several contain
machine-specific absolute paths from the sessions in which the chapters were
first authored. All of their output already lives in `src/`.

## Layout

```
src/
  pages/       one fragment per page (edit these)
  templates/   shared partials: _head, _sidebar, _mainopen, _foot
index.html     built cover (root, for GitHub Pages)
pages/         built sub-pages
```
