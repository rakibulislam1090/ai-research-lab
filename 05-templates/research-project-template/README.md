# 🧩 Research Project Template

Copy this structure into a **new private repository** for each paper
(for example, `paper-genai-adoption`). Make it public only after publication.

```
paper-<short-name>/
├── README.md              # Title, research question, status, authors
├── docs/
│   ├── proposal.md        # Research gap, theory, hypotheses
│   ├── questionnaire.md   # Items and their sources (adapted from ...)
│   └── ethics.md          # Consent text, ethics approval reference
├── data/
│   ├── raw/               # ❌ never commit (ignored by .gitignore)
│   ├── processed/         # anonymized and cleaned data (still private)
│   └── synthetic/         # safe demo data (can be public later)
├── analysis/
│   ├── 01_cleaning.py
│   ├── 02_descriptives.py
│   └── 03_pls_sem_notes.md
├── results/               # Tables and figures
└── manuscript/            # ❌ never commit drafts publicly
```

## README template for a paper repository

```markdown
# <Paper title>

**Status:** 🔬 In progress | 📝 Under review | ✅ Published
**Authors:** <names>  ·  **Supervisor:** <name>
**Target journal:** <journal> (kept private until a decision)

## Research question
## Theoretical framework
## Method (sample, instrument, analysis technique)
## Reproducibility (how to run the analysis)
## Citation (after publication: APA 7 + DOI)
```

## Before making a paper repository public, check that:

- [ ] The paper is accepted or published
- [ ] Your supervisor and co-authors agree
- [ ] The journal's policy allows sharing code and data
- [ ] Participant consent allows data sharing (otherwise share code only)
- [ ] Git history has no raw or personal data
- [ ] The README has the citation and DOI
