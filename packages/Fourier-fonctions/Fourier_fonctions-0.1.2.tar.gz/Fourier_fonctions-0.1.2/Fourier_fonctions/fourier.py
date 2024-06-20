# Fourier_fonctions/fourier.py

import numpy as np

def transformee_fourier(signal):
    """
    Calcule la transformée de Fourier d'un signal donné.

    Parameters:
    signal (np.array): Le signal d'entrée.

    Returns:
    np.array: La transformée de Fourier du signal.
    """
    return np.fft.fft(signal)

def transformee_inversee_fourier(spectre):
    """
    Calcule la transformée de Fourier inverse d'un spectre donné.

    Parameters:
    spectre (np.array): Le spectre d'entrée.

    Returns:
    np.array: Le signal temporel reconstruit.
    """
    return np.fft.ifft(spectre)
