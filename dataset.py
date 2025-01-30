import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 1️⃣ Charger le dataset
file_path = "/mnt/data/seattle-weather.csv"
data = pd.read_csv(file_path)

# 2️⃣ Convertir la date et trier les données
data['date'] = pd.to_datetime(data['date'])
data = data.sort_values(by="date")

# 3️⃣ Associer chaque type de météo à une couleur de flamme
weather_colors = {
    "rain": "blue",
    "drizzle": "lightblue",
    "snow": "white",
    "fog": "gray",
    "sun": "orange",
    "cloud": "purple"
}

# Assigner une couleur à chaque ligne
data['color'] = data['weather'].map(weather_colors).fillna("red")  # Par défaut, rouge

# 4️⃣ Normaliser les températures et précipitations
data['temp_scaled'] = (data['temp_max'] - data['temp_max'].min()) / (data['temp_max'].max() - data['temp_max'].min())
data['precip_scaled'] = (data['precipitation'] - data['precipitation'].min()) / (data['precipitation'].max() - data['precipitation'].min())

# 5️⃣ Générer les flammes
plt.figure(figsize=(12, 6))
x_values = np.linspace(-1, 1, 100)  # Axe X de la flamme

for i, row in enumerate(data.sample(50)):  # Prendre 50 jours au hasard pour éviter une surcharge
    flame_height = row['temp_scaled'] * 5  # Hauteur proportionnelle à la température
    flame_width = row['precip_scaled'] * 3 + 0.5  # Largeur proportionnelle à la pluie

    # Générer une forme de flamme avec une fonction sinusoïdale
    y_values = np.sin(x_values * np.pi) * flame_height  

    # Positionner la flamme sur l’axe X
    x_position = i * 0.5  
    
    # Dessiner la flamme
    plt.fill_between(x_values + x_position, y_values, color=row['color'], alpha=0.7)

# 6️⃣ Personnalisation du graphique
plt.title("🔥 Weather Flames: Température & Précipitations 🔥", fontsize=14, fontweight="bold", color="red")
plt.axis("off")  # Cacher les axes pour un effet artistique
plt.show()


# data=pd.read_csv("C:/Users/nouhaila/Downloads/seattle-weather.csv")
#print(data.head())
# Clean data: Handling missing values
#data.fillna(method='ffill', inplace=True)
#data['temp_wave'] = np.sin(np.linspace(0, 10, len(data))) * 5 + data['temp_max']
#colors = sns.color_palette("coolwarm", len(data))
#plt.figure(figsize=(12, 6))

# Tracer la courbe de température
#plt.plot(data['date'], data['temp_max'], label='Temperature (°C)')

# Ajouter les étiquettes et le titre
#plt.xlabel('Date and Time')  # Étiquette pour l'axe X
#plt.ylabel('Temperature (°C)')  # Étiquette pour l'axe Y
#plt.title('Temperature Over Time')  # Titre du graphique
#for i in range(len(data) - 1):
 #   plt.plot(data['date'].iloc[i:i+2], data['temp_wave'].iloc[i:i+2], color=colors[i], linewidth=2)


# Tracer la courbe de précipitation
#plt.plot(data['date'], data['precipitation'], label='Précipitation')

# Ajouter les étiquettes et le titre
#plt.xlabel('Date and Time')  # Étiquette pour l'axe X
#plt.ylabel('precipitation')  # Étiquette pour l'axe Y
#plt.title('precipitation')  # Titre du graphique
#plt.title(" Température sous forme de Vague Artistique ", fontsize=16, fontweight="bold", color="darkblue")
#plt.xlabel("Date", fontsize=12, color="gray")
#plt.ylabel("Température (°C)", fontsize=12, color="gray")
#plt.xticks(rotation=45)
#plt.grid(False)

# Rotation des étiquettes sur l'axe X
#plt.xticks(rotation=45)

# Afficher la légende et le graphique
#plt.legend()
#plt.show() 

