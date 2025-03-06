from textual.app import App
from textual.widgets import Header, Static, Digits, Placeholder, Footer
from textual.containers import Vertical
from .calculator import Calculator
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
        self.compute_stack = ComputeStack(self.calc)
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


    def action_signal(self, signal: str) -> None:
        self.calc.receive(signal)

class ComputeStack(Vertical):
    def __init__(self, calc: Calculator, **kwargs):
        super().__init__(classes = "compute_stack", **kwargs)
        self.calc = calc
        self.border_title = "COMPUTE"
        self.register_stack = RegisterStack(self.calc)
        self.shortcuts = ShortcutPanel()

    def on_mount(self):
        self.mount(self.register_stack, self.shortcuts)

class ShortcutPanel(Placeholder):
    def __init__(self, **kwargs):
        super().__init__(classes = "shortcut_panel", **kwargs)
        self.border_title = "SHORTCUTS"

class RegisterStack(Vertical):
    def __init__(self, calc: Calculator, **kwargs):
        super().__init__(classes = "register_stack", **kwargs)
        self.calc = calc
        self.border_title = "REGISTERS"
        self.t = Register(self.calc, "T REGISTER", 3)
        self.z = Register(self.calc, "Z REGISTER", 2)
        self.y = Register(self.calc, "Y REGISTER", 1)
        self.x = Register(self.calc, "X REGISTER", 0)

    def on_mount(self):
        self.mount(self.x, self.y, self.z, self.t)

class Register(Digits):
    def __init__(self, calc: Calculator, border_title: str, index: int, **kwargs):
        super().__init__("---", classes = "register", id = f"register_{index}", **kwargs)
        self.calc = calc
        self.index = index
        self.calc.add_listener(self.update_value)
        self.border_title = border_title
        self.update(self.calc.peek(self.index))

    def update_value(self):
        self.update(self.calc.peek(self.index))