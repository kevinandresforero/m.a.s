import numpy as np
import matplotlib.pyplot as plt

A = 3  # Amplitud
w = 2  # Frecuencia angular
t = np.linspace(0, 2*np.pi, 1000)  # Rango de t

x = A * np.cos(w * t)  # Movimiento
d2x_dt2 = -A * w**2 * np.cos(w * t)  # Segunda derivada

plt.plot(d2x_dt2, x)
plt.title('Espacio de Fase $d^2x/dt^2$ vs $x$')
plt.xlabel('$d^2x/dt^2$')
plt.ylabel('$x$')
plt.grid(True)
plt.show()
