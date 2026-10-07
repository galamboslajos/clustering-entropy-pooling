# Clustering for Entropy Pooling

A research project exploring clustering-based joint macro states for multi-asset scenario modelling with Entropy Pooling (EP). The proposed extension replaces manually defined states, such as fixed 25th/75th percentile partitions, with data-driven clusters and investigates their use within the existing scenario pipeline.

## Foundation and attribution

This project builds on the investment and risk modelling pipeline developed by [Fortitudo Technologies](https://github.com/fortitudo-tech), particularly [fortitudo.tech](https://github.com/fortitudo-tech/fortitudo.tech) and the [Portfolio Construction and Risk Management examples](https://github.com/fortitudo-tech/pcrm-book). Credit for the underlying framework and original examples belongs to their authors.

The intended contribution here is the clustering application and its evaluation, presented as an extension of that work. Any reused or adapted upstream code will retain its attribution and applicable license notices. This is an independent project and does not imply Fortitudo's endorsement.

## Status

Daily dataset preparation and clustering analysis are implemented. A short research report will follow.

## Daily dataset

Open [`01_daily_macro_dataset.ipynb`](01_daily_macro_dataset.ipynb) in VS Code and select a Python kernel. Install dependencies with `python -m pip install -r requirements.txt`, then run all cells. The notebook constructs a 15-year dataset of S&P 500 closes, 10-year breakeven inflation, 10-year real Treasury yields, the 10y–2y Treasury slope, the Baa–10y Treasury credit spread (FRED BAA10Y), VIX, VIX3M, VIX minus VIX3M, and the S&P 500/gold ratio (calculated from `GC=F` gold futures closes; gold is retained only as a raw source). It also constructs eight S&P 500 technical features: 63-day log momentum, 252-day trailing drawdown, 21-day annualized realized volatility, the 21/126-day log volatility ratio, 21-day log-return trend efficiency, Wilder RSI14, the 200-day moving-average gap, and Wilder ATR percent14. Two earlier years of equity OHLC provide warmup before the 15-year window is exported. Change `AS_OF` to update the window.

Sources are Yahoo Finance, FRED, and Cboe. Downloads, CSV datasets, and retrieval metadata are saved locally under `data/` (ignored by Git). The notebook reports missing observations and discusses adding monthly earnings using release dates and historical vintages.

Continue in [`02_clustering_analysis.ipynb`](02_clustering_analysis.ipynb), which follows the step-by-step style of the MIT practice notebook while using the 17 market features. It compares K-means, K-medoids (FasterPAM), agglomerative clustering, Gaussian mixtures and DBSCAN, with empirical profiles, PCA/t-SNE views and consistent geometric metrics. The final sections tune model parameters, compare PCA95 and robust-scaling calibrations, check initialization stability and present a 20-row comparison table. All geometric scores use the original standardized feature space; DBSCAN noise is excluded and coverage is reported. GMM model selection uses BIC only within one fixed representation. Tables, configurations, labels and figures are saved under `data/clustering/`. The MIT `practice.ipynb` remains a read-only reference.

---checking git vscode
