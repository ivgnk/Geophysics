"""
DeepSeek 26/02/2026
12. Миксины
Миксин (mixin) — это класс, содержащий методы для использования другими классами,
но не предназначенный для самостоятельного создания экземпляров.

Миксины реализуют принцип композиции:
они добавляют определённую функциональность к классам через множественное наследование.

Ключевые особенности:
- фокусируются на поведении, а не на сущности объекта;
- предоставляют модульную функциональность;
- позволяют избежать дублирования кода (принцип DRY);
- обычно не имеют состояния (или минимальное);
- используются через множественное наследование;
- не зависят от конкретных классов — могут применяться в разных контекстах.
"""
class ExportMixin:
    def to_csv(self, filename):
        import csv
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            if hasattr(self, 'get_data'):
                writer.writerows(self.get_data())
        print(f"Сохранено в {filename}")

class PlotMixin:
    def quick_plot(self):
        import matplotlib.pyplot as plt
        if hasattr(self, 'depths') and hasattr(self, 'values'):
            plt.plot(self.values, self.depths)
            plt.gca().invert_yaxis()
            plt.show()

# Использование миксинов
class WellLog(ExportMixin, PlotMixin):
    def __init__(self, name):
        self.name = name
        self.depths = []
        self.values = []

    def add(self, depth, value):
        self.depths.append(depth)
        self.values.append(value)

    def get_data(self):
        return list(zip(self.depths, self.values))

# Вся функциональность в одном классе
log = WellLog("GK-1")
log.add(2500, 45)
log.add(2510, 78)
log.add(2520, 92)

log.to_csv("well_data.csv")  # из ExportMixin
# log.quick_plot()           # из PlotMixin
