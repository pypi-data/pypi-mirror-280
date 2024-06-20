import numpy as np
import matplotlib.pyplot as plt


#calcul de la correlation croisee :
#R_x1x2(tau)=int_-inf^+inf(x1(t)x2(t+tau)dt)



# Paramètres des signaux
f1 = 10  # fréquence en Hz pour x1(t)
f2 = 8   # fréquence en Hz pour x2(t)
theta = np.pi / 4  # phase en radians pour x2(t)

# Définition des fonctions x1(t) et x2(t)
def x1(t):
    return np.sin(2 * np.pi * f1 * t)

def x2(t):
    return np.sin(2 * np.pi * f2 * t + theta)

# Définition de la fonction de corrélation croisée
def cross_correlation(x1, x2, max_delay):
    correlation = np.zeros(2 * max_delay + 1)
    for delay in range(-max_delay, max_delay + 1):
        if delay < 0:
            correlation[max_delay + delay] = np.sum(x1[:delay] * x2[-delay:])
        elif delay == 0:
            correlation[max_delay] = np.sum(x1 * x2)
        else:
            correlation[max_delay + delay] = np.sum(x1[delay:] * x2[:-delay])
    return correlation

# Échantillonnage temporel
fs = 1000  # fréquence d'échantillonnage en Hz
t = np.arange(0, 1, 1/fs)  # échantillonnage sur une période de 1 seconde

# Calcul de la corrélation croisée pour un retard maximal de 100 ms (0.1 seconde)
max_delay_samples = int(0.1 * fs)
correlation = cross_correlation(x1(t), x2(t), max_delay_samples)

# Échantillons de délai en secondes
tau = np.arange(-max_delay_samples/fs, max_delay_samples/fs + 1/fs, 1/fs)

# Tracé de la fonction de corrélation croisée
plt.figure(figsize=(10, 6))
plt.plot(tau, correlation)
plt.title('Corrélation croisée entre x1(t) et x2(t)')
plt.xlabel('Retard temporel (s)')
plt.ylabel('Corrélation croisée')
plt.grid(True)
plt.show()
