"""FCC Data Analysis #5 — Sea Level Predictor (linear regression)."""
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress


def draw_plot():
    df = pd.read_csv("epa-sea-level.csv")
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_all = pd.Series(range(df["Year"].min(), 2051))
    ax.plot(years_all, res.intercept + res.slope * years_all, "r-",
            label=f"All data: {res.slope:.4f}x+{res.intercept:.4f}")

    recent = df[df["Year"] >= 2000]
    res2 = linregress(recent["Year"], recent["CSIRO Adjusted Sea Level"])
    years_recent = pd.Series(range(2000, 2051))
    ax.plot(years_recent, res2.intercept + res2.slope * years_recent, "g-",
            label=f"2000+: {res2.slope:.4f}x+{res2.intercept:.4f}")

    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.legend()
    fig.savefig("sea_level_plot.png")
    return ax
