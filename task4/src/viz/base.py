import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.viz.style import new_fig, save


def add_bar_labels(ax: plt.Axes, is_pct: bool = False):
    for container in ax.containers:
        values = [bar.get_height() for bar in container]
        all_int = all(float(v).is_integer() for v in values if v == v)
        fmt = ("%.0f%%" if all_int else "%.2f%%") if is_pct else "%.0f"
        ax.bar_label(container, fmt=fmt, padding=3)


def bar(data: pd.Series, title: str, xlabel: str, ylabel: str,
        filename: str = None, color: str = None, show_labels: bool = True, is_pct: bool = False):
    fig, ax = new_fig()
    data.plot(kind="bar", ax=ax, color=color, edgecolor="white")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.tick_params(axis="x", rotation=45)
    if show_labels:
        add_bar_labels(ax, is_pct=is_pct)
    fig.tight_layout()
    if filename:
        save(fig, filename)
    return fig, ax


def horizontal_bar(data: pd.Series, title: str, xlabel: str, ylabel: str,
                   filename: str = None, show_labels: bool = True, is_pct: bool = False):
    fig, ax = new_fig()
    data.plot(kind="barh", ax=ax, edgecolor="white")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if show_labels:
        for container in ax.containers:
            values = [bar.get_width() for bar in container]
            all_int = all(float(v).is_integer() for v in values if v == v)
            fmt = ("%.0f%%" if all_int else "%.2f%%") if is_pct else "%.0f"
            ax.bar_label(container, fmt=fmt, padding=3)
    fig.tight_layout()
    if filename:
        save(fig, filename)
    return fig, ax


def line(data: pd.DataFrame, x: str, y: str, title: str, xlabel: str, ylabel: str, filename: str = None):
    fig, ax = new_fig()
    ax.plot(data[x], data[y], marker="o", linewidth=1.5, markersize=3)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()
    if filename:
        save(fig, filename)
    return fig, ax


def histogram(data: pd.Series, title: str, xlabel: str, ylabel: str, bins: int = 30, filename: str = None):
    fig, ax = new_fig()
    sns.histplot(data.dropna(), bins=bins, ax=ax, kde=True)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    fig.tight_layout()
    if filename:
        save(fig, filename)
    return fig, ax


def pie(data: pd.Series, title: str, filename: str = None):
    fig, ax = new_fig()
    ax.pie(data.values, labels=data.index, autopct="%1.1f%%", startangle=90)
    ax.set_title(title)
    fig.tight_layout()
    if filename:
        save(fig, filename)
    return fig, ax


def scatter(data: pd.DataFrame, x: str, y: str, title: str, xlabel: str, ylabel: str, filename: str = None):
    fig, ax = new_fig()
    sns.scatterplot(data=data, x=x, y=y, ax=ax, alpha=0.6)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    fig.tight_layout()
    if filename:
        save(fig, filename)
    return fig, ax