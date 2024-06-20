import matplotlib.pyplot as plt
import numpy as np

# CONVOLUTION :

#DEBUG
def debug():
    print("DEBUG")
    print(f"Values : {len(values)} - Hamming : {len(hamming)}")
    print(f"Values shape : {values.shape} - Hamming shape : {hamming.shape} - Convolution : {convolution.shape}")

nb_plot = 3

#Etape 1 : Génération du Signal Sinusoïdal

frequence = 5 # Hz
temps = 2 # secondes
N = 100

values = np.linspace(start=0, stop=temps, num=N)

signal = np.sin(frequence * 2 * np.pi * values)

figure, axis = plt.subplots(nrows=nb_plot, ncols=1)

axis[0].plot(values, signal)
axis[0].set_title(f"Fonction Sinus ({frequence}Hz | {temps} secondes)")
#plt.figure(0)



#Etape 2 : Création de la Fenêtre de Hamming

hamming = np.hamming(N)

axis[1].plot(values, hamming)
axis[1].set_title("Fenêtre de Hamming")

#Etape 3 : Convolution du Signal avec la Fenêtre de Hamming
convolution = np.convolve(a=signal, v=hamming, mode='same')

debug()

axis[2].plot(values, convolution)
axis[2].set_title(f"Convolution du signal avec la fenêtre de Hamming")

plt.tight_layout() # Permet de bien affiché avec les espaces entre les graphiques
plt.show()


