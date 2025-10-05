import streamlit as st
import os

st.title("PM2.5 Air Pollution Analysis and Forecast Dashboard")

st.header("Historical Data and Predictions")

plot_files = [f for f in os.listdir('plots') if f.endswith('.png')]

for plot_file in plot_files:
    country_name = plot_file.replace('_forecast.png', '').replace('_', ' ')
    st.subheader(f"PM2.5 Concentration Forecast for {country_name}")
    st.image(os.path.join('plots', plot_file))

st.header("Findings")

st.markdown("""
Here are some key findings from the analysis and time series forecasting of PM2.5 air pollution:

* **Overall Trends:** Analyze the plots for each country to identify general trends in PM2.5 concentrations over the historical period (2010-2019). Note which countries show increasing, decreasing, or relatively stable pollution levels.
* **Predicted Future Trends:** Examine the predicted future trends (2020-2029) for each country. Note which countries are predicted to see increases or decreases in pollution, and consider the uncertainty intervals around these predictions.
* **High and Low Pollution Levels:** Identify countries with historically high and low PM2.5 concentrations. Observe if these countries are predicted to maintain their relative positions in the future.
* **Uncertainty:** Pay attention to the width of the uncertainty intervals in the forecasts. Wider intervals indicate less certainty in the predictions, which might be due to more volatile historical data or limitations of the model.
* **Potential Factors:** While this analysis focuses on time series trends, real-world air pollution is influenced by various factors like industrial activity, traffic, geographical location, and environmental regulations. Consider how these factors might play a role in the observed historical data and predicted future trends.

This dashboard provides a country-by-country view of historical PM2.5 data and future predictions based on the trained Prophet model. Further analysis could involve exploring the underlying causes of these trends and incorporating additional relevant data for more comprehensive insights.
""")
