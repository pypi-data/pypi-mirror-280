import numpy as np
import matplotlib.pyplot as plt

# Paramètres du signal
f = 80  # Fréquence du signal en Hz
duration = 0.2  # Durée en secondes
fs = 2000  # Fréquence d'échantillonnage (doit être au moins 2 fois la fréquence du signal selon Nyquist-Shannon)

# Générer le vecteur de temps
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

# Générer le signal sinusoïdal
signal = np.sin(2 * np.pi * f * t)

# Ajouter du bruit gaussien
noise = np.random.normal(0, 0.2, signal.shape)
noisy_signal = signal + noise

# Définir la taille de la fenêtre pour le filtre de moyenne mobile
window_size = 20

# Appliquer le filtre de moyenne mobile (convolution)
window = np.ones(window_size) / window_size
filtered_signal = np.convolve(noisy_signal, window, mode='same')

# Tracer les signaux
plt.figure(figsize=(10, 6))
plt.plot(t, noisy_signal, label='Signal avec bruit', color='blue')
plt.plot(t, filtered_signal, label='Signal filtré', color='orange', linestyle='--')
plt.xlabel('Temps [s]')
plt.ylabel('Amplitude')
plt.title('Signal Sinusoïdal avec Bruit et Signal Filtré')
plt.legend()
plt.grid()
plt.show()
