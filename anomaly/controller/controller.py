from PyQt6.QtWidgets import QApplication
import sys
from anomaly.model import model
from anomaly.UI import window
from anomaly.common import useful

class controller:   # define the controller class.
    def __init__(self):
        self.startup()  # run the startup method that intializes various parameters of the controller, view and model
        self.stack = model.model(self)  # create an instance of the model that runs the mathematical logic
        self.application = QApplication(sys.argv)   # create a PyQt application
        self.application.setStyleSheet(useful.DARKMODE)   # I think this is junk and needs to be removed?
        self.window = window.viewWindow(self)   # create an instance of the main view objects
        self.window.show()  # show the main window
        sys.exit(self.application.exec())
        
    
    def startup(self):
        self.trigMode = 'radians'
        self.mode = "DARKMODE"
    
    def update(self):   # updates the window's stack display
        self.window.updateStack()   # calls the window's method that updates it's stack
    
    def appendNumber(self, value):  # append a number to the stack, or perform other logical actions
        if value in self.stack.validNumbers:    # checks to see if the number passed to the function is a valid number
            self.stack.appendNumber(value)  # tells the model to append a number to it's input field
            self.update()   # update the window to reflect the changes

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

    def enterNumber(self):
        self.stack.appendToStack()
        self.update()
    
    def delete(self):
        self.stack.delete()
        self.update()
    
    def operator(self, value):
        self.stack.operator(value)
        self.update()
    
    def addPi(self):
        self.stack.addPi()
        self.update()
    
    def clearStack(self):
        self.stack.clearStack()
        self.update()
    
    def switchMode(self):
        if self.mode == "DARKMODE":
            self.application.setStyleSheet(useful.LIGHTMODE)
            self.mode = "LIGHTMODE"
        elif self.mode == "LIGHTMODE":
            self.application.setStyleSheet(useful.DARKMODE)
            self.mode = "DARKMODE"
        else:
            pass