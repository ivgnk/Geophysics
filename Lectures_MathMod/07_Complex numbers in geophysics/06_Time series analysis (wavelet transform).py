"""
6. Анализ временных рядов (вейвлет‑преобразование) — завершение
Задача: применить комплексный вейвлет (Морле) для анализа геофизического временного ряда —
выявить частотно‑временную структуру сигнала (например, сейсмической активности или климатических колебаний).
"""
import numpy as np
import matplotlib.pyplot as plt
import pycwt as cwt

# 1. Генерируем сигнал
t = np.linspace(0, 1, 500, endpoint=False)
signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 10 * t)
dt = float(t[1] - t[0]) # шаг по времени для сигнала

# 2. Параметры вейвлет‑преобразования
dj = 0.125      # шаг по масштабу (логарифмический)
s0 = 2 * dt     # начальный масштаб (в секундах)
J = 50          # число масштабов
wavelet = 'morlet'  # тип вейвлета

# 3. Вычисляем CWT
W, scales, freqs, coi, _, _ = cwt.cwt(
    signal, dt, dj, s0, J, wavelet=wavelet
)
# 4. Мощность (модуль в квадрате)
power = np.abs(W)**2

# 5. Визуализация
plt.figure(figsize=(14, 10))
plt.subplot(2, 1, 1)
plt.plot(t, signal); plt.grid()
plt.title('Исходный сигнал')
plt.xlabel('Время (с)'); plt.ylabel('Амплитуда')

plt.subplot(2, 1, 2)
plt.contourf(t, scales, power, levels=100, cmap='CMRmap')
plt.yscale('log')
plt.title('Вейвлет‑спектр (pycwt)')
plt.xlabel('Время (с)'); plt.ylabel('Масштаб (с)')
plt.colorbar(label='Мощность')
plt.show()
