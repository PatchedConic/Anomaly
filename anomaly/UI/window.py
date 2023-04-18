from PyQt6.QtWidgets import QGridLayout, QWidget
from anomaly.UI import UI
from PyQt6 import QtGui


class viewWindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.welcomeMsg = ''# """Welcome to Anomaly\nA basic RPN calculator"""
        self.controllerHandle = parent
        self.resize(400,600)
        self.setWindowTitle("Anomaly Calc")
        self.setWindowIcon(QtGui.QIcon("materialCalc.png"))
        print
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.UI = UI.UI(self, self.layout, self.controllerHandle)

    def buildStackString(self):
        self.stackString = ''
        for i in self.controllerHandle.stack.stack:
            self.stackString += '\u203A ' + str(i) + '\n'
        self.stackString += '\u203A ' + self.controllerHandle.stack.inputField

    def updateStack(self):
        self.UI.stackValue.buildStackString(self.controllerHandle)