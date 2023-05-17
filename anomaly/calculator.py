import math

from anomaly.stack import Stack

class Calculator():
    def __init__(self):
        self.stack = Stack()
        self.angular = "rad"

    def set_radians(self):
        self.angular = "rad"

    def set_degrees(self):
        self.angular = "deg"

    def get_angular(self):
        return self.angular
    
    def add(self):
        x = self.stack.pop()
        y = self.stack.pop()
        if x == None:
            return
        if y == None:
            self.stack.add_number(x)
            return
        self.stack.add_number(str(float(y)+float(x)))
        return

    def subtract(self):
        x = self.stack.pop()
        y = self.stack.pop()
        if x == None:
            return
        if y == None:
            self.stack.add_number(x)
            return
        self.stack.add_number(str(float(y)-float(x)))
        return

    def multiply(self):
        x = self.stack.pop()
        y = self.stack.pop()
        if x == None:
            return
        if y == None:
            self.stack.add_number(x)
            return
        self.stack.add_number(str(float(y)*float(x)))
        return

    def divide(self):
        x = self.stack.pop()
        y = self.stack.pop()
        if x == None:
            return
        if y == None:
            self.stack.add_number(x)
            return
        self.stack.add_number(str(float(y)/float(x)))
        return
    
    def power(self):
        x = self.stack.pop()
        y = self.stack.pop()
        if x == None:
            return
        if y == None:
            self.stack.add_number(x)
            return
        self.stack.add_number(str(float(y)**float(x)))
        return
    
    def root(self):
        x = self.stack.pop()
        y = self.stack.pop()
        if x == None:
            return
        if y == None:
            self.stack.add_number(x)
            return
        self.stack.add_number(str(float(y)**(1/float(x))))
        return
    
    def inverse(self):
        x = self.stack.pop()
        if x == None:
            return
        self.stack.add_number(str(1/float(x)))
        return
    
    def negate(self):
        x = self.stack.pop()
        if x == None:
            return
        self.stack.add_number(str(-1*float(x)))
        return
    
    def sin(self):
        x = self.stack.pop()
        if x == None:
            return
        if self.get_angular() == 'rad':
            self.stack.add_number(str(math.sin(float(x))))
            return
        elif self.get_angular() == 'deg':
            self.stack.add_number(str(math.sin(float(x)*2*math.pi/360)))
            return
        return
    
    def cos(self):
        x = self.stack.pop()
        if x == None:
            return
        if self.get_angular() == 'rad':
            self.stack.add_number(str(math.cos(float(x))))
            return
        elif self.get_angular() == 'deg':
            self.stack.add_number(str(math.cos(float(x)*2*math.pi/360)))
            return
        return
    
    def tan(self):
        x = self.stack.pop()
        if x == None:
            return
        if self.get_angular() == 'rad':
            self.stack.add_number(str(math.tan(float(x))))
            return
        elif self.get_angular() == 'deg':
            self.stack.add_number(str(math.tan(float(x)*2*math.pi/360)))
            return
        return
    
    def asin(self):
        x = self.stack.pop()
        if x == None:
            return
        if self.get_angular() == 'rad':
            self.stack.add_number(str(math.asin(float(x))))
            return
        elif self.get_angular() == 'deg':
            self.stack.add_number(str((360/(2*math.pi)*math.asin(float(x)))))
            return
        return
    
    def acos(self):
        x = self.stack.pop()
        if x == None:
            return
        if self.angular == 'rad':
            self.stack.add_number(str(math.acos(float(x))))
            return
        elif self.angular == 'deg':
            self.stack.add_number(str((360/(2*math.pi)*math.acos(float(x)))))
            return
        return
    
    def atan(self):
        x = self.stack.pop()
        if x == None:
            return
        if self.angular == 'rad':
            self.stack.add_number(str(math.atan(float(x))))
            return
        elif self.angular == 'deg':
            self.stack.add_number(str((360/(2*math.pi)*math.atan(float(x)))))
            return
        return
    
    def ln(self):
        x = self.stack.pop()
        if x == None:
            return
        self.stack.add_number(str(math.log(float(x))))
        return
    
    def log(self):
        x = self.stack.pop()
        if x == None:
            return
        self.stack.add_number(str(math.log10(float(x))))
        return
    
    def nat_exp(self):
        x = self.stack.pop()
        if x == None:
            return
        self.stack.add_number(str(math.e**float(x)))
        return
    
    def sqrt(self):
        x = self.stack.pop()
        if x == None:
            return
        self.stack.add_number(str(float(x)**(1/2)))
        return
    
    def squared(self):
        x = self.stack.pop()
        if x == None:
            return
        self.stack.add_number(str(float(x)**2))
        return
    def pi(self):
        self.stack.add_number(math.pi)

    def e(self):
        self.stack.add_number(math.e)
        