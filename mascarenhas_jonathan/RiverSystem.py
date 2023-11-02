from RiverIterator import RiverIterMain
from RiverIterator import UpdateRiverIterator
from RiverIterator import SectionDetailsIterator
from RiverPart import Boat
from RiverPart import Section
from RiverPart import Lock


class RiverSystem:
    def __init__(self):
        self.__index = -1
        self.__river = [Section(6, 0), Lock(0), Section(3, 1)]

        for i in range(len(self.__river) - 1):
            self.__river[i].nextPart = self.__river[i + 1]

        # last section is the last section
        self.__river[-1].lastSection = True

        self.__upper = RiverIterMain(self.__river)
        self.__lower = self.__upper.getLowerRiver()

    def addDefaultBoat(self, boat):
        # get first section
        init_section = self.__river[0]

        # if there's a boat already, make a new boat to
        # increment the serial number then do not use it
        if (not init_section.hasBoatBegin()):
            # add boat to this section
            init_section.addBoat(boat)

    def handleSOLID(self):
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
        newRiver = []

        # call iterator to update river
        for i in UpdateRiverIterator(self.__river):
            newRiver.insert(0, i)

        self.__river = newRiver

        # update upper and lower
        self.__upper = RiverIterMain(self.__river)
        self.__lower = self.__upper.getLowerRiver()

    def getSectionDetails(self):
        index = 1
        for sec in SectionDetailsIterator(self.__river):
            if (sec is not None):
                print('Section ' + str(index))
                print('Boats: ' + str(sec.getNumBoats()) + \
                      ' Flow: ' + str(sec.getFlow()))
                print()
                index += 1


    def addCustomBoat(self, enginePower, travelMethod):
        # make new boat
        newBoat = Boat(enginePower)
        # set boat strategy
        if (travelMethod == 2):
            newBoat.strategy = 'max'

        # add boat to beginning
        self.addDefaultBoat(newBoat)

    def makeTesterRiver(self):
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



    def __str__(self):
        lowerRiverString = ''
        upperRiverString = ''
        for i in self.__upper:
            upperRiverString += i
        for j in self.__lower:
            lowerRiverString += j

        return upperRiverString + '\n' + lowerRiverString
