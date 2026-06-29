import pandas as pd


def build_schema(df):
    lines = []
    lines.append("Shape: {:,} rows x {} columns\n".format(df.shape[0], df.shape[1]))
    lines.append("{:<30} {:<15} {:<12} {}".format("Column", "Dtype", "Non-Null", "Sample Values"))
    lines.append("-" * 85)

    for col in df.columns:
        dtype = str(df[col].dtype)
        non_null = df[col].notna().sum()
        pct = "{:.0f}%".format(non_null / len(df) * 100) if len(df) else "-"
        sample_vals = df[col].dropna().unique()
        if len(sample_vals) > 5:
            sample_vals = sample_vals[:5]
        samples = ", ".join(str(v) for v in sample_vals)
        if len(samples) > 60:
            samples = samples[:57] + "..."
        lines.append("{:<30} {:<15} {:>6} ({:<4}) {}".format(col, dtype, non_null, pct, samples))

    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    if numeric_cols:
        lines.append("\nNumeric summary:")
        try:
            lines.append(df[numeric_cols].describe().round(2).to_string())
        except Exception:
            pass

    return "\n".join(lines)
