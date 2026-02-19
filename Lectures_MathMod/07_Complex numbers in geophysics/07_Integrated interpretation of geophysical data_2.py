"""
7. Комплексная интерпретация геофизических данных (интегрированный индекс)
Задача: объединить несколько геофизических полей
(гравитационное, магнитное, сейсмическое) в единый комплексный показатель для выявления аномалий.
"""

import numpy as np
import matplotlib.pyplot as plt

# 1. Исходные данные (пример)
np.random.seed(42)  # для воспроизводимости результатов
A = np.random.randn(50, 50) * 100  # магнитное поле, нТл
B = np.random.randn(50, 50) * 50   # гравитационное поле, мГал
C = np.random.randn(50, 50) * 20   # сопротивление, Ом·м

# 2. Нормировка
A_norm = (A - np.mean(A)) / np.std(A)
B_norm = (B - np.mean(B)) / np.std(B)
C_norm = (C - np.mean(C)) / np.std(C)

# 3. Комплексный индекс
Z = A_norm + 1j * B_norm

Z_abs = np.abs(Z)  # модуль
phi = np.angle(Z)   # фаза в радианах

# 4. Взвешивание
alpha = 0.3
weight = 1 + alpha * np.abs(C_norm)
Z_weighted = Z_abs * weight

# 5. Визуализация — улучшенная версия с заполнением всей площади
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Комплексная интерпретация геофизических данных: интегральный индекс',
           fontsize=16, fontweight='bold', y=0.95)

# Настройка отображения без отступов
plt.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.05,
                wspace=0.15, hspace=0.2)

# Карта 1: Модуль |Z|
im1 = axes[0, 0].imshow(Z_abs, cmap='jet', aspect='auto', interpolation='bilinear')
axes[0, 0].set_title('|Z| (модуль интегрального индекса)', fontsize=12, pad=10)
axes[0, 0].axis('off')  # Убираем оси для полного заполнения

# Добавление цветовой шкалы с правильной привязкой
cbar1 = plt.colorbar(im1, ax=axes[0, 0], orientation='vertical', shrink=0.8, pad=0.02)
cbar1.set_label('Амплитуда', fontsize=10)

# Карта 2: Фаза φ
im2 = axes[0, 1].imshow(phi, cmap='hsv', aspect='auto', interpolation='bilinear',
              vmin=-np.pi, vmax=np.pi)
axes[0, 1].set_title('φ (фаза интегрального индекса)', fontsize=12, pad=10)
axes[0, 1].axis('off')

cbar2 = plt.colorbar(im2, ax=axes[0, 1], orientation='vertical', shrink=0.8, pad=0.02,
              ticks=[-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
cbar2.set_label('Фаза, рад', fontsize=10)
cbar2.set_ticklabels(['-π', '-π/2', '0', 'π/2', 'π'])

# Карта 3: Нормированное сопротивление C
im3 = axes[1, 0].imshow(C_norm, cmap='terrain', aspect='auto', interpolation='bilinear')
axes[1, 0].set_title('C_норм (сопротивление)', fontsize=12, pad=10)
axes[1, 0].axis('off')

cbar3 = plt.colorbar(im3, ax=axes[1, 0], orientation='vertical', shrink=0.8, pad=0.02)
cbar3.set_label('Норм. сопротивление', fontsize=10)

# Карта 4: Взвешенный индекс Z_взв
im4 = axes[1, 1].imshow(Z_weighted, cmap='hot', aspect='auto', interpolation='bilinear')
axes[1, 1].set_title('Z_взв (взвешенный интегральный индекс)', fontsize=12, pad=10)
axes[1, 1].axis('off')

cbar4 = plt.colorbar(im4, ax=axes[1, 1], orientation='vertical', shrink=0.8, pad=0.02)
cbar4.set_label('Взвешенный индекс', fontsize=10)

# Дополнительная настройка для максимального заполнения
for ax in axes.flat:
    ax.set_aspect('auto')
    ax.autoscale(enable=True, axis='both', tight=True)

plt.tight_layout()
plt.show()
