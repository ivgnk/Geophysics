"""
4. Обработка магнитометрических данных (комплексный потенциал)
Задача: вычислить комплексный магнитный потенциал для дипольного источника.
"""

import numpy as np
import matplotlib.pyplot as plt


def magnetic_potential(x, z, m, z0):
    """
    Комплексный магнитный потенциал диполя на глубине z0.

    Параметры:
    - x, z: координаты точки наблюдения (массивы)
    - m: комплексный момент диполя (например, 1 + 0.5j)
    - z0: глубина центра диполя (положительное число)
    Возвращает:
    - комплексный потенциал в точках (x, z)
    """
    r = x + 1j * (z - z0)  # комплексное расстояние
    return m / r


# 1. Настройка сетки
x = np.linspace(-10, 10, 200)
z = np.linspace(0, 15, 150)
X, Z = np.meshgrid(x, z)

# 2. Параметры диполя
m = 1 + 0.5j  # комплексный момент (амплитуда и фаза)
z0 = 5  # глубина диполя (м)

# 3. Вычисляем комплексный потенциал
pot = magnetic_potential(X, Z, m, z0)

# 4. Модуль потенциала (то, что визуализируем)
magnitude = np.abs(pot)

# 5. Визуализация: два подграфика с заполнением и сеткой
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# --- Вариант 1: линейная (равномерная) шкала ---
cax1 = ax1.contourf(X, Z, magnitude, levels=30, cmap='viridis', extend='both')
ax1.set_title('Модуль потенциала |U| (линейная шкала)', fontsize=14)
ax1.set_xlabel('x (м)')
ax1.set_ylabel('z (м)')
ax1.axis('tight')  # заполняет область графика без лишнего пространства
ax1.grid(True, linestyle='--', alpha=0.6, color='white')  # сетка поверх цветовой заливки
ax1.tick_params(axis='both', which='major', labelsize=10)

# Цветная шкала
cbar1 = plt.colorbar(cax1, ax=ax1, pad=0.02)
cbar1.set_label('|U| (отн. ед.)', fontsize=11)
cbar1.ax.tick_params(labelsize=10)

# --- Вариант 2: логарифмическая шкала ---
# Преобразуем magnitude в log10, избегая log(0)
log_magnitude = np.log10(magnitude + 1e-10)  # добавляем малое число для устойчивости

cax2 = ax2.contourf(X, Z, log_magnitude, levels=30, cmap='plasma', extend='both')
ax2.set_title('Модуль потенциала log₁₀(|U|) (логарифмическая шкала)', fontsize=14)
ax2.set_xlabel('x (м)')
ax2.set_ylabel('z (м)')
ax2.axis('tight')  # заполняет область графика без лишнего пространства
ax2.grid(True, linestyle='--', alpha=0.6, color='white')  # сетка поверх цветовой заливки
ax2.tick_params(axis='both', which='major', labelsize=10)

# Цветная шкала
cbar2 = plt.colorbar(cax2, ax=ax2, pad=0.02)
cbar2.set_label('log₁₀(|U|)', fontsize=11)
cbar2.ax.tick_params(labelsize=10)

# Общий заголовок и настройка макета
plt.suptitle('Комплексный магнитный потенциал диполя: сравнение шкал', fontsize=16, y=0.98)
plt.tight_layout(rect=(0, 0, 1, 0.95))  # оставляет место для субтитула
plt.show()
