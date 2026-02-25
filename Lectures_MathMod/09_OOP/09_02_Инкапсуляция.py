"""
DeepSeek 26/02/2026
2. Инкапсуляция
"""
class CoreSample:
    def __init__(self, well, depth):
        self.well = well
        self.depth = depth
        self._porosity = None  # "приватный" атрибут
        self.__permeability = None  # "сильно приватный"

    @property
    def porosity(self):
        return self._porosity

    @porosity.setter
    def porosity(self, value):
        if 0 <= value <= 50:
            self._porosity = value
        else:
            raise ValueError("Некорректная пористость")

    def set_permeability(self, value):
        if value > 0:
            self.__permeability = value

    def get_permeability(self):
        return self.__permeability


# Использование
core = CoreSample("West-1", 2450)
core.porosity = 18.5  # через setter
core.set_permeability(120)  # через метод
print(f"Пористость: {core.porosity}%")
print(f"Проницаемость: {core.get_permeability()} мД")