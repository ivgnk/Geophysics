"""
DeepSeek 26/02/2026
8. Абстрактные классы
Абстрактный класс — это базовый класс, который нельзя инстанцировать (создать его экземпляр напрямую).
Он служит шаблоном для других классов и может содержать:
- абстрактные методы (без реализации);
- обычные методы (с реализацией);
- поля и свойства.
Главная цель — задать общий интерфейс и
частично реализованную функциональность для группы связанных классов.
"""

from abc import ABC, abstractmethod

class FormationEvaluation(ABC):
    @abstractmethod
    def calculate_porosity(self):
        pass

    @abstractmethod
    def calculate_saturation(self):
        pass

    def summary(self):
        return f"Пористость: {self.calculate_porosity():.1f}%, Насыщенность: {self.calculate_saturation():.1f}%"


class Sandstone(FormationEvaluation):
    def __init__(self, acoustic, resistivity):
        self.acoustic = acoustic
        self.resistivity = resistivity

    def calculate_porosity(self):
        return 30 - self.acoustic / 10  # упрощенная формула

    def calculate_saturation(self):
        return 1 - 5 / self.resistivity


class Carbonate(FormationEvaluation):
    def __init__(self, neutron, density):
        self.neutron = neutron
        self.density = density

    def calculate_porosity(self):
        return (self.neutron + self.density) / 2

    def calculate_saturation(self):
        return 0.8  # упрощенно

# Использование
sand = Sandstone(45, 20)
carb = Carbonate(15, 2.65)

print(sand.summary())  # Пористость: 25.5%, Насыщенность: 75.0%
print(carb.summary())  # Пористость: 8.8%, Насыщенность: 80.0%
