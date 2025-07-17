from PyQt6.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QPushButton

from PyQt6.QtCore import Qt

class Anomaly(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Epoch")
        self.resize(320, 508)
        self.setMinimumSize(320, 508)

        self.centralWidget = QWidget()
        self.centralWidget.setObjectName("central_widget")
        self.layout = QVBoxLayout()
        self.centralWidget.setLayout(self.layout)
        self.setCentralWidget(self.centralWidget)

        self.layout.addWidget(Register_Stack())
        self.test_button = QPushButton("Test")
        self.layout.addWidget(self.test_button)

class Register_Stack(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("register_stack")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.setFixedHeight(168)
        self.setFixedWidth(280)
        self.layout.addWidget(QPushButton("Test", objectName="register_0"))
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)