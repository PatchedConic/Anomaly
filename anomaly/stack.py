class Stack():
    def __init__(self):
        self.stack = [] # The stack list object will contain the stack entries in string format.

    def add_digit(self, *digits):
        "Adds a digit to the end of the number currently on top of the stack"
        for digit in digits:    #Loop through each digit passed to the function
            if len(self.stack) < 1: self.add_number()   #Checks that the stack is not currently empty, and creates a new number if it is
            if digit != '.':    #If the digit is not a decimal point, add it to the end of the number currently on top of the stack
                self.stack[-1] = self.stack[-1]+str(digit)
            elif digit == '.' and '.' not in self.stack[-1]:    #If the digit is a decimal point, check to make sure there isn't already a decimal point before adding it to the number
                self.stack[-1] = self.stack[-1]+str(digit)
            else: pass

    def add_number(self, *arg):
        "Adds a number or numbers to the top of the stack on a first in, last out basis"
        try:
            for i in arg:   #Append each number to the stack in the list of numbers passed to the function
                self.stack.append(str(i))
            self.stack.append('')
        except ValueError:
            pass

    def pop(self):
        "Pops the top number off the stack and returns it"
        try:
            if self.stack[-1] == '': self.stack.pop()   #Check to make sure that the current number isn't blank
            return self.stack.pop() #Pop and return the number from the top of the stack.
        except:
            return None

    def delete_digit(self):
        "Deletes the trailing digit from the top number in the stack"
        if self.stack[-1] != '':    #Check to make sure that the current number isn't blank
            self.stack[-1] = self.stack[-1][:len(self.stack[-1])-1] #Strip the trailing digit from the current number
        else:
            pass

    def clear(self):
        "Clears the current number on the stack, or the entire stack if the current number is a blank"
        try:
            if self.stack[-1] != '':    #If there is a current number, clear the current number
                self.stack[-1] = ''
            elif self.stack[-1] == '':  #If there is not a current number, clear the entire stack
                self.stack = []
            else:
                pass
        except IndexError:
            pass
