"""
DeepSeek 26/02/2026
5. Магические методы (dunder methods)
Специальные методы с двойным подчеркиванием для перегрузки операторов.
"""
class StratigraphicUnit:
    def __init__(self, name, top, bottom):
        self.name = name
        self.top = top
        self.bottom = bottom
        self.thickness = bottom - top

    def __str__(self):
        return f"{self.name}: {self.top}-{self.bottom} м"

    def __repr__(self):
        return f"StratigraphicUnit('{self.name}', {self.top}, {self.bottom})"

    def __len__(self):
        return int(self.thickness)

    def __contains__(self, depth):
        return self.top <= depth <= self.bottom

    def __lt__(self, other):
        return self.top < other.top

# Использование
bazhen = StratigraphicUnit("Бажен", 2700, 2780)
achimov = StratigraphicUnit("Ачимов", 2780, 2850)

print(bazhen)  # Бажен: 2700-2780 м
print(repr(bazhen))  # StratigraphicUnit('Бажен', 2700, 2780)
print(len(bazhen))  # 80
print(2500 in bazhen)  # False
print(2750 in bazhen)  # True
print(bazhen < achimov)  # True (Бажен выше)

