import numpy as np
import matplotlib.pyplot as plt

# Parámetros de los péndulos
A1 = 2  # Amplitud del péndulo 1
A2 = 3  # Amplitud del péndulo 2
w1 = 3  # Frecuencia angular del péndulo 1
w2 = 4  # Frecuencia angular del péndulo 2
phi1 = 0  # Fase del péndulo 1
phi2 = np.pi/2  # Fase del péndulo 2

# Rango de tiempo
t = np.linspace(0, x|10*np.pi, 1000)

# Cálculo de las posiciones
x = A1 * np.sin(w1 * t + phi1)
y = A2 * np.sin(w2 * t + phi2)

# Figura y subplots
fig, axs = plt.subplots(2, 2, sharex=True, sharey=False)

# Subplot 1: Onda 1 - Circunferencia - x
theta_x = w1 * t + phi1
x_c1 = A1 * np.cos(theta_x)
y_c1 = A1 * np.sin(theta_x)
axs[1, 1].add_artist(plt.Circle((0, 0), A1, fill=False))
axs[1, 1].plot(x_c1, y_c1, 'o-', color='red')
axs[1, 1].set_xlabel('t')
axs[1, 1].set_ylabel('x = A1 * sen(wt)')

# Subplot 2: Figura de Lissajous
axs[0, 1].plot(x, y)
axs[0, 1].set_xlabel('t')
axs[0, 1].set_ylabel('y')

# Subplot 3: Onda 2 - Circunferencia - y
axs[0, 0].add_artist(plt.Circle((0, 0), A2, fill=False))
x_c2 = A2 * np.cos(w2 * t + phi2)
y_c2 = A2 * np.sin(w2 * t + phi2)
axs[0, 0].plot(x_c2, y_c2, 'o-', color='blue')
axs[0, 0].set_ylabel('y = A2 * sen(wt + π/2)')

# Ajustar espacio entre subplots
plt.subplots_adjust(hspace=0.5, wspace=0.5)

# Mostrar figura
plt.show()
