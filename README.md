# Clustering for Entropy Pooling

A research project exploring clustering-based joint macro states for multi-asset scenario modelling with Entropy Pooling (EP). The proposed extension replaces manually defined states, such as fixed 25th/75th percentile partitions, with data-driven clusters and investigates their use within the existing scenario pipeline.

## Foundation and attribution

This project builds on the investment and risk modelling pipeline developed by [Fortitudo Technologies](https://github.com/fortitudo-tech), particularly [fortitudo.tech](https://github.com/fortitudo-tech/fortitudo.tech) and the [Portfolio Construction and Risk Management examples](https://github.com/fortitudo-tech/pcrm-book). Credit for the underlying framework and original examples belongs to their authors.

The intended contribution here is the clustering application and its evaluation, presented as an extension of that work. Any reused or adapted upstream code will retain its attribution and applicable license notices. This is an independent project and does not imply Fortitudo's endorsement.

## Status

Dataset preparation started. Clustering experiments and a short research report will follow.

## Daily dataset

Open [`01_daily_macro_dataset.ipynb`](01_daily_macro_dataset.ipynb) in VS Code and select a Python kernel. Install dependencies with `python -m pip install -r requirements.txt`, then run all cells. The notebook constructs a 15-year dataset of S&P 500 closes, 10-year breakeven inflation, 10-year real Treasury yields, the 10y–2y Treasury slope, the Baa–10y Treasury credit spread (FRED BAA10Y), VIX, VIX3M, and VIX minus VIX3M. Change `AS_OF` to update the window.

Sources are Yahoo Finance, FRED, and Cboe. Downloads, CSV datasets, and retrieval metadata are saved locally under `data/` (ignored by Git). The notebook reports missing observations and discusses adding monthly earnings using release dates and historical vintages.

Continue in [`02_clustering_analysis.ipynb`](02_clustering_analysis.ipynb), which loads the saved daily levels, previews the first rows, and shows a compact mosaic of all eight series, then transforms equity returns, scales features, applies PCA, and evaluates clustering.

---checking git vscode
