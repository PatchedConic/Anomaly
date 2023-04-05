from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QKeySequence, QShortcut


class funcButton(QPushButton):
    def __init__(self, textValue, functionValue, shortcut='', altText='', altFunction='', altShortcut=''):
        QPushButton.__init__(self, textValue)
        self.shifted = False
        self.altText = altText
        self.altFunction = altFunction
        self.altShortcut = altShortcut
        self.textValue = textValue
        self.functionValue = functionValue
        self.shortcut = shortcut
        self.clicked.connect(lambda: self.fire(functionValue))
        if shortcut != '':
            self.primeShortcut = QShortcut(QKeySequence(shortcut),self)
            self.primeShortcut.activated.connect(lambda: self.fire(functionValue))
        if self.altShortcut != '':
            self.secondaryShortcut = QShortcut(QKeySequence(self.altShortcut), self)
            self.secondaryShortcut.activated.connect(lambda: self.fire(altFunction))
    def fire(self, Value):
        from anomaly import applicationController
        applicationController.append(Value)
    def shift(self):
        if self.shifted == False:
            if self.altText != '' and self.altFunction != '':
                self.disconnect()
                self.clicked.connect(lambda:self.fire(self.altFunction))
                self.setText(self.altText)
                self.shifted = True
        elif self.shifted == True:
            self.disconnect()
            self.clicked.connect(lambda:self.fire(self.functionValue))
            self.setText(self.textValue)
            self.shifted = False
        return



class button(QPushButton):
    def __init__(self, textValue):
        QPushButton.__init__(self, textValue)

        # self.setStyleSheet("""
        # font-size: 18px; 
        # background-color: transparent; 
        # outline: none; 
        # border: 2px solid #3c3836; 
        # margin: 4px;
        # padding: 4px;
        # border-radius: 4px;
        # """)