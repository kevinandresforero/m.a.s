import numpy as np
import matplotlib.pyplot as plt

# Parámetros
A = 190  # Amplitud
w = 100  # Frecuencia angular
t = np.linspace(0, 2 * np.pi, 1000)  # Rango de t

# Funciones
x = A * np.cos(w * t)
dx_dt = -A * w * np.sin(w * t)
d2x_dt2 = -A * w**2 * np.cos(w * t)

plt.figure(figsize=(14, 4.5))

plt.subplot(1, 3, 1)
plt.plot(dx_dt, x)
plt.title('Espacio de Fase dx/dt vs. x')
plt.xlabel('dx_dt (m/s)')
plt.ylabel('x (m)')
plt.grid(True)


plt.subplot(1, 3, 2)
plt.plot(d2x_dt2, x)
plt.title('Espacio de Fase d²x/dt² vs. x')
plt.xlabel('d²x/dt² (m/s²)')
plt.ylabel('x (m)')
plt.grid(True)

plt.subplot(1, 3, 3)
plt.plot(d2x_dt2, dx_dt)
plt.title('Espacio de Fase d²x/dt² vs. dx/dt')
plt.xlabel('d²x/dt² (m/s²)')
plt.ylabel('dx/dt (m/s)')
plt.grid(True)

plt.tight_layout()
plt.show()
