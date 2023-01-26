from PyQt6.QtWidgets import QGridLayout, QWidget
from PyQt6.QtGui import QKeySequence, QShortcut
from anomaly.UI import UI

class viewWindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.shiftOn = False
        self.welcomeMsg = ''# """Welcome to Anomaly\nA basic RPN calculator"""
        self.controllerHandle = parent
        self.resize(400,600)
        self.setWindowTitle("Anomaly Calc")
        self.updateStyle()
        self.loadShortcuts()
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.UI = UI.UI(self, self.layout, self.controllerHandle)
        self.shiftHeld = False

    def shiftClicked(self):
        if self.shiftOn == False:
            self.UI.buttonShift.setStyleSheet("""
            background-color: {0};
            color: {1};
                """.format(self.controllerHandle.fgColor, self.controllerHandle.bgColor))
            self.shiftOn = True
            self.UI.buttonSin.setText("asin")        
            self.UI.buttonSin.disconnect()
            self.UI.buttonSin.clicked.connect(lambda:self.controllerHandle.operator("arcsin"))
            self.UI.buttonCos.setText("acos")
            self.UI.buttonCos.disconnect()        
            self.UI.buttonCos.clicked.connect(lambda:self.controllerHandle.operator("arccos"))
            self.UI.buttonTan.setText("atan")
            self.UI.buttonTan.disconnect()        
            self.UI.buttonTan.clicked.connect(lambda:self.controllerHandle.operator("arctan"))
            self.UI.buttonLn.setText("e\u02E3")
            self.UI.buttonLn.disconnect()
            self.UI.buttonLn.clicked.connect(lambda:self.controllerHandle.operator("e"))
        elif self.shiftOn == True:
            self.UI.buttonShift.setStyleSheet("""
            background-color: {0};
            color: {1};
            """.format(self.controllerHandle.bgColor, self.controllerHandle.fgColor))
            self.shiftOn = False
            self.UI.buttonSin.setText("sin")
            self.UI.buttonSin.disconnect()        
            self.UI.buttonSin.clicked.connect(lambda:self.controllerHandle.operator("sin"))
            self.UI.buttonCos.setText("cos")
            self.UI.buttonCos.disconnect()        
            self.UI.buttonCos.clicked.connect(lambda:self.controllerHandle.operator("cos"))
            self.UI.buttonTan.setText("tan")
            self.UI.buttonTan.disconnect()        
            self.UI.buttonTan.clicked.connect(lambda:self.controllerHandle.operator("tan"))
            self.UI.buttonLn.disconnect()
            self.UI.buttonLn.setText("ln")
            self.UI.buttonLn.clicked.connect(lambda:self.controllerHandle.operator("ln"))

    def degreeMode(self):
        if self.controllerHandle.trigMode == 'radians':
            self.controllerHandle.trigMode = 'degrees'
            self.UI.modeButton.setText('Deg')
        elif self.controllerHandle.trigMode == 'degrees':
            self.controllerHandle.trigMode = 'radians'
            self.UI.modeButton.setText('Rad')

    def newShortcut(self, dict):
        anObject = QShortcut(QKeySequence(dict['shortcut']), self)
        anObject.activated.connect(lambda:self.controllerHandle.appendNumber(dict['num']))
        return anObject

    def loadShortcuts(self):
        self.shortcuts = []
        for i in self.controllerHandle.shortcuts:
            self.shortcuts.append(self.newShortcut(i))

    def updateStyle(self):
        if self.controllerHandle.hasColors == False:
            self.setStyleSheet('')
        else:
            self.setStyleSheet("""
            QWidget {{
                background-color: {0};
                color: {1};
            }}
            QPushButton {{
                background-color: {0};
                color: {1};
            }}
            QTextEdit {{
                border: 2px solid {2};
                border-radius: 3px;
            }}
            QPushButton {{
                font-size: 18px;
                background-color: {0};
                color: {1}
            }}
            """.format(self.controllerHandle.bgColor, self.controllerHandle.fgColor, self.controllerHandle.accentColor))
        self.update()

    def buildStackString(self):
        self.stackString = ''
        for i in self.controllerHandle.stack.stack:
            self.stackString += '\u2E30 ' + str(i) + '\n'
        self.stackString += '\u2E30 ' + self.controllerHandle.stack.inputField

    def updateStack(self):
        self.buildStackString()
        self.UI.stackValue.setText(self.stackString)