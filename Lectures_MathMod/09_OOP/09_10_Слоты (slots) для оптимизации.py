"""
DeepSeek 26/02/2026
10. Слоты (slots) для оптимизации
Слоты — специальный атрибут класса (__slots__), который позволяет:
- экономить память за счёт отказа от словаря __dict__ для хранения атрибутов;
- ускорить доступ к атрибутам (работа с массивом вместо хэш‑таблицы);
- запретить динамическое добавление новых атрибутов в экземпляры класса.
По умолчанию каждый экземпляр класса имеет словарь __dict__,
где хранятся все атрибуты объекта.
Слоты заменяют этот словарь фиксированной структурой данных.
"""
# Обычный класс
class SeismicTrace:
    def __init__(self, number, x, y):
        self.number = number
        self.x = x
        self.y = y
        self.amplitude = [0] * 1000

# Класс со слотами (экономит память)
class SeismicTraceOptimized:
    __slots__ = ['number', 'x', 'y', 'amplitude']

    def __init__(self, number, x, y):
        self.number = number
        self.x = x
        self.y = y
        self.amplitude = [0] * 1000

# Сравнение
import sys
trace1 = SeismicTrace(1, 100, 200)
trace2 = SeismicTraceOptimized(1, 100, 200)

print(f"Обычный класс: {sys.getsizeof(trace1.__dict__)} байт на __dict__")
print(f"Со слотами: нет __dict__ - {hasattr(trace2, '__dict__')}")