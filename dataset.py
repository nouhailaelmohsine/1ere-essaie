import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('C:\Users\nouhaila\Downloads\weather_data.csv.zip')
print(data.head())
# Clean data: Handling missing values
data.fillna(method='ffill', inplace=True)

# Tracer la courbe de température
plt.plot(data['Date_Time'], data['Temperature_C'], label='Temperature (°C)')

# Ajouter les étiquettes et le titre
plt.xlabel('Date and Time')  # Étiquette pour l'axe X
plt.ylabel('Temperature (°C)')  # Étiquette pour l'axe Y
plt.title('Temperature Over Time')  # Titre du graphique

# Rotation des étiquettes sur l'axe X
plt.xticks(rotation=45)

# Afficher la légende et le graphique
plt.legend()
plt.show()
