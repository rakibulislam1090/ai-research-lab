"""
Reliability analysis for a Likert-scale survey (synthetic data).

What this script shows:
    1. How to simulate realistic survey data (so no real participant data is exposed).
    2. Descriptive statistics for each item.
    3. Cronbach's alpha for each construct (internal-consistency reliability).
    4. Corrected item-total correlation (which items fit their construct weakly).

Constructs used in the example (a typical technology-adoption model):
    PE  = Performance Expectancy   (e.g., "Using GenAI improves my productivity")
    EE  = Effort Expectancy        (e.g., "GenAI tools are easy to use")
    BI  = Behavioral Intention     (e.g., "I intend to keep using GenAI")
"""

import numpy as np
import pandas as pd

# A fixed seed makes the "random" data identical on every run (reproducibility).
RNG = np.random.default_rng(seed=42)

# Construct name -> number of items measuring it.
CONSTRUCTS = {"PE": 4, "EE": 4, "BI": 3}


def simulate_likert_survey(n_respondents: int = 300) -> pd.DataFrame:
    """Create synthetic 5-point Likert responses.

    Each construct has one hidden "true" score per respondent. Every item is that
    true score plus some noise, so items of the same construct correlate with
    each other, just like in a real survey.
    """
    columns = {}
    for construct, n_items in CONSTRUCTS.items():
        latent = RNG.normal(loc=0, scale=1, size=n_respondents)  # hidden true score
        for i in range(1, n_items + 1):
            noise = RNG.normal(loc=0, scale=0.7, size=n_respondents)
            raw = 3 + latent + noise  # centre the scale on 3 (the "neutral" point)
            # Round to whole numbers and clip to the 1..5 Likert range.
            columns[f"{construct}{i}"] = np.clip(np.rint(raw), 1, 5).astype(int)
    return pd.DataFrame(columns)


def cronbach_alpha(items: pd.DataFrame) -> float:
    """Cronbach's alpha = (k / (k - 1)) * (1 - sum of item variances / variance of total score).

    k is the number of items. If items move together, the variance of the total
    is large compared with the individual variances, so alpha goes towards 1.
    """
    k = items.shape[1]
    item_variances = items.var(axis=0, ddof=1).sum()
    total_variance = items.sum(axis=1).var(ddof=1)
    return (k / (k - 1)) * (1 - item_variances / total_variance)


def corrected_item_total(items: pd.DataFrame) -> pd.Series:
    """Correlation of each item with the sum of the *other* items in its construct.

    "Corrected" means the item is excluded from the total, otherwise it would
    correlate with itself and look better than it really is.
    """
    total = items.sum(axis=1)
    return pd.Series(
        {col: items[col].corr(total - items[col]) for col in items.columns},
        name="corrected_item_total_r",
    )


def main() -> None:
    df = simulate_likert_survey()
    print(f"Synthetic sample: {len(df)} respondents, {df.shape[1]} items\n")

    print("=== Descriptive statistics ===")
    print(df.describe().T[["mean", "std", "min", "max"]].round(2), "\n")

    print("=== Reliability by construct ===")
    rows = []
    for construct in CONSTRUCTS:
        # Select the columns that belong to this construct, e.g. PE1..PE4.
        items = df.filter(regex=f"^{construct}\\d+$")
        alpha = cronbach_alpha(items)
        rows.append({
            "construct": construct,
            "items": items.shape[1],
            "cronbach_alpha": round(alpha, 3),
            "meets_0.70": "yes" if alpha >= 0.70 else "no",
        })
        print(f"\n{construct} item-total correlations:")
        print(corrected_item_total(items).round(3).to_string())

    print("\n=== Summary ===")
    print(pd.DataFrame(rows).to_string(index=False))


if __name__ == "__main__":
    main()
