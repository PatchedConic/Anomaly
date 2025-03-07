from textual.app import App
from textual.widgets import Header, Digits, Placeholder, Footer, Label
from textual.containers import Vertical
from .calculator import Calculator

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
        ("0", "signal('0')", ""),
        (".", "signal('.')", ""),
        ("enter", "signal('enter')", "enter"),
        ("space", "signal('enter')", "enter"),
        ("*", "signal('multiply')", "Multiply"),
        ("/", "signal('divide')", "Divide"),
        ("+", "signal('sum')", "Add"),
        ("-", "signal('subtract')", "Subtract"),
        ("s", "signal('sin')", "sin"),
        ("c", "signal('cos')", "cos"),
        ("t", "signal('tan')", "tan"),
        ("S", "signal('asin')", "asin"),
        ("C", "signal('acos')", "acos"),
        ("T", "signal('atan')", "atan"),
        ("^", "signal('power')", "Power"),
        ("n", "signal('negate')", "negate"),
        ("w", "signal('swap')", "swap"),
        ("r", "signal('sqrt')", "square root"),
        ("p", "signal('pi')", "pi"),
        ("e", "signal('nat_exp')", "natural exponent"),
        ("i", "signal('invert')", "invert"),
        ("l", "signal('ln')", "ln"),
        ("escape", "signal('clear')", "clear"),
        ("backspace", "signal('backspace')", "backspace"),
    ]
    CSS_PATH = "horizontal_layout.tcss"
     
    def __init__(self, calc: Calculator):
        super().__init__()
        self.calc = calc
        self.compute_stack = ComputeStack(self.calc)
        self.trace = Trace(self.calc)
        

    def compose(self):
        yield Header()
        yield self.compute_stack
        yield self.trace
        yield Footer()

    def on_mount(self):
        self.title = "Anomaly"
        self.sub_title = "An RPN calculator"


    def action_signal(self, signal: str) -> None:
        self.calc.receive(signal)

class Trace(Vertical):
    
    def __init__(self, calc: Calculator):
        super().__init__(classes = "trace")
        self.border_title="TRACE"
        self.calc = calc
        self.calc.add_listener(self.update)

    def clear(self) -> None:
        self.remove_children(selector='*')

    def update(self) -> None:
        self.clear()
        for entry in self.calc.history:
            self.mount(Label(entry))


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
        self.mount(self.t, self.z, self.y, self.x)

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