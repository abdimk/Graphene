"""
Abdisa Merga(@Abdimk)
2022
"""
from random import shuffle
import shutil
import sys 
import os
from tokenize import PseudoExtras
import traceback
from PyQt6 import *
from PySide2 import *
from PySide2 import QtCore
from PySide2 import QtGui
from PyQt6.QtGui import QIcon
from ui_main_interface import *
from qt_material import *
import psutil
import datetime
import platform
from time import sleep
from multiprocessing import cpu_count
from PySide2extn import *
platforms = {
    'linux' : 'Linux',
    'linux1' : 'Linux',
    'linux2' : 'Linux',
    'darwin': 'OS X',
    'win32' : 'Windows' 
}

class WorkerSignals(QObject):
    def __init__(self):
        super().__init__()
        

    '''
    Defines the signals available from a running worker thread.
    Supported signals are:

    finished 
         No data

    error
        tuple(exctype, value,traceback.format_exc())

    result 
        object data returned from processing, anything

    progress int indicating % progress
    '''

    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)



class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to hundelr work thread setup, signals and
    wrap-up

    :param callback: The function worker thread setup, signals and wrap-up

    :param callback: The Funtion callback to run on this worker thread
    Supplied args and kwargs will be passed through to the runner 
    '''
    def __init__(self, fn, *args, **kwargs) -> None:
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args 
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        #Add the Callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress


    @Slot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs
        '''
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result) # return the result of the processing

        finally:
            self.signals.finished.emit() # Done












class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        apply_stylesheet(app, theme='dark_cyan.xml')
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setGeometry(100,500, 1000,700)
        self.center()
        self.oldPos = self.pos()

        #shadow Effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 550))


        self.ui.centralwidget.setGraphicsEffect(self.shadow)


        self.setWindowIcon(QIcon("icons/tv.svg"))
        self.setWindowTitle("Graphine panel")



        QSizeGrip(self.ui.size_grip)


        #Minimize window
        #self.restore_or_maximize_window()
        self.ui.minmize_window_button.clicked.connect(lambda: self.showMinimized())

        #Close Window
        self.ui.close_window_button.clicked.connect(lambda: self.close())

        #Restore Window
        self.ui.restore_window_button.clicked.connect(lambda: self.restore_or_maximize_window())
    # def restore_or_maximize_window(self, **kwargs):
    #     if self.isMaximized():
    #         self.showNormal()
    #         #self.ui.restoreWindowButton.setIcon(QtGui.QIcon(u""))

    #     else:
    #         self.showMaximized()
    #         #self.ui.restoreWindowButton.setIcon(QtGui.QIcon(u""))




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

        for w in self.ui.menu_frame.findChildren(QPushButton):
            # Add click even listener
            w.clicked.connect(self.applyButtonStyle)


        # Start Thread
        self.threadpool = QThreadPool()
        self.battery()
        #self.cpu_ram()
        self.system_info()
        self.processes()
        self.storage_partions()
        self.sensors_information()
        self.networks()
        self.psutil_thread()





    #create Thread function
    def psutil_thread(self):
        # Live CPU Information
        worker = Worker(self.cpu_ram)

        #Start Worker
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.finished.connect(self.progress_fn)


        battery_worker = Worker(self.battery)

        # battery_worker.signals.result.connect(self.print_output)
        # battery_worker.signals.finished.connect(self.thread_complete)
        # battery_worker.signals.finished.connect(self.progress_fn)

        # Execute
        self.threadpool.start(worker)

    def print_output(self, s): # 
        print(s)

    def thread_complete(self):
        print("THREAD COMPLETE!")

    def progress_fn(self, n=0):
        print("%d%% done" % n)










    #Slide Left menu function
    def SlideLeftMenu(self):
        #get the current left menu width
        width = self.ui.left_menu_const_frame.width()

        #if Minmized 
        if width == 40:
            newwidth = 200
        else: # if maximized 
            #Restore menu
            newwidth = 40

        #Animate
        self.anmation = QPropertyAnimation(self.ui.left_menu_const_frame, b"minimumWidth")

        self.anmation.setDuration(250)
        self.anmation.setStartValue(width)
        self.anmation.setEndValue(newwidth)
        self.anmation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.anmation.start()



    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            #self.ui.restoreWindowButton.setIcon(QtGui.QIcon(u""))

        else:
            self.showMaximized()
            #self.ui.restoreWindowButton.setIcon(QtGui.QIcon(u""))
    def applyButtonStyle(self):
        #Reset style for other buttons
        for w in self.ui.menu_frame.findChildren(QPushButton):
            #if the button name is not equal to clicked button name
            if w.objectName() != self.sender().objectName():
                # Create default style by removing the left border
                w.setStyleSheet("border-bottom: none;")
        
        self.sender().setStyleSheet("border-bottom: 2px solid")
        return 
    #System CPU and RAM information
    def cpu_ram(self, progress_callback):
        #Live CPU and RAM Information 
        while True:
            totalRam = 1.0
            totalRam = psutil.virtual_memory()[0] * totalRam
            totalRam = totalRam / (1024 * 1024 * 1024)
            self.ui.total_ram.setText(str("{:.4f}".format(totalRam) + 'GB'))

            availRam = 1.0 
            #availRam = psutil.virtual_memory([1]) * availRam
            availRam = psutil.virtual_memory()[1] * availRam
            availRam = availRam / (1024 * 1024 * 1024)
            self.ui.available_ram.setText(str("{:.4f}".format(availRam) + 'GB'))



            ramUsed = 1.0
            ramUsed = psutil.virtual_memory()[3] * ramUsed
            ramUsed = ramUsed / (1024 * 1024 * 1024)
            self.ui.used_ram.setText(str("{:.4f}".format(ramUsed) + 'GB'))

            ramFree = 1.0
            ramFree = psutil.virtual_memory()[4] * ramFree
            ramFree = ramFree / (1024 * 1024 * 1024)
            self.ui.free_ram.setText(str("{:.4f}".format(ramFree) + 'GB'))


            core = cpu_count()
            self.ui.cpu_count.setText(str(core))

            ramUsages = str(psutil.virtual_memory()[2]) + "%"
            self.ui.ram_Usage.setText("{:.4f}".format(totalRam) + 'GB')

            cpuPer = psutil.cpu_percent()
            self.ui.cpu_per.setText(str(cpuPer) + "%")


            cpuMainCore = psutil.cpu_count(logical=False)
            self.ui.cpu_main_core.setText(str(cpuMainCore))


            #CPU Percentage Indicator
            #Set Progress Bar Value
            self.ui.cpu_percentage.rpb_setMaximum(100)
            #Set Progress bar Values
            self.ui.cpu_percentage.rpb_setValue(cpuPer)
            #Set Progress Bar Style
            self.ui.cpu_percentage.rpb_setBarStyle('Hybrid2')
            #Set Progress Bar Line Color
            self.ui.cpu_percentage.rpb_setLineColor((255, 30, 99))

            #Set Progress Bar Text Color
            self.ui.cpu_percentage.rpb_setPieColor((45, 74, 83))
            #
            self.ui.cpu_percentage.rpb_setTextColor((255, 255, 255))

            self.ui.cpu_percentage.rpb_setInitialPos('West')

            self.ui.cpu_percentage.rpb_setTextFormat('Percentage')
            #Set Progress Bar Font
            self.ui.cpu_percentage.rpb_setTextFont('Arial')
            #
            self.ui.cpu_percentage.rpb_setLineWidth(15)

            self.ui.cpu_percentage.rpb_setPathWidth(15)

            self.ui.cpu_percentage.rpb_setLineCap('RoundCap')




            #RAM USAGE INDICATOR SPIRAL PROGRESSBAR

            self.ui.ram_percantage.spb_setMinimum((0, 0, 0))

            self.ui.ram_percantage.spb_setMaximum((totalRam, totalRam, totalRam))

            #set progress bar color

            self.ui.ram_percantage.spb_setValue((availRam, ramUsed, ramFree))
            
            self.ui.ram_percantage.spb_lineColor(((6, 233, 38), (6, 201, 233), (233, 6, 201)))
            
            self.ui.ram_percantage.spb_setInitialPos(('West', 'West', 'West'))

            self.ui.ram_percantage.spb_lineWidth(15)

            self.ui.ram_percantage.spb_lineStyle(('SolidLine', 'SolidLine', 'SolidLine'))

            self.ui.ram_percantage.spb_lineCap(('RoundCap','RoundCap','RoundCap'))

            self.ui.ram_percantage.spb_setPathHidden(True)
            
            sleep(1)

    
    # Get System information
    def system_info(self):
        #time = datetime.datetime.now().strftime("%I:%M:%S %P")
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.ui.system_date.setText(str(date))
        #self.ui.system_time.setText(str(time))

        self.ui.system_machine.setText(platform.machine())
        self.ui.system_version.setText(platform.version())
        self.ui.system_platform.setText(platform.platform())
        self.ui.system_system.setText(platform.system())
        self.ui.system_processor.setText(platform.processor())

    #a function to create a tabel widgets
    def create_table_widget(self,rowPosition, columnPosition, text, tableName):
        qtabelwidgetitem = QTableWidgetItem()

        # use getattr()
        getattr(self.ui, tableName).setItem(rowPosition, columnPosition, qtabelwidgetitem)
        qtabelwidgetitem = getattr(self.ui, tableName).item(rowPosition, columnPosition)

        qtabelwidgetitem.setText(text)
    #Running Process
    def processes(self):
        for x in psutil.pids():
            rowPosition = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowPosition)

            try:
                process = psutil.Process(x)

                self.create_table_widget(rowPosition, 0,str(process.pid), "tableWidget")

                self.create_table_widget(rowPosition, 1, process.name(),"tableWidget")

                self.create_table_widget(rowPosition, 2, process.status(), "tableWidget")

                self.create_table_widget(rowPosition, 3, str(datetime.datetime.utcfromtimestamp(process.create_time()).strftime("%Y-%m-%d %H:%M:%S")), 'tableWidget')

                #create a cell widget
                suspend_btn = QPushButton(self.ui.tableWidget)
                suspend_btn.setText('Suspend')
                suspend_btn.setStyleSheet("color: brown")
                self.ui.tableWidget.setCellWidget(rowPosition, 4, suspend_btn)

                resume_btn = QPushButton(self.ui.tableWidget)
                resume_btn.setText('Resume')
                resume_btn.setStyleSheet("color: green")
                self.ui.tableWidget.setCellWidget(rowPosition, 5, resume_btn)

                terminate_btn = QPushButton(self.ui.tableWidget)
                terminate_btn.setText("Terminate")
                terminate_btn.setStyleSheet("color: orange")
                self.ui.tableWidget.setCellWidget(rowPosition, 6, terminate_btn)

                kill_btn = QPushButton(self.ui.tableWidget)
                kill_btn.setText("Kill")
                kill_btn.setStyleSheet("Color: red")
                self.ui.tableWidget.setCellWidget(rowPosition, 7, kill_btn)

            except Exception as e:
                print(e)

            
        self.ui.activity_search.textChanged.connect(self.findName)
    #search activity tabel
    def findName(self):
        name = self.ui.activity_search.text().lower()
        for row in range(self.ui.tableWidget.rowCount()):
            item = self.ui.tableWidget.item(row, 1)

            self.ui.tableWidget.setRowHidden(row, name not in item.text().lower())

    def storage_partions(self):
        global platforms
        storage_device = psutil.disk_partitions(all=False)
        z = 0
        for x in storage_device:
            rowPosition = self.ui.storageTable.rowCount()
            self.ui.storageTable.insertRow(rowPosition)

            self.create_table_widget(rowPosition, 0, x.device, "storageTable")
            self.create_table_widget(rowPosition, 1, x.mountpoint, "storageTable")
            self.create_table_widget(rowPosition, 2, x.fstype, "storageTable")
            self.create_table_widget(rowPosition, 3, x.opts, "storageTable")
            
            if sys.platform == 'linux' or sys.platform =='linux1' or sys.platform =='linux2':
                self.create_table_widget(rowPosition, 4, str(x.maxfile), "storageTable")
                self.create_table_widget(rowPosition, 5, str(x.maxpath), "storageTable")

            elif sys.platform == 'win32':
                self.create_table_widget(rowPosition, 4, str(x.maxfile), "storageTable")
                self.create_table_widget(rowPosition, 5, str(x.maxpath), "storageTable")

            else:
                self.create_table_widget(rowPosition, 4, "Function not available on" + platforms[sys.platform], "storageTable")
                self.create_table_widget(rowPosition, 5, "Function not available on " + platforms[sys.platform], "storageTable")
            
            #print(psutil.disk_usage(x.device))
            disk_usage = shutil.disk_usage(x.mountpoint)

            #print(disk_usage.total)
            self.create_table_widget(rowPosition, 6, str(round((disk_usage.total / (1024 * 1024 * 1024)))) + 'GB', "storageTable")
            self.create_table_widget(rowPosition, 7, str(round((disk_usage.free / (1024 * 1024 * 1024)))) + 'GB', "storageTable")
            self.create_table_widget(rowPosition, 8, str(round((disk_usage.used / (1024 * 1024 * 1024)))) + 'GB', "storageTable")


            full_disk = (disk_usage.used / disk_usage.total) * 100
            progressbar = QProgressBar(self.ui.storageTable)
            progressbar.setObjectName(u"progressbar")
            progressbar.setValue(full_disk)
            self.ui.storageTable.setCellWidget(rowPosition, 9, progressbar)
    
    #Sensor Information
    def sensors_information(self):

        if sys.platform == 'linux' or sys.platform == 'linux1' or sys.platform == 'linux2':

            for x in psutil.sensors_temperatures():
                for y in psutil.sensors_temperatures()[x]:

                    #create new row
                    rowPosition = self.ui.sensorTable.rowCount()
                    self.ui.sensorTable.insertRow(rowPosition)

                    self.create_table_widget(rowPosition, 0, x, "sensorTable")
                    self.create_table_widget(rowPosition, 1, y.label, "sensorTable")
                    self.create_table_widget(rowPosition, 2, str(y.current), "sensorTable")
                    self.create_table_widget(rowPosition, 3, str(y.high), "sensorTable")
                    self.create_table_widget(rowPosition, 4, str(y.critical), "sensorTable")

                    temp_per = (y.current / y.high) * 100
                    progressBar = QProgressBar(self.ui.sensorTable)
                    progressBar.setObjectName(u"progressBar")
                    progressBar.setValue(temp_per)
                    self.ui.sensorTable.setCellWidget(rowPosition, 5, progressBar)
        else:
            global platforms

            rowPosition = self.ui.sensorTable.rowCount()
            self.ui.sensorTable.insertRow(rowPosition)
            self.create_table_widget(rowPosition, 0, "Function is not supported on " + platforms[sys.platform],"sensorTable")

            self.create_table_widget(rowPosition, 1, "N/A", "sensorTable")
            self.create_table_widget(rowPosition, 2, "N/A", "sensorTable")
            self.create_table_widget(rowPosition, 3, "N/A", "sensorTable")
            self.create_table_widget(rowPosition, 4, "N/A", "sensorTable")
            self.create_table_widget(rowPosition, 5, "N/A", "sensorTable")


    #Network Information
    def networks(self):
        for x in psutil.net_if_stats():
            z = psutil.net_if_stats()

            rowPosition = self.ui.net_stats_table.rowCount()
            self.ui.net_stats_table.insertRow(rowPosition)

            self.create_table_widget(rowPosition, 0, x, "net_stats_table")
            self.create_table_widget(rowPosition, 1, str(z[x].isup), "net_stats_table")
            self.create_table_widget(rowPosition, 2, str(z[x].duplex), "net_stats_table")
            self.create_table_widget(rowPosition, 1, str(z[x].speed), "net_stats_table")
            self.create_table_widget(rowPosition, 1, str(z[x].mtu), "net_stats_table")

        #NET IO Counters
        for x in psutil.net_io_counters(pernic=True):
            z = psutil.net_io_counters(pernic=True)

            rowPosition = self.ui.net_io_table.rowCount()
            self.ui.net_io_table.insertRow(rowPosition)

            self.create_table_widget(rowPosition, 0, x, "net_io_table")
            self.create_table_widget(rowPosition, 1, str(z[x].bytes_sent), "net_io_table")
            self.create_table_widget(rowPosition, 2, str(z[x].bytes_recv), "net_io_table")
            self.create_table_widget(rowPosition, 3, str(z[x].packets_sent), "net_io_table")
            self.create_table_widget(rowPosition, 4, str(z[x].packets_recv), "net_io_table")
            self.create_table_widget(rowPosition, 5, str(z[x].errin), "net_io_table")
            self.create_table_widget(rowPosition, 6, str(z[x].errout), "net_io_table")
            self.create_table_widget(rowPosition, 7, str(z[x].dropin), "net_io_table")
            self.create_table_widget(rowPosition, 8, str(z[x].dropout), "net_io_table")

        #Net Addresses
        for x in psutil.net_if_addrs():
            z = psutil.net_if_addrs()

            for y in z[x]:
                rowPosition = self.ui.net_addresses_table.rowCount()
                self.ui.net_addresses_table.insertRow(rowPosition)

                self.create_table_widget(rowPosition, 0, str(x), "net_addresses_table")
                self.create_table_widget(rowPosition, 1, str(y.family), "net_addresses_table")
                self.create_table_widget(rowPosition, 2, str(y.address), "net_addresses_table")
                self.create_table_widget(rowPosition, 3, str(y.netmask), "net_addresses_table")
                self.create_table_widget(rowPosition, 4, str(y.broadcast), "net_addresses_table")
                self.create_table_widget(rowPosition, 5, str(y.ptp), "net_addresses_table")
        
        #Net Connections
        for x in psutil.net_connections():
            z = psutil.net_connections()

            rowPosition = self.ui.net_connections_table.rowCount()
            self.ui.net_connections_table.insertRow(rowPosition)


            self.create_table_widget(rowPosition, 0, str(x.fd), "net_connections_table")
            self.create_table_widget(rowPosition, 1, str(x.family), "net_connections_table")    
            self.create_table_widget(rowPosition, 2, str(x.type), "net_connections_table")
            self.create_table_widget(rowPosition, 3, str(x.laddr), "net_connections_table")
            self.create_table_widget(rowPosition, 4, str(x.raddr), "net_connections_table")
            self.create_table_widget(rowPosition, 5, str(x.status), "net_connections_table")
            self.create_table_widget(rowPosition, 6, str(x.pid), "net_connections_table")
            


            
























    # A Python Fucntion to convert seconds to hours 
    # The F**K you say! don't even think about it (to use datetime)
    def secs2hours(self, secs):
        mm,ss = divmod(secs, 60)
        hh, mm = divmod(mm, 60)

        return "%d:%02d:%02d (H:M:S)" % (hh, mm, ss)

    def battery(self):
        batt = psutil.sensors_battery()

        if not hasattr(psutil, "sensors_battery"):
            self.ui.battery_status.setText("Platform not supported")

        if batt is None:
            self.ui.battery_status.setText("No battery installed")
        
        if batt.power_plugged:
            self.ui.battery_charge.setText(str(round(batt.percent,2))+"%")
            self.ui.battery_time_left.setText("N/A")
            if batt.percent < 100:
                self.ui.battery_status.setText("Charging")
            else:
                self.ui.battery_status.setText("Fully Charged")

            self.ui.battery_plugged.setText("Yes")
        else:
            self.ui.battery_charge.setText(str(round(batt.percent, 2))+"%")
            self.ui.battery_time_left.setText(self.secs2hours(batt.secsleft))
            if batt.percent < 100:
                self.ui.battery_status.setText("Discharging")
            else:
                self.ui.battery_status.setText("Fully Charged")

            self.ui.battery_plugged.setText("No")
        #BATTERY POWER INDICATOR USING ROUND PROGRESS BAR
        self.ui.battery_usage.rpb_setMaximum(100)
        #Set Progress Values
        self.ui.battery_usage.rpb_setValue(batt.percent)
        #Set Progress Bar Style
        self.ui.battery_usage.rpb_setBarStyle('Hybrid2')
        #Set Progress Bar Line Color
        self.ui.battery_usage.rpb_setLineColor((225, 30, 99))
        #Set Progress Bar Line Color
        self.ui.battery_usage.rpb_setPieColor((45, 74, 83))

        #Set Progress Bar Text Color
        self.ui.battery_usage.rpb_setTextColor((255, 255, 255))

        #Set Progress Bar Starting Postion
        self.ui.battery_usage.rpb_setInitialPos('West')

        #Set Progress Bar Text Type
        self.ui.battery_usage.rpb_setTextFormat('Percentage')

        #Set Progress Bar Font
        self.ui.battery_usage.rpb_setLineWidth(15)

        #Progress Bar Line Width
        self.ui.battery_usage.rpb_setPathWidth(15)

        #Set Progress Bar Line Cap
        self.ui.battery_usage.rpb_setLineCap('RoundCap')










app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())

