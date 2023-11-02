from RiverPart import RiverPart

class Section(RiverPart):
    def __init__(self, length, flow):
        """
        Initialize a new section in the river.

        @param length: The length of the section.
        @type length: int

        @param flow: The flow rate of the section.
        @type flow: int
        """
        super().__init__()
        self.__length = length
        self.__flow = flow
        self.__collection = [None] * self.__length
        self.type = 'section'
        self.lastSection = False

    def __str__(self):
        """
        Generate a string representation of the section's contents.

        @param self: The instance of the class.
        @type self: Section

        This method generates a string representation of the section's contents, where '⛴' represents a boat and '〜〜〜' represents an empty space.

        @return: A string representation of the section's contents.
        @rtype: str
        """
        sectionStr = ''
        for i in self.__collection:
            if (i == None):
                sectionStr += '〜〜〜'
            else:
                sectionStr += '⛴〜〜'

        return sectionStr

    def hasBoatBegin(self):
        """
        Check if the section has a boat at the beginning.

        @param self: The instance of the class.
        @type self: Section

        This method checks if the section has a boat at the beginning (at the first position of its collection).

        @return: True if a boat is at the beginning of the section, False otherwise.
        @rtype: bool
        """
        if (self.__collection[0]):
            return True
        return False

    def hasBoatEnd(self):
        """
        Check if the section has a boat at the end.

        @param self: The instance of the class.
        @type self: Section

        This method checks if the section has a boat at the end (at the last position of its collection).

        @return: True if a boat is at the end of the section, False otherwise.
        @rtype: bool
        """
        if (self.__collection[-1]):
            return True
        return False

    def addBoat(self, boat):
        """
        Add a boat to the beginning of the section.

        @param self: The instance of the class.
        @type self: Section

        @param boat: The boat to be added to the section.
        @type boat: Boat

        This method adds a boat to the beginning of the section by placing it at the first position of the section's collection.

        @return: None
        @rtype: None
        """
        # add a boat to the beginning of the river/section
        self.__collection[0] = boat

    def getEndBoat(self):
        """
        Get the boat at the end of the section.

        @param self: The instance of the class.
        @type self: Section

        This method retrieves the boat at the end of the section, which is located at the last position of the section's collection.

        @return: The boat at the end of the section, or None if there is no boat.
        @rtype: Boat or None
        """
        return self.__collection[-1]

    def moveBoat(self, atIndex):
        """
        Move a boat within the section or to the next river part.

        @param self: The instance of the class.
        @type self: Section

        @param atIndex: The index of the boat to be moved within the section.
        @type atIndex: int

        This method moves a boat within the section or to the next river part, depending on the boat's movement step and the section's position within the river.

        @return: None
        @rtype: None
        """
        curr_boat = self.__collection[atIndex]
        step = curr_boat.step

        if (step < 1):
            step = 1

        # check if we are the last section
        if (self.lastSection):
            # check if last index of last section
            if (atIndex == len(self.__collection) - 1):
                # just set current index to None
                self.__collection[atIndex] = None

            # not last index
            else:
                # set atIndex + step to atIndex
                self.__collection[atIndex + step] = self.__collection[atIndex]

                # set current index to None
                self.__collection[atIndex] = None

        # not at the last section
        else:
            # check if we are the last index of this section
            if (atIndex == len(self.__collection) - 1):
                # move to the next riverPart (not sure if this should be split up for lock and section)

                # get next riverPart
                nextRiverPart = self.nextPart

                # addBoat to the next riverPart
                nextRiverPart.addBoat(self.__collection[atIndex])

                # remove boat from current Section at 'atIndex'
                self.__collection[atIndex] = None

            # not last index, move to next index
            else:
                # next index could be

                # set atIndex + step to atIndex
                self.__collection[atIndex + step] = self.__collection[atIndex]

                # set current index to None
                self.__collection[atIndex] = None

    def getLength(self):
        """
        Get the length of the section.

        @param self: The instance of the class.
        @type self: Section

        This method retrieves the length of the section.

        @return: The length of the section.
        @rtype: int
        """
        return self.__length

    def getFlow(self):
        """
        Get the flow rate of the section.

        @param self: The instance of the class.
        @type self: Section

        This method retrieves the flow rate of the section.

        @return: The flow rate of the section.
        @rtype: int
        """
        return self.__flow

    def getCollection(self):
        """
        Get the collection representing the section's contents.

        @param self: The instance of the class.
        @type self: Section

        This method retrieves the collection representing the section's contents, which is a list containing boats and empty spaces.

        @return: The collection of the section's contents.
        @rtype: list
        """
        return self.__collection

    def setCollection(self, newCollection):
        """
        Set the collection representing the section's contents.

        @param self: The instance of the class.
        @type self: Section

        @param newCollection: The new collection to replace the section's current contents.
        @type newCollection: list

        This method sets the collection representing the section's contents to the provided new collection.

        @return: None
        @rtype: None
        """
        self.__collection = newCollection

    def getNumBoats(self):
        """
        Get the number of boats in the section.

        @param self: The instance of the class.
        @type self: Section

        This method counts the number of boats in the section's collection.

        @return: The number of boats in the section.
        @rtype: int
        """
        count = 0
        for i in self.__collection:
            if (i):
                count += 1
        return count


    def hasBoat(self, currIndex):
        """
        Check if the section has a boat at a specified index.

        @param self: The instance of the class.
        @type self: Section

        @param currIndex: The index to check for the presence of a boat in the section.
        @type currIndex: int

        This method checks if the section has a boat at the specified index in its collection.

        @return: True if a boat is at the specified index, False otherwise.
        @rtype: bool
        """
        if (self.__collection[currIndex] != None):
            return True
        return False


    def hasNext(self, currIndex):
        """
        Check if there is a next position for the boat at the specified index based on its strategy.

        @param self: The instance of the class.
        @type self: Section

        @param currIndex: The index of the boat for which the next position is checked.
        @type currIndex: int

        This method checks if there is a next position for the boat at the specified index based on its strategy. It considers the boat's strategy and determines whether it can move to the next position.

        @return: True if there is a next position for the boat, False otherwise.
        @rtype: bool
        """
        # check current boat's strategy
        curr_boat = self.__collection[currIndex]
        step = curr_boat.getPower() - self.getFlow()

        if (curr_boat.strategy == 'steady'):
            return self.hasNextSteady(currIndex)
        else:
            # get "step" for the boat
            return self.hasNextMax(currIndex, step)

    # GRADING: STEADY_TRAVEL.
    def hasNextSteady(self, currIndex):
        """
        Check if there is a next position for the boat at the specified index based on a 'steady' strategy.

        @param self: The instance of the class.
        @type self: Section

        @param currIndex: The index of the boat for which the next position is checked.
        @type currIndex: int

        This method checks if there is a next position for the boat at the specified index based on a 'steady' strategy. It considers the boat's position within the section and determines whether it can move to the next position within the section or to the next river part.

        @return: True if there is a next position for the boat, False otherwise.
        @rtype: bool
        """
        # if we are at the last element, check next element's status
        if (currIndex == len(self.__collection) - 1):
            # get next element
            nextElement = self.nextPart

            # if nextElement is None, we have finished our iteration
            if (nextElement is None):
                return False

            # if lock, check if there is a boat in it already
            if (nextElement.type == 'lock'):
                nextLock = nextElement
                #print(nextLock)
                #print(nextLock.level)
                # if there is a boat in it already
                if (nextLock.hasBoat()):
                    return True

                # no boat BUT level is not zero return True
                # this means its not ready to accept a boat
                if (nextLock.level > 0):
                    return True

                else:
                    return False

            # if section, check if there is a boat at the begin
            elif (nextElement.type == 'section'):
                if (nextElement.hasBoatBegin()):
                    return True
                return False

            # we are at the last section and last element in that section, we can exit
            else:
                return True

        # we are not at the last element of the section
        # check if we can move to the next element within this section
        else:
            # check if next index is empty
            if (self.__collection[currIndex + 1] == None):
                return False
            return True

    #  GRADING: MAX_TRAVEL.
    def hasNextMax(self, currIndex, step):
        """
        Check if there is a next position for the boat at the specified index based on a 'max' strategy.

        @param self: The instance of the class.
        @type self: Section

        @param currIndex: The index of the boat for which the next position is checked.
        @type currIndex: int

        @param step: The step value for boat movement based on its strategy.
        @type step: int

        This method checks if there is a next position for the boat at the specified index based on a 'max' strategy. It considers the boat's position within the section, its step value, and determines whether it can move to the next position within the section or to the next river part.

        @return: True if there is a next position for the boat, False otherwise.
        @rtype: bool
        """
        # get curr boat
        curr_boat = self.__collection[currIndex]

        # if we are at the last index of this section, check next riverPart
        if (currIndex == len(self.__collection) - 1):
            # get next element
            nextElement = self.nextPart

            # if nextElement is None, we have finished our iteration
            if (nextElement is None):
                return False

            # if lock, check if there is a boat in it already
            if (nextElement.type == 'lock'):
                nextLock = nextElement

                # if there is a boat in it already
                if (nextLock.hasBoat()):
                    return True

                #print(nextLock)
                #print(nextLock.level)

                # no boat BUT level is not zero return True
                # this means its not ready to accept a boat
                if (nextLock.level != 0):
                    return True

                else:
                    return False

            # if section, check if there is a boat at the beginning
            elif (nextElement.type == 'section'):
                if (nextElement.hasBoatBegin()):
                    return True
                return False

            # we are at the last section and last element in that section, we can exit
            else:
                return False

        # we are not at the last element of the section
        # check if we can move to the next element within this section
        else:
            # if currIndex + step is greater than the length of our section, then
            # we place the boat at the end of the section and then in the lock/out of river
            # for the next update
            if (currIndex + step > len(self.__collection) - 1):
                # update the boat step to equal last index in collection
                curr_boat.step = len(self.__collection) - 1 - currIndex

                # however, we may have a boat in front of us before we get there
                # or at that position
                temp = currIndex
                while (temp < currIndex + curr_boat.step):
                    temp += 1
                    # alas we has encountered a boat
                    if (self.__collection[temp] != None):
                        curr_boat.step = temp - currIndex - 1
                        break

            else:
                curr_boat.step = step
                # same here
                temp = currIndex
                maxStep = currIndex + curr_boat.step
                while (temp < maxStep):
                    temp += 1
                    # alas we has encountered a boat
                    if (self.__collection[temp] != None):
                        curr_boat.step = temp - currIndex - 1
                        break
