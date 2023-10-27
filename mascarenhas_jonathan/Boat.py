# Boat class that uses the strategy

class Boat:
    def __init__(self, behavior):
        self.behavior = behavior

    def set_behavior(self, behavior):
        self.behavior = behavior

    def move(self):
        self.behavior.move()
