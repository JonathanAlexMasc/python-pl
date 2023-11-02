# from abc import ABC, abstractmethod
#
# class BoatMovementStrategy(ABC):
#     @abstractmethod
#     def moveBoat(self, atIndex):
#         pass
#
# class MoveSteady(BoatMovementStrategy):
#     def moveBoat(self, atIndex):
#         # check if we are the last section
#         if (self.lastSection):
#             # check if last index of last section
#             if (atIndex == len(self.__collection) - 1):
#                 # just set current index to None
#                 self.__collection[atIndex] = None
#
#             # not last index
#             else:
#                 # set atIndex + step to atIndex
#                 self.__collection[atIndex + step] = self.__collection[atIndex]
#
#                 # set current index to None
#                 self.__collection[atIndex] = None
#
#         # not at the last section
#         else:
#             # check if we are the last index of this section
#             if (atIndex == len(self.__collection) - 1):
#                 # move to the next riverPart (not sure if this should be split up for lock and section)
#
#                 # get next riverPart
#                 nextRiverPart = self.nextPart
#
#                 # addBoat to the next riverPart
#                 nextRiverPart.addBoat(self.__collection[atIndex])
#
#                 # remove boat from current Section at 'atIndex'
#                 self.__collection[atIndex] = None
#
#             # not last index, move to next index
#             else:
#                 # next index could be
#
#
#                 # set atIndex + step to atIndex
#                 self.__collection[atIndex + step] = self.__collection[atIndex]
#
#                 # set current index to None
#                 self.__collection[atIndex] = None
#
# class MoveMaxSpeed(BoatMovementStrategy):
#     def moveBoat(self, section, atIndex, step=1):
#         # Implement logic to move a boat to the next river part (lock or section)
#         # ...
#         pass
