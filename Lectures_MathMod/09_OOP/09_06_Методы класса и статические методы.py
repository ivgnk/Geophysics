"""
DeepSeek 26/02/2026
6. Методы класса и статические методы
Метод класса — это метод, который привязан к классу, а не к его экземпляру.
Он получает класс (обычно обозначается как cls) в качестве первого неявного аргумента.

Статический метод — это метод, который принадлежит классу,
но не имеет доступа к классу (cls) или экземпляру (self).
Он ведёт себя как обычная функция,
но находится внутри класса из соображений логической организации кода.
"""

class Reservoir:
    company = "GeoOil"
    recovery_factor = 0.35

    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

    @classmethod
    def set_recovery(cls, factor):
        cls.recovery_factor = factor

    @classmethod
    def from_string(cls, data_string):
        name, volume = data_string.split('-')
        return cls(name, float(volume))

    @staticmethod
    def oil_price(quality):
        if quality == "light":
            return 85
        elif quality == "heavy":
            return 65
        return 75

    def reserves(self):
        return self.volume * self.recovery_factor

# Использование
Reservoir.set_recovery(0.40)  # классовый метод
res = Reservoir.from_string("Priobskoe-5000000")  # альтернативный конструктор
print(res.reserves())  # 2000000.0
print(Reservoir.oil_price("light"))  # 85 (статический метод)