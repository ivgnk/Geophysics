"""
DeepSeek 26/02/2026
1. Классы и объекты
"""
class Well:
    """Класс для представления скважины"""
    company = "GeoDrill"  # атрибут класса

    def __init__(self, name, depth):
        self.name = name  # атрибуты объекта
        self.depth = depth
        self.gamma_log = []

    def add_gamma(self, value):
        self.gamma_log.append(value)

    def info(self):
        return f"{self.name}, глубина {self.depth}м, точек ГК: {len(self.gamma_log)}"

# Создание объектов
well1 = Well("West-1", 2500)
well2 = Well("East-1", 2800)

well1.add_gamma(45)
well1.add_gamma(52)
print(well1.info())  # West-1, глубина 2500м, точек ГК: 2
print(well2.company)  # GeoDrill