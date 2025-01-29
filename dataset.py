import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
data=pd.read_csv("C:/Users/nouhaila/Downloads/seattle-weather.csv")
print(data.head())
# Clean data: Handling missing values
data.fillna(method='ffill', inplace=True)
data['temp_wave'] = np.sin(np.linspace(0, 10, len(data))) * 5 + data['temp_max']
colors = sns.color_palette("coolwarm", len(data))
plt.figure(figsize=(12, 6))

# Tracer la courbe de température
plt.plot(data['date'], data['temp_max'], label='Temperature (°C)')

# Ajouter les étiquettes et le titre
plt.xlabel('Date and Time')  # Étiquette pour l'axe X
plt.ylabel('Temperature (°C)')  # Étiquette pour l'axe Y
plt.title('Temperature Over Time')  # Titre du graphique
for i in range(len(data) - 1):
    plt.plot(data['date'].iloc[i:i+2], data['temp_wave'].iloc[i:i+2], color=colors[i], linewidth=2)


# Tracer la courbe de précipitation
#plt.plot(data['date'], data['precipitation'], label='Précipitation')

# Ajouter les étiquettes et le titre
#plt.xlabel('Date and Time')  # Étiquette pour l'axe X
#plt.ylabel('precipitation')  # Étiquette pour l'axe Y
#plt.title('precipitation')  # Titre du graphique
plt.title(" Température sous forme de Vague Artistique ", fontsize=16, fontweight="bold", color="darkblue")
plt.xlabel("Date", fontsize=12, color="gray")
plt.ylabel("Température (°C)", fontsize=12, color="gray")
plt.xticks(rotation=45)
plt.grid(False)

# Rotation des étiquettes sur l'axe X
plt.xticks(rotation=45)

# Afficher la légende et le graphique
plt.legend()
plt.show()
