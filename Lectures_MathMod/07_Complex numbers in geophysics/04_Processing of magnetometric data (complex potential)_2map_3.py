"""
4. Обработка магнитометрических данных (комплексный потенциал)
Задача: вычислить комплексный магнитный потенциал для дипольного источника.
"""

import numpy as np
import matplotlib.pyplot as plt

def magnetic_potential(x, z, m, z0, mu0=4e-7 * np.pi):
    """
    Комплексный магнитный потенциал диполя на глубине z0 (в СИ).
    Параметры:
    - x, z: координаты (м)
    - m: магнитный момент диполя (А·м²)
    - z0: глубина центра диполя (м, положительное число)
    - mu0: магнитная постоянная (Гн/м), по умолчанию 4π×10⁻⁷

    Возвращает:
    - комплексный потенциал U в точках (x, z) (размерность: А)
    """
    r = x + 1j * (z - z0)  # комплексное расстояние (м)
    return m / (4 * np.pi * r)  # U в амперах (А)

# 1. Настройка сетки (ось Z направлена вниз: от 0 до 15 м)
x = np.linspace(-10, 10, 200)  # горизонталь, м
z = np.linspace(0, 15, 150)  # глубина, м (0 = поверхность, 15 = глубина)
X, Z = np.meshgrid(x, z)

# 2. Параметры диполя (физические единицы)
m = 1e4 + 0.5e4j  # магнитный момент: 10000 + 5000j А·м²
z0 = 5.0  # глубина диполя: 5 м
mu0 = 4e-7 * np.pi  # магнитная постоянная, Гн/м

# 3. Вычисляем комплексный потенциал (результат в А)
pot = magnetic_potential(X, Z, m, z0, mu0)
magnitude = np.abs(pot)  # модуль потенциала, А

# 4. Визуализация: два подграфика с осью Z вниз и сеткой
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# --- Вариант 1: линейная шкала ---
cax1 = ax1.contourf(X, Z, magnitude, levels=30, cmap='viridis', extend='both')
ax1.set_title('|U| (А), линейная шкала', fontsize=14)
ax1.set_xlabel('x (м)')
ax1.set_ylabel('Глубина z (м)')  # явно указываем, что Z — глубина
ax1.invert_yaxis()  # инвертируем ось Y: 0 наверху, 15 внизу
ax1.axis('tight')
ax1.grid(True, linestyle='--', alpha=0.6, color='white')
ax1.tick_params(axis='both', which='major', labelsize=10)

# Цветная шкала
cbar1 = plt.colorbar(cax1, ax=ax1, pad=0.02)
cbar1.set_label('|U| (А)', fontsize=11)
cbar1.ax.tick_params(labelsize=10)

# --- Вариант 2: логарифмическая шкала ---
log_magnitude = np.log10(magnitude + 1e-10)  # log₁₀(|U| + ε), А

cax2 = ax2.contourf(X, Z, log_magnitude, levels=30, cmap='plasma', extend='both')
ax2.set_title('log₁₀(|U|) (log А), логарифмическая шкала', fontsize=14)
ax2.set_xlabel('x (м)')
ax2.set_ylabel('Глубина z (м)')
ax2.invert_yaxis()  # ось Z вниз
ax2.axis('tight')
ax2.grid(True, linestyle='--', alpha=0.6, color='white')
ax2.tick_params(axis='both', which='major', labelsize=10)

# Цветная шкала
cbar2 = plt.colorbar(cax2, ax=ax2, pad=0.02)
cbar2.set_label('log₁₀(|U|) (log А)', fontsize=11)
cbar2.ax.tick_params(labelsize=10)

# Общий заголовок и макет
plt.suptitle('Комплексный магнитный потенциал диполя: |U| в амперах (А)\n'
             'Ось Z направлена вниз (глубина)', fontsize=16, y=0.98)
plt.tight_layout(rect=(0, 0, 1, 0.95)); plt.show()