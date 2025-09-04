# Time Series Forecasting App  – ARIMA & SARIMAX

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://time-series-forecast-chatlify-akx.streamlit.app/)

###  Live Demo  
Experience the app in action: [**Forecast Your Data Now →**](https://time-series-forecast-chatlify-akx.streamlit.app/)

---

##  Overview  
This interactive app enables you to perform time series forecasting using advanced models—**ARIMA** and **SARIMAX**—through an intuitive web interface powered by Streamlit.

-  Upload any CSV with a date column and a numeric value column.
-  Automatically handles messy date formats with a built-in cleaning pipeline.
-  Choose between ARIMA or seasonal SARIMAX models.
-  Visualize forecasts with dynamic charts and tabular results.
-  Ideal for analysts, data scientists, and non-technical users alike.

---

##  Features

| Feature                | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| **File Upload**         | Drag-and-drop CSV upload handled directly in the sidebar.                   |
| **Auto-cleaning**       | Attempts basic date parsing; if it fails, strips headers, coerces dates, and drops invalid rows. |
| **Model Selection**     | Choose between ARIMA (non-seasonal) and SARIMAX (seasonal-aware).           |
| **Parameter Controls**  | Customize `p`, `d`, `q`, and seasonal `P`, `D`, `Q`, `s` parameters on-the-fly. |
| **Forecast Horizon**    | Control how far into the future to forecast (1–36 months).                  |
| **Interactive Charts**  | Clean, wide-format plot comparing actual values vs. forecasted values.       |
| **Forecast Table**      | View forecast values in a structured, exportable table.                     |

---

##  Quick Start

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/Time-Series-Forecast-Chatlify.git
   cd Time-Series-Forecast-Chatlify
