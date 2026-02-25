"""
DeepSeek 26/02/2026
11. Дескрипторы
Дескриптор — это механизм, описывающий поведение свойства объекта
при операциях чтения, записи, перечисления и т.д.
Типы дескрипторов
1. Дескриптор данных (Data Descriptor):
- value — значение свойства;
- writable — можно ли изменить значение;
- enumerable — перечисляется ли в циклах;
- configurable — можно ли переконфигурировать.
2. Дескриптор доступа (Accessor Descriptor):
- get — функция-геттер;
- set — функция-сеттер;
- enumerable;
- configurable.
"""
class PositiveNumber:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        return obj.__dict__.get(self.name, 0)

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError(f"{self.name} должен быть положительным")
        obj.__dict__[self.name] = value

class WellParameter:
    depth = PositiveNumber()
    temperature = PositiveNumber()

    def __init__(self, name, depth, temperature):
        self.name = name
        self.depth = depth
        self.temperature = temperature

# Использование
param = WellParameter("West-1", 2500, 85)
print(param.depth)  # 2500
# param.depth = -100    # ValueError!