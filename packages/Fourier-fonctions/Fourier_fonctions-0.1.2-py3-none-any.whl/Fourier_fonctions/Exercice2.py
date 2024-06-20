import numpy as np
import matplotlib.pyplot as plt

#On définit les différentes variables
duration = 1 # Par défaut on met la durée à 1
fe = 1000 # fréquence d'échantillonage = 1000 selon l'énoncé

# On définit notre échantillon
t = np.linspace(0, duration, int(fe*duration))

#On calcul le signal
signal = np.sin(2*np.pi*50*t) + np.sin(2*np.pi*150*t) + np.sin(2*np.pi*200*t)

facteurZeroPadding = 5
nouvelle_longueur = len(signal) * facteurZeroPadding

#On ajoute du zéro padding au signal
signalPadding = np.pad(signal, (0, nouvelle_longueur - len(signal)), mode="constant")

#On calcul la transformée de Fourier
transformeeFourier = np.fft.fft(signalPadding)

#On récupère les fréquences de la transformée
freqTransformee = np.linspace(0, fe, len(transformeeFourier))

#On affiche les différents graphes
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title("Signal original")

plt.subplot(2, 1, 2)
plt.plot(freqTransformee, np.abs(transformeeFourier))
plt.title("Transformee de Fourier")

plt.xlim([0, fe / 2])

# Frequences 50, 150 et 200 dans le signal
plt.tight_layout()
plt.show()