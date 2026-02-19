"""
4. Обработка магнитометрических данных (комплексный потенциал)
Задача: вычислить комплексный магнитный потенциал для дипольного источника.
"""

import numpy as np

def magnetic_potential(x, z, m, z0):
    """
    Комплексный магнитный потенциал диполя на глубине z0.
    x, z — координаты точки наблюдения
    m — момент диполя (комплексный)
    z0 — глубина диполя
    """
    r = x + 1j * (z - z0)
    return m / r

# Сеть точек
x = np.linspace(-5, 5, 100)
z = np.linspace(0, 10, 100)
X, Z = np.meshgrid(x, z)

# Диполь на глубине 3 м, момент m = 1+0.5j
m = 1 + 0.5j
z0 = 3

# Вычисляем потенциал
pot = magnetic_potential(X, Z, m, z0)

# Визуализируем модуль потенциала
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
plt.contourf(X, Z, np.abs(pot), levels=20, cmap="viridis")
plt.colorbar(label="|Потенциал|")
plt.title("Модуль комплексного магнитного потенциала")
plt.xlabel("x (м)"); plt.ylabel("z (м)")
plt.grid(True); plt.show()
