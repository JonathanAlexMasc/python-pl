from RiverIterator import RiverIterMain
from RiverIterator import UpdateRiverIterator
from RiverIterator import SectionDetailsIterator
from Boat import Boat
from Section import Section
from Lock import Lock


class RiverSystem:
    """
    Class representing a river system.

    This class defines a river system consisting of sections and locks. It initializes the river system with a predefined configuration.

    """
    def __init__(self):
        """
        This is the constructor for a class that represents a river with sections and locks.

        @ivar __index: An integer representing the index of the river.
        @type __index: int

        @ivar __river: A list of river components, including sections and locks.
        @type __river: list[Section or Lock]

        This constructor initializes the river by setting the index, creating a list of river components, and establishing relationships between them.

        It sets the 'nextPart' attribute of each component to the following component in the river, and it marks the last section as the last section in the river.
        """
        self.__index = -1
        self.__river = [Section(6, 0), Lock(0), Section(3, 1)]

        for i in range(len(self.__river) - 1):
            self.__river[i].nextPart = self.__river[i + 1]

        # last section is the last section
        self.__river[-1].lastSection = True



    def addDefaultBoat(self, boat):
        """
        Add a default boat to the first section of the river.

        @param self: The instance of the class.
        @type self: YourClass

        @param boat: The boat to be added to the first section.
        @type boat: Boat

        This method adds a default boat to the first section of the river if there's no boat already in that section. If there's already a boat, a new boat is created with an incremented serial number, and the new boat is added to the section.

        @return: None if the river is empty or if the first section already has a boat, else the boat is added to the section.
        @rtype: None or Boat
        """
        if (self.__river == []):
            return
        # get first section
        init_section = self.__river[0]

        # if there's a boat already, make a new boat to
        # increment the serial number then do not use it
        if (not init_section.hasBoatBegin()):
            # add boat to this section
            init_section.addBoat(boat)

    def handleSOLID(self):
        """
        Handle the SOLID principles with boat and section objects.

        @param self: The instance of the class.
        @type self: RiverSystem

        This method demonstrates the use of SOLID principles with boat and section objects. It creates three Boat objects, one Section object, one Lock object, and one RiverSystem object. Then, it adds boats to the Section and Lock objects and demonstrates their string representations using the `print` function.

        @return: None
        @rtype: None
        """
        boat1 = Boat()
        boat2 = Boat()
        boat3 = Boat()
        section1 = Section(1, 0)
        section1.addBoat(boat1)
        lock1 = Lock(0)
        lock1.addBoat(boat2)
        system = RiverSystem()
        system.addDefaultBoat(boat3)

        # GRADING: TO_STR
        print(boat1)
        print(section1)
        print(lock1)
        print(system)

    def updateOne(self):
        """
        Update the river by iterating through an update iterator.

        @param self: The instance of the class.
        @type self: RiverSystem

        This method updates the river by iterating through an update iterator and replacing the old river with the updated river.

        @return: None
        @rtype: None
        """
        newRiver = []

        # call iterator to update river
        for i in UpdateRiverIterator(self.__river):
            newRiver.insert(0, i)

        self.__river = newRiver

    def getSectionDetails(self):
        """
        Get and display details of each section in the river.

        @param self: The instance of the class.
        @type self: RiverSystem

        This method retrieves and displays details of each section in the river using an iterator. It prints information about the section, including the number of boats and the flow rate.

        @return: None
        @rtype: None
        """
        index = 1
        for sec in SectionDetailsIterator(self.__river):
            if (sec is not None):
                print('Section ' + str(index))
                print('Boats: ' + str(sec.getNumBoats()) + \
                      ' Flow: ' + str(sec.getFlow()))
                print()
                index += 1


    def addCustomBoat(self, enginePower, travelMethod):
        """
        Add a custom boat to the river with specified engine power and travel method.

        @param self: The instance of the class.
        @type self: RiverSystem

        @param enginePower: The engine power of the new boat.
        @type enginePower: int

        @param travelMethod: The travel method for the new boat (1 for default, 2 for maximum speed).
        @type travelMethod: int

        This method creates a new boat with the specified engine power and travel method and adds it to the river. If the travel method is 2, the boat's strategy is set to 'max.'

        @return: None
        @rtype: None
        """
        # make new boat
        newBoat = Boat(enginePower)
        # set boat strategy
        if (travelMethod == 2):
            newBoat.strategy = 'max'

        # add boat to beginning
        self.addDefaultBoat(newBoat)

    def makeTesterRiver(self):
        """
        Create a tester river with sections, locks, and fill behaviors.

        @param self: The instance of the class.
        @type self: RiverSystem

        This method creates a tester river configuration with sections, locks, and specified fill behaviors. It sets up the river components and establishes the relationships between them. The resulting river configuration can be used for testing and evaluation.

        @return: None
        @rtype: None
        """
        section1 = Section(5, 0)
        lock1 = Lock(0)
        lock1.fillBehavior = 'none'
        section2 = Section(6, 2)
        lock2 = Lock(2)
        lock2.fillBehavior = 'basic'
        section3 = Section(3, 3)
        lock3 = Lock(5)
        lock3.fillBehavior = 'fast-fill'

        self.__river = []
        self.__river.append(section1)
        self.__river.append(lock1)
        self.__river.append(section2)
        self.__river.append(lock2)
        self.__river.append(section3)
        self.__river.append(lock3)

        for i in range(len(self.__river) - 1):
            part = self.__river[i]
            part.nextPart = self.__river[i + 1]

        self.__upper = RiverIterMain(self.__river)
        self.__lower = self.__upper.getLowerRiver()

    def addSection(self, len, flow):
        newSection = Section(len, flow)
        self.__river.append(newSection)

    def addLock(self, behavior, depth):
        """
        Add a new section to the river with the specified length and flow.

        @param self: The instance of the class.
        @type self: RiverSystem

        @param length: The length of the new section.
        @type length: int

        @param flow: The flow rate of the new section.
        @type flow: int

        This method creates a new river section with the specified length and flow rate and adds it to the river.

        @return: None
        @rtype: None
        """
        newLock = Lock(depth)
        if (behavior == 1):
            newLock.fillBehavior = 'none'
        elif (behavior == 2):
            newLock.fillBehavior = 'basic'
        else:
            newLock.fillBehavior = 'fast-empty'

        self.__river.append(newLock)

    def setRiverEmpty(self):
        """
        Set the river to an empty state.

        @param self: The instance of the class.
        @type self: RiverSystem

        This method sets the river to an empty state by clearing the list of river components.

        @return: None
        @rtype: None
        """
        self.__river = []

    def makeAssociations(self):
        """
        Establish associations between river components.

        @param self: The instance of the class.
        @type self: RiverSystem

        This method establishes associations between river components by setting the 'nextPart' attribute for each component to the following component in the river. Additionally, it marks the last section as the last section in the river if there are components in the river.

        @return: None
        @rtype: None
        """
        for i in range(len(self.__river) - 1):
            part = self.__river[i]
            part.nextPart = self.__river[i + 1]

        if (len(self.__river) > 0):
            self.__river[-1].lastSection = True

    def __str__(self):
        """
        Generate a string representation of the river configuration.

        @param self: The instance of the class.
        @type self: RiverSystem

        This method generates a string representation of the river configuration, including both the upper and lower sections of the river.

        @return: A string representation of the river configuration.
        @rtype: str
        """
        lowerRiverString = ''
        upperRiverString = ''

        self.__upper = RiverIterMain(self.__river)
        self.__lower = self.__upper.getLowerRiver()

        for i in self.__upper:
            upperRiverString += i
        for j in self.__lower:
            lowerRiverString += j

        return upperRiverString + '\n' + lowerRiverString
