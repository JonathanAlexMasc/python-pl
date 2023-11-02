'''
CHECKLIST


Grading tags in for all lines marked with *			__✓_

Tierless str meets D in SOLID (hidden test)*			__✓_
Check if above is done, but not its test was not reached	__(I have finished all the tests)_

1. Initial Show system\Got it compiling
Menu\initial system working					__✓_
Bad input handled						__✓_

2. Add Default
Added and shown properly					_✓__
Second+ item ignored						__✓_

3. Basic Update (single)
Moves along section						__✓_
String format correct						__✓_
Iterator used*							__✓_

4. Basic Update (multiple)					__✓_

5. Multi Update
Updates correctly						_✓__
Bad input handled						_✓__

6. Show details
Shows details properly 						__✓_
Iterator used*							__✓_

6. Add user specified item
Basic movement still works					_✓__
Powered works							__✓_
No passing							__✓_

7. Tester part 1
Boats works up to second lock 					__✓_
Formatting correct 						_✓__

8. Tester part 2
Boats works up to end						_✓__
Strategy pattern for basic fill*				_✓__
Strategy pattern for fast empty*				_✓__

9. Custom belt **
String formatting correct					_✓__
Everything still works 						_✓__
Bad input handled 						_✓__


A491-ACF0

'''




from RiverSystem import RiverSystem
from Boat import Boat


class InputOutOfRangeError(Exception):
    """
    Custom exception class for input out of range error.

    This exception is raised when an input option is provided outside the range of 0 to 7.

    @raises InputOutOfRangeError: An exception is raised with an error message when input is out of range.
    """
    def __init__(self):
        super().__init__("Input an option in the range 0-7")


class SpecialException(Exception):
    """
    Custom exception class for a special exception.

    This exception is raised when a specific condition is met and it is not possible to accept the provided value.

    @raises SpecialException: An exception is raised with an error message when the condition is met.
    """
    def __init__(self):
        super().__init__("Cannot accept value")


class TravelMethodError(Exception):
    """
    Custom exception class for travel method input error.

    This exception is raised when a travel method option is provided outside the valid range of 1 to 2.

    @raises TravelMethodError: An exception is raised with an error message when the input is out of range.
    """
    def __init__(self):
        super().__init__("Input an option in the range 1-2")


def cleanInput(prompt):
    result = input(prompt)
    # strips out blank lines in input
    while result == '':
        result = input()

    return result


def main():
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
            print(menu)
            choice = int(cleanInput("Choice:> "))

            # out of range
            if choice < -1 or choice > 7:
                raise InputOutOfRangeError()

            if choice is None:
                break

            # add default box
            if choice == 1:
                boat = Boat()
                # add a default boat at the left end of the river
                mySystem.addDefaultBoat(boat)
                print(mySystem)

            # update one time
            elif choice == 2:
                mySystem.updateOne()
                print(mySystem)

            # update X number of times
            elif choice == 3:
                updateCount = int(cleanInput("How many updates:> "))
                for i in range(updateCount):
                    mySystem.updateOne()
                    print(mySystem)

            # print out station details
            elif choice == 4:
                mySystem.getSectionDetails()

            # make a new box of any size
            elif choice == 5:
                enginePower = int(cleanInput("What engine power:> "))
                travelMethod = int(cleanInput("What travel method. (1) Steady or (2) Max :> "))

                if (travelMethod < 1 or travelMethod > 2):
                    raise TravelMethodError()

                mySystem.addCustomBoat(enginePower, travelMethod)
                print(mySystem)
            # make new system
            elif choice == 6:
                mySystem.makeTesterRiver()
                print(mySystem)

            # make new system
            elif choice == 7:
                mySystem.setRiverEmpty()

                n = 'go'
                while (n != 'n'):
                    try:
                        option1 = int(cleanInput("Section (1) or Lock (2):> "))

                        if (option1 < 1 or option1 > 2):
                            raise TravelMethodError()

                        if (option1 == 1):
                            length = int(cleanInput("Length:> "))
                            flow = int(cleanInput("Flow:> "))
                            mySystem.addSection(length, flow)
                        else:
                            behavior = int(cleanInput("Fill behavior: None (1), Basic (2), or Fast Empty (3):> "))
                            if (behavior < 1 or behavior > 3):
                                raise SpecialException()

                            depth = int(cleanInput("Depth:> "))
                            mySystem.addLock(behavior, depth)

                    except TravelMethodError as t:
                        print(t)
                    except SpecialException as s:
                        print(s)
                    except ValueError:
                        print("Cannot accept value")

                    n = cleanInput("Add another component (n to stop):> ")

                mySystem.makeAssociations()
                print(mySystem)

            # debug/check for D in SOLID in __str__
            elif choice == -1:
                mySystem.handleSOLID()

            elif choice == 0 or '0' or None:
                choice = 0
            else:
                raise Exception("Please ")
        except ValueError:
            print("Please, input a positive integer")
        except InputOutOfRangeError as e:
            print(e)
        except TravelMethodError as e:
            print(e)
            print(mySystem)
        # except:
        # print(traceback.format_exc())


if __name__ == '__main__':
    main()
