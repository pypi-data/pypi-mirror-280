import numpy as np
import matplotlib.pyplot as plt

def moyenneMobile(signal, windowSize) :
    return np.convolve(signal, np.ones(windowSize) / windowSize, 'same')

duration = 10
f = 150
fe = 2*f

t = np.linspace(0, duration, fe)

signal = np.sin(2*np.pi*f*t)

signal += np.random.normal(0.1, 0.5, len(signal))

windowSize = 30

convolution = moyenneMobile(signal, windowSize)

plt.plot(t, signal)
plt.plot(t, convolution, "--")

plt.show()