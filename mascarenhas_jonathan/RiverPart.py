from abc import ABC, abstractmethod

class RiverPart(ABC):
    def __init__(self):
        pass

    def __str__(self):
        pass



class Boat(RiverPart):
    # Class variable to keep track of the next available ID
    next_id = 1
    def __init__(self, power=1, behavior=None):
        super().__init__()
        self.__id = Boat.next_id
        Boat.next_id += 1
        self.__power = power
        self.__str = '⛴'
        self.__behavior = behavior

    def __str__(self):
        return self.__str

    def getID(self):
        return self.__id

    def getType(self):
        return 'boat'

    def move(self):
        self.__behavior.move()



class Section(RiverPart):
    def __init__(self, length, flow):
        super().__init__()
        self.__length = length
        self.__flow = flow
        self.__collection = [None] * self.__length

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
        #add a boat to the beginning of the river/section
        self.__collection[0] = boat

    def getEndBoat(self):
        return self.__collection[-1]

    def getType(self):
        return 'section'

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



class Lock(RiverPart):
    def __init__(self, depth):
        super().__init__()
        self.__depth = depth
        self.__collection = [None]
        self.__str = '_X( ' + str(self.__depth) + ')_'

    def __str__(self):
        #if boat
        if (self.__collection[0] == None):
            return '_X( ' + str(self.__depth) + ')_'

        else:
            return '_⛴( ' + str(self.__depth) + ')_'

    def getType(self):
        return 'lock'

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
        return self.__depth

    def getCollection(self):
        return self.__collection

