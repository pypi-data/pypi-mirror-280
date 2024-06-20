import numpy as np
import matplotlib.pyplot as plt

nb_plot = 3

#Etape 1 : Génération du Signal Sinusoïdal

frequence = 5 # Hz
temps = 2 # durée : 2s
nb_echantillons = 1000 # nombre echantillons (sampling rate)

echantillon = np.linspace(start=0, stop=temps, num=nb_echantillons)

signal = np.sin(2 * np.pi * frequence * echantillon)

plt.subplot(nb_plot, 1, 1)
plt.plot(echantillon, signal)
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')
plt.title("signal sinusoıdal avec une frequence de 5 Hz et une duree de 2 secondes")
plt.grid()

#Etape 2 : Création de la Fenêtre de Hamming

fenetre_hamming = np.hamming(nb_echantillons)
signal_hamming = signal * fenetre_hamming

plt.subplot(nb_plot, 1, 2)
plt.plot(echantillon, fenetre_hamming)
plt.title('Signal Sinusoïdal Fenêtre de Hamming')
plt.grid()

plt.tight_layout()
plt.show()