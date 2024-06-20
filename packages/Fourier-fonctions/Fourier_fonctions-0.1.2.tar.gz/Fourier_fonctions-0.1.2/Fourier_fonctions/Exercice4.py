import numpy as np
import matplotlib.pyplot as plt

f1 = 15
f2 = 27
teta = np.pi/4
duration = 1
sampling_rate = 1000

t = np.linspace(0, duration, int(sampling_rate*duration))

x1 = np.sin(2*np.pi*f1*t)
x2 = np.sin(2*np.pi*f2*t + teta)

#Corrélation Croisée
correlation = np.correlate(x1, x2, 'full')

#Génération des Déplacements
lags = np.arange(-len(x1) + 1, len(x1))

# Trouver le décalage correspondant au pic de corrélation
lag_index = np.argmax(np.abs(correlation))
time_lag = lags[lag_index] / sampling_rate

# Afficher les résultats
print(f"Le retard temporel entre les deux signaux est de {time_lag} secondes")

t_correlation = np.linspace(0, 1, len(correlation))

plt.subplot(2, 1, 1)
plt.plot(t, x1)
plt.plot(t, x2)

plt.subplot(2, 1, 2)
plt.plot(t_correlation, correlation)

plt.show()