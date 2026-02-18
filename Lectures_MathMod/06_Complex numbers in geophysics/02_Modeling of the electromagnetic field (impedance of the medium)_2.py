"""
2. Моделирование электромагнитного поля (импеданс среды)
Задача: вычислить комплексный импеданс Z=R+iX для слоистой среды в магнитотеллурике
"""
import numpy as np
import matplotlib.pyplot as plt

def complex_impedance(resistivity, frequency, mu=4e-7 * np.pi):
    """
    Вычисляет комплексный импеданс для однородной среды.

    Параметры:
    - resistivity: удельное сопротивление (Ом·м)
    - frequency: частота (Гц)
    - mu: магнитная проницаемость (Гн/м), по умолчанию — для вакуума

    Возвращает:
    - Z: комплексный импеданс (Ом)
    """
    omega = 2 * np.pi * frequency
    Z = np.sqrt(1j * omega * mu / resistivity)
    return Z

# Параметры расчёта
resistivity_values = [10, 50, 100, 500, 1000]  # Ом·м (разные геологические слои)
frequencies = np.logspace(-3, 4, 500)  # частоты от 0.001 до 10 000 Гц

# Подготовка данных
results = {}
for rho in resistivity_values:
    Z_data = np.array([complex_impedance(rho, f) for f in frequencies])
    results[rho] = {
        'magnitude': np.abs(Z_data),
        'phase_deg': np.angle(Z_data, deg=True),
        'real': np.real(Z_data),
        'imag': np.imag(Z_data)
    }

# Создание визуализации
fig = plt.figure(figsize=(16, 12))
fig.suptitle('Комплексный импеданс геоэлектрической среды\n'
          'Зависимость от частоты и удельного сопротивления', fontsize=16, y=0.95)

# 1. График модуля импеданса |Z| vs частота
ax1 = plt.subplot(2, 3, 1)
for rho, data in results.items():
    ax1.loglog(frequencies, data['magnitude'], label=f'ρ = {rho} Ом·м', linewidth=2)
ax1.set_xlabel('Частота (Гц)', fontsize=12)
ax1.set_ylabel('|Z| (Ом)', fontsize=12)
ax1.set_title('Модуль импеданса', fontsize=14)
ax1.legend(fontsize=10)
ax1.grid(True, which='both', alpha=0.3)
ax1.axhline(y=1, color='k', linestyle='--', alpha=0.5)

# 2. График фазы импеданса vs частота
ax2 = plt.subplot(2, 3, 2)
for rho, data in results.items():
    ax2.semilogx(frequencies, data['phase_deg'], label=f'ρ = {rho} Ом·м', linewidth=2)
ax2.set_xlabel('Частота (Гц)', fontsize=12)
ax2.set_ylabel('Фаза (градусы)', fontsize=12)
ax2.set_title('Фаза импеданса', fontsize=14)
ax2.legend(fontsize=10)
ax2.grid(True, which='both', alpha=0.3)
ax2.axhline(y=45, color='r', linestyle='--', alpha=0.7, label='Теоретическая фаза 45°')
ax2.legend()

# 3. График действительной части vs частота
ax3 = plt.subplot(2, 3, 3)
for rho, data in results.items():
    ax3.loglog(frequencies, data['real'], label=f'ρ = {rho} Ом·м', linewidth=2)
ax3.set_xlabel('Частота (Гц)', fontsize=12)
ax3.set_ylabel('Re(Z) (Ом)', fontsize=12)
ax3.set_title('Действительная часть', fontsize=14)
ax3.legend(fontsize=10)
ax3.grid(True, which='both', alpha=0.3)

# 4. График мнимой части vs частота
ax4 = plt.subplot(2, 3, 4)
for rho, data in results.items():
    ax4.loglog(frequencies, data['imag'], label=f'ρ = {rho} Ом·м', linewidth=2)
ax4.set_xlabel('Частота (Гц)', fontsize=12)
ax4.set_ylabel('Im(Z) (Ом)', fontsize=12)
ax4.set_title('Мнимая часть', fontsize=14)
ax4.legend(fontsize=10)
ax4.grid(True, which='both', alpha=0.3)

# 5. График зависимости |Z| от ρ на фиксированной частоте
ax5 = plt.subplot(2, 3, 5)
fixed_freq = 10  # Гц
Z_at_freq = [complex_impedance(rho, fixed_freq) for rho in resistivity_values]
magnitudes_at_freq = np.abs(Z_at_freq)
ax5.loglog(resistivity_values, magnitudes_at_freq, 'o-', linewidth=2, markersize=8)
ax5.set_xlabel('Удельное сопротивление ρ (Ом·м)', fontsize=12)
ax5.set_ylabel(f'|Z| при f = {fixed_freq} Гц (Ом)', fontsize=12)
ax5.set_title(f'Импеданс на частоте {fixed_freq} Гц', fontsize=14)
ax5.grid(True, which='both', alpha=0.3)

# 6. Годограф импеданса (комплексная плоскость)
ax6 = plt.subplot(2, 3, 6)
for rho in [10, 100, 1000]:  # выбираем три характерных значения
    data = results[rho]
    ax6.plot(data['real'], data['imag'],
               label=f'ρ = {rho} Ом·м', linewidth=2)
ax6.set_xlabel('Re(Z)', fontsize=12)
ax6.set_ylabel('Im(Z)', fontsize=12)
ax6.set_title('Годограф импеданса\n(комплексная плоскость)', fontsize=14)
ax6.legend(fontsize=10)
ax6.grid(True, alpha=0.3)
ax6.axis('equal')

plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.show()

# Вывод числовых данных для ключевых точек
print("Результаты моделирования импеданса:")
print("=" * 50)
print(f"{'Частота (Гц)':<12} {'ρ (Ом·м)':<10} {'|Z| (Ом)':<12} {'Фаза (°)':<10}")
print("-" * 50)

sample_freqs = [0.1, 1, 10, 100]
sample_rhos = [10, 100, 1000]

for f in sample_freqs:
    for rho in sample_rhos:
        Z = complex_impedance(rho, f)
        print(f"{f:<12} {rho:<10} {np.abs(Z):<12.4f} {np.angle(Z, deg=True):<10.2f}")

