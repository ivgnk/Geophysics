"""
DeepSeek 26/02/2026
3. Наследование
"""
class BaseWell:
    def __init__(self, name, depth):
        self.name = name
        self.depth = depth

    def drill(self):
        return f"Бурение {self.name}"

class VerticalWell(BaseWell):
    def drill(self):
        return f"Вертикальное бурение {self.name} до {self.depth}м"

class HorizontalWell(BaseWell):
    def __init__(self, name, depth, horizontal_length):
        super().__init__(name, depth)
        self.horizontal_length = horizontal_length

    def drill(self):
        return f"Горизонтальное бурение {self.name}: вертикально {self.depth}м, горизонтально {self.horizontal_length}м"

# Использование
v_well = VerticalWell("V-100", 2500)
h_well = HorizontalWell("H-200", 2800, 1200)

print(v_well.drill())  # Вертикальное бурение V-100 до 2500м
print(h_well.drill())  # Горизонтальное бурение H-200: вертикально 2800м, горизонтально 1200м
