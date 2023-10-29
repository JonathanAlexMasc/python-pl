import traceback
from RiverSystem import RiverSystem
from RiverPart import Boat
from RiverPart import Section
from RiverPart import Lock

class InputOutOfRangeError(Exception):
    def __init__(self):
        super().__init__("Input an option in the range 0-7")

def cleanInput(prompt):
    result = input(prompt)
    # strips out blank lines in input
    while result == '':
        result = input( )

    return result


def main( ):
    mySystem = RiverSystem()
    print(mySystem)

    menu = "\n" \
           "1) Add Default Boat\n" \
           "2) Update One Tick\n" \
           "3) Update X Ticks\n" \
           "4) Show Section Details\n" \
           "5) Add Boat\n" \
           "6) Make Tester\n" \
           "7) Make New Simulator\n" \
           "0) Quit\n"

    choice = -1
    while choice != 0:
        try:
            print( menu )
            choice = int(cleanInput( "Choice:> " ))

            #out of range
            if (choice < -1 or choice > 7):
                raise InputOutOfRangeError()

            # add default box
            if choice == 1:
                boat = Boat()
                #add a default boat at the left end of the river
                mySystem.addDefaultBoat(boat)
                print(mySystem)

            # update one time
            elif choice == 2:
                mySystem.updateOne()
                print(mySystem)

            # update X number of times
            elif choice == 3:
                updateCount = int(cleanInput( "How many updates:> " ))
                for i in range(updateCount):
                    mySystem.updateOne()
                    print(mySystem)

            # print out station details
            elif choice == 4:
                mySystem.getSectionDetails()

            # make a new box of any size
            elif choice == 5:
                print( "TODO" )

            # make new system
            elif choice == 6:
                print( "TODO" )

            # make new system
            elif choice == 7:
                print( "TODO" )

            # debug/check for D in SOLID in __str__
            elif choice == -1:
                mySystem.handleSOLID()


            elif choice == 0 or '0':
                choice = 0
            else:
                raise Exception("Please ")
        except ValueError:
            print("Please, input a positive integer")
        except InputOutOfRangeError as e:
            print(e)

if __name__ == '__main__':
    main( )
