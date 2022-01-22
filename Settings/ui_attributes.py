import os
import sys
from PySide2 import *
from qt_material import *
from PySide2 import QtCore,QtGui
from custom_UI.ui_main_interface import *
import PySide2extn
import ctypes
from Functions.battery import BatteyPlugin
from Functions.CPUandRAM import CPUANDRAM
from Futures.slideMenu import SlideClassMenu
from Functions.systemInfo import SYSTEMINFO
from Functions.process import RunningProcess
from Functions.storage import STORAGE
from Functions.sensors import SENSORS
from Functions.mynetwork import NETWORKS
from locathreading.workerfunction import Worker,WorkerSignals


class MainWindow(QMainWindow,SlideClassMenu,BatteyPlugin,CPUANDRAM,SYSTEMINFO,RunningProcess,STORAGE,SENSORS,NETWORKS,Worker,WorkerSignals):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #apply_stylesheet(app, theme='dark_cyan.xml')

        #removing the title window by setting framelesswindowhit
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 550))
        self.myappid = 'mycompany.myproduct.subproduct.version'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(self.myappid)
        self.sysicon = QSystemTrayIcon(QIcon("custom_UI/icons/b.png"),parent=self)
        self.sysicon.setToolTip('Graphene')

        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        self.setWindowIcon(QIcon("custom_UI/icons/tv.svg"))
        self.setWindowTitle("Graphene")
        QSizeGrip(self.ui.size_grip)


        #Minimize window
        #self.restore_or_maximize_window()
        self.ui.minmize_window_button.clicked.connect(lambda: self.showMinimized())

        #Close Window
        self.ui.close_window_button.clicked.connect(lambda: self.close())

        #Restore Window
        self.ui.restore_window_button.clicked.connect(lambda: self.restore_or_maximize_window())

        ########################################################################
        #NAVIGATION
        ########################################################################
        #Navigate to the CPU page 
        self.ui.cpu_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.cpu_and_memory))

        #Navigate to Battery page
        self.ui.battery_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.battery))

        #Navigate to system info
        self.ui.system_information_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.system_information))
        
        #Navigate to activities page
        self.ui.activity_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.activities))

        #Navigate to storage page 
        self.ui.storage_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.storage))

        #Navigate to sensors page
        self.ui.sensors_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.sensor)) 

        #Navigate to network page
        self.ui.network_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.network))      

        self.ui.open_close_slider_bar_button.clicked.connect(lambda: self.SlideLeftMenu())
        ###################################################################################

        for w in self.ui.menu_frame.findChildren(QPushButton):
            # Add click even listener
            w.clicked.connect(self.applyButtonStyle)

    def applyButtonStyle(self):
        #Reset style for other buttons
        for w in self.ui.menu_frame.findChildren(QPushButton):
            #if the button name is not equal to clicked button name
            if w.objectName() != self.sender().objectName():
                # Create default style by removing the left border
                w.setStyleSheet("border-bottom: none;")
        
        self.sender().setStyleSheet("border-bottom: 2px solid")
        return         

    def restore_or_maximize_window(self, **kwargs):
        if self.isMaximized():
            self.showNormal()
            #self.ui.restore_window_button.setIcon(QtGui.QIcon(u""))

        else:
            self.showMaximized()
            #self.ui.restore_window_button.setIcon(QtGui.QIcon(u""))

    ################################################################
    #Function to Move the Window on  mouse drag event on the title bar
    ################################################################


    # def center(self):
    #     qr = self.frameGeometry()
    #     cp = QDesktopWidget().availableGeometry().center()
    #     qr.moveCenter(cp)
    #     self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    ############################################################
    #create Thread function
    def psutil_thread(self):
        # Live CPU Information
        worker = Worker(self.cpu_ram)
        #1
        #Start Worker
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.finished.connect(self.progress_fn)
        self.threadpool.start(worker)

        #2
        battery_worker = Worker(self.battery)

        battery_worker.signals.result.connect(self.print_output)
        battery_worker.signals.finished.connect(self.thread_complete)
        battery_worker.signals.finished.connect(self.progress_fn)

        # Execute
        self.threadpool.start(battery_worker)

        #3
        system_info_worker = Worker(self.system_info)

        system_info_worker.signals.result.connect(self.print_output)
        system_info_worker.signals.finished.connect(self.thread_complete)
        system_info_worker.signals.finished.connect(self.progress_fn)

        # Execute
        self.threadpool.start(system_info_worker)


    def print_output(self, s): # 
        print(s)

    def thread_complete(self):
        print("THREAD COMPLETE!")

    def progress_fn(self, n=0):
        print("%d%% done" % n)









