import sys
# from anomaly import entry
from anomaly.controller import controller

applicationController = controller.controller()

if __name__ == "__main__":
    sys.exit(applicationController.application.exec())
    
