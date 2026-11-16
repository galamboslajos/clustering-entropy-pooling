"""Plot notebook 04's chosen K-means assignments from the paper snapshot."""
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

paper_dir = Path(__file__).resolve().parent
labels = pd.read_csv(
    paper_dir / "tables/fixed11_ep_selected_assignments.csv",
    index_col="date", parse_dates=["date"],
)["Cluster"]

fig, ax = plt.subplots(figsize=(7.2, 2.5), layout="constrained")
for state, color in zip(sorted(labels.unique()), sns.color_palette("colorblind", 2)):
    dates = labels.index[labels.eq(state)]
    ax.scatter(dates, [state] * len(dates), marker="|", s=90,
               linewidths=1, alpha=0.8, color=color)
ax.set(yticks=[0, 1], yticklabels=["0 (stress)", "1 (calmer)"],
       ylim=(-0.45, 1.45), xlim=(labels.index.min(), labels.index.max()),
       xlabel="Date", ylabel="Cluster", title="Fixed eleven-input K-means: daily assignments")
ax.xaxis.set_major_locator(mdates.YearLocator(2))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
ax.grid(axis="x", alpha=0.2)
ax.spines[["top", "right"]].set_visible(False)
fig.savefig(paper_dir / "images/fixed11_kmeans_timeline.png", dpi=240)
plt.close(fig)
