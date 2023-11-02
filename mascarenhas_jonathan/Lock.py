from RiverPart import RiverPart

class Lock(RiverPart):
    def __init__(self, depth):
        """
        Initialize a new lock with the given depth.

        @param self: The instance of the class.
        @type self: Lock

        @param depth: The depth of the lock.
        @type depth: int

        This constructor creates a new lock with the specified depth. By default, the lock has no boats, and its fill behavior is set to 'none'.

        @ivar depth: The depth of the lock.
        @type depth: int
        """
        super().__init__()
        self.depth = depth
        self.__collection = [None]
        self.__str = '_X( ' + str(self.depth) + ')_'
        self.type = 'lock'
        self.fillBehavior = 'none' # can be 'basic' 'fast-fill'
        self.level = 0

    def __str__(self):
        """
        Get the string representation of the lock.

        @param self: The instance of the class.
        @type self: Lock

        This method returns the string representation of the lock, which may include a boat if present.

        @return: The string representation of the lock.
        @rtype: str
        """
        # if boat
        if (self.__collection[0] == None):
            return '_X( ' + str(self.depth) + ')_'

        else:
            return '_⛴( ' + str(self.depth) + ')_'

    def addBoat(self, boat):
        """
        Add a boat to the lock.

        @param self: The instance of the class.
        @type self: Lock

        @param boat: The boat to be added to the lock.
        @type boat: Boat

        This method adds the specified boat to the lock.

        @return: None
        @rtype: None
        """
        self.__collection[0] = boat

    def hasBoat(self):
        """
        Check if the lock has a boat.

        @param self: The instance of the class.
        @type self: Lock

        This method checks if the lock has a boat inside it.

        @return: True if the lock has a boat, False otherwise.
        @rtype: bool
        """
        if (self.__collection[0]):
            return True
        return False

    def getBoat(self):
        """
        Get the boat inside the lock.

        @param self: The instance of the class.
        @type self: Lock

        This method retrieves the boat that is inside the lock.

        @return: The boat inside the lock, or None if the lock is empty.
        @rtype: Boat or None
        """
        return self.__collection[0]

    def removeBoat(self):
        """
        Remove the boat from the lock.

        @param self: The instance of the class.
        @type self: Lock

        This method removes the boat from the lock.

        @return: None
        @rtype: None
        """
        self.__collection[0] = None

    def getDepth(self):
        """
        Get the depth of the lock.

        @param self: The instance of the class.
        @type self: Lock

        This method retrieves the depth of the lock.

        @return: The depth of the lock.
        @rtype: int
        """
        return self.depth

    def getCollection(self):
        """
        Get the collection of boats in the lock.

        @param self: The instance of the class.
        @type self: Lock

        This method retrieves the collection of boats currently in the lock.

        @return: A list representing the collection of boats in the lock.
        @rtype: list
        """
        return self.__collection


    def hasNext(self, temp1):
        """
        Check if there is a boat in the next section or lock.

        @param self: The instance of the class.
        @type self: Lock

        @param temp1: A temporary value used in the check.
        @type temp1: Any

        This method checks if there is a boat in the next section or lock. It considers the type of the next river part and its boat presence to determine if there is a boat in the next section or lock.

        @return: True if there is a boat in the next section or lock, False otherwise.
        @rtype: bool
        """
        # get next section
        nextSection = self.nextPart

        # next part is another section or we are
        # emptying out
        if (nextSection is None):
            return False

        # next part could be another lock,
        if (nextSection.type == 'lock'):
            if (nextSection.hasBoat()):
                return True
            return False

        # if boat at the beginning of the section
        if (nextSection.hasBoatBegin()):
            return True

        # no boat
        return False


    def moveBoat(self, temp):
        """
        Move a boat according to the lock's fill behavior.

        @param self: The instance of the class.
        @type self: Lock

        @param temp: A temporary value used in the move operation.
        @type temp: Any

        This method moves a boat within the lock or to the next section based on the lock's fill behavior. There are three types of moves: 'none,' 'basic,' and 'fast-empty.'

        - 'none': Move the boat from the lock to the next section or empty out.
        - 'basic': Perform the basic fill behavior.
        - 'fast-empty': Perform the fast empty behavior.

        @return: None
        @rtype: None
        """
        # three types of moves - the one below, basic, and fast empty

        if (self.fillBehavior == 'none'):
            # move boat from current lock to the next section or empty out

            # get next Section
            nextSection = self.nextPart

            if (nextSection is not None):
                # add boat to this section
                nextSection.addBoat(self.__collection[0])

            # remove boat from lock
            self.__collection[0] = None

        elif (self.fillBehavior == 'basic'):
            self.basicFill()

        else:
            self.fastEmpty()

    # GRADING: BASIC_FILL
    def basicFill(self):
        """
        Perform basic filling behavior in the lock.

        @param self: The instance of the class.
        @type self: Lock

        This method performs the basic filling behavior in the lock, allowing a boat to move out of the lock when the lock's water level reaches its depth.

        @return: None
        @rtype: None
        """
        # for basic, we can move a boat out
        # only if level == depth
        # level is updated by one at each step

        # if we have a boat in the lock, start filling
        if (self.hasBoat()):
            if (self.level < self.depth - 1):
                self.level += 1
            else:
                self.level = self.depth
                # we have reached level == depth, exit the boat
                # get next Section
                nextSection = self.nextPart

                if (nextSection is not None):
                    # add boat to this section
                    nextSection.addBoat(self.__collection[0])

                # remove boat from lock
                self.__collection[0] = None

    # GRADING: FAST_EMPTY.
    def fastEmpty(self):
        """
        Perform fast emptying behavior in the lock.

        @param self: The instance of the class.
        @type self: Lock

        This method performs the fast emptying behavior in the lock, allowing a boat to move out of the lock when the lock's water level reaches its depth.

        @return: None
        @rtype: None
        """
        # if we have a boat in the lock, start filling
        if (self.hasBoat()):
            if (self.level < self.depth - 1):
                self.level += 1
            else:
                self.level = self.depth
                # we have reached level == depth, exit the boat
                # get next Section
                nextSection = self.nextPart

                if (nextSection is not None):
                    # add boat to this section
                    nextSection.addBoat(self.__collection[0])

                # remove boat from lock
                self.__collection[0] = None
