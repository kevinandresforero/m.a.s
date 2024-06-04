import numpy as np
import matplotlib.pyplot as plt

# Parámetros de los péndulos
A1 = 1  # Amplitud del primer MAS
A2 = 1  # Amplitud del segundo MAS
w1 = 1  # Frecuencia angular del primer MAS
w2 = 3  # Frecuencia angular del segundo MAS
phi1 = 0  # Angulo de desfase del primer MAS
phi2 = np.pi/2 #np.pi/3  # Angulo de desfase del segundo MAS

# Rango de tiempo
t = np.linspace(0, 10*np.pi, 1000)

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
axs[1, 1].plot(x_c1, y_c1, 'o-', color='blue')
axs[1, 1].set_xlabel('x1')
axs[1, 1].set_ylabel('y1 = A1 * sen(w1t + phi1)')

# Subplot 2: Figura de Lissajous
axs[0, 1].plot(x, y, color='red')
axs[0, 1].set_xlabel('x')
axs[0, 1].set_ylabel('y')

# Subplot 3: Onda 2 - Circunferencia - y
axs[0, 0].add_artist(plt.Circle((0, 0), A2, fill=False))
x_c2 = A2 * np.cos(w2 * t + phi2)
y_c2 = A2 * np.sin(w2 * t + phi2)
axs[0, 0].set_xlabel('x2')
axs[0, 0].plot(x_c2, y_c2, 'o-', color='green')
axs[0, 0].set_ylabel('y2 = A2 * sen(w2t + phi2)')

# Ajustar espacio entre subplots
plt.subplots_adjust(hspace=0.5, wspace=0.5)

# Mostrar figura
plt.show()
