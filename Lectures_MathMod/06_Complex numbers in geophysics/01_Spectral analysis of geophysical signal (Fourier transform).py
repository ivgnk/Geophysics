"""
1. Спектральный анализ геофизического сигнала (преобразование Фурье)
Задача: разложить временной сигнал (например, сейсмограмму)
на гармонические составляющие с амплитудами и фазами.
"""

import numpy as np
import matplotlib.pyplot as plt

# Модель сейсмического сигнала: сумма двух синусоид + шум
t = np.linspace(0, 2, 512, endpoint=False)
signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 12 * t) + 0.2 * np.random.randn(len(t))

# Преобразование Фурье: получаем комплексный спектр
fft_result = np.fft.fft(signal)
freqs = np.fft.fftfreq(len(t), d=t[1] - t[0])

# Вычисление амплитуды и фазы
amplitudes = np.abs(fft_result)
phases = np.angle(fft_result)

# Визуализация
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(freqs[:len(freqs)//2], amplitudes[:len(amplitudes)//2])
plt.title("Амплитудный спектр")
plt.xlabel("Частота (Гц)"); plt.ylabel("Амплитуда")
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(freqs[:len(freqs)//2], phases[:len(phases)//2])
plt.title("Фазовый спектр");
plt.xlabel("Частота (Гц)"); plt.ylabel("Фаза (рад)")
plt.grid(); plt.show()
