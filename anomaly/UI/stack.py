from PyQt6.QtWidgets import QTextEdit
from anomaly.common import useful

class stack(QTextEdit):
    def __init__(self, parentWidget):
        QTextEdit.__init__(self)
        self.setReadOnly(True)
        self.ensureCursorVisible()
        self.customFont = self.font()
        self.customFont.setPointSize(18)
        self.setFont(self.customFont)
        self.setText(useful.WELCOMEMSG)
        parentWidget.addWidget(self, 0,0)

    def buildStackString(self, controllerHandle):
        self.stackString = ''
        for i in controllerHandle.stack.stack:
            self.stackString += '\u203A ' + str(i) + '\n'
        if controllerHandle.stack.inputField != '':
            self.stackString += '\u203A ' + controllerHandle.stack.inputField
        self.setText(self.stackString)