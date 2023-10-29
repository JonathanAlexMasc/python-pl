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
        self.__upper = RiverIterMain(self.__river)
        self.__lower = self.__upper.getLowerRiver()

    def addDefaultBoat(self, boat):
        #get first section
        init_section = self.__river[0]

        #if there's a boat already, make a new boat to
        #increment the serial number then do not use it
        if (not init_section.hasBoatBegin()):
            #add boat to this section
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

        #GRADING: TO_STR
        print(boat1)
        print(section1)
        print(lock1)
        print(system)

    def updateOne(self):
        newRiver = []
        #call iterator to update river
        for i in UpdateRiverIterator(self.__river):
            newRiver.append(i)

        self.__river = newRiver

        #update upper and lower
        self.__upper = RiverIterMain(self.__river)
        self.__lower = self.__upper.getLowerRiver()

    def getSectionDetails(self):
        index = 1
        for sec in SectionDetailsIterator(self.__river):
            currSection = sec
            if (currSection):
                print('Section ' + str(index))
                print('Boats: ' + str(currSection.getNumBoats()) + \
                      ' Flow: ' + str(currSection.getFlow()))
                print()
                index += 1




    def __str__(self):
        lowerRiverString = ''
        upperRiverString = ''
        for i in self.__upper:
            upperRiverString += i
        for j in self.__lower:
            lowerRiverString += j

        return upperRiverString + '\n' + lowerRiverString

