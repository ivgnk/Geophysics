"""
3. Анализ сейсмической волны (комплексная амплитуда)
Задача: моделировать затухающую сейсмическую волну с комплексной амплитудой.
"""
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2, 400)
omega = 2 * np.pi * 3  # частота 3 Гц
alpha = 0.5  # коэффициент затухания

# Комплексная амплитуда: A(t) = exp(-αt) * exp(iωt)
A = np.exp(-alpha * t) * np.exp(1j * omega * t)

# Реальная часть — наблюдаемая волна
wave = np.real(A)

plt.figure(figsize=(10, 4))
plt.plot(t, wave, label="Реальная часть A(t)")
plt.title("Затухающая сейсмическая волна")
plt.xlabel("Время (с)")
plt.ylabel("Амплитуда")
plt.grid(True); plt.legend(); plt.show()


