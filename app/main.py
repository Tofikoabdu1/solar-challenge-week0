import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import f_oneway

# Page config
st.set_page_config(page_title="Solar Dashboard", layout="wide")
st.markdown("<style>footer {visibility: hidden;}</style>", unsafe_allow_html=True)

# Title
st.title("🌞 Solar Data Comparison Dashboard")
st.markdown("Compare solar metrics across Benin, Sierra Leone, and Togo with interactive filters and insights.")

# Sidebar filters
st.sidebar.header("🔧 Filters")
selected_countries = st.sidebar.multiselect(
    "Select countries",
    ["Benin", "Sierra Leone", "Togo"],
    default=["Benin", "Sierra Leone", "Togo"]
)
metric = st.sidebar.selectbox("Select metric", ['GHI', 'DNI', 'DHI'])

# Date range filter
start_date = st.sidebar.date_input("Start date", pd.to_datetime("2025-01-01"))
end_date = st.sidebar.date_input("End date", pd.to_datetime("2025-12-31"))

# Load and combine data
@st.cache_data
def load_data():
    benin = pd.read_csv('data/benin_clean.csv', parse_dates=['Timestamp'])
    sierra = pd.read_csv('data/sierraleone_clean.csv', parse_dates=['Timestamp'])
    togo = pd.read_csv('data/togo_clean.csv', parse_dates=['Timestamp'])
    benin['Country'] = 'Benin'
    sierra['Country'] = 'Sierra Leone'
    togo['Country'] = 'Togo'
    return pd.concat([benin, sierra, togo], ignore_index=True)

df = load_data()
df = df[df['Country'].isin(selected_countries)]
df = df[(df['Timestamp'] >= pd.to_datetime(start_date)) & (df['Timestamp'] <= pd.to_datetime(end_date))]

# ANOVA p-value
if len(selected_countries) == 3:
    b = df[df['Country'] == 'Benin']['GHI']
    s = df[df['Country'] == 'Sierra Leone']['GHI']
    t = df[df['Country'] == 'Togo']['GHI']
    f_stat, p_val = f_oneway(b, s, t)
    st.sidebar.markdown(f"**ANOVA p-value (GHI):** `{p_val:.4f}`")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["📦 Boxplot", "📈 Summary Table", "🏆 GHI Ranking", "📊 Correlation Heatmap"])

with tab1:
    st.subheader(f"{metric} Distribution by Country")
    fig, ax = plt.subplots()
    sns.boxplot(x='Country', y=metric, data=df, ax=ax)
    st.pyplot(fig)

with tab2:
    st.subheader("Summary Statistics")
    summary = df.groupby('Country')[['GHI', 'DNI', 'DHI']].agg(['mean', 'median', 'std']).round(2)
    st.dataframe(summary)

with tab3:
    st.subheader("Average GHI Ranking")
    avg_ghi = df.groupby('Country')['GHI'].mean().sort_values(ascending=False)
    st.bar_chart(avg_ghi)

with tab4:
    st.subheader("Correlation Heatmap")
    corr = df[['GHI', 'DNI', 'DHI', 'Tamb', 'RH', 'WS', 'WSgust']].corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

# Download button
st.sidebar.markdown("### 📥 Download Filtered Data")
st.sidebar.download_button(
    label="Download CSV",
    data=df.to_csv(index=False),
    file_name="filtered_solar_data.csv",
    mime="text/csv"
)

# Footer
st.markdown("""
    <hr style="margin-top: 2rem;">
    <div style="text-align: center; font-size: 0.9rem;">
        Built by Tofik | 10 Academy Week 0 | 🌞 Solar Data Dashboard
    </div>
""", unsafe_allow_html=True)
