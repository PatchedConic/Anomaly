from textual.containers import Vertical
from textual.widgets import Label
from .calculator import Calculator

class Trace(Vertical):
    
    def __init__(self):
        super().__init__(classes = "trace")
        self.border_title="TRACE"

    def update(self,calc: Calculator) -> None:
        self.remove_children(selector= "*")
        for line in calc.history:
            self._add_child(Label(line))


