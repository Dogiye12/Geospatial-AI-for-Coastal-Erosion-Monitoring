import pandas as pd
import numpy as np

# Reproducibility
np.random.seed(42)
n_points = 320

# Generate synthetic coastline lons/lats
lons = np.linspace(3.0, 6.5, n_points)
lats = 4.55 + 0.15*np.sin((lons-3.0)*np.pi/1.5) + np.random.normal(0, 0.005, size=n_points)

# Synthetic drivers
wave_energy = np.clip(0.4 + 0.4*np.sin((lons-2.5)*np.pi/1.2) + np.random.normal(0,0.05,n_points), 0, 1)
slope = np.clip(0.3 + 0.3*np.cos((lons-3.2)*np.pi/1.7) + np.random.normal(0,0.04,n_points), 0.05, 1)

river_mouths = np.array([3.4, 4.1, 5.2, 6.1])
dist_to_river = np.min(np.abs(lons.reshape(-1,1) - river_mouths.reshape(1,-1)), axis=1)
sediment_supply = np.exp(-dist_to_river/0.3) + 0.1*np.random.rand(n_points)
sediment_supply = (sediment_supply - sediment_supply.min())/(sediment_supply.max()-sediment_supply.min())

human_activity = 0.2 + 0.6*np.random.rand(n_points)
for c,lvl in [(3.8,0.8),(5.6,0.85)]:
    human_activity += lvl*np.exp(-((lons - c)**2)/(2*0.06**2))
human_activity = (human_activity - human_activity.min())/(human_activity.max()-human_activity.min())

veg_stability = 0.3 + 0.6*np.random.rand(n_points)
veg_stability = (veg_stability - veg_stability.min())/(veg_stability.max()-veg_stability.min())

curvature = np.gradient(np.gradient(lats))
curvature = (curvature - curvature.min())/(curvature.max()-curvature.min()+1e-9)

# Pressure → shoreline change
pressure = (0.9*wave_energy + 0.8*human_activity - 0.7*slope - 1.0*sediment_supply - 0.6*veg_stability + 0.3*curvature)
pressure = (pressure - pressure.mean())/pressure.std()
decadal_change = -40*pressure + np.random.normal(0,6,n_points)

pos_2000 = np.zeros(n_points)
pos_2010 = pos_2000 + decadal_change
pos_2020 = pos_2010 + (decadal_change*(0.8+0.4*np.random.rand(n_points)))
pos_2024 = pos_2020 + (decadal_change*0.4 + np.random.normal(0,3,n_points))

erosion_rate = (pos_2024 - pos_2000)/(2024-2000)
erosion_risk = (erosion_rate < -1.2).astype(int)

# Build dataframe
df = pd.DataFrame({
    "lon": lons,
    "lat": lats,
    "wave_energy": wave_energy,
    "slope": slope,
    "sediment_supply": sediment_supply,
    "human_activity": human_activity,
    "veg_stability": veg_stability,
    "curvature": curvature,
    "shoreline_2000_m": pos_2000,
    "shoreline_2010_m": pos_2010,
    "shoreline_2020_m": pos_2020,
    "shoreline_2024_m": pos_2024,
    "erosion_rate_m_per_yr": erosion_rate,
    "erosion_risk": erosion_risk
})

# Save outputs
df.to_csv("synthetic_coastal_erosion_dataset.csv", index=False)
df.to_excel("synthetic_coastal_erosion_dataset.xlsx", index=False)

print("Synthetic dataset saved as CSV and Excel.")
