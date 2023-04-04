from anomaly.UI.settings import SettingsDialog
from anomaly.UI import stack
from anomaly.UI import buttons

class UI:
    def __init__(self, parentHandle, layoutHandle, controllerHandle) -> None:
        self.layoutHandle = layoutHandle
        self.parentHandle = parentHandle
        self.controllerHandle = controllerHandle
        self.settings_dialog = SettingsDialog(self.controllerHandle)
        self.create_stackUI(self.layoutHandle)
        self.buttonGrid = buttons.Buttons(self.layoutHandle, self.controllerHandle, parentHandle)

    def create_stackUI(self, layoutHandle):    
        self.stackValue = stack.stack(layoutHandle)



