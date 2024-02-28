import numpy as np
import matplotlib.pyplot as plt

# Parámetros
A = 3  # Amplitud
w = 2  # Frecuencia angular

# Rango de t
t = np.linspace(0, 2*np.pi, 100)  # De 0 a 2π con 100 puntos

# Definición de la función
y = A * np.cos(w * t)

import matplotlib.pyplot as plt

# Graficar
plt.plot(t, y)
plt.title('Función A*cos(wt)')
plt.xlabel('t (s)')
plt.ylabel('x (m)')
plt.grid(True)
plt.show()

