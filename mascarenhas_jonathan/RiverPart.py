class RiverPart:
    def __init__(self, name, length, next_part=None):
        self.name = name
        self.length = length
        self.next_part = next_part

    def add_next_part(self, next_part):
        self.next_part = next_part

    def describe(self):
        description = f"Name: {self.name}, Length: {self.length} km"
        if self.next_part:
            description += f", Next Part: {self.next_part.name}"
        print(description)
