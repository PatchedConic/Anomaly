import argparse
from .calculator import Calculator

def is_float(*values: str) -> bool:
    for value in values:
        try:
            float(value)
            pass
        except: return False
    return True

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('arguments', nargs = "*")

    args = parser.parse_args()

    calc = Calculator()

    for value in args.arguments:
        if is_float(value) == True:
            calc.receive(value)
            calc.enter()
        else:
            calc.receive(value)
    
    print(calc.get_stack())

if __name__ == "__main__":
    main()