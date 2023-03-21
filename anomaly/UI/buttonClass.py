from PyQt6.QtWidgets import QPushButton

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
