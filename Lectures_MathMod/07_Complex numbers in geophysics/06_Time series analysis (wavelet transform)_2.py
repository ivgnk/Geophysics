"""
6. Анализ временных рядов (вейвлет‑преобразование) — завершение
Задача: применить комплексный вейвлет (Морле) для анализа геофизического временного ряда —
выявить частотно‑временную структуру сигнала (например, сейсмической активности или климатических колебаний).
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

def morlet_wavelet(t, scale, omega0=5.0):
    """
    Вейвлет Морле (комплексный).
    Параметры:
    - t: массив временных отсчётов (относительно центра вейвлета)
    - scale: масштаб (с)
    - omega0: безразмерный параметр (обычно 5–6)
    Возвращает:
    - массив значений вейвлета (комплексный)
    """
    # Нормализующий множитель
    norm = np.pi ** (-0.25) * np.sqrt(2 / scale)
    # Комплексная экспонента
    exp_term = np.exp(1j * omega0 * t / scale)
    # Гауссова огибающая
    gauss = np.exp(-0.5 * (t / scale) ** 2)
    return norm * exp_term * gauss

# 1. Генерируем временной ряд
t = np.linspace(0, 1, 500, endpoint=False)
signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 10 * t)
dt = t[1] - t[0]

# 2. Параметры вейвлет‑преобразования
scales = np.logspace(np.log10(2 * dt), np.log10(0.5), 50)  # масштабы (с)
omega0 = 5.0  # параметр вейвлета Морле

# 3. Вычисляем CWT вручную
W = np.zeros((len(scales), len(signal)), dtype=complex)

for i, scale in enumerate(scales):
    # Создаём массив временных отсчётов для вейвлета
    t_wavelet = np.arange(-5 * scale, 5 * scale + dt, dt)  # окно ±5 масштабов
    if len(t_wavelet) == 0:
        t_wavelet = np.array([0])

    # Вычисляем вейвлет
    wavelet = morlet_wavelet(t_wavelet, scale, omega0)
    # Нормализуем (чтобы энергия не зависела от масштаба)
    wavelet /= np.sqrt(np.sum(np.abs(wavelet) ** 2))
    # Свёртка с сигналом
    W[i, :] = convolve(signal, wavelet, mode='same', method='auto')

# 4. Мощность вейвлет‑спектра
power = np.abs(W) ** 2

# 5. Визуализация
plt.figure(figsize=(14, 10))

plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Исходный сигнал'); plt.grid(True)
plt.xlabel('Время (с)'); plt.ylabel('Амплитуда')

plt.subplot(2, 1, 2)
plt.contourf(t, scales, power, levels=100, cmap='CMRmap')
plt.yscale('log')
plt.title('Вейвлет‑спектр (ручное CWT)')
plt.xlabel('Время (с)'); plt.ylabel('Масштаб (с)')
plt.colorbar(label='Мощность')
plt.show()
