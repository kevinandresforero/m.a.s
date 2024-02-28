import numpy as np
import matplotlib.pyplot as plt

# R# Define las constantes
R = 1.0  # Por ejemplo, 1 metro
L = 2.0  # Por ejemplo, 2 metros
omega = 2 * np.pi  # Frecuencia angular, por ejemplo 2*pi para 1 ciclo/seg

# Crea un array de valores de tiempo t desde 0 hasta 10 segundos con 1000 puntos
t = np.linspace(0, 10, 1000)

# Calcula la ecuación
posicion = R * np.cos(omega * t) + np.sqrt(L**2 - R**2 * np.sin(omega * t)**2)

# Calcula la ecuación
parte1 = -R * omega * np.sin(omega * t)
parte2 = (R**2 * omega * np.sin(2 * omega * t)) / (2 * np.sqrt(L**2 - R**2 * np.sin(omega * t)**2))

# Calcula la ecuación completa
velocidad = parte1 - parte2

plt.plot(velocidad, posicion)
plt.title('Espacio de Fase Velocidad vs Posición')
plt.xlabel('Velocidad (m/s)')
plt.ylabel('x (m)')
plt.grid(True)
plt.show()
