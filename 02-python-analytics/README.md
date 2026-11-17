# 🐍 Python Analytics

Reproducible analysis scripts. Every script here runs on **synthetic (computer-generated) data**,
so no real participant data is ever exposed.

## Scripts

| Script | What it does |
|---|---|
| [`reliability_analysis.py`](reliability_analysis.py) | Generates a synthetic Likert-scale survey, then computes descriptive statistics, Cronbach's alpha, and the corrected item–total correlation for each construct |

## How to run

```bash
pip install -r requirements.txt
python reliability_analysis.py
```

## Why synthetic data?

Real survey data contains information about participants, and sharing it requires their consent
and ethics approval. Synthetic data shows the **method** without any of that risk. Once a paper
is published, the real analysis can be linked from [`../publications/`](../publications/), but only
if the consent and the journal's policy allow it.
