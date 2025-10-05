# NASA_SPACE_APP_CHALLENGE
NASA Space Apps Challenge: Urban Climate Lens

Team Etoile Noir

Authors: Shashwat & Sameer

🌍 Project Overview

Urban Climate Lens is a data-driven solution developed as part of the NASA Space Apps Challenge. Our goal: map, analyze, and forecast PM2.5 air pollution risk across countries like India and Bangladesh, using NASA satellite data, open AI tools, and advanced forecasting models.

This public notebook and dashboard provide transparent, science-based insights for planners, policy makers, and the global community.

🚀 What Does This Repo Contain?
Untitled0.ipynb:
Colab-based Jupyter notebook for air pollution (PM2.5) analysis and forecasting using Python, Pandas, Prophet, and matplotlib.
Features:

Historic and predicted PM2.5 levels by country

Plotting and PNG export for dashboard

Data cleaning, trend analysis, and uncertainty quantification

pm25-air-pollution.csv:
Raw and clean air pollution data used for modeling

app.py (optional):
Demo Streamlit dashboard code — visualize model results, add interactive features, share live demos!

📊 Data Sources
NASA MODIS VIIRS AOD (PM2.5)

World Health Organization (reference ranges)

Dataset covers 2010–2029 (historic + forecast for major South Asian countries).

🧑‍💻 How to Run It
Open Untitled0.ipynb in Google Colab (recommended for easy package install)

Upload/copy pm25-air-pollution.csv as needed

Run all cells to generate historical analysis, build forecasts, and auto-save plots (as PNG)

To launch further dashboards, run app.py with Streamlit

bash
pip install streamlit prophet pandas matplotlib
streamlit run app.py
(Make sure the plots/ folder contains plot PNGs generated from your notebook.)

🧩 Features
Interactive pollution prediction/planning notebook

Dashboard (if running app.py):

Multi-country selection and plots

Insights and action recommendations

“What-if” scenario sliders for interventions (trees, emissions, etc.)

Planned: live AI Copilot FAQ

📄 License
MIT License — free to use, remix, and expand.

🤝 Join & Collaborate
Fork this repo, add your city or dataset, expand for other risk layers (heat, NDVI, etc.)

Contact Team Etoile Noir for improvement/collaboration/prizes

NASA Space Apps Challenge 2025 — mapping hope, one city at a time.

