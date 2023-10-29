import traceback
from RiverPart import Section
class RiverIterMain:
    def __init__(self, river):
        self.__river = river

    def __iter__(self):
        self.__index = -1
        return self

    def getLowerRiver(self):
        return idIterator(self.__river)

    def updateRiver(self):
        return UpdateRiverIterator(self.__river)

    def __next__(self):
        try:
            self.__index += 1
            temp = self.__river[self.__index]
            riverStr = ''
            # if section, output waves or waves with boat
            if (temp.getType() == 'section'):
                sectionArr = temp.getCollection()
                for i in sectionArr:
                    if (i == None):
                        riverStr += '〜〜〜'
                    else:
                        riverStr += '⛴〜〜'

            # if not section then lock, return lock with/without boat in it
            else:
                # no boat
                lockInst = temp.getCollection()[0]
                if (lockInst == None):
                    riverStr += '_X( ' + str(temp.getDepth()) + ')_'
                else:
                    riverStr += '_⛴( ' + str(temp.getDepth()) + ')_'
            return riverStr
        except:
            raise StopIteration()


class idIterator:
    def __init__(self, river):
        self.__river = river

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        try:
            self.__index += 1
            temp = self.__river[self.__index]
            # if section, output waves or waves with boat
            if (temp.getType() == 'section'):
                sectionArr = temp.getCollection()
                sectionStr = ''
                for i in sectionArr:
                    if (i == None):
                        sectionStr += '〜〜〜'
                    else:
                        #i == Boat
                        sectionStr += str(i.getID()) + getWave(i.getID())

                return sectionStr

            else:
                currLock = temp
                #if lock is empty
                if (currLock.hasBoat()):
                    return str(currLock.getBoat().getID()) + create_dots_string(currLock.getBoat().getID())
                return '.......'
        except:
            raise StopIteration()

#make an iterator for updating the contents of the river
class UpdateRiverIterator:
    prevSection = None
    lockBoat = None

    def __init__(self, river):
        self.__river = river
        self.__newRiver = [None] * len(self.__river)

    def __iter__(self):
        self.__riverIndex = -1
        return self

    def __next__(self):
        try:
            self.__riverIndex += 1

            #get river element
            riverElement = self.__river[self.__riverIndex]

            #if riverPart is a section
            if (riverElement.getType() == 'section'):
                #update prevSection
                UpdateRiverIterator.prevSection = riverElement

                oldSectionCollection = riverElement.getCollection()
                newSectionCollection = [UpdateRiverIterator.lockBoat]

                #as we moved the lockBoat out, set it to None
                UpdateRiverIterator.lockBoat = None

                #update this section
                for i in range(len(oldSectionCollection) - 1):
                    newSectionCollection.append(oldSectionCollection[i])

                #make a new section with params of old section
                #but new collection
                newSection = Section(riverElement.getLength(), riverElement.getFlow())
                newSection.setCollection(newSectionCollection)

                return newSection

            #if riverPart is a lock
            if (riverElement.getType() == 'lock'):
                currLock = riverElement
                #if lock currently has a boat, assign it to class var LockBoat
                if (currLock.hasBoat()):
                    nextSection = self.__river[self.__riverIndex + 1]
                    UpdateRiverIterator.lockBoat = currLock.getBoat()
                    currLock.removeBoat()

                #if prevSection has a boat at the end, move it in
                if (UpdateRiverIterator.prevSection.hasBoatEnd()):
                    #add a boat to lock
                    currLock.addBoat(UpdateRiverIterator.prevSection.getEndBoat())

                return currLock

        except:
            #print( traceback.format_exc( ) )
            raise StopIteration()

#iterator for getting section details
class SectionDetailsIterator:
    def __init__(self, river):
        self.__river = river

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        try:
            self.__index += 1
            #if river part is a section, return
            riverPart = self.__river[self.__index]
            if (riverPart.getType() == 'section'):
                return riverPart


        except:
            raise StopIteration()

def getWave(num):
    if 0 <= num < 10:  # Check if the number is a single-digit number
        return '〜〜'
    elif 10 <= num <= 99:  # Check if the number is a two-digit number
        return '〜'

def create_dots_string(num):
    if 0 <= num < 10:  # Check if the number is a single-digit number
        return '......'
    elif 10 <= num <= 99:  # Check if the number is a two-digit number
        return '.....'
