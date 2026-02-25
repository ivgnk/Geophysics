"""
DeepSeek 26/02/2026
7. Композиция и агрегация
Агрегация — это отношение «целое‑часть», при котором часть может существовать независимо от целого.
Это слабая связь между объектами.
Композиция — это отношение «целое‑часть», при котором часть не может существовать без целого.
Это сильная связь между объектами.
"""
# Композиция (часть не существует без целого)
class Bit:
    def __init__(self, type_name):
        self.type = type_name

    def rotate(self):
        return f"{self.type} долото вращается"


class DrillString:
    def __init__(self, bit_type):
        self.bit = Bit(bit_type)  # композиция - создается внутри

    def drill(self):
        return f"Бурение: {self.bit.rotate()}"


# Агрегация (часть может существовать отдельно)
class Geologist:
    def __init__(self, name):
        self.name = name

    def interpret(self, data):
        return f"{self.name} интерпретирует {data}"


class Project:
    def __init__(self, name):
        self.name = name
        self.geologists = []  # агрегация - список геологов

    def add_geologist(self, geologist):
        self.geologists.append(geologist)


# Использование
# Композиция
drill = DrillString("PDC")
print(drill.drill())  # Бурение: PDC долото вращается

# Агрегация
ivan = Geologist("Иван")
petr = Geologist("Петр")
project = Project("Приобское")
project.add_geologist(ivan)
project.add_geologist(petr)  # геологи существуют и вне проекта