# 🌊 Geospatial-AI-for-Coastal-Erosion-Monitoring

This project demonstrates how **synthetic geospatial datasets** and **AI models** can be used to monitor and predict **coastal erosion risks**.  
It simulates shoreline changes, environmental drivers, and human pressures, then applies machine learning to assess erosion rates and classify vulnerable zones.

---

## 📌 Features
- Generate **>300 synthetic coastal transect points** with longitude/latitude.  
- Simulate **shoreline positions (2000–2024)** influenced by natural and human drivers.  
- Compute **erosion rate (m/yr)** and assign **binary erosion risk labels**.  
- Export results to **CSV, Excel, and GeoJSON** for analysis or GIS visualization.  
- Machine learning models:
  - **Regression** → predict erosion rates.  
  - **Classification** → predict erosion risk categories.  
- Outputs include:
  - Feature importance plots  
  - Regression fit visualization  
  - Interactive **Folium erosion risk map** (2030 forecast)  

---

## 📂 Project Structure
├── generate_synthetic_coastal_erosion_data.py # Script to generate dataset
├── data/
│ ├── synthetic_coastal_erosion_dataset.csv # Generated dataset (CSV)
│ ├── synthetic_coastal_erosion_dataset.xlsx # Generated dataset (Excel)
│ └── coastline_points.geojson # (Optional) geospatial export
├── outputs/
│ ├── feature_importance.png # Driver importance
│ ├── regression_fit.png # Regression model fit
│ └── erosion_risk_map.html # Interactive map
└── README.md # Project documentation

yaml
Copy code

---

## ⚙️ Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/Geospatial-AI-for-Coastal-Erosion-Monitoring.git
cd Geospatial-AI-for-Coastal-Erosion-Monitoring

pip install -r requirements.txt
Core dependencies:

numpy, pandas, matplotlib

scikit-learn

geopandas, shapely

folium

🚀 Usage
Run the synthetic data generator:

bash
Copy code
python generate_synthetic_coastal_erosion_data.py
Train ML models, analyze erosion drivers, and create outputs:

bash
Copy code
python geospatial_ai_coastal_erosion.py
📊 Example Dataset Preview
lon	lat	wave_energy	slope	sediment_supply	human_activity	shoreline_2024_m	erosion_rate_m_per_yr	erosion_risk
3.00	4.55	0.79	0.57	0.17	0.34	-143.07	-5.96	1
3.01	4.55	0.82	0.65	0.16	0.18	-90.26	-3.76	1

🌍 Applications
Coastal risk assessment and planning.

Integration with GIS tools (QGIS, ArcGIS, Folium).

Training/testing AI models for shoreline monitoring.

Educational use in climate-tech and geospatial analytics.

📜 License
MIT License. Free to use and adapt for research and educational purposes.

✨ Acknowledgements
This project is synthetic and intended for demonstration.
For real-world applications, replace synthetic inputs with actual datasets (e.g., satellite-derived shorelines, wave climate, bathymetry, and NDVI).


Author: Amos Meremu Dogiye
Github: https://github.com/Dogiye12

