import sys
from PySide2.QtWidgets import QApplication
from Settings import ui_attributes
from PySide2.QtCore import QThreadPool
from qt_material import *


class Run_App(ui_attributes.MainWindow):
    def __init__(self):
        super().__init__()
        apply_stylesheet(app, theme='dark_cyan.xml')
        self.threadpool = QThreadPool()
        #self.battery()
        #self.cpu_ram()
        #self.system_info()
        self.processes()
        self.storage_partions()
        self.sensors_information()
        self.networks()
        self.show()
        self.psutil_thread()



if __name__=="__main__":
    app = QApplication(sys.argv)
    main_window = Run_App()
    sys.exit(app.exec_())