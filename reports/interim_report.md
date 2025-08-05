# 📊 Task 1: Defining the Analysis Workflow and Understanding the Data

---

## 🧭 1. Data Analysis Workflow Overview

The project aims to detect and interpret significant structural shifts in Brent oil prices using **changepoint analysis**. The workflow for this project includes:

1. **Data Acquisition**:
   - Load daily Brent oil price data (`BrentOilPrices.csv`) spanning multiple years.
   - Handle missing values and ensure data consistency in timestamps and formatting.

2. **Exploratory Data Analysis (EDA)**:
   - Visualize time series to inspect trends, volatility, seasonality.
   - Compute rolling averages and volatility metrics to understand market behavior.

3. **Time Series Diagnostics**:
   - Test for **stationarity** using the Augmented Dickey-Fuller test.
   - Identify **trend** and **seasonal** components using decomposition.

4. **Event Dataset Compilation**:
   - Compile a curated set of geopolitical, economic, and OPEC-related events (see Section 2 below).
   - Match event dates to potential inflection points in the oil price time series.

5. **Change Point Detection**:
   - Apply **Bayesian change point detection** (e.g., via `pymc`, `ruptures`, or `bayesian_changepoint_detection`) to identify abrupt structural changes.
   - Extract and interpret break dates, segment parameters, and posteriors.

6. **Interpretation and Communication**:
   - Visualize changepoints and annotate them with relevant events.
   - Produce dashboards and visual summaries for technical and non-technical stakeholders.

7. **Reporting**:
   - Generate an interim and final report with findings, visualizations, assumptions, and recommendations.

---

## 📅 2. Event Data Compilation

The table below lists major events that could potentially explain structural changes in Brent oil prices. These will later be compared with detected changepoints.

| Date       | Event Description                                                    |
|------------|-----------------------------------------------------------------------|
| 2008-09    | Global financial crisis (Lehman collapse, oil demand shock)           |
| 2010-01    | Arab Spring unrest begins                                             |
| 2011-03    | Libyan Civil War affects oil supply                                   |
| 2014-11    | OPEC decision not to cut production despite price fall                |
| 2016-01    | Lifting of Iran sanctions                                             |
| 2018-10    | US sanctions on Iran oil exports reimposed                            |
| 2019-09    | Attack on Saudi Aramco oil facilities                                 |
| 2020-03    | COVID-19 pandemic + Russia-Saudi oil price war                        |
| 2020-04    | Oil prices crash; WTI goes negative, Brent collapses                  |
| 2021-03    | Global recovery begins post-COVID; oil demand surges                  |
| 2022-02    | Russia invades Ukraine, supply shock escalates                        |
| 2023-10    | Escalation of Middle East tensions                                    |

The dataset will be saved as `event_metadata.csv` and used for changepoint interpretation.

---

## ⚖️ 3. Assumptions and Limitations

### Assumptions:
- Daily Brent oil prices reflect market consensus of supply-demand fundamentals.
- Major geopolitical or economic events lead to market behavior changes detectable in price data.
- Event date proximity to detected changepoints suggests potential impact.

### Limitations:
- **Correlation ≠ Causation**: Just because a changepoint occurs near an event does not prove the event caused the price shift.
- **Noise and Lag**: Prices may react to rumors, expectations, or with a delay, making exact attribution difficult.
- **Data Granularity**: Daily frequency may miss intra-day dynamics.
- **Model Dependency**: Changepoint models rely on assumptions of normality, independence, and may overfit in noisy regimes.

---

## 📡 4. Communication Channels and Formats

To communicate results effectively to both technical and business stakeholders, the following channels and formats will be used:

| Audience        | Format                         | Tool                          |
|-----------------|--------------------------------|-------------------------------|
| Data Scientists | Jupyter notebooks, dashboards  | Python, Streamlit             |
| Executives      | Reports, Slide decks           | Word/PDF, PowerPoint          |
| Public/Clients  | Infographics, Interactive plots| Plotly, Streamlit dashboard   |
| Versioning      | GitHub repo with Markdown docs | Git, GitHub Pages             |

---

## 📚 5. Understanding the Data and Model

### 5.1 Time Series Properties of Brent Oil Data

The Brent oil price time series exhibits the following:

- **Trend**: Long-term upward or downward price movements tied to economic cycles.
- **Volatility Clustering**: Periods of calm and turbulence driven by global events.
- **Seasonality**: Weak or absent in daily data, but cyclical behavior may emerge in longer windows.
- **Non-stationarity**: Price levels and variance change over time. This requires transformation (e.g., log returns) or changepoint modeling.

### 5.2 Purpose of Change Point Models

Change point models are used to:
- Detect **structural breaks** in time series data (e.g., mean shifts, variance changes).
- Segment time periods into regimes with distinct statistical properties.
- Infer **when** significant behavioral shifts occurred in the market.

This is particularly important for oil prices, where shifts in production policy or crises can abruptly change pricing dynamics.

### 5.3 Expected Outputs and Interpretation

A changepoint model provides:

| Output                    | Description                                                  |
|---------------------------|--------------------------------------------------------------|
| Changepoint Dates         | Time indices where structural breaks occur                   |
| Regime Parameters         | Mean/variance of price in each segment                       |
| Posterior Probabilities   | Probability of a changepoint at each time step               |
| Uncertainty Quantification| Confidence in model results via Bayesian inference           |

#### Limitations:
- May miss subtle shifts.
- Sensitive to hyperparameter settings.
- Can overfit if too many changepoints are allowed.

---

✅ This completes Task 1 and sets the foundation for time series modeling, interpretation, and communication.
