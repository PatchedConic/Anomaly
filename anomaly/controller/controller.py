from PyQt6.QtWidgets import QApplication
import sys
from anomaly.model import model
from anomaly.UI import window
from anomaly.common import useful

class controller:   # define the controller class.
    def __init__(self):
        self.startup()  # run the startup method that intializes various parameters of the controller, view and model
        self.stack = model.model(self)  # create an instance of the model that runs the mathematical logic
        self.application = QApplication(sys.argv)
        self.window = window.viewWindow(self)   # create an instance of the main view objects
        self.window.setStyleSheet(useful.DARKMODE)
        self.window.show()  # show the main window
    
    def startup(self):
        self.trigMode = 'radians'
        self.mode = "DARKMODE"
    
    def update(self):   # updates the window's stack display
        self.window.updateStack()   # calls the window's method that updates it's stack
    
    def append(self, value):  # append a number to the stack, or perform other logical actions
        print(value)
        if value == 'return':
            self.stack.appendToStack()
            self.update()
            return
        elif value == 'pi':
            self.stack.addPi()
            self.update()
            return
        elif value == 'clear':
            self.stack.clearStack()
            self.update()
            return
        elif value == 'del':
            self.stack.delete()
            self.update()
            return
        if value in self.stack.validNumbers:    # checks to see if the number passed to the function is a valid number
            self.stack.appendNumber(value)  # tells the model to append a number to it's input field
            self.update()   # update the window to reflect the changes
            return
        elif value in self.stack.twoParameterOperators or self.stack.singleParameterOperators:
            self.stack.operator(value)
            self.update()
            return
        return
        

    def set_mode(self, trig_mode = ""):
        if trig_mode != "":
            self.trigMode = trig_mode
        elif trig_mode == "":
            if self.trigMode == "radians":
                self.trigMode = "degrees"
            else:
                self.trigMode = "radians"
        return
    
    def get_mode(self):
        if self.trigMode == "radians":
            return "Rad"
        else:
            return "Deg"
    
    def delete(self):
        self.stack.delete()
        self.update()
    
    def addPi(self):
        self.stack.addPi()
        self.update()
    
    def clearStack(self):
        self.stack.clearStack()
        self.update()
    
    def switchMode(self):
        if self.mode == "DARKMODE":
            self.window.setStyleSheet(useful.LIGHTMODE)
            self.mode = "LIGHTMODE"
        elif self.mode == "LIGHTMODE":
            self.window.setStyleSheet(useful.DARKMODE)
            self.mode = "DARKMODE"
        else:
            pass