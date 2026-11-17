# ✅ PLS-SEM Assessment Checklist

A step-by-step checklist for reporting a reflective PLS-SEM model (for example, in SmartPLS).

> **Status:** learning note. The thresholds below are commonly reported rules of thumb. Verify them
> against the original sources before using them in a manuscript.

---

## Step 1: Measurement Model (Reflective)

| Criterion | What it checks | Common rule of thumb |
|---|---|---|
| Indicator loadings | Each item reflects its construct | ≥ 0.708 preferred |
| Cronbach's alpha | Internal consistency (conservative) | ≥ 0.70 |
| Composite reliability (ρc) | Internal consistency | 0.70 to 0.95 (values above 0.95 may signal redundant items) |
| AVE | Convergent validity | ≥ 0.50 |
| HTMT | Discriminant validity | < 0.85 (strict) or < 0.90 (lenient) |
| Fornell–Larcker | Discriminant validity (older criterion) | √AVE > inter-construct correlations |

**Why the 0.708 loading?** 0.708² ≈ 0.50, so the construct explains about half of the item's variance.

## Step 2: Structural Model

| Criterion | What it checks | Notes |
|---|---|---|
| VIF (collinearity) | Predictors are not redundant | Ideally below about 3 |
| Path coefficients (β) | Strength and direction of hypotheses | Use bootstrapping (for example, 5,000 subsamples) for significance |
| R² | Explained variance | Interpret relative to the discipline |
| f² | Effect size of each predictor | 0.02 small, 0.15 medium, 0.35 large |
| Q² / PLSpredict | Predictive relevance | Report PLSpredict where possible |

## Step 3: Robustness (often requested by Q1 reviewers)

- [ ] Common method bias (for example, a full collinearity VIF test)
- [ ] Mediation analysis with bootstrapped indirect effects
- [ ] Moderation or multi-group analysis (MGA), with a measurement invariance check (MICOM)
- [ ] Endogeneity check, if relevant

---

## ⚠️ Common Mistakes

1. Reporting only Fornell–Larcker. Many reviewers now expect **HTMT**.
2. Deleting items only to raise AVE without discussing content validity.
3. Reporting p-values without **effect sizes** and **confidence intervals**.
4. Using PLS-SEM without justifying **why** PLS and not CB-SEM.

## 📚 Key Sources (verify the edition and details before citing)

- Hair, J. F., Hult, G. T. M., Ringle, C. M., & Sarstedt, M. *A primer on partial least squares
  structural equation modeling (PLS-SEM)*. SAGE. (Check for the latest edition.)
- Henseler, J., Ringle, C. M., & Sarstedt, M. (2015). A new criterion for assessing discriminant
  validity in variance-based structural equation modeling. *Journal of the Academy of Marketing
  Science, 43*(1), 115–135.
