import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Définition de la fonction f(t)
def f(t):
    return np.sin(2 * np.pi * 10 * t) + np.cos(2 * np.pi * 10 * t) + 10 * np.sin(2 * np.pi * 2 * t)

# Paramètres d'échantillonnage
fs = 300  # Fréquence d'échantillonnage en Hz
duration = 1.0  # Durée en secondes
t = np.arange(0, duration, 1/fs)  # Vecteur temps basé sur la fréquence d'échantillonnage

# Échantillonnage de la fonction
f_t = f(t)  # Calcul des valeurs de f(t) aux instants d'échantillonnage

# Zero padding: ajout de zéros pour augmenter la résolution en fréquence
N = len(f_t)
N_padded = 2**int(np.ceil(np.log2(N)))  # Prochain nombre de points de la FFT qui est une puissance de 2
f_t_padded = np.pad(f_t, (0, N_padded - N), 'constant')  # Padding avec des zéros

# Calcul de la transformée de Fourier sans zero padding
F = fft(f_t)
F_magnitude = np.abs(F) / N  # Magnitude de la FFT

# Fréquences correspondantes
freqs = fftfreq(N, 1/fs)

# Calcul de la transformée de Fourier avec zero padding
F_padded = fft(f_t_padded)
F_padded_magnitude = np.abs(F_padded) / N_padded  # Magnitude de la FFT avec padding

# Fréquences correspondantes pour le signal paddé
freqs_padded = fftfreq(N_padded, 1/fs)

# Tracé du signal original
plt.figure(figsize=(18, 8))

plt.subplot(3, 1, 1)
plt.plot(t, f_t)
plt.title('Signal original f(t)')
plt.xlabel('Temps [s]')
plt.ylabel('Amplitude')

# Tracé du spectre de magnitude sans zero padding
plt.subplot(3, 1, 2)
plt.plot(freqs[:N//2], F_magnitude[:N//2])  # Seule la moitié positive est pertinente
plt.title('Spectre de Magnitude du Signal (sans zero padding)')
plt.xlabel('Fréquence (Hz)')
plt.ylabel('Magnitude')

# Tracé du spectre de magnitude avec zero padding
plt.subplot(3, 1, 3)
plt.plot(freqs_padded[:N_padded//2], F_padded_magnitude[:N_padded//2])  # Seule la moitié positive est pertinente
plt.title('Spectre de Magnitude du Signal (avec zero padding)')
plt.xlabel('Fréquence (Hz)')
plt.ylabel('Magnitude')

plt.tight_layout()
plt.show()

# Identification des composantes fréquentielles
# On peut simplement regarder les pics dans le spectre de magnitude pour identifier les fréquences principales
peak_threshold = 0.1  # Seuil pour détecter les pics significatifs
peaks = freqs[np.where(F_magnitude > peak_threshold)]
peaks_padded = freqs_padded[np.where(F_padded_magnitude > peak_threshold)]
print("Composantes fréquentielles principales (sans zero padding) : ", peaks[peaks >= 0])
print("Composantes fréquentielles principales (avec zero padding) : ", peaks_padded[peaks_padded >= 0])
