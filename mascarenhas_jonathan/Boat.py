from RiverPart import RiverPart

class Boat(RiverPart):
    """
    A class representing a boat in the river system.

    @ivar next_id: A class variable to keep track of the next available boat ID.
    @type next_id: int
    """
    next_id = 1

    def __init__(self, power=1):
        """
        Initialize a new boat with the given power.

        @param self: The instance of the class.
        @type self: Boat

        @param power: The power of the boat.
        @type power: int

        This constructor creates a new boat with a unique ID and the specified power. The boat's default strategy is 'steady' with a step size of 1.

        @ivar __id: The unique ID of the boat.
        @type __id: int

        @ivar __power: The power of the boat.
        @type __power: int

        @ivar __str: The string representation of the boat (⛴).
        @type __str: str

        @ivar type: The type of the boat ('boat').
        @type type: str

        @ivar step: The step size for boat movement.
        @type step: int

        @ivar strategy: The strategy for boat movement ('steady' or 'max').
        @type strategy: str
        """
        super().__init__()
        self.__id = Boat.next_id
        Boat.next_id += 1
        self.__power = power
        self.__str = '⛴'
        self.type = 'boat'
        self.step = 1
        self.strategy = 'steady'

    def __str__(self):
        """
        Get the string representation of the boat.

        @param self: The instance of the class.
        @type self: Boat

        This method returns the string representation of the boat (⛴).

        @return: The string representation of the boat.
        @rtype: str
        """
        return self.__str

    def getID(self):
        """
        Get the unique ID of the boat.

        @param self: The instance of the class.
        @type self: Boat

        This method retrieves the unique ID of the boat.

        @return: The unique ID of the boat.
        @rtype: int
        """
        return self.__id

    def getPower(self):
        """
        Get the power of the boat.

        @param self: The instance of the class.
        @type self: Boat

        This method retrieves the power of the boat.

        @return: The power of the boat.
        @rtype: int
        """
        return self.__power
