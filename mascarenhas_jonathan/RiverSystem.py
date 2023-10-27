class RiverSystem:
    def __init__(self, name):
        self.name = name
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def describe(self):
        print(f"River System: {self.name}")
        for part in self.parts:
            part.describe()
