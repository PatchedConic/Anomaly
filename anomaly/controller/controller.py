from PyQt6.QtWidgets import QApplication
import tomli
import sys
from anomaly.common import useful
from anomaly.model import model
from anomaly.UI import window

class controller:   # define the controller class.
    def __init__(self):
        self.startup()  # run the startup method that intializes various parameters of the controller, view and model
        self.stack = model.model(self)  # create an instance of the model that runs the mathematical logic
        self.application = QApplication(sys.argv)   # create a PyQt application
        self.application.setStyleSheet("""QPushButton { font-size: 18px;}""")   # I think this is junk and needs to be removed?
        self.window = window.viewWindow(self)   # create an instance of the main view objects
        self.window.show()  # show the main window
        sys.exit(self.application.exec())
    
    def startup(self):
        self.hasColors = True
        self.configPath = useful.check_for_config()
        if self.configPath == False:
            self.hasColors = False
            self.trigMode = 'radians'
            self.shortcuts = []
        else:
            with open(self.configPath, mode='rb') as self.cfg:
                self.configFile = tomli.load(self.cfg)
            try:
                self.trigMode = self.configFile['mode']['angle']
            except KeyError:
                self.trigMode = 'radians'
            try:
                self.shortcuts = self.configFile['shortcut']
            except KeyError:
                self.shortcuts = []
            self.set_colorscheme(self.configFile["colors"]["colorscheme"])
    
    def update(self):   # updates the window's stack display
        self.window.updateStack()   # calls the window's method that updates it's stack
    
    def appendNumber(self, value):  # append a number to the stack, or perform other logical actions
        if value in self.stack.validNumbers:    # checks to see if the number passed to the function is a valid number
            self.stack.appendNumber(value)  # tells the model to append a number to it's input field
            self.update()   # update the window to reflect the changes

        elif value in self.stack.singleParameterOperators or value in self.stack.twoParameterOperators: # checks to see if the parameter is a valid operator
            self.operator(value)    # passes the parameter to the operator function

        elif value == 'backspace':  # checks to see if the parameter is a backspace
            self.delete()   # calls the backspace function

        elif value == 'clear':  # checks to see if the parameter is a clear stack command
            self.clearStack()   # calls the clear stack function

        elif value == 'enter':  # 
            self.enterNumber()
        elif value == 'pi':
            self.addPi()

    def set_mode(self, trig_mode):
        self.trigMode = trig_mode
    
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
    
    def set_colorscheme(self, color_name):

        self.colorscheme = self.configFile['colors']['colorscheme']
        if self.colorscheme == "default":
            self.hasColors = False
        else:
            for colorscheme in self.configFile['colorscheme']:
                if self.configFile['colorscheme'][colorscheme]['name'] == color_name:
                    self.bgColor = self.configFile['colorscheme'][colorscheme]['background-color']
                    self.fgColor = self.configFile['colorscheme'][colorscheme]['foreground-color']
                    self.accentColor = self.configFile['colorscheme'][colorscheme]['accent-color']
                else:       
                    pass
        try:
            self.window.updateStyle()
        except AttributeError:
            pass

    def get_colors(self):
        colors_list = []
        for colorscheme in self.configFile['colorscheme']:
                colors_list.append(self.configFile['colorscheme'][colorscheme]['name'])
        return colors_list