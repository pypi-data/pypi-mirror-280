import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# On définit la fonction g(t)
def g(t) : 
    return np.cos(2*np.pi*5*t) + np.cos(2*np.pi*100*t) + np.cos(2*np.pi*100*t)

#On définit la durée
duration = 0.5
#On définit la fréquence d'echantillonage qui correspond à au moins la fréquence max de la fonction x2 d'après le théorème de Nyquist-Shannon soit fe > 200
fe = 1000
#On définit un tableau de points
x = np.linspace(0, duration, int(fe*duration))

#On créé un tableau qui contient les harmoniques
harmoniques = [50, 100, 500]

#On affiche le signal original
plt.subplot(4, 1, 1)
plt.plot(x, g(x))
plt.title("Signal original")

#On créé une boucle qui calcule et affiche le calcul de la série de fourier pour chaque harmonique
for i, harmonique in enumerate(harmoniques) :
    #On initialise les tableaux qui vont contenir les An et les Bn
    An = []
    Bn = []
    sum = 0
    #On effectue le calcul de la série de Fourier pour chaque harmonique
    for n in range(harmonique) :
        #On reprend les calcule de la série de Fourier pour calculer les An et les Bn, on utilise la fonction quad de scipy pour intégrer
        #on récupère g(t) notre fonction et on intégère sur une période de -pi à pi
        An.append(quad(lambda t : g(t) * np.cos(n*t), -np.pi, np.pi)[0] / np.pi)
        Bn.append(quad(lambda t : g(t) * np.sin(n*t), -np.pi, np.pi)[0] / np.pi)

        #Si c'est la premier harmonique on ajoute uniquement A0 en suivant la formule
        if n == 0 :
            sum += An[n] / 2
        else :
            #Sinon on fait le calcul complet de la série de Fourier
            sum += An[n] * np.cos(n*x) + Bn[n] * np.sin(n*x)

    #On ajoute un nouveau graphe à la suite des autres figures
    plt.subplot(4, 1, i+2)
    #On affiche la transformée pour x harmoniques et le titre
    plt.plot(x, sum)
    plt.title(f"Série de Fourier avec harmonique {harmonique}")

#On lance l'affichage sur pyplot
plt.tight_layout()
plt.show()
        