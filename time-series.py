import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA
from pandas.tseries.offsets import DateOffset

st.set_page_config(
    page_title="Time Series Forecasting App",
    page_icon="📊",
    layout="wide",
)

st.markdown(
    """
    <div style="text-align: center; padding: 20px; background-color: #1E1E1E; border-radius: 10px;">
        <h1 style="color: #4B8BBE; font-size: 40px; margin-bottom: 10px;">
            📊 Time Series Forecasting
        </h1>
        <h3 style="color: #FFD43B; margin-top: 0;">
            Using <span style="color:#4B8BBE;">ARIMA</span> & <span style="color:#306998;">SARIMAX</span> Models
        </h3>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# Sidebar for data upload and settings
with st.sidebar:
    st.header("Upload & Settings")
    uploaded_file = st.file_uploader("Upload your time series CSV", type=["csv"], key="file_uploader_main")
    st.markdown("Select model and parameters after upload.")
    st.markdown("---")
    st.markdown("Built by Akash Kumar")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.markdown("### 1. Preview Data")
    st.dataframe(df.head())

    date_col = st.selectbox("Date column:", df.columns)
    value_col = st.selectbox("Value column:", df.columns)

    # Cleaning layer
    try:
        df[date_col] = pd.to_datetime(df[date_col])
    except Exception:
        st.warning("Parsing failed, applying auto-cleaning.")
        df.columns = df.columns.str.strip()
        df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
        df = df.dropna(subset=[date_col])

    df.set_index(date_col, inplace=True)
    df = df[[value_col]].dropna()

    st.markdown("### 2. Time Series Data")
    st.line_chart(df)

    model_type = st.selectbox("Choose model:", ["ARIMA", "SARIMAX"], key="model_type")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("ARIMA Parameters")
        p = st.number_input("p (AR)", 0, 5, value=1)
        d = st.number_input("d (I)", 0, 2, value=1)
        q = st.number_input("q (MA)", 0, 5, value=1)
        if model_type == "SARIMAX":
            st.subheader("Seasonal Parameters")
            P = st.number_input("P (Seasonal AR)", 0, 5, value=1, key='P')
            D = st.number_input("D (Seasonal I)", 0, 2, value=1, key='D')
            Q = st.number_input("Q (Seasonal MA)", 0, 5, value=1, key='Q')
            s = st.number_input("s (Seasonal Period)", 1, 24, value=12, key='s')

    forecast_months = st.slider("Forecast horizon (months)", 1, 36, 12)

    if st.button("Run Forecast"):
        if model_type == "ARIMA":
            model = ARIMA(df[value_col], order=(p, d, q))
            results = model.fit()
        else:
            model = sm.tsa.statespace.SARIMAX(df[value_col], order=(p, d, q), seasonal_order=(P, D, Q, s))
            results = model.fit(disp=False)

        future_dates = [df.index[-1] + DateOffset(months=i) for i in range(1, forecast_months + 1)]
        future = pd.DataFrame(index=future_dates, columns=[value_col])
        forecast = results.predict(start=len(df), end=len(df) + forecast_months - 1, dynamic=True)
        future["forecast"] = forecast.values
        combined = pd.concat([df, future])

        st.markdown("### 3. Forecast Results")
        fig, ax = plt.subplots(figsize=(12, 6))
        combined[value_col].plot(ax=ax, color="blue", label="Actual")
        combined["forecast"].plot(ax=ax, color="orange", label="Forecast")
        ax.legend(frameon=True)
        st.pyplot(fig)

        st.markdown("### 4. Forecast Table")
        st.dataframe(future[["forecast"]].round(2))
