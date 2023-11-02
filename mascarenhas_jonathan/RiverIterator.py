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
            if (temp.type == 'section'):
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
                #print(temp.getDepth())
                #print(temp)
                #print("Lock Level is: ", temp.level)
                if (lockInst == None):
                    riverStr += '_X( ' + str(temp.level) + ')_'
                else:
                    riverStr += '_⛴( ' + str(temp.level) + ')_'
            return riverStr
        except:
            #print(traceback.format_exc())
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
            if (temp.type == 'section'):
                sectionArr = temp.getCollection()
                sectionStr = ''
                for i in sectionArr:
                    if (i == None):
                        sectionStr += '〜〜〜'
                    else:
                        # i == Boat
                        sectionStr += str(i.getID()) + getWave(i.getID())

                return sectionStr

            else:
                currLock = temp
                # if lock is empty
                if (currLock.hasBoat()):
                    return str(currLock.getBoat().getID()) + create_dots_string(currLock.getBoat().getID())
                return '.......'
        except:
            #print(traceback.format_exc())
            raise StopIteration()


# make an iterator for updating the contents of the river
# go from end to begining
class UpdateRiverIterator:

    def __init__(self, river):
        self.__river = river

    def __iter__(self):
        self.__riverIndex = len(self.__river)
        return self

    def __next__(self):
        try:
            self.__riverIndex -= 1

            # if riverIndex < 0, throw exception
            if (self.__riverIndex < 0):
                raise Exception

            # get river element
            riverElement = self.__river[self.__riverIndex]

            if (riverElement.type == 'lock' and (not riverElement.hasBoat()) and riverElement.level != 0):
                 if (riverElement.fillBehavior == 'basic'):
                     riverElement.level -= 1
                 else:
                     riverElement.level -= 2
                     if (riverElement.level < 0):
                         riverElement.level = 0

            # get the collection for this riverELement
            elementCollection = riverElement.getCollection()

            # loop backwards through the elements of the riverELement
            for i in range(len(elementCollection) - 1, -1, -1):
                # if the element is a boat, check if it can be moved forward
                if (elementCollection[i] != None):
                    # if boat can be moved forward, move it
                    if (not riverElement.hasNext(i)):
                        # move the boat
                        riverElement.moveBoat(i)

                # no boat but element is lock with non zero level
                # if (riverElement.type == 'lock' and not riverElement.hasBoat()):
                #     if (riverElement.level != 0):
                #         riverElement.level -= 1


            return riverElement

        except:
           #print(traceback.format_exc())
           raise StopIteration()


# iterator for getting section details
class SectionDetailsIterator:
    def __init__(self, river):
        self.__river = river

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        try:
            self.__index += 1
            # if river part is a section, return
            riverPart = self.__river[self.__index]
            if (riverPart.type == 'section'):
                return riverPart

        except:
            #print(traceback.format_exc())
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
