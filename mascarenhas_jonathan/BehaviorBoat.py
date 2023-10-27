from abc import ABC, abstractmethod
from Boat import Boat

# Define the BehaviorBoat interface (strategy)
class BehaviorBoat(ABC):
    @abstractmethod
    def move(self):
        pass

# Concrete implementations of BehaviorBoat
class Steady(BehaviorBoat):
    def move(self):
        print("Steady, not moving")

class MaxSpeed(BehaviorBoat):
    def move(self):
        print("Max speed!")

# Create Boat instances with different behaviors
steady_boat = Boat(Steady())
fast_boat = Boat(MaxSpeed())

# Use the boats
print("Steady Boat:")
steady_boat.move()  # Output: Steady, not moving

print("\nFast Boat:")
fast_boat.move()  # Output: Max speed!
