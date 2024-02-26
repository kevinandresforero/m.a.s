import numpy as np
import matplotlib.pyplot as plt

A = 3  # Amplitud
w = 2  # Frecuencia angular
t = np.linspace(0, 2*np.pi, 1000)  # Rango de t

dx_dt = -A * w * np.sin(w * t)  # Primera derivada
d2x_dt2 = -A * w**2 * np.cos(w * t)  # Segunda derivada

plt.plot(d2x_dt2, dx_dt)
plt.title('Espacio de Fase $d^2x/dt^2$ vs $dx/dt$')
plt.xlabel('$d^2x/dt^2$')
plt.ylabel('$dx/dt$')
plt.grid(True)
plt.show()
