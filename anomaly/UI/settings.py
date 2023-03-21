from PyQt6.QtWidgets import QDialog, QComboBox, QGridLayout

class SettingsDialog(QDialog):
    def __init__(self, controllerHandle):
        super().__init__()
        self.setWindowTitle("Calculator Settings")
        self.controllerHandle = controllerHandle
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.default_units = DefaultTrig()
        self.layout.addWidget(self.default_units)
        

class DefaultTrig(QComboBox):
    def __init__(self):
        super().__init__()
        self.addItems(["Radians", "Degrees"])
    


