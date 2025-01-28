from textual.app import App
from textual.widgets import Header, Static, Digits, Placeholder, Footer
from textual.containers import Vertical
from .calculator import Calculator
from .TUI_Shortcuts import ShortcutsPanel
from .TUI_Trace import Trace

class TUI_App(App):
    BINDINGS = [
        ("q", "quit", "Quit Application"),
        ("1", "signal('1')", ""),
        ("2", "signal('2')", ""),
        ("3", "signal('3')", ""),
        ("4", "signal('4')", ""),
        ("5", "signal('5')", ""),
        ("6", "signal('6')", ""),
        ("7", "signal('7')", ""),
        ("8", "signal('8')", ""),
        ("9", "signal('9')", ""),
        ("0", "signal('10')", ""),
        (".", "signal('.')", ""),
        ("enter", "signal('enter')", ""),
        ("space", "signal('enter')", ""),
        ("*", "signal('multiply')", ""),
        ("/", "signal('divide')", ""),
        ("+", "signal('sum')", ""),
        ("-", "signal('subtract')", ""),
        ("s", "signal('sin')", ""),
        ("c", "signal('cos')", ""),
        ("t", "signal('tan')", ""),
        ("S", "signal('asin')", ""),
        ("C", "signal('acos')", ""),
        ("T", "signal('atan')", ""),
        ("^", "signal('power')", ""),
        ("n", "signal('negate')", ""),
        ("w", "signal('swap')", ""),
        ("r", "signal('sqrt')", ""),
        ("p", "signal('pi')", ""),
        ("e", "signal('nat_exp')", ""),
        ("i", "signal('invert')", ""),
        ("l", "signal('ln')", ""),
        ("escape", "signal('clear')", ""),
    ]
    CSS_PATH = "horizontal_layout.tcss"
     
    def __init__(self, calc: Calculator):
        super().__init__()
        self.calc = calc
        self.calc.add_listener(self.update)

        self.t = Digits(classes = "register", id = "t_register", value = self.calc.peek(3))
        self.t.border_title = "T REGISTER"
        self.z = Digits(classes = "register", id = "z_register", value = self.calc.peek(2))
        self.z.border_title = "Z REGISTER"
        self.y = Digits(classes = "register", id = "y_register", value = self.calc.peek(1))
        self.y.border_title = "Y REGISTER"
        self.x = Digits(classes= "register", id = "x_register", value = self.calc.peek())
        self.x.border_title = "X REGISTER"

        self.register_stack = Vertical(self.t,
                                        self.z,
                                        self.y,
                                        self.x,
                                        classes = "register_stack")
        self.register_stack.border_title = "REGISTERS"
        

        self.shortcut_panel = Placeholder(classes = "shortcut_panel")
        self.shortcut_panel.border_title = "SHORTCUTS"

        self.compute_stack = Vertical(self.register_stack,
                                        self.shortcut_panel,
                                        classes = "compute_stack")
        self.compute_stack.border_title = "COMPUTE"

        self.trace = Trace()
        

    def compose(self):
        yield Header()
        yield self.compute_stack
        yield self.trace
        yield Footer()
        self.trace.update(self.calc)

    def on_mount(self):
        self.title = "Anomaly"
        self.sub_title = "An RPN calculator"

    def update(self):
        self.x.update(self.calc.peek())
        self.y.update(self.calc.peek(1))
        self.z.update(self.calc.peek(2))
        self.t.update(self.calc.peek(3))
        self.trace.update(self.calc)

    def action_signal(self, signal: str) -> None:
        self.calc.receive(signal)