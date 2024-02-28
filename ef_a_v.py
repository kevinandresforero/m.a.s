import numpy as np
import matplotlib.pyplot as plt

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
velocidad = parte1 - parte2

# Calcula los componentes de la ecuación
cos_omega_t = np.cos(omega * t)
cos_2omega_t = np.cos(2 * omega * t)
sin_omega_t = np.sin(omega * t)
sin_2omega_t = np.sin(2 * omega * t)
denominador = (L**2 - R**2 * sin_omega_t**2)**0.5

# Primer término de la ecuación
primer_termino = -R * omega**2 * cos_omega_t

# Segundo término de la ecuación
segundo_termino_numerador = R * omega**2 * (4 * omega * cos_2omega_t * (L**2 - R**2 * sin_omega_t**2) + R**2 * omega * sin_2omega_t)
segundo_termino = segundo_termino_numerador / (4 * denominador)

# Combinar los términos para obtener la segunda derivada d^2x/dt^2
aceleracion = primer_termino - segundo_termino

plt.plot(aceleracion, velocidad)
plt.title('Espacio de Fase aceleracion vs velocidad')
plt.xlabel('aceleracion (m/s²)')
plt.ylabel('velocidad (m/s)')
plt.grid(True)
plt.show()
