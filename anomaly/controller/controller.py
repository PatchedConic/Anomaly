from PyQt6.QtWidgets import QApplication
import tomli
import sys
from anomaly.common import useful
from anomaly.model import model
from anomaly.UI import window

class controller:
    def __init__(self):
        self.startup()
        self.stack = model.model(self)
        self.application = QApplication(sys.argv)
        self.application.setStyleSheet("""QPushButton { font-size: 18px;}""")
        self.window = window.viewWindow(self)
        self.window.show()
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
    
    def update(self):
        self.window.updateStack()
    
    def appendNumber(self, value):
        if value in self.stack.validNumbers:
            self.stack.appendNumber(value)
            self.update()
        elif value in self.stack.singleParameterOperators or value in self.stack.twoParameterOperators:
            self.operator(value)
        elif value == 'backspace':
            self.delete()
        elif value == 'clear':
            self.clearStack()
        elif value == 'enter':
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