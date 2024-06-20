import matplotlib.pyplot as plt
import numpy as np

def filtre_Moyen_Mobile(signal, taille_fenetre):
    hamming = np.hamming(taille_fenetre*2)
    convolution = np.convolve(a=signal, v=hamming, mode='same')
    return convolution

#Etape 1 : Génération du Signal Sinusoïdal

nb_plot = 2

frequence = 5 # Hz
temps = 2 # secondes
N = 200

values = np.linspace(start=0, stop=temps, num=N)

# Signal avec du bruit
signal = np.sin(frequence * 2 * np.pi * values) + 0.5 * np.random.randn(N)

figure, axis = plt.subplots(nrows=nb_plot, ncols=1)

axis[0].plot(values, signal)
axis[0].set_title(f"Fonction Sinus avec bruit")



signal_filtre = filtre_Moyen_Mobile(signal, frequence)

axis[1].plot(values, signal_filtre)
axis[1].set_title(f"Fonction Sinus avec bruit filtré")

plt.tight_layout() # Permet de bien affiché avec les espaces entre les graphiques
plt.show()