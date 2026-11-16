"""Plot the chosen model's saved daily labels for the paper."""
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

paper_dir = Path(__file__).resolve().parent
labels = pd.read_csv(
    paper_dir.parent / "data/clustering/all_model_assignments.csv",
    index_col="date", parse_dates=["date"],
)["K-means / Robust"]

fig, ax = plt.subplots(figsize=(7.2, 2.6), layout="constrained")
for state, color in zip([0, 1], sns.color_palette("colorblind", 2)):
    observations = labels.loc[labels == state]
    ax.scatter(observations.index, observations, marker="|", s=110,
               linewidths=1.1, alpha=0.8, color=color)
ax.set(yticks=[0, 1], yticklabels=["0 (calmer)", "1 (stressed)"],
       ylim=(-0.45, 1.45), xlim=(labels.index.min(), labels.index.max()),
       xlabel="Date", ylabel="Cluster", title="Historical cluster assignments")
ax.xaxis.set_major_locator(mdates.YearLocator(2))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
ax.grid(axis="x", alpha=0.2)
ax.spines[["top", "right"]].set_visible(False)
images = paper_dir / "images"
images.mkdir(exist_ok=True)
fig.savefig(images / "cluster_timeline.png", dpi=300)
plt.close(fig)
