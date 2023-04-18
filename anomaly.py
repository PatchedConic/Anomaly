# import runpy
# runpy.run_module('anomaly', run_name='__main__')
import sys
import anomaly

if __name__ == "__main__":
    sys.exit(anomaly.applicationController.application.exec())