import numpy as np
from scipy.signal import convolve
import math

# Parámetros en decibeles
db1 = 100
db2 = 100
w1 = 4  # Frecuencia angular del primer MAS
w2 = 4  # Frecuencia angular del segundo MAS
phi1 = 0  # Angulo de desfase del primer MAS
phi2 = 0  # Angulo de desfase del segundo MAS
t = np.linspace(0, 10, 1000)  # Rango de tiempo

import numpy as np

def get_amplitude_and_frequency(signal):
    """
    Calcula la amplitud y la frecuencia dominante de una señal de ruido.

    Args:
        signal (np.ndarray): Señal de ruido (array de NumPy).
        sampling_rate (float): Tasa de muestreo de la señal.

    Returns:
        tuple: Amplitud y frecuencia dominante de la señal.
    """

    sampling_rate = 1000

    # Calcula la transformada de Fourier de la señal
    fourier_transform = np.fft.fft(signal)
    
    # Obtiene las frecuencias correspondientes a los coeficientes de Fourier
    frequencies = np.fft.fftfreq(len(signal), 1 / sampling_rate)
    
    # Calcula la amplitud de cada componente de frecuencia
    amplitudes = np.abs(fourier_transform)
    
    # Encuentra el índice de la componente de frecuencia con la máxima amplitud
    max_amplitude_idx = np.argmax(amplitudes)
    
    # Obtiene la amplitud y la frecuencia dominante
    amplitude = amplitudes[max_amplitude_idx]
    frequency = np.abs(frequencies[max_amplitude_idx])
    
    return amplitude, frequency

def db_to_amp(db):
    """
    Convierte un valor en decibeles a amplitud.
    
    Args:
        db (float): Valor en decibeles.
    
    Returns:
        float: Amplitud correspondiente.
    """
    amp = 10 ** (db / 20)
    return amp

def amp_to_db(amp):
    """
    Convierte un valor de amplitud a decibeles.
    
    Args:
        amp (float): Valor de amplitud.
    
    Returns:
        float: Valor en decibeles correspondiente.
    """
    if amp == 0:
        return -math.inf
    else:
        db = 20 * math.log10(amp)
        return db

# Parámetros
A1 = db_to_amp(db1) # Amplitud del primer MAS
A2 = db_to_amp(db2)  # Amplitud del segundo MAS
print("amplitudes: ", A1, A2)


# Cálculo de las funciones
y1 = A1 * np.sin(w1 * t + phi1)
y2 = A2 * np.sin(w2 * t + phi2)
Am = A1 + A2 
Ws =  np.sin(w1 * t + phi1) + np.sin(w2 * t + phi2)
x = y1 + y2


# Obener frrecuancia y amplitude de la superposición
amplitude, frequency = get_amplitude_and_frequency(x)
print("DB: ", amp_to_db(amplitude),"\nFrecuencia: ",frequency)

#   script para graficar
'''
import matplotlib.pyplot as plt
# Figura y ejes
fig, axs = plt.subplots(3, 1, sharex=True, figsize=(8, 6))

# Gráfica de la superposición
axs[0].plot(t, x, color='red', label='Superposición con ruido')
axs[0].set_ylabel('x')
axs[0].legend()

# Gráfica del primer MAS
axs[1].plot(t, y1, color='blue', label='MAS 1 con ruido')
axs[1].set_ylabel('y1')
axs[1].legend()

# Gráfica del segundo MAS
axs[2].plot(t, y2, color='green', label='MAS 2 con ruido')
axs[2].set_xlabel('t (s)')
axs[2].set_ylabel('y2')
axs[2].legend()

# Ajustar espacio entre subplots
plt.subplots_adjust(hspace=0.5)

# Mostrar figura
plt.show()
'''
