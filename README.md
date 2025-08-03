# Brent Oil Change Point Analysis

**Project Title**: Change Point Analysis and Statistical Modelling of Brent Oil Prices
**Organization**: Birhan Energies
**Duration**: July–August 2025
**Team Leads**: Mahlet, Rediet, Kerod, Rehmet

---

## 🌍 Business Objective

This project investigates how key geopolitical, economic, and policy-related events have historically impacted Brent crude oil prices. By using Bayesian change point analysis, we aim to detect structural breaks in oil prices and associate them with real-world events such as OPEC decisions, political unrest, sanctions, and global crises.

**Goal**: Provide actionable, data-driven insights to investors, policymakers, and energy firms for better decision-making under market volatility.

---

## 🧪 Project Scope

- **Detect**: Structural change points in the Brent oil price time series (1987–2022)
- **Link**: Detected change points to historical events (OPEC decisions, wars, sanctions, etc.)
- **Quantify**: Changes in statistical properties (mean, volatility) pre/post events
- **Visualize**: Results through an interactive dashboard (Flask + React)

---

## 🗃️ Project Structure

```text
brent-oil-change-point-analysis/
├── data/                 # Raw, interim, and processed datasets
├── notebooks/            # Jupyter notebooks for EDA, modeling, and post-analysis
├── src/                  # Modular Python scripts (data loading, modeling, plotting)
│   ├── data/
│   ├── models/
│   └── utils/
├── dashboard/            # Flask + React dashboard
│   ├── backend/          # Flask API
│   └── frontend/         # React app
├── reports/              # Interim & final reports, screenshots
├── figures/              # Plots and images
├── requirements.txt      # Python dependencies
├── README.md             # Project overview
└── .gitignore
```

---

## 🔍 Methodology

### 1. Data Preparation & EDA
- Daily Brent oil prices from May 1987 to September 2022
- Converted to log returns for stationarity
- Volatility clustering and trends visualized

### 2. Event Mapping
- Manually researched and compiled major global events from 2010–2022
- Stored in a structured CSV format (`data/events.csv`)

### 3. Bayesian Change Point Detection
- Implemented using **PyMC3**
- Models sudden shifts in mean price due to external events
- Monte Carlo Markov Chain (MCMC) used for posterior inference

### 4. Insight Extraction
- Matched detected change points to event timeline
- Quantified effect sizes (% change in mean, volatility spikes)
- Generated interpretative plots and business insights

### 5. Dashboard Development
- Flask backend APIs serve model outputs and metadata
- React frontend presents interactive visualizations:
  - Time series with event overlays
  - Change point markers
  - Event drill-downs and filters

---

## 📈 Key Learning Outcomes

- Bayesian inference using PyMC3
- Change point detection in time series
- Monte Carlo Markov Chain (MCMC) sampling
- Statistical storytelling and event association
- Dashboard design using Flask + React

---

## 🚀 Getting Started

### 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

### 🧪 Running Notebooks

Launch Jupyter Lab:

```bash
jupyter lab
```

Recommended order:
1. `01_eda_visualization.ipynb`
2. `02_event_annotation.ipynb`
3. `03_bayesian_changepoint_model.ipynb`
4. `04_post_model_analysis.ipynb`

### 🌐 Run Dashboard

#### Backend (Flask):

```bash
cd dashboard/backend
python app.py
```

#### Frontend (React):

```bash
cd dashboard/frontend
npm install
npm start
```

---

## 📊 Sample Insights

- In **April 2020**, coinciding with COVID-19 demand collapse, oil prices dropped over 60% — a change point detected with >95% certainty.
- Following the **Russia-Ukraine conflict** (Feb 2022), a sharp increase in price volatility was observed, marked by a model-identified structural break.

---

## 📚 References

- [Bayesian Change Point Detection in PyMC3](https://forecastegy.com/posts/change-point-detection-time-series-python/)
- [Data Science Workflow](https://www.datascience-pm.com/data-science-workflow/)
- [MCMC Explained](https://towardsdatascience.com/monte-carlo-markov-chain-mcmc-explained-94e3a6c8de11)
- [React Dashboard Template](https://github.com/flatlogic/react-dashboard)

---

## 🧑‍💻 Contributors

- Mahlet — Domain Lead, Time Series Modeling
- Rediet — Bayesian Inference & PyMC3
- Kerod — Statistical Analysis & Change Point Detection
- Rehmet — Dashboard Development (React + Flask)

---

## 📄 License

This project is licensed under the MIT License. See [`LICENSE`](./LICENSE) for details.

---

## 🌟 Acknowledgments

This project was developed as part of the **10 Academy Week 10 Challenge** under the mentorship of Mahlet, Rediet, Kerod, and Rehmet.

```
