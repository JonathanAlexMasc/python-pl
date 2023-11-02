from abc import ABC, abstractmethod

class RiverPart(ABC):
    """
    Abstract base class for river parts.

    This class defines the structure for river parts in the system.

    @ivar nextPart: A reference to the next river part.
    @type nextPart: RiverPart
    @ivar type: The type of the river part.
    @type type: str
    """
    @abstractmethod
    def __init__(self):
        """
        Initialize a RiverPart.

        This constructor sets the instance variables nextPart and type to their initial values.
        """
        self.nextPart = None
        self.type = ''

    @abstractmethod
    def __str__(self):
        """
        Return a string representation of the river part.

        @return: A string representation of the river part.
        @rtype: str
        """
        pass



