from PyQt6.QtWidgets import QDialog, QComboBox, QGridLayout

class SettingsDialog(QDialog):
    def __init__(self, controllerHandle):
        super().__init__()
        self.setWindowTitle("Calculator Settings")
        self.controllerHandle = controllerHandle
        self.colors_list = self.controllerHandle.get_colors()
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.color_picker = ColorPicker(self.controllerHandle.get_colors(), self.controllerHandle)
        self.layout.addWidget(self.color_picker)
        self.default_units = DefaultTrig()
        self.layout.addWidget(self.default_units)
        
class ColorPicker(QComboBox):
    def __init__(self, list, controllerHandle):
        super().__init__()
        self.controllerHandle = controllerHandle
        self.addItems(list)
        self.currentTextChanged.connect(self.set_colorscheme)

    def set_colorscheme(self):
        self.controllerHandle.set_colorscheme(self.currentText())

class DefaultTrig(QComboBox):
    def __init__(self):
        super().__init__()
        self.addItems(["Radians", "Degrees"])
    


