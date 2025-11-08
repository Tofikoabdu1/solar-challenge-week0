# 🌞 Solar Data Discovery — 10 Academy Week 0

This project analyzes solar energy data from **Benin**, **Sierra Leone**, and **Togo** to uncover patterns, clean anomalies, and build a dashboard for cross-country comparison. It includes exploratory data analysis (EDA), statistical testing, and a deployable Streamlit dashboard.

---

## 📁 Folder Structure
```
solar-challenge-week0/
├── data/                      # Raw and cleaned CSV files (excluded via .gitignore)
│   ├── benin.csv
│   ├── benin_clean.csv
│   ├── sierraleone.csv
│   ├── sierra_clean.csv
│   ├── togo.csv
│   ├── togo_clean.csv
│   └── ...
├── notebooks/                 # Jupyter notebooks for EDA and analysis
│   ├── benin_eda.ipynb        # Task 2: EDA and cleaning for Benin
│   ├── sierraleone_eda.ipynb       # Task 2: EDA and cleaning for Sierra Leone
│   ├── togo_eda.ipynb         # Task 2: EDA and cleaning for Togo
│   ├── compare_countries.ipynb # Task 3: Cross-country comparison
├── app/                       # Streamlit dashboard application
│   ├── main.py                # Main dashboard script
│   ├── utils.py               # (Optional) helper functions for data processing
│   └── __init__.py
├── scripts/                   # Documentation and helper scripts
│   ├── README.md              # Dashboard usage instructions
│   └── __init__.py
├── requirements.txt           # Python dependencies
├── .gitignore                 # Files and folders to exclude from Git tracking
└── README.md                  # Project overview and instructions
```
---

## ✅ Tasks Overview

### Task 1: Environment Setup
- Created and activated Python virtual environment
- Installed required libraries via `requirements.txt`
- Verified reproducibility with `requirements.txt` and `README.md`

### Task 2: Data Profiling & Cleaning
- Loaded Benin dataset
- Performed missing value analysis and outlier removal (Z-score)
- Cleaned and exported dataset
- Visualized solar metrics, temperature, humidity, and sensor cleaning impact

### Task 3: Cross-Country Comparison
- Combined cleaned datasets from Benin, Sierra Leone, and Togo
- Compared GHI, DNI, DHI via boxplots and summary statistics
- Ran ANOVA/Kruskal–Wallis tests to assess significance
- Highlighted key insights and ranked countries by solar potential

### Bonus: Streamlit Dashboard
- Built interactive dashboard with:
  - Country and metric selectors
  - Date range filter
  - Boxplots, summary tables, correlation heatmaps
  - Download button for filtered data
- Deployed to Streamlit Cloud

---

## 🚀 How to Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/Tofikoabdu1/solar-challenge-week0.git
cd solar-challenge-week0
```
### 2. Activate virtual environment
```bash
source venv/Scripts/activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the dashboard
```bash
streamlit run app/main.py
```

---

## 📊 Key Features
- Cleaned and validated solar datasets
- Statistical comparison across countries
- Interactive dashboard with professional UI
- Downloadable filtered data
- Ready-to-deploy Streamlit app


