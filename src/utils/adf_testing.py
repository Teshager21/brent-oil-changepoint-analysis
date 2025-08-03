import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from pathlib import Path

# Paths
DATA_PATH = Path("data/raw/BrentOilPrices.csv")
REPORT_PATH = Path("reports/adf_test_report.md")
PLOT_DIR = Path("reports/figures")
PLOT_DIR.mkdir(parents=True, exist_ok=True)

# Load data
df = pd.read_csv(DATA_PATH)
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df = df.dropna(subset=["Date"])
df = df.sort_values("Date")
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df = df.dropna(subset=["Price"])
df["Price_diff"] = df["Price"].diff()


# ADF Test Function
def run_adf(series, name):
    result = adfuller(series.dropna())
    summary = {
        "ADF Statistic": result[0],
        "p-value": result[1],
        "Critical Values": result[4],
        "Stationary?": "Yes" if result[1] < 0.05 else "No",
    }
    return name, summary


# Run tests
original_result = run_adf(df["Price"], "Original Series")
diff_result = run_adf(df["Price_diff"], "1st Difference")

# Save report
with open(REPORT_PATH, "w") as f:
    f.write("# ADF Test Report\n\n")
    for name, res in [original_result, diff_result]:
        f.write(f"## {name}\n")
        for key, val in res.items():
            if key == "Critical Values":
                f.write("### Critical Values:\n")
                for level, crit_val in val.items():
                    f.write(f"- {level}: {crit_val:.4f}\n")
            else:
                f.write(f"- **{key}**: {val}\n")
        f.write("\n---\n\n")

# Plotting
plt.figure(figsize=(12, 5))
plt.plot(df["Date"], df["Price"], label="Original")
plt.title("Brent Oil Price - Original Series")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.tight_layout()
plt.savefig(PLOT_DIR / "original_series.png")
plt.close()

plt.figure(figsize=(12, 5))
plt.plot(df["Date"], df["Price_diff"], label="1st Difference", color="orange")
plt.title("Brent Oil Price - 1st Differenced Series")
plt.xlabel("Date")
plt.ylabel("Differenced Price")
plt.legend()
plt.tight_layout()
plt.savefig(PLOT_DIR / "differenced_series.png")
plt.close()

print(
    "✅ ADF tests completed and saved.\n📝 Report: "
    "reports/adf_test_report.md\n📊 Plots saved in: reports/figures/"
)
