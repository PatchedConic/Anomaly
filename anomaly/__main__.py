import argparse
from .calculator import Calculator
from .calculator import FUNCTIONS
from .common import *
# from .GUI import GUI_Application
from .TUI import TUI_App
def main():

    parser = argparse.ArgumentParser(description= """A basic RPN calculator. CLI functionality can be obtained by passing a space
                                     seperated series of numbers or operators as arguments.""")

    parser.add_argument('arguments', nargs = "*")
    parser.add_argument("-l", "--list", help = "Displays a list of possible operations", action = 'store_true')
    parser.add_argument("-d", "--degrees", help = "Set calculator to degree mode.", action = "store_true")
    parser.add_argument("-g", "--GUI", help = "Run GUI", action = "store_true")
    parser.add_argument("-t", "--TUI", action = "store_true")
    args = parser.parse_args()

    calc = Calculator()

    if args.list:
        for entry in FUNCTIONS.keys():
            print(entry)
        return
    
    if args.degrees:
        calc.mode = 'degrees'

    if not args.GUI and not args.TUI:
        for value in args.arguments:
            if is_float(value) == True:
                calc.receive(value)
                calc.enter()
            else:
                calc.receive(value)
        
        print(calc.get_stack())

    if args.GUI:
        # app = GUI_Application(calc)
        # app.window.mainloop()
        return
    if args.TUI:
        app = TUI_App(calc)
        app.run()
        print(calc.stack)
        print(calc.buffer)
        print(calc.history)
if __name__ == "__main__":
    main()