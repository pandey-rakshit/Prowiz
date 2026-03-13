import matplotlib.pyplot as plt
import seaborn as sns
from config.settings import PLOT_THEME, PLOT_PALETTE, FIG_SIZE, DPI
from config.paths import CHARTS_DIR


def apply_theme():
    sns.set_theme(style=PLOT_THEME, palette=PLOT_PALETTE)
    plt.rcParams.update({
        "figure.figsize"  : FIG_SIZE,
        "axes.titlesize"  : 14,
        "axes.labelsize"  : 12,
        "xtick.labelsize" : 10,
        "ytick.labelsize" : 10,
        "figure.dpi"      : DPI,
        "axes.grid"       : False 
    })


def save(fig: plt.Figure, filename: str):
    CHARTS_DIR.mkdir(parents=True, exist_ok=True)
    path = CHARTS_DIR / filename
    fig.savefig(path, bbox_inches="tight", dpi=DPI)
    plt.close(fig)


def new_fig(nrows: int = 1, ncols: int = 1, **kwargs) -> tuple:
    apply_theme()
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, **kwargs)
    return fig, ax