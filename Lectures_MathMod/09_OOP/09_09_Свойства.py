"""
DeepSeek 26/02/2026
9. Свойства (Properties) и дескрипторы
Свойство — это атрибут класса, который выглядит как обычное поле,
но на самом деле контролируется методами доступа (геттером и сеттером).
В Python свойства создаются с помощью декоратора @property.

Дескриптор — это механизм, описывающий поведение свойства объекта при операциях чтения, записи, перечисления и т.д.
Типы дескрипторов
Дескриптор данных (Data Descriptor):
- value — значение свойства;
- writable — можно ли изменить значение;
- enumerable — перечисляется ли в циклах;
- configurable — можно ли переконфигурировать.

Дескриптор доступа (Accessor Descriptor):
- get — функция-геттер;
- set — функция-сеттер;
- enumerable;
- configurable.

В Python дескрипторы — это объекты, реализующие один или несколько специальных методов:
__get__(self, instance, owner);
__set__(self, instance, value);
__delete__(self, instance).
"""

class OilReservoir:
    def __init__(self, area, thickness, porosity, saturation):
        self._area = area
        self._thickness = thickness
        self._porosity = porosity
        self._saturation = saturation

    @property
    def volume(self):
        """Объем породы"""
        return self._area * self._thickness

    @property
    def pore_volume(self):
        """Объем пор"""
        return self.volume * self._porosity / 100

    @property
    def oil_volume(self):
        """Объем нефти в пластовых условиях"""
        return self.pore_volume * self._saturation / 100

    @property
    def stoiip(self):
        """Геологические запасы (Stock Tank Oil Initially In Place)"""
        return self.oil_volume / 1.3  # деление на объемный коэффициент

    @property
    def porosity(self):
        return self._porosity

    @porosity.setter
    def porosity(self, value):
        if 0 <= value <= 40:
            self._porosity = value
        else:
            raise ValueError("Пористость должна быть 0-40%")

# Использование
reservoir = OilReservoir(1_000_000, 20, 18, 65)
print(f"Объем породы: {reservoir.volume:.0f} м³")
print(f"Объем пор: {reservoir.pore_volume:.0f} м³")
print(f"Геологические запасы: {reservoir.stoiip:.0f} м³")

reservoir.porosity = 20  # через setter
print(f"Новая пористость: {reservoir.porosity}%")