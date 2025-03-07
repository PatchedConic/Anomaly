import math
from .common import *


class Calculator:
    """
    The core calculator class.
    
    Methods:
        get_stack(None): returns the calculator's stack as a list.
        
        push(*values): pushes *values to the calculator's stack.

        pop(a): pops the value at index a from the calculator's stack and returns
        it.

        peek(a): returns the value in the calculators stack at index a without
        altering the stack.

        enter(): pushes the value on the calculator's buffer onto the stack.

        add_listener(function): adds function to the calculator's listeners to be called
        during an update.

        get_buffer(): returns the calculator's current buffer string.

        notify_listeners(): calls all functions in the calculator's listeners list.

        receive(signal): takes a char or operand and adds it to the buffer string or 
        calls the relevant operator as appropriate.
        """
    def __init__(self):
        self.stack = []
        self.buffer = ""
        self.listeners = []
        self.mode = 'radians'
        self.history = []

    def get_stack(self) -> list:
        """
        Return stack as list

        Args: 
            none
        
        Returns:
            list: calculator stack
        """
        return self.stack

    def push(self, *values: float) -> None:
        """
        Add values to stack.
        
        Args:
            *float: value to add to stack
            
        Returns:
            none
        """
        for value in values:    #Loop through arguments
            try:
                self.stack.insert(0, float(value))  #Add value to stack
                self.history.append(str(value))
            except:   #If not valid, do nothing
                pass
        return
        
    def pop(self, position: int = 0) -> float | None:
        """
        Pop value from stack

        Args:
            int: index to pop. Defaults to 0.

        Returns:
            float: value in stack at position specified.
        """
        try:
            return self.stack.pop(position) #If stack position exists, pop and return
        except IndexError:  #If index does not exist, do nothing
            return None
        
    def enter(self) -> None:
        """
        Push buffer onto stack.

        Args:
            none
        
        Returns:
            none
        """
        if self.buffer != "":   #Check that buffer is not empty
            self.push(float(self.buffer))   #Push buffer to stack
            self.buffer = ""    #Clear buffer
            return
        
        return
        
    def peek(self, position: int = 0) -> str:
        """
        Peek at stack.

        Args:
            position (int): index of stack. Defaults to 0.

        Returns:
            float: value of stack at position.
        """
        if self.buffer != "":
            if position > 0:
                try: 
                    return str(self.stack[position-1])
                except IndexError:
                    return "---"
            return self.buffer
        
        try:
            return(str(self.stack[position]))
        except IndexError:
            return "---"

    def get_buffer(self) -> str | None:
        """
        Return buffer.

        Args:
            none
        
        Returns:
            string: Buffer string
        """
        if self.buffer != "":   #Return buffer if it is not empty
            return self.buffer
        else:   #Else return first element in stack
            return str(self.peek())
        
    def add_listener(self, func_pointer: object) -> None:
        """
        Add listener function.

        Args:
            func_pointer (function): function pointer.

        Returns:
            none.
        """
        self.listeners.append(func_pointer) #Append function_pointer to listeners
        return
    
    def notify_listeners(self) -> None:
        """
        Call listener functions.

        Args:
            none
        
        Returns:
            none
        """
        for i in self.listeners:    #Loop through listeners list
            i() #Call each function
        return
    
    def receive(self, *signals: str) -> None:
        """
        Receive a char or operator and compute.

        Args:
            *signals (str): Char or operator string.

        Returns:
            None

        Raises:
            Exception: invalid char or operator.
        """
        for signal in signals:
            if is_float(signal) == True or signal == '.':
                if "." in signal:
                    if "." not in self.buffer:
                        self.buffer += signal
                    else:
                        pass
                else:
                    self.buffer += signal
                self.notify_listeners()
                return
            elif signal in FUNCTIONS.keys():
                try:
                    FUNCTIONS[signal](self)
                    self.notify_listeners()
                except ValueError:
                    self.history.append("Math domain error")
                    self.buffer = ""
                    self.notify_listeners()
                return
            else:
                raise Exception(f"Invalid signal sent: {signal}")
        

def backspace(calc: Calculator) -> None:
    """
    Delete char from buffer.
    
    Args:
        calc (Calculator): active calculator
    """
    try:
        calc.buffer = calc.buffer[:-1]        
    except IndexError:
        pass
    return

def sum(calc: Calculator) -> None:
    """
    Add two values in stack.

    Args:
        calc (Calculator): Active calculator
    """
    if calc.buffer != "":
        calc.enter()

    if len(calc.get_stack()) < 2:
        return None
    
    calc.history.append("sum")
    a = calc.pop(1)
    b = calc.pop()

    if a is not None and b is not None:
        calc.push(a+b)
        return
    
    return

def subtract(calc: Calculator) -> None:
    """
    Subtract two values in stack.

    Args:
        calc (Calculator): Active calculator
    """
    if calc.buffer != "":
        calc.enter()

    if len(calc.get_stack()) < 2:
        return
    
    calc.history.append("subtract")
    a = calc.pop(1)
    b = calc.pop()

    if a is not None and b is not None:
        calc.push(a-b)
        return
    
    return

def multiply(calc: Calculator) -> None:
    """
    Multiply two values in stack.

    Args:
        calc (Calculator): Active calculator
    """
    if calc.buffer != "":
        calc.enter()

    if len(calc.get_stack()) < 2:
        return
    
    calc.history.append("multiply")

    a = calc.pop(1)
    b = calc.pop()
    if a != None and b != None:
        calc.push(a*b)
        return
    return
    
def divide(calc: Calculator) -> None:
    """
    Divide two values in stack.

    Args:
        calc (Calculator): Active calculator
    """
    if calc.buffer != "":
        calc.enter()

    if len(calc.get_stack()) < 2:
        return
    
    calc.history.append("divide")

    a = calc.pop(1)
    b = calc.pop()

    if a != None and b != None:
        if b != math.nan:
            try:
                calc.push(a/b)
                return
            except ZeroDivisionError:
                calc.push(math.nan)
                return
        else:
            calc.push(math.nan)
            return

    return

def power(calc: Calculator) -> None:
    """
    Raise value to power
    
    Args:
        calc (Calculator): Active calculator"""
    if calc.buffer != "":
        calc.enter()
    
    if len(calc.get_stack()) < 2:
        return
    
    calc.history.append("^")

    a = calc.pop(1)
    b = calc.pop()
    if a != None and b != None:
        calc.push(math.pow(a, b))
        return
    
    return

def negate(calc: Calculator) -> None:
    """
    Negate buffer or stack value.

    Args:
        calc (Calculator): Active calculator
    """

    if calc.buffer != "":
        if calc.buffer.startswith("-"):
            calc.buffer = "-" + calc.buffer
            return
        calc.buffer =  calc.buffer.lstrip("-")
        return
    
    calc.history.append("negate")

    a = calc.pop()
    if a is not None:
        calc.push(-1*a)
        return
    
    return

    
def swap(calc: Calculator) -> None:
    """
    Swap stack values.

    Args:
        calc (Calculator): active calculator
    """
    if calc.buffer != "":
        calc.enter()

    if len(calc.get_stack()) < 2:
        return
    
    calc.history.append("swap")

    a = calc.pop(1)
    b = calc.pop()
    if a != None and b != None:
        calc.push(b, a)
        return
    else:
        return
    
def sqrt(calc: Calculator) -> None:
    """Take the square root.
    
    Args:
        calc (Calculator): active calculator"""
    if calc.buffer != "":
        calc.enter()
    if len(calc.get_stack()) < 1:
        return
    
    calc.history.append("sqrt")

    a = calc.pop()
    if a != None:
        calc.push(math.sqrt(a))
        return
    return

def square(calc: Calculator) -> None:
    """
    Square value.

    Args:
        calc (Calculator): active calculator
    """
    if calc.buffer != "":
        calc.enter()

    if len(calc.get_stack()) < 1:
        return

    calc.history.append("square")

    a = calc.pop()
    if a != None:
        calc.push(math.pow(a, 2))
        return
    return
        
def pi(calc: Calculator) -> None:
    """
    Push Pi onto stack.

    Args:
        calc (Calculator): active calculator
    """
    if calc.buffer != "":
        calc.enter()

    calc.push(math.pi)
    return

def nat_exp(calc: Calculator) -> None:
    """
    Push e onto stack.

    Args:
        calc (Calculator): active calculator
    """
    if calc.buffer != "":
        calc.enter()

    calc.push(math.e)
    return

def invert(calc: Calculator) -> None:
    """
    Invert top value in stack.

    Args:
        calc (Calculator): active calculator
    """
    if calc.buffer != "":
        calc.enter()
    if len(calc.get_stack()) < 1:
        return
    
    calc.history.append("invert")

    a = calc.pop()
    if a != None:
        calc.push(1/a)
        return
    return
    
def sin(calc: Calculator) -> None:
    """
    Take the sin of value.

    Args:
        calc (Calculator): active calculator
    """
    if calc.buffer != "":
        calc.enter()

    if len(calc.get_stack()) < 1:
        return
    
    calc.history.append("sin")

    a = calc.pop()
    if a != None:
        if calc.mode == 'radians':
            calc.push(math.sin(a))
            return
        calc.push(math.sin(a*2*math.pi/360))
        return
    return
    
def cos(calc: Calculator) -> None:
    """
    Take the cos of value.

    Args:
        calc (Calculator): active calculator
    """
    if calc.buffer != "":
        calc.enter()

    if len(calc.get_stack()) < 1:
        return
    
    calc.history.append("cos")

    a = calc.pop()
    if a != None:
        if calc.mode == 'radians':
            calc.push(math.cos(a))
            return
        calc.push(math.cos(a*2*math.pi/360))
        return
    return
    
def tan(calc: Calculator) -> None:
    """
    Take the tab of value.

    Args:
        calc (Calculator): active calculator
    """
    if calc.buffer != "":
        calc.enter()

    if len(calc.get_stack()) < 1:
        return
        
    calc.history.append("tan")

    a = calc.pop()
    if a != None:
        if calc.mode == 'radians':
            calc.push(math.tan(a))
            return
        calc.push(math.tan(a*2*math.pi/360))
        return
    return

def asin(calc: Calculator) -> None:
    """
    Take the asin of value.

    Args:
        calc (Calculator): active calculator
    """
    if calc.buffer != "":
        calc.enter()

    if len(calc.get_stack()) < 1:
        return
        
    calc.history.append("asin")

    a = calc.pop()
    if a != None:
        if calc.mode == 'radians':
            calc.push(math.asin(a))
            return
        calc.push(math.asin(a)*360/(2*math.pi))
        return
    
    return
    
def acos(calc: Calculator) -> None:
    """
    Take the acos of value.

    Args:
        calc (Calculator): active calculator
    """
    if calc.buffer != "":
        calc.enter()

    if len(calc.get_stack()) < 1:
        return
        
    calc.history.append("acos")

    a = calc.pop()
    if a != None:
        if calc.mode == 'radians':
            calc.push(math.acos(a))
            return
        calc.push(math.acos(a)*360/(2*math.pi))
        return
    return
    
def atan(calc: Calculator) -> None:
    """
    Take the atan of value.

    Args:
        calc (Calculator): active calculator
    """
    if calc.buffer != "":
        calc.enter()

    if len(calc.get_stack()) < 1:
        return
        
    calc.history.append("atan")

    a = calc.pop()
    if a != None:
        if calc.mode == 'radians':
            calc.push(math.atan(a))
            return
        calc.push(math.atan(a)*360/(2*math.pi))
        return
    return
    
def ln(calc: Calculator) -> None:
    """Take the natural log of value.
    
    Args:
        calc (Calculator): active calculator"""
    if calc.buffer != "":
        calc.enter()

    if len(calc.get_stack()) < 1:
        return
    
    calc.history.append("ln")

    a = calc.pop()
    if a is not None:
        calc.push(math.log(a))
        return
    return 

def enter(calc: Calculator) -> None:
    if calc.buffer != "":
        calc.enter()
        return
    
    return

def clear(calc: Calculator) -> None:
    if calc.buffer != "":
        calc.buffer = ""
        return
    calc.stack = []
    return

FUNCTIONS = {
    "sum": sum,
    "+": sum,
    "subtract": subtract,
    "-": subtract,
    "multiply": multiply,
    "x": multiply,
    "divide": divide,
    "/": divide,
    "power": power,
    "negate": negate,
    "n": negate,
    "swap": swap,
    "s": swap,
    "sqrt": sqrt,
    "square": square,
    "pi": pi,
    "natural_exponent": nat_exp,
    "e": nat_exp,
    "invert": invert,
    "i": invert,
    "sin": sin,
    "cos": cos,
    "tan": tan,
    "asin": asin,
    "acos": acos,
    "atan": atan,
    "ln": ln,
    "enter": enter,
    "clear": clear,
    "backspace": backspace
}