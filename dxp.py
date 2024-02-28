import numpy as np

# R# Define las constantes
R = 1.0  # Por ejemplo, 1 metro
L = 2.0  # Por ejemplo, 2 metros
omega = 2 * np.pi  # Frecuencia angular, por ejemplo 2*pi para 1 ciclo/seg

# Crea un array de valores de tiempo t desde 0 hasta 10 segundos con 1000 puntos
t = np.linspace(0, 10, 1000)

# Calcula la ecuación
parte1 = -R * omega * np.sin(omega * t)
parte2 = (R**2 * omega * np.sin(2 * omega * t)) / (2 * np.sqrt(L**2 - R**2 * np.sin(omega * t)**2))

# Calcula la ecuación completa
resultado = parte1 - parte2


import matplotlib.pyplot as plt

# Usando el mismo código de cálculo que antes

# Ahora, grafica el resultado
plt.plot(t, resultado)
plt.xlabel('Tiempo (s)')
plt.ylabel('velocidad (m/s)')
plt.title('Gráfico de la velocidad con respecto al tiempo')
plt.grid(True)
plt.show()
