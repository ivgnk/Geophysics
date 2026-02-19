"""
7. Комплексная интерпретация геофизических данных (интегрированный индекс)
Задача: объединить несколько геофизических полей
(гравитационное, магнитное, сейсмическое) в единый комплексный показатель для выявления аномалий.
"""

import numpy as np
import matplotlib.pyplot as plt

# 1. Моделируем три геофизических поля на сетке 50×50
np.random.seed(42)
N = 50
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)
X, Y = np.meshgrid(x, y)

# Гравитационное поле (аномалия в центре)
grav = -1 / np.sqrt(X**2 + Y**2 + 1) + 0.1 * np.random.randn(N, N)

# Магнитное поле (линейная аномалия)
mag = X + 0.05 * np.random.randn(N, N)

# Сейсмическая скорость (кольцевая структура)
vel = np.exp(-(X**2 + Y**2)) * np.cos(5 * np.sqrt(X**2 + Y**2)) + 0.05 * np.random.randn(N, N)

# 2. Нормируем поля на [0, 1]
def normalize(arr):
    return (arr - arr.min()) / (arr.max() - arr.min() + 1e-10)

grav_n = normalize(grav)
mag_n = normalize(mag)
vel_n = normalize(vel)

# 3. Строим комплексный индекс:
# - каждое поле — действительная или мнимая часть
# - комбинация: Z = grav + i*mag + (1+i)*vel
Z = grav_n + 1j * mag_n + (1 + 1j) * vel_n

# 4. Вычисляем характеристики комплексного индекса
magnitude = np.abs(Z)      # суммарная «сила» аномалии
phase = np.angle(Z)        # фазовый контраст (тип аномалии)
real_part = np.real(Z)    # вклад гравитации и скорости
imag_part = np.imag(Z)    # вклад магнетизма и скорости

# 5. Визуализация
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
plt.suptitle("Комплексная интерпретация геофизических данных", fontsize=16)

axes[0, 0].contourf(X, Y, grav_n, cmap='viridis')
axes[0, 0].set_title("Грав.поле (нормированное)")

axes[0, 1].contourf(X, Y, mag_n, cmap='plasma')
axes[0, 1].set_title("Магн.поле (нормированное)")

axes[0, 2].contourf(X, Y, vel_n, cmap='cividis')
axes[0, 2].set_title("Скорость (нормированная)")

axes[1, 0].contourf(X, Y, magnitude, cmap='Reds')
axes[1, 0].set_title("Модуль |Z| (сила аномалии)")

axes[1, 1].contourf(X, Y, phase, cmap='twilight')
axes[1, 1].set_title("Фаза arg(Z) (тип аномалии)")

axes[1, 2].contourf(X, Y, real_part, cmap='Greens', alpha=0.7)
axes[1, 2].contour(X, Y, imag_part, colors='orange', linewidths=1)
axes[1, 2].set_title("Re(Z) и Im(Z)")

for ax in axes.flat:
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

plt.show()
