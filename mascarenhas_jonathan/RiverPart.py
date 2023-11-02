from abc import ABC, abstractmethod


class RiverPart(ABC):
    @abstractmethod
    def __init__(self):
        self.nextPart = None
        self.type = ''

    @abstractmethod
    def __str__(self):
        pass


class Boat(RiverPart):
    # Class variable to keep track of the next available ID
    next_id = 1

    def __init__(self, power=1):
        super().__init__()
        self.__id = Boat.next_id
        Boat.next_id += 1
        self.__power = power
        self.__str = '⛴'
        self.type = 'boat'
        self.step = 1
        self.strategy = 'steady'

    def __str__(self):
        return self.__str

    def getID(self):
        return self.__id

    def getPower(self):
        return self.__power


class Section(RiverPart):
    def __init__(self, length, flow):
        super().__init__()
        self.__length = length
        self.__flow = flow
        self.__collection = [None] * self.__length
        self.type = 'section'
        self.lastSection = False

    def __str__(self):
        sectionStr = ''
        for i in self.__collection:
            if (i == None):
                sectionStr += '〜〜〜'
            else:
                sectionStr += '⛴〜〜'

        return sectionStr

    def hasBoatBegin(self):
        if (self.__collection[0]):
            return True
        return False

    def hasBoatEnd(self):
        if (self.__collection[-1]):
            return True
        return False

    def addBoat(self, boat):
        # add a boat to the beginning of the river/section
        self.__collection[0] = boat

    def getEndBoat(self):
        return self.__collection[-1]

    def moveBoat(self, atIndex):
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
        return self.__length

    def getFlow(self):
        return self.__flow

    def getCollection(self):
        return self.__collection

    def setCollection(self, newCollection):
        self.__collection = newCollection

    def getNumBoats(self):
        count = 0
        for i in self.__collection:
            if (i):
                count += 1
        return count

    # returns True if section has a boat at given index
    def hasBoat(self, currIndex):
        if (self.__collection[currIndex] != None):
            return True
        return False

    # function that takes current index and returns True if NEXT index
    # has a boat and false otherwise
    def hasNext(self, currIndex):
        # check current boat's strategy
        curr_boat = self.__collection[currIndex]
        step = curr_boat.getPower() - self.getFlow()

        if (curr_boat.strategy == 'steady'):
            self.hasNextSteady(currIndex)
        else:
            # get "step" for the boat
            self.hasNextMax(currIndex, step)

    def hasNextSteady(self, currIndex):
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
                print(nextLock)
                print(nextLock.level)
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

    def hasNextMax(self, currIndex, step):
        # get curr boat
        curr_boat = self.__collection[currIndex]

        # max step is

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

                print(nextLock)
                print(nextLock.level)

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


class Lock(RiverPart):
    def __init__(self, depth):
        super().__init__()
        self.depth = depth
        self.__collection = [None]
        self.__str = '_X( ' + str(self.depth) + ')_'
        self.type = 'lock'
        self.fillBehavior = 'none' # can be 'basic' 'fast-fill'
        self.level = 0

    def __str__(self):
        # if boat
        if (self.__collection[0] == None):
            return '_X( ' + str(self.depth) + ')_'

        else:
            return '_⛴( ' + str(self.depth) + ')_'

    def addBoat(self, boat):
        self.__collection[0] = boat

    def hasBoat(self):
        if (self.__collection[0]):
            return True
        return False

    def getBoat(self):
        return self.__collection[0]

    def removeBoat(self):
        self.__collection[0] = None

    def getDepth(self):
        return self.depth

    def getCollection(self):
        return self.__collection

    # returns True if there is a boat next, false otherwise
    def hasNext(self, temp1):
        # get next section
        nextSection = self.nextPart

        # next part is another section or we are
        # emptying out
        if (nextSection is None):
            return False

        # if boat at the beginning of the section
        if (nextSection.hasBoatBegin()):
            return True

        # no boat
        return False

    def moveBoat(self, temp):
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



        else:
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
