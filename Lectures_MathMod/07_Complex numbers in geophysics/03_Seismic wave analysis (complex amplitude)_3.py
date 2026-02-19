"""
3. Анализ сейсмической волны (комплексная амплитуда)
Задача: моделировать затухающую сейсмическую волну с комплексной амплитудой.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert

# Параметры модели
t = np.linspace(0, 2, 400)
omega = 2 * np.pi * 3  # частота 3 Гц
alpha = 0.5  # коэффициент затухания

# Комплексная амплитуда
A_complex = np.exp(-alpha * t) * np.exp(1j * omega * t)

# Реальная часть — наблюдаемая волна
wave_real = np.real(A_complex)
wave_imag = np.imag(A_complex)

# Аналитический сигнал через преобразование Гильберта
analytic_signal = hilbert(wave_real)
instantaneous_amplitude = np.abs(analytic_signal)
instantaneous_phase = np.unwrap(np.angle(analytic_signal))  # развёрнутая фаза
instantaneous_frequency = np.diff(instantaneous_phase) / (2 * np.pi) / (t[1] - t[0])

# Визуализация
plt.figure(figsize=(12, 8))

plt.subplot(4, 1, 1)
plt.plot(t, wave_real, label="Реальная часть A(t)", linestyle='-')
plt.plot(t, wave_imag, label="Мнимая часть A(t)", linestyle='--')
plt.title("Исходный сейсмический сигнал")
plt.legend(); plt.ylabel("Амплитуда"); plt.grid(True)

plt.subplot(4, 1, 2)
plt.plot(t, instantaneous_amplitude, 'r', label="Мгновенная амплитуда (огибающая)")
plt.title("Мгновенная амплитуда"); plt.ylabel("A(t)"); plt.grid(True)

plt.subplot(4, 1, 3)
plt.plot(t, instantaneous_phase, 'g', label="Мгновенная фаза")
plt.title("Мгновенная фаза"); plt.ylabel("φ(t)"); plt.grid(True)

plt.subplot(4, 1, 4)
plt.plot(t[1:], instantaneous_frequency, 'm', label="Мгновенная частота")
plt.title("Мгновенная частота"); plt.xlabel("Время (с)"); plt.ylabel("f(t), Гц"); plt.grid(True)

plt.tight_layout(); plt.show()