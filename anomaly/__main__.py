import argparse
from .calculator import Calculator
from .calculator import FUNCTIONS
from .common import *

def main():

    parser = argparse.ArgumentParser(description= """A basic RPN calculator. CLI functionality can be obtained by passing a space
                                     seperated series of numbers or operators as arguments.""")

    parser.add_argument('arguments', nargs = "*")
    parser.add_argument("-l", "--list", help = "Displays a list of possible operations", action = 'store_true')
    args = parser.parse_args()

    calc = Calculator()

    if args.list:
        for entry in FUNCTIONS.keys():
            print(entry)
        return

    for value in args.arguments:
        if is_float(value) == True:
            calc.receive(value)
            calc.enter()
        else:
            calc.receive(value)
    
    print(calc.get_stack())

if __name__ == "__main__":
    main()