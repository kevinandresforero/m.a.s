import numpy as np
import matplotlib.pyplot as plt

A = 3  # Amplitud
w = 2  # Frecuencia angular
t = np.linspace(0, 2*np.pi, 1000)  # Rango de t

x = A * np.cos(w * t)
dx_dt = -A * w * np.sin(w * t)

plt.plot(dx_dt ,x)
plt.title('Espacio de Fase dx/dt vs x')
plt.xlabel('dx/dt')
plt.ylabel('x')
plt.grid(True)
plt.show()
