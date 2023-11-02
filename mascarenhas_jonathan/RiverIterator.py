class RiverIterMain:
    """
    Iterator for a river representation.

    This iterator allows you to iterate over a river, producing a textual representation of each element in the river.

    @param river: The river to iterate over.
    @type river: River
    """
    def __init__(self, river):
        """
        Initialize the RiverIterMain iterator.

        @param river: The river to iterate over.
        @type river: River
        """
        self.__river = river

    def __iter__(self):
        """
        Initialize the iterator.

        @return: The iterator itself.
        """
        self.__index = -1
        return self

    def getLowerRiver(self):
        """
        Get an iterator for a lower river.

        @return: An iterator for a lower river.
        @rtype: idIterator
        """
        return idIterator(self.__river)

    def updateRiver(self):
        """
        Get an iterator to update the river.

        @return: An iterator to update the river.
        @rtype: UpdateRiverIterator
        """
        return UpdateRiverIterator(self.__river)

    def __next__(self):
        """
        Get the next element in the river.

        @return: A textual representation of the next element in the river.
        @rtype: str

        @raise StopIteration: When there are no more elements in the river.
        """
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
                lockInst = temp.getCollection()[0]
                if (lockInst == None):
                    riverStr += '_X( ' + str(temp.level) + ')_'
                else:
                    riverStr += '_⛴( ' + str(temp.level) + ')_'
            return riverStr
        except:
            raise StopIteration()


class idIterator:
    """
    Iterator for retrieving identifiers from a river representation.

    This iterator allows you to iterate over a river and retrieve identifiers or representations of elements.

    @param river: The river to iterate over.
    @type river: River
    """
    def __init__(self, river):
        """
        Initialize the idIterator.

        @param river: The river to iterate over.
        @type river: River
        """
        self.__river = river

    def __iter__(self):
        """
        Initialize the iterator.

        @return: The iterator itself.
        """
        self.__index = -1
        return self

    def __next__(self):
        """
        Get the next identifier or representation from the river.

        @return: The identifier or representation of the next element in the river.
        @rtype: str

        @raise StopIteration: When there are no more elements in the river.
        """
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
            # print(traceback.format_exc())
            raise StopIteration()



class UpdateRiverIterator:
    """
    Iterator for updating a river representation.

    This iterator allows you to iterate over a river and update its elements based on certain rules.

    @param river: The river to iterate over and update.
    @type river: River
    """
    def __init__(self, river):
        """
        Initialize the UpdateRiverIterator.

        @param river: The river to iterate over and update.
        @type river: River
        """
        self.__river = river

    # GRADING: ITER_ALL.
    def __iter__(self):
        """
        Initialize the iterator.

        @return: The iterator itself.
        """
        self.__riverIndex = len(self.__river)
        return self

    # GRADING: LOOP_ALL
    def __next__(self):
        """
        Update the next element in the river.

        @return: The updated element in the river.
        @rtype: RiverElement

        @raise StopIteration: When there are no more elements in the river to update.
        """
        try:
            self.__riverIndex -= 1

            # if riverIndex < 0, throw exception
            if (self.__riverIndex < 0):
                raise Exception

            # get river element
            riverElement = self.__river[self.__riverIndex]

            # update river element at each stage
            if (riverElement.type == 'lock' and (not riverElement.hasBoat()) and riverElement.level != 0):
                if (riverElement.fillBehavior == 'basic'):
                    riverElement.level -= 1
                    # print(riverElement.level)
                else:
                    riverElement.level -= 2
                    if (riverElement.level < 0):
                        riverElement.level = 0

            # get the collection for this riverELement
            elementCollection = riverElement.getCollection()

            # GRADING: LOOP_ALL - put a tag here too since I did not know which one was being referenced
            # loop backwards through the elements of the riverELement
            for i in range(len(elementCollection) - 1, -1, -1):
                # if the element is a boat, check if it can be moved forward
                if (elementCollection[i] != None):
                    if (not riverElement.hasNext(i)):
                        # move the boat
                        riverElement.moveBoat(i)

            return riverElement

        except:
            raise StopIteration()



class SectionDetailsIterator:
    """
    Iterator for retrieving details of river sections.

    This iterator allows you to iterate over a river and retrieve details of each section.

    @param river: The river to iterate over.
    @type river: River
    """
    def __init__(self, river):
        """
        Initialize the SectionDetailsIterator.

        @param river: The river to iterate over.
        @type river: River
        """
        self.__river = river

    # GRADING: ITER_RESTRICT.
    def __iter__(self):
        """
        Initialize the iterator.

        @return: The iterator itself.
        """
        self.__index = -1
        return self

    # GRADING: LOOP_RESTRICT
    def __next__(self):
        """
        Get the details of the next section in the river.

        @return: The details of the next section in the river.
        @rtype: RiverSection

        @raise StopIteration: When there are no more sections in the river.
        """
        try:
            self.__index += 1
            # if river part is a section, return
            riverPart = self.__river[self.__index]
            if (riverPart.type == 'section'):
                return riverPart

        except:
            raise StopIteration()


def getWave(num):
    """
    Get a wave representation based on the input number.

    Returns a wave representation string for a given number. If the number is a single-digit number (0-9), it returns '〜〜'.
    If the number is a two-digit number (10-99), it returns '〜'.

    :param num: The input number to determine the wave representation.
    :type num: int

    :return: The wave representation string.
    :rtype: str
    """

    if 0 <= num < 10:
        return '〜〜'
    elif 10 <= num <= 99:
        return '〜'


def create_dots_string(num):
    """
    Create a string of dots based on the input number.

    Returns a string of dots based on the input number. If the number is a single-digit number (0-9), it returns '......'.
    If the number is a two-digit number (10-99), it returns '.....'.

    :param num: The input number to determine the dots string.
    :type num: int

    :return: The dots string.
    :rtype: str
    """
    if 0 <= num < 10:
        return '......'
    elif 10 <= num <= 99:
        return '.....'

