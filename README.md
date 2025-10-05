# NASA_SPACE_APP_CHALLENGE

# 🌍 NASA Space Apps Challenge: Urban Climate Lens  

**Team:** Étoile Noir  
**Authors:** Shashwat & Sameer  

---

## 🛰️ Project Overview  
**Urban Climate Lens** is a data-driven solution developed as part of the **NASA Space Apps Challenge**.  
Our mission: to **map, analyze, and forecast PM2.5 air pollution risks** across countries like **India and Bangladesh**, using **NASA satellite data**, **open AI tools**, and **advanced forecasting models**.  

This public notebook and dashboard provide **transparent, science-based insights** for planners, policymakers, and the global community.  

---

## 🚀 Repository Contents  

### 📘 `Air_pollution.ipynb`  
A Colab-based **Jupyter Notebook** for PM2.5 air pollution analysis and forecasting using:
- Python  
- Pandas  
- Prophet  
- Matplotlib  

**Features include:**  
- Historical and predicted PM2.5 levels by country  
- Plotting and PNG export for dashboard  
- Data cleaning, trend analysis, and uncertainty quantification  

---

### 📁 `pm25-air-pollution.csv`  
- Contains both **raw and cleaned PM2.5 data** used for modeling and forecasting.  

---

### 💻 `app.py` (optional)  
Demo **Streamlit dashboard** for visualizing model results and adding interactivity.  
Use it to build and share live demos!  

---

## 📊 Data Sources  
- **NASA MODIS VIIRS AOD (PM2.5)**  
- **World Health Organization (WHO)** — for reference ranges  

**Dataset coverage:**  
2010–2029 (historical + forecasted data for major South Asian countries)  

---

## 🧑‍💻 How to Run  

### Option 1: Run in Google Colab (Recommended)
1. Open `Untitled0.ipynb` in **Google Colab**  
2. Upload or copy `pm25-air-pollution.csv` to the runtime environment  
3. Run all cells to:
   - Generate historical analysis  
   - Build forecasts  
   - Auto-save plots (as PNGs in the `/plots` folder)  

### Option 2: Launch the Dashboard Locally
```bash
pip install streamlit prophet pandas matplotlib
streamlit run app.py
