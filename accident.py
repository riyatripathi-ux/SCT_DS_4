import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap

# Load dataset
df = pd.read_csv('US_Accidents_Dec20.csv')

# Convert date/time columns
df['Start_Time'] = pd.to_datetime(df['Start_Time'])

# Extract hour of day
df['Hour'] = df['Start_Time'].dt.hour

# Group accidents by weather condition
weather_counts = df['Weather_Condition'].value_counts().head(10)

# Plot top weather conditions for accidents
plt.figure(figsize=(10,6))
sns.barplot(x=weather_counts.values, y=weather_counts.index)
plt.title('Top Weather Conditions for Accidents')
plt.show()

# Prepare data for map heatmap (latitude, longitude)
accident_map = folium.Map(location=[df['Start_Lat'].mean(), df['Start_Lng'].mean()], zoom_start=6)

heat_data = list(zip(df['Start_Lat'], df['Start_Lng']))

HeatMap(heat_data, radius=10).add_to(accident_map)

# Save map
accident_map.save("accident_hotspots.html")
