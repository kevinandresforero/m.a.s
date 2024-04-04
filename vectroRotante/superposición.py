import numpy as np
import matplotlib.pyplot as plt

# Parámetros
A1 = 1  # Amplitud del primer MAS
A2 = 2  # Amplitud del segundo MAS
w1 = 2  # Frecuencia angular del primer MAS
w2 = 3  # Frecuencia angular del segundo MAS
phi1 = 0  # Angulo de desfase del primer MAS
phi2 = np.pi/3  # Angulo de desfase del segundo MAS
t = np.linspace(0, 10, 1000)  # Rango de tiempo

# Cálculo de las funciones
x = A1 * np.sin(w1 * t + phi1) + A2 * np.sin(w2 * t + phi2)
y1 = A1 * np.sin(w1 * t + phi1)
y2 = A2 * np.sin(w2 * t + phi2)

# Figura y ejes
fig, axs = plt.subplots(3, 1, sharex=True)

# Gráfica de la superposición
axs[0].plot(t, x, color='red', label='Superposición')
axs[0].set_ylabel('x')
axs[0].legend()

# Gráfica del primer MAS
axs[1].plot(t, y1, color='blue', label='MAS 1')
axs[1].set_ylabel('y1')
axs[1].legend()

# Gráfica del segundo MAS
axs[2].plot(t, y2, color='green', label='MAS 2')
axs[2].set_xlabel('t (s)')
axs[2].set_ylabel('y2')
axs[2].legend()

# Ajustar espacio entre subplots
plt.subplots_adjust(hspace=0.5)

# Mostrar figura
plt.show()
