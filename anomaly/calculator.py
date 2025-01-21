import math
import re

CHARS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]

class Calculator:
    def __init__(self):
        self.stack = []
        self.buffer = ""
        self.listeners = []

    def get_stack(self) -> list:
        return self.stack

    def push(self, *values: float) -> None:
        for value in values:
            if value != "":
                self.stack.insert(0, value)
            else:
                pass
        return
        
    def pop(self, position: int = 0) -> float | None:
        try:
            return self.stack.pop(position)
        except IndexError:
            return None
        
    def enter(self) -> None:
        if self.buffer != "":
            self.push(float(self.buffer))
            self.buffer = ""
            return
        else:
            return
        
    def peek(self, position: int = 0) -> float | None:
        try:
            return self.stack[position]
        except IndexError:
            return None
    
    def get_buffer(self) -> str | None:
        if self.buffer != "":
            return self.buffer
        else:
            return str(self.peek())
        
    def add_listener(self, func_pointer: object) -> None:
        self.listeners.append(func_pointer)
        return
    
    def notify_listeners(self) -> None:
        for i in self.listeners:
            i()
        return
    
    def receive(self, signal: str) -> None:
        if is_float(signal) == True:
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
            self.enter()
            FUNCTIONS[signal](self)
            self.notify_listeners()
            return
        else:
            raise Exception(f"Invalid signal sent: {signal}")
        
def is_float(*values: str) -> bool:
    for value in values:
        try:
            float(value)
        except ValueError:
            return False
    return True

def sum(calc: Calculator) -> None:
    a = calc.pop(1)
    b = calc.pop()
    if a != None and b != None:
        calc.push(a+b)
        return
    else:
        return
    
def subtract(calc: Calculator) -> None:
    a = calc.pop(1)
    b = calc.pop()
    if a != None and b != None:
        calc.push(a-b)
        return
    else:
        return

def multiply(calc: Calculator) -> None:
    a = calc.pop(1)
    b = calc.pop()
    if a != None and b != None:
        calc.push(a*b)
        return
    else:
        return
    
def divide(calc: Calculator) -> None:
    a = calc.pop(1)
    b = calc.pop()
    if a != None and b != None:
        calc.push(a/b)
        return
    else:
        return

def power(calc: Calculator) -> None:
    a = calc.pop(1)
    b = calc.pop()
    if a != None and b != None:
        calc.push(math.pow(a, b))
        return
    else:
        return

def negate(calc: Calculator) -> None:
    a = calc.pop()
    if a != None:
        calc.push(-1*a)
        return
    else:
        return
    
def swap(calc: Calculator) -> None:
    a = calc.pop(1)
    b = calc.pop()
    if a != None and b != None:
        calc.push(b, a)
        return
    else:
        return
    
def sqrt(calc: Calculator) -> None:
    a = calc.pop()
    if a != None:
        calc.push(math.sqrt(a))
        return
    else:
        return

def square(calc: Calculator) -> None:
    a = calc.pop()
    if a != None:
        calc.push(math.pow(a, 2))
        return
    else: 
        return
        
def pi(calc: Calculator) -> None:
    calc.push(math.pi)
    return

def nat_exp(calc: Calculator) -> None:
    calc.push(math.e)
    return

def invert(calc: Calculator) -> None:
    a = calc.pop()
    if a != None:
        calc.push(1/a)
        return
    else:
        return
    
def sin(calc: Calculator) -> None:
    a = calc.pop()
    if a != None:
        calc.push(math.sin(a))
        return
    else:
        return
    
def cos(calc: Calculator) -> None:
    a = calc.pop()
    if a != None:
        calc.push(math.cos(a))
        return
    else:
        return
    
def tan(calc: Calculator) -> None:
    a = calc.pop()
    if a != None:
        calc.push(math.tan(a))
        return
    else:
        return

def asin(calc: Calculator) -> None:
    a = calc.pop()
    if a != None:
        calc.push(math.asin(a))
        return
    else:
        return
    
def acos(calc: Calculator) -> None:
    a = calc.pop()
    if a != None:
        calc.push(math.acos(a))
        return
    else:
        return
    
def atan(calc: Calculator) -> None:
    a = calc.pop()
    if a != None:
        calc.push(math.atan(a))
        return
    else:
        return

FUNCTIONS = {
    "sum": sum,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
    "power": power,
    "negate": negate,
    "swap": swap,
    "sqrt": sqrt,
    "square": square,
    "pi": pi,
    "natural_exponent": nat_exp,
    "invert": invert,
    "sin": sin,
    "cos": cos,
    "tan": tan,
    "asin": asin,
    "acos": acos,
    "atan": atan
}

# def sin(item) -> float:
#     try:
#         if item.trigMode == 'radians':
#             theta = item.pop()
#             if theta % math.pi == 0: return 0
#             else: return math.sin(theta)
#         elif item.trigMode == 'degrees':
#             return sind(item)
#         else: raise Exception("Holy fuck")
#     except:
#         raise Exception("Holy fuck")

# def cos(item) -> float:
#     try:
#         if item.trigMode == 'radians':
#             theta = item.pop()
#             if (theta+math.pi/2) % (math.pi) == 0: return 0
#             else: return math.cos(theta)
#         elif item.trigMode == 'degrees':
#             return cosd(item)
#     except:
#         pass

# def tan(item) -> float:
#     try:
#         if item.trigMode == 'radians':
#             theta = item.pop()
#             if (theta+math.pi/2) % math.pi == 0: return math.nan
#             elif (theta % math.pi) == 0: return 0
#             else: return math.tan(theta)
#         elif item.trigMode == 'degrees':
#             return tand(item)
#     except:
#         pass

# def sind(item) -> float:
#     try:
#         theta = item.pop()
#         if theta % 180 == 0:
#             return 0
#         else:
#             return math.sin(theta*2*math.pi/360)
#     except:
#         pass

# def cosd(item) -> float:
#     try:
#         theta = item.pop()
#         if (theta+90) % 180 == 0: return 0
#         else:
#             return sin(theta*2*math.pi/360)
#     except:
#         pass

# def tand(item) -> float:
#     try:
#         theta = item.pop()
#         if (theta + 90) % 180 == 0: return math.nan
#         elif theta % 180 == 0: return 0
#         else:
#             return tan(theta*2*math.pi/360)
#     except:
#         pass

# def asin(item) -> float:
#     try:
#         if item.trigMode == 'radians':
#             return math.asin(item.pop())
#         elif item.trigMode == 'degrees':
#             return asind(item)
#     except:
#         raise Exception

# def acos(item) -> float:
#     try:
#         if item.trigMode == 'radians':
#             return math.acos(item.pop())
#         elif item.trigMode == 'degrees':
#             return acosd(item)
#     except:
#         pass

# def atan(item) -> float:
#     try:
#         if item.trigMode == 'radians':
#             return math.atan(item.pop())
#         elif item.trigMode == 'degrees':
#             return atand(item)
#     except:
#         pass

# def asind(item) -> float:
#     try:
#         return (math.asin(item.pop())*360/(math.pi*2))
#     except:
#         pass

# def acosd(item) -> float:
#     try:
#         return math.acos(item.pop())*360/(math.pi*2)
#     except:
#         pass

# def atand(item) -> float:
#     try:
#         return math.atan(item.pop())*360/(math.pi*2)
#     except:
#         pass

# def addition(item) -> float:
#     if len(item)>1 : return item.pop() + item.pop()
#     else:
#         pass

# def subtract(item) -> float:
#     if len(item)>1 : return item.pop(1)-item.pop()
#     else:
#         pass

# def multiply(item) -> float:
#     if len(item)>1 : return item.pop() * item.pop()
#     else:
#         pass

# def divide(item) -> float:
#     if len(item)>1 : 
#         return (item.pop(1) / item.pop())
#     else:
#         pass
# def negate(item) -> float:
#     if len(item) > 0: return item.pop()*-1
#     else:
#         pass

# def factorial(item) -> int:
#     if len(item) > 0:
#         try:
#             return math.factorial(int(item.pop()))
#         except:
#             pass
#     else: pass

# def power(item) -> float:
#     if len(item) > 1:
#         return math.pow(item.pop(1), item.pop())
#     else: pass

# def invert(item) -> float:
#     if len(item) > 0:
#         return 1/item.pop() 
#     else: pass

# def square(item) -> float:
#     if len(item) > 0:
#         return math.pow(item.pop(), 2)
#     else: pass

# def sqrt(item) -> float:
#     if len(item) > 0:
#         return math.sqrt(item.pop())
#     else: pass

# def pi(item) -> float:
#     return math.pi

# def e(item) -> float:
#     return math.e

# def log(item) -> float:
#     if len(item) > 0:
#         return math.log(item.pop())
#     else: pass

# def swap(item) -> None:
#     if len(item) > 1:
#         first = item.pop()
#         second = item.pop()
#         item.push(first, second)


# FUNCTIONS_DICT = {
#     "+":funcs.addition,
#     "-":funcs.subtract,
#     "*":funcs.multiply,
#     "/":funcs.divide,
#     "negate":funcs.negate,
#     "!":funcs.factorial,
#     "^":funcs.power,
#     "invert":funcs.invert,
#     "sin":funcs.sin,
#     "cos":funcs.cos,
#     "tan":funcs.tan,
#     "sind":funcs.sind,
#     "cosd":funcs.cosd,
#     "tand":funcs.tand,
#     "asin":funcs.asin,
#     "acos":funcs.acos,
#     "atan":funcs.atan,
#     "asind":funcs.asind,
#     "acosd":funcs.acosd,
#     "atand":funcs.atand,
#     "square":funcs.square,
#     "sqrt":funcs.sqrt,
#     "log":funcs.log,
#     "e":funcs.e,
#     "pi":funcs.pi,
#     "swap": funcs.swap
# }