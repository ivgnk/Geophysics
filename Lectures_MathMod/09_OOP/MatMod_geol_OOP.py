class Well:
    """Класс для представления скважины"""
    company = "GeoDrill"

    def __init__(self, name, depth):
        self.name = name
        self.depth = depth
        self.status = "planned"

    def drill(self, meters):
        self.depth += meters
        return f"{self.name} пробурена до {self.depth} м"

    def __str__(self):
        return f"{self.name}, глубина {self.depth} м"


class Formation:
    """Класс для представления геологического пласта"""

    def __init__(self, name, top, bottom, lithology):
        self.name = name
        self.top = top
        self.bottom = bottom
        self.lithology = lithology
        self.porosity = None

    def thickness(self):
        return self.bottom - self.top

    def __contains__(self, depth):
        return self.top <= depth <= self.bottom


class Core:
    """Класс для работы с керном"""
    def __init__(self, well, interval):
        self.well = well
        self.interval = interval
        self.samples = []

    def add_sample(self, depth, length):
        self.samples.append({"depth": depth, "length": length})

    def recovery(self):
        total = sum(s["length"] for s in self.samples)
        return (total / self.interval) * 100