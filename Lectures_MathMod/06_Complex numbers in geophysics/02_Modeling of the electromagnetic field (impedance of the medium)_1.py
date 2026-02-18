"""
2. Моделирование электромагнитного поля (импеданс среды)
Задача: вычислить комплексный импеданс Z=R+iX для слоистой среды в магнитотеллурике
"""
import numpy as np

def complex_impedance(resistivity, frequency, mu=4e-7 * np.pi):
    """
    Комплексный импеданс для однородной среды.
    resistivity — удельное сопротивление (Ом·м)
    frequency — частота (Гц)
    mu — магнитная проницаемость (Гн/м)
    """
    omega = 2 * np.pi * frequency
    Z = np.sqrt(1j * omega * mu / resistivity)
    return Z

# Пример для разных частот
frequencies = [0.01, 0.1, 1, 10]  # Гц
resistivity = 100  # Ом·м

for f in frequencies:
    Z = complex_impedance(resistivity, f)
    print(f"f={f} Гц: Z={Z:.4f} (|Z|={np.abs(Z):.4f}, фаза={np.angle(Z)*180/np.pi:.2f}°)")

