#! /bin/python3

import os
import sys
from pynput import keyboard

stack = []
operatorList = ["+","-","*","/", "q", "c", "d"]

def compute(keyPress):
    global stack
    if keyPress == "+":
        val1 = stack.pop()
        val2 = stack.pop()
        newVal = val2 + val1
        stack.append(newVal)
    elif keyPress == "-":
        val1 = stack.pop()
        val2 = stack.pop()
        newVal = val2 - val1
        stack.append(newVal)
    elif keyPress == "*":
        val1 = stack.pop()
        val2 = stack.pop()
        newVal = val2 * val1
        stack.append(newVal)
    elif keyPress == "/":
        val1 = stack.pop()
        val2 = stack.pop()
        newVal = val2 / val1
        stack.append(newVal)
    elif keyPress == "q":
        os.system('clear')
        sys.exit("Thanks for playing")
    elif keyPress == "c":
        stack = []
    elif keyPress == "d":
        stack.pop()
    else:
        pass


class cliOutput:
    def __init__(self):
        try:
            os.system('clear')
            for item in stack:
                print('->{}'.format(item))
        except:
            pass
    def update(self):
        os.system('clear')
        for item in stack:
            print('->{}'.format(item))        
        


def main():
    view = cliOutput()
    while True:
        newVal = input(">>")
        if newVal in operatorList:
            compute(newVal)
            view.update()
        elif newVal == '':
            view.update()
        elif float(newVal):
            stack.append(float(newVal))
            view.update()
        else:
            view.update()

if __name__ == "__main__":
    main()
