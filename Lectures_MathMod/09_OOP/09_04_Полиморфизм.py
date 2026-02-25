"""
DeepSeek 26/02/2026
4. Полиморфизм
"""

class GeophysicalMethod:
    def process(self, data):
        pass

class Seismic(GeophysicalMethod):
    def process(self, data):
        return f"Сейсмообработка {len(data)} трасс"

class Resistivity(GeophysicalMethod):
    def process(self, data):
        return f"Инверсия ВЭЗ: {data} Ом·м"

class Gravity(GeophysicalMethod):
    def process(self, data):
        return f"Редукция Буге: аномалия {data} мГал"

# Функция с полиморфизмом
def process_data(method, data):
    print(method.process(data))

# Использование
methods = [Seismic(), Resistivity(), Gravity()]
for m in methods:
    process_data(m, [100])  # один интерфейс - разная реализация