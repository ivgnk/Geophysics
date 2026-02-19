"""
5. Моделирование диффузии в пористой среде
Задача: решить уравнение диффузии в комплексной плоскости (аналитическое решение).
"""

import numpy as np
import matplotlib.pyplot as plt

def diffusion_complex(x, t, D=1):
    """
    Аналитическое решение уравнения диффузии через комплексную функцию.
    x — координата
    t — время
    D — коэффициент диффузии
    """
    if t == 0:
        return np.zeros_like(x)
    return np.exp(-x**2 / (4 * D * t)) / np.sqrt(4 * np.pi * D * t)

x = np.linspace(-5, 5, 200)
t_values = [0.1, 0.5, 1.0, 2.0]

plt.figure(figsize=(10, 6))
for t in t_values:
    u = diffusion_complex(x, t)
    plt.plot(x, u, label=f"t={t}")

plt.title("Диффузия в пористой среде")
plt.xlabel("x"); plt.ylabel("Концентрация")
plt.legend(); plt.grid(True); plt.show()