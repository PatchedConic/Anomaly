from anomaly.controller import controller
import sys

applicationController = controller.controller()

if __name__ == "__main__":
    sys.exit(applicationController.application.exec())