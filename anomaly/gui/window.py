from PyQt6.QtWidgets import QGridLayout, QWidget, QPushButton, QTextEdit
from PyQt6.QtGui import QKeySequence, QShortcut


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
        self.UI()
        self.shiftHeld = False

    def shiftClicked(self):
        if self.shiftOn == False:
            self.buttonShift.setStyleSheet("""
            background-color: {0};
            color: {1};
                """.format(self.controllerHandle.fgColor, self.controllerHandle.bgColor))
            self.shiftOn = True
            self.buttonSin.setText("asin")        
            self.buttonSin.disconnect()
            self.buttonSin.clicked.connect(lambda:self.controllerHandle.operator("arcsin"))
            self.buttonCos.setText("acos")
            self.buttonCos.disconnect()        
            self.buttonCos.clicked.connect(lambda:self.controllerHandle.operator("arccos"))
            self.buttonTan.setText("atan")
            self.buttonTan.disconnect()        
            self.buttonTan.clicked.connect(lambda:self.controllerHandle.operator("arctan"))
        elif self.shiftOn == True:
            self.buttonShift.setStyleSheet("""
            background-color: {0};
            color: {1};
            """.format(self.controllerHandle.bgColor, self.controllerHandle.fgColor))
            self.shiftOn = False
            self.buttonSin.setText("sin")
            self.buttonSin.disconnect()        
            self.buttonSin.clicked.connect(lambda:self.controllerHandle.operator("sin"))
            self.buttonCos.setText("cos")
            self.buttonCos.disconnect()        
            self.buttonCos.clicked.connect(lambda:self.controllerHandle.operator("cos"))
            self.buttonTan.setText("tan")
            self.buttonTan.disconnect()        
            self.buttonTan.clicked.connect(lambda:self.controllerHandle.operator("tan"))

    def degreeMode(self):
        if self.controllerHandle.trigMode == 'radians':
            self.controllerHandle.trigMode = 'degrees'
            self.modeButton.setText('Deg')
        elif self.controllerHandle.trigMode == 'degrees':
            self.controllerHandle.trigMode = 'radians'
            self.modeButton.setText('Rad')

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
        self.stackValue.setText(self.stackString)

    def UI(self):
        self.stackValue = QTextEdit()
        self.stackValue.setReadOnly(True)
        self.stackValue.ensureCursorVisible()
        self.stackFont = self.stackValue.font()
        self.stackFont.setPointSize(18)
        self.stackValue.setFont(self.stackFont)
        self.stackValue.setText(self.welcomeMsg)
        self.layout.addWidget(self.stackValue,0,0)

        self.buttonGrid = QGridLayout()
        self.button0 = QPushButton("0")
        self.button0.clicked.connect(lambda:self.controllerHandle.appendNumber("0"))
        self.buttonDot = QPushButton(".")
        self.buttonDot.clicked.connect(lambda:self.controllerHandle.appendNumber("."))
        self.buttonEnter = QPushButton("Enter")
        self.buttonEnter.clicked.connect(lambda:self.controllerHandle.enterNumber())
        self.button1 = QPushButton("1")
        self.button1.clicked.connect(lambda:self.controllerHandle.appendNumber("1"))
        self.button2 = QPushButton("2")
        self.button2.clicked.connect(lambda:self.controllerHandle.appendNumber("2"))
        self.button3 = QPushButton("3")
        self.button3.clicked.connect(lambda:self.controllerHandle.appendNumber("3"))
        self.buttonPlus = QPushButton("+")
        self.buttonPlus.clicked.connect(lambda:self.controllerHandle.operator("+"))
        self.button4 = QPushButton("4")
        self.button4.clicked.connect(lambda:self.controllerHandle.appendNumber("4"))
        self.button5 = QPushButton("5")
        self.button5.clicked.connect(lambda:self.controllerHandle.appendNumber("5"))
        self.button6 = QPushButton("6")
        self.button6.clicked.connect(lambda:self.controllerHandle.appendNumber("6"))
        self.buttonMinus = QPushButton("-")
        self.buttonMinus.clicked.connect(lambda:self.controllerHandle.operator("-"))
        self.button7 = QPushButton("7")
        self.button7.clicked.connect(lambda:self.controllerHandle.appendNumber("7"))
        self.button8 = QPushButton("8")
        self.button8.clicked.connect(lambda:self.controllerHandle.appendNumber("8"))
        self.button9 = QPushButton("9")
        self.button9.clicked.connect(lambda:self.controllerHandle.appendNumber("9"))
        self.buttonMult = QPushButton("\u00D7")
        self.buttonMult.clicked.connect(lambda:self.controllerHandle.operator("*"))
        self.buttonSin = QPushButton("Sin")        
        self.buttonSin.clicked.connect(lambda:self.controllerHandle.operator("sin"))
        self.buttonCos = QPushButton("Cos")
        self.buttonCos.clicked.connect(lambda:self.controllerHandle.operator("cos"))
        self.buttonTan = QPushButton("Tan")
        self.buttonTan.clicked.connect(lambda:self.controllerHandle.operator("tan"))
        self.buttonDiv = QPushButton("\u00F7")
        self.buttonDiv.clicked.connect(lambda:self.controllerHandle.operator("/"))
        self.buttonPi = QPushButton("\u03C0")
        self.buttonPi.clicked.connect(lambda:self.controllerHandle.addPi())
        self.buttonPlusMinus = QPushButton("\u00B1")
        self.buttonPlusMinus.clicked.connect(lambda:self.controllerHandle.operator("plusminus"))
        self.buttonSwap = QPushButton("X \u21C6 Y")
        self.buttonSwap.clicked.connect(lambda:self.controllerHandle.operator("swap"))
        self.buttonClear = QPushButton("C")
        self.buttonClear.clicked.connect(lambda:self.controllerHandle.clearStack())
        self.buttonShift = QPushButton("\u2191")
        self.buttonShift.clicked.connect(lambda:self.shiftClicked())
        self.buttonLn = QPushButton("ln")
        self.buttonLn.clicked.connect(lambda:self.controllerHandle.operator("ln"))
        self.buttonExp = QPushButton("y\u02E3")
        self.buttonExp.clicked.connect(lambda:self.controllerHandle.operator("^"))
        self.buttonBackspace = QPushButton("\u2190")
        self.buttonBackspace.clicked.connect(lambda:self.controllerHandle.delete())
        self.modeButton = QPushButton(self.controllerHandle.trigMode)
        self.modeButton.clicked.connect(lambda:self.degreeMode())


        self.buttonGrid.addWidget(self.button0,7,0)
        self.buttonGrid.addWidget(self.buttonDot,7,1)
        self.buttonGrid.addWidget(self.buttonEnter, 7, 2, 1, 2)
        self.buttonGrid.addWidget(self.button1, 6, 0)
        self.buttonGrid.addWidget(self.button2, 6, 1)
        self.buttonGrid.addWidget(self.button3, 6, 2)
        self.buttonGrid.addWidget(self.buttonPlus, 6, 3)        
        self.buttonGrid.addWidget(self.button4, 5, 0)
        self.buttonGrid.addWidget(self.button5, 5, 1)
        self.buttonGrid.addWidget(self.button6, 5, 2)
        self.buttonGrid.addWidget(self.buttonMinus, 5, 3)
        self.buttonGrid.addWidget(self.button7,4, 0)
        self.buttonGrid.addWidget(self.button8, 4, 1)
        self.buttonGrid.addWidget(self.button9, 4, 2)
        self.buttonGrid.addWidget(self.buttonMult, 4, 3)
        self.buttonGrid.addWidget(self.buttonSin, 3, 0)
        self.buttonGrid.addWidget(self.buttonCos, 3, 1)
        self.buttonGrid.addWidget(self.buttonTan, 3, 2)
        self.buttonGrid.addWidget(self.buttonDiv, 3, 3)
        self.buttonGrid.addWidget(self.buttonPi, 2, 0)
        self.buttonGrid.addWidget(self.buttonPlusMinus, 2, 1)
        self.buttonGrid.addWidget(self.buttonSwap, 2, 2)
        self.buttonGrid.addWidget(self.buttonClear, 2, 3)
        self.buttonGrid.addWidget(self.buttonShift, 1, 0)
        self.buttonGrid.addWidget(self.buttonLn, 1, 1)
        self.buttonGrid.addWidget(self.buttonExp, 1, 2)
        self.buttonGrid.addWidget(self.buttonBackspace, 1, 3)
        self.buttonGrid.addWidget(self.modeButton, 0, 0)

        self.layout.addLayout(self.buttonGrid, 1, 0, 2,1)