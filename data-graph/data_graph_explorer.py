"""FCC Data Graph Explorer."""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def load_csv(path):
    return pd.read_csv(path)


def histogram(df, column, bins=20):
    fig, ax = plt.subplots()
    ax.hist(df[column].dropna(), bins=bins)
    ax.set_xlabel(column); ax.set_ylabel("Frequency")
    ax.set_title(f"Histogram of {column}")
    fig.savefig(f"hist_{column}.png"); plt.close(fig)


def scatter(df, x_col, y_col):
    fig, ax = plt.subplots()
    ax.scatter(df[x_col], df[y_col], alpha=0.5)
    ax.set_xlabel(x_col); ax.set_ylabel(y_col)
    ax.set_title(f"{y_col} vs {x_col}")
    fig.savefig(f"scatter_{x_col}_{y_col}.png"); plt.close(fig)


def line_plot(df, x_col, y_col):
    fig, ax = plt.subplots()
    ax.plot(df[x_col], df[y_col])
    ax.set_xlabel(x_col); ax.set_ylabel(y_col)
    fig.savefig(f"line_{x_col}_{y_col}.png"); plt.close(fig)


def summary(df):
    return df.describe(include="all")
