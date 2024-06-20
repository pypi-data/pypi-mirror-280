import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft


# Définition de la fonction g(t)
def g(t):
    return np.sin(2 * np.pi * 30 * t) + np.cos(2 * np.pi * 10 * t)


# Paramètres d'échantillonnage
fs = 2000  # Fréquence d'échantillonnage en Hz
duration = 0.8  # Durée en secondes
t = np.arange(0, duration, 1 / fs)  # Vecteur temps basé sur la fréquence d'échantillonnage

# Échantillonnage de la fonction
g_t = g(t)  # Calcul des valeurs de g(t) aux instants d'échantillonnage


# Fonction pour calculer l'approximation de la série de Fourier
def fourier_series_approximation(g_t, n_harmonics):
    N = len(g_t)  # Nombre total d'échantillons
    G = fft(g_t)  # Calcul de la transformée de Fourier discrète
    G_approx = np.zeros(N, dtype=complex)  # Initialisation des coefficients de Fourier approchés

    # Conserver les n premières harmoniques (partie positive et négative)
    G_approx[:n_harmonics] = G[:n_harmonics]  # Premières n_harmonics harmoniques positives
    G_approx[-n_harmonics + 1:] = G[-n_harmonics + 1:]  # Premières n_harmonics harmoniques négatives

    # Retour à l'espace temporel en utilisant la transformée de Fourier inverse
    g_approx_t = ifft(G_approx)

    return np.real(g_approx_t)  # Retourne la partie réelle du signal approché


# Approximation avec n=5, 10 et 200 harmoniques
g_approx_5 = fourier_series_approximation(g_t, 5)
g_approx_10 = fourier_series_approximation(g_t, 10)
g_approx_200 = fourier_series_approximation(g_t, 200)

# Tracé des résultats
plt.figure(figsize=(14, 8))

# Tracé de la fonction originale
plt.subplot(2, 2, 1)
plt.plot(t, g_t, label='Original')
plt.title('Original function g(t)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()

# Tracé de l'approximation avec n=5 harmoniques
plt.subplot(2, 2, 2)
plt.plot(t, g_approx_5, label='Approximation n=5', color='orange')
plt.title('Fourier Approximation with n=5')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()

# Tracé de l'approximation avec n=10 harmoniques
plt.subplot(2, 2, 3)
plt.plot(t, g_approx_10, label='Approximation n=10', color='green')
plt.title('Fourier Approximation with n=10')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()

# Tracé de l'approximation avec n=200 harmoniques
plt.subplot(2, 2, 4)
plt.plot(t, g_approx_200, label='Approximation n=200', color='red')
plt.title('Fourier Approximation with n=200')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()

# Ajustement de la mise en page des sous-graphiques
plt.tight_layout()
plt.show()
