import numpy as np

# Define las constantes
r = 1.0  # Ajusta según sea necesario
L = 2.0  # Ajusta según sea necesario
R = 1.0  # Ajusta según sea necesario
omega = 2 * np.pi  # Ejemplo: Frecuencia angular

# Crea un array de valores de tiempo t
t = np.linspace(0, 10, 1000)  # Desde 0 hasta 10 segundos

# Calcula los componentes de la ecuación
cos_omega_t = np.cos(omega * t)
cos_2omega_t = np.cos(2 * omega * t)
sin_omega_t = np.sin(omega * t)
sin_2omega_t = np.sin(2 * omega * t)
denominador = (L**2 - R**2 * sin_omega_t**2)**0.5

# Primer término de la ecuación
primer_termino = -r * omega**2 * cos_omega_t

# Segundo término de la ecuación
segundo_termino_numerador = r * omega**2 * (4 * omega * cos_2omega_t * (L**2 - R**2 * sin_omega_t**2) + r**2 * omega * sin_2omega_t)
segundo_termino = segundo_termino_numerador / (4 * denominador)

# Combinar los términos para obtener la segunda derivada d^2x/dt^2
d2x_dt2 = primer_termino - segundo_termino

import matplotlib.pyplot as plt

# Crea una figura y un eje para la gráfica
fig, ax = plt.subplots()

# Grafica d2x/dt2 vs. tiempo t
ax.plot(t, d2x_dt2, label=r'$\frac{d^2x}{dt^2}$')

# Añade un título y etiquetas a los ejes
ax.set_title('Aceleración')
ax.set_xlabel('Tiempo (s)')
ax.set_ylabel(r'Aceleración (m/s²)')

# Añade una leyenda
ax.legend()

# Muestra la gráfica
plt.show()