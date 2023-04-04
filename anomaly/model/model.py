import math

class model:
    def __init__(self, controllerHandle):
        self.stack = []
        self.inputField = ''
        self.controllerHandle = controllerHandle
        self.twoParameterOperators = ['+','-','*','/','swap','^', 'root']
        self.singleParameterOperators = ['plusminus', 'sin','cos','tan','ln', 'asin', 'acos', 'atan', 'e', 'inv', 'log']
        self.validNumbers = ['1','2','3','4','5', '6','7','8', '9', '0', '.']



            
    def clearStack(self):
        self.stack = []
        self.inputField = ''

    def addPi(self):
        if self.isValid():
            self.appendToStack()
        self.inputField = str(math.pi)
        self.appendToStack()

    def validOperator(self, value):
        if value in self.twoParameterOperators or value in self.singleParameterOperators:
            return True
        else:
            return False
    def hasTwoValues(self):
        try:
            self.stack[-1]
            try:
                self.stack[-2]
                return True
            except IndexError:
                return False
        except:
            return False

    def sin(self, value):
        if self.controllerHandle.trigMode == "radians":
            if value % math.pi == 0:
                return 0
            else:
                return math.sin(value)
        elif self.controllerHandle.trigMode == "degrees":
            if value % 90 == 0:
                return 0
            else:
                return math.sin(value*2*math.pi/360)

    def cos(self, value):
        if self.controllerHandle.trigMode == "radians":
            return math.cos(value)
        elif self.controllerHandle.trigMode == "degrees":
            return math.cos(value*2*math.pi/360)
 
    def tan(self, value):
        if self.controllerHandle.trigMode == "radians":
            return math.tan(value)
        elif self.controllerHandle.trigMode == "degrees":
            return math.tan(value*2*math.pi/360)
    
    def asin(self,value):
        if self.controllerHandle.trigMode == 'radians':
            return math.asin(value)
        elif self.controllerHandle.trigMode == 'degrees':
            return math.asin(value)*360/(2*math.pi)

    def acos(self,value):
        if self.controllerHandle.trigMode == 'radians':
            return math.acos(value)
        elif self.controllerHandle.trigMode == 'degrees':
            return math.acos(value)*360/(2*math.pi)

    def atan(self,value):
        if self.controllerHandle.trigMode == 'radians':
            return math.atan(value)
        elif self.controllerHandle.trigMode == 'degrees':
            return math.atan(value)*360/(2*math.pi)

    def operator(self, value):
        if self.validOperator(value):
            if value in self.singleParameterOperators:
                if self.isValid():
                    self.appendToStack()
                else:
                    pass
                if self.isValid(-2):
                    try:
                        if value == "plusminus":
                            self.stack[-1] = self.stack[-1]*-1
                        elif value == 'sin':
                            self.stack[-1] = self.sin(self.stack[-1])
                        elif value == 'cos':
                            self.stack[-1] = self.cos(self.stack[-1])
                        elif value == 'tan':
                            self.stack[-1] = self.tan(self.stack[-1])
                        elif value == 'ln':
                            self.stack[-1] = math.log(self.stack[-1])
                        elif value == 'asin':
                            self.stack[-1] = self.asin(self.stack[-1])
                        elif value == 'acos':
                            self.stack[-1] = self.acos(self.stack[-1])
                        elif value == 'atan':
                            self.stack[-1] = self.atan(self.stack[-1])
                        elif value == 'e':
                            self.stack[-1] = math.exp(self.stack[-1])
                        elif value == 'log':
                            self.stack[-1] = math.log(self.stack[-1], 10)
                        elif value == 'inv':
                            self.stack[-1] = 1/self.stack[-1]
                    except ZeroDivisionError:
                        pass
                    except ValueError:
                        pass
                    except IndexError:
                        self.stack = []
                else:
                    pass
                    
            elif value in self.twoParameterOperators:
                if self.isValid():
                    self.appendToStack()
                else:
                    pass
                if self.hasTwoValues():
                    try:
                        if value == '+':
                            self.valueX = self.stack.pop()
                            self.valueY = self.stack.pop()
                            self.stack.append(self.valueY+self.valueX)
                        elif value == '-':
                            self.valueX = self.stack.pop()
                            self.valueY = self.stack.pop()
                            self.stack.append(self.valueY-self.valueX)
                        elif value == '*':
                            self.valueX = self.stack.pop()
                            self.valueY = self.stack.pop()
                            self.stack.append(self.valueY*self.valueX)
                        elif value == '/':
                            self.valueX = self.stack.pop()
                            self.valueY = self.stack.pop()
                            self.stack.append(self.valueY/self.valueX)
                        elif value == 'swap':
                            self.valueX = self.stack.pop()
                            self.valueY = self.stack.pop()
                            self.stack.append(self.valueX)
                            self.stack.append(self.valueY)
                        elif value == '^':
                            self.valueX = self.stack.pop()
                            self.valueY = self.stack.pop()
                            self.stack.append(math.pow(self.valueY,self.valueX))
                        elif value == 'root':
                            self.valueX = self.stack.pop()
                            self.valueY = self.stack.pop()
                            if self.valueY < 0:
                                raise ZeroDivisionError
                            self.stack.append(math.pow(self.valueY, float(1/self.valueX)))

                    except ZeroDivisionError:
                        pass
                else:
                    pass
        else:
            pass
    
    def appendNumber(self, value):
        if value in self.validNumbers:
            if value == '.':
                if self.hasDecimal():
                    pass
                else:
                    self.inputField += str(value)
            else:
                self.inputField += str(value)
    
    def hasDecimal(self):
        for i in str(self.inputField):
            if i == '.':
                return True
        return False

    
    def appendToStack(self, value = ''):
        if self.isValid():
            self.stack.append(float(self.inputField))
            self.inputField = ''
        else:
            pass

    def isValid(self, index = -1):
        try:
            if index == -1:
                float(self.inputField)
                return True
            elif index < -1:
                float(self.stack[index+1])
                return True
            else:
                return False
        except:
            return False

    def delete(self):
        if self.inputField != '':
            self.inputField = self.inputField[:len(self.inputField)-1]
        else:
            pass