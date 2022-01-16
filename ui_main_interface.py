from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2extn.RoundProgressBar import roundProgressBar
from PySide2extn.SpiralProgressBar import spiralProgressBar

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(629, 506)
        MainWindow.setStyleSheet(u"*{\n"
"border:none;\n"
"background-color:\"#001f3f\";\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"*{\n"
"background-color:\"#001f3f\";\n"
"}")
        self.header_frame.setFrameShape(QFrame.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_left_frame = QFrame(self.header_frame)
        self.header_left_frame.setObjectName(u"header_left_frame")
        self.header_left_frame.setStyleSheet(u"padding:0;\n"
"margin:0;\n"
"")
        self.header_left_frame.setFrameShape(QFrame.StyledPanel)
        self.header_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_left_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.open_close_slider_bar_button = QPushButton(self.header_left_frame)
        self.open_close_slider_bar_button.setObjectName(u"open_close_slider_bar_button")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.open_close_slider_bar_button.setFont(font)
        self.open_close_slider_bar_button.setStyleSheet(u"margin:0;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/menumulti.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.open_close_slider_bar_button.setIcon(icon)
        self.open_close_slider_bar_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.open_close_slider_bar_button, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.header_left_frame, 0, Qt.AlignLeft)

        self.header_center_frame = QFrame(self.header_frame)
        self.header_center_frame.setObjectName(u"header_center_frame")
        self.header_center_frame.setFrameShape(QFrame.StyledPanel)
        self.header_center_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_center_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.header_center_frame)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.header_center_frame)

        self.header_right_frame = QFrame(self.header_frame)
        self.header_right_frame.setObjectName(u"header_right_frame")
        self.header_right_frame.setFrameShape(QFrame.StyledPanel)
        self.header_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_right_frame)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minmize_window_button = QPushButton(self.header_right_frame)
        self.minmize_window_button.setObjectName(u"minmize_window_button")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/minimize 1.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minmize_window_button.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.minmize_window_button)

        self.restore_window_button = QPushButton(self.header_right_frame)
        self.restore_window_button.setObjectName(u"restore_window_button")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.restore_window_button)

        self.close_window_button = QPushButton(self.header_right_frame)
        self.close_window_button.setObjectName(u"close_window_button")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/close-error.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.close_window_button)


        self.horizontalLayout.addWidget(self.header_right_frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_body_frame = QFrame(self.centralwidget)
        self.main_body_frame.setObjectName(u"main_body_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body_frame.sizePolicy().hasHeightForWidth())
        self.main_body_frame.setSizePolicy(sizePolicy)
        self.main_body_frame.setFrameShape(QFrame.StyledPanel)
        self.main_body_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.main_body_frame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.left_menu_const_frame = QFrame(self.main_body_frame)
        self.left_menu_const_frame.setObjectName(u"left_menu_const_frame")
        self.left_menu_const_frame.setMinimumSize(QSize(40, 0))
        self.left_menu_const_frame.setMaximumSize(QSize(20, 16777215))
        self.left_menu_const_frame.setStyleSheet(u"background-color: rgb(0, 31, 63);")
        self.left_menu_const_frame.setFrameShape(QFrame.StyledPanel)
        self.left_menu_const_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.left_menu_const_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.menu_frame = QFrame(self.left_menu_const_frame)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMinimumSize(QSize(100, 0))
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.menu_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.activity_button = QPushButton(self.menu_frame)
        self.activity_button.setObjectName(u"activity_button")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/electrical-sensor.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.activity_button.setIcon(icon4)
        self.activity_button.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.activity_button, 3, 0, 1, 1, Qt.AlignLeft)

        self.system_information_button = QPushButton(self.menu_frame)
        self.system_information_button.setObjectName(u"system_information_button")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/computer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.system_information_button.setIcon(icon5)
        self.system_information_button.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.system_information_button, 2, 0, 1, 1, Qt.AlignLeft)

        self.battery_button = QPushButton(self.menu_frame)
        self.battery_button.setObjectName(u"battery_button")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/batterybv.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.battery_button.setIcon(icon6)
        self.battery_button.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.battery_button, 1, 0, 1, 1, Qt.AlignLeft)

        self.cpu_button = QPushButton(self.menu_frame)
        self.cpu_button.setObjectName(u"cpu_button")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/externalpng.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cpu_button.setIcon(icon7)
        self.cpu_button.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.cpu_button, 0, 0, 1, 1, Qt.AlignLeft)

        self.label_3 = QLabel(self.menu_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setMargin(5)

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1, Qt.AlignLeft)

        self.storage_button = QPushButton(self.menu_frame)
        self.storage_button.setObjectName(u"storage_button")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/folder-data-storage.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.storage_button.setIcon(icon8)
        self.storage_button.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.storage_button, 4, 0, 1, 1, Qt.AlignLeft)

        self.sensors_button = QPushButton(self.menu_frame)
        self.sensors_button.setObjectName(u"sensors_button")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/network-share.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sensors_button.setIcon(icon9)
        self.sensors_button.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.sensors_button, 5, 0, 1, 1, Qt.AlignLeft)

        self.network_button = QPushButton(self.menu_frame)
        self.network_button.setObjectName(u"network_button")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/network (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.network_button.setIcon(icon10)
        self.network_button.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.network_button, 6, 0, 1, 1, Qt.AlignLeft)

        self.label_4 = QLabel(self.menu_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4.setMargin(5)

        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1, Qt.AlignLeft)

        self.label_5 = QLabel(self.menu_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_5.setMargin(5)

        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1, Qt.AlignLeft)

        self.label_6 = QLabel(self.menu_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_6.setMargin(5)

        self.gridLayout.addWidget(self.label_6, 3, 1, 1, 1, Qt.AlignLeft)

        self.label_7 = QLabel(self.menu_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_7.setMargin(5)

        self.gridLayout.addWidget(self.label_7, 4, 1, 1, 1, Qt.AlignLeft)

        self.label_8 = QLabel(self.menu_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_8.setMargin(5)

        self.gridLayout.addWidget(self.label_8, 5, 1, 1, 1, Qt.AlignLeft)

        self.label_9 = QLabel(self.menu_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_9.setMargin(5)

        self.gridLayout.addWidget(self.label_9, 6, 1, 1, 1, Qt.AlignLeft)


        self.horizontalLayout_8.addWidget(self.menu_frame, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_7.addWidget(self.left_menu_const_frame)

        self.main_body_contents_frame = QFrame(self.main_body_frame)
        self.main_body_contents_frame.setObjectName(u"main_body_contents_frame")
        self.main_body_contents_frame.setFrameShape(QFrame.StyledPanel)
        self.main_body_contents_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.main_body_contents_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget = QStackedWidget(self.main_body_contents_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.cpu_and_memory = QWidget()
        self.cpu_and_memory.setObjectName(u"cpu_and_memory")
        self.verticalLayout_4 = QVBoxLayout(self.cpu_and_memory)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.cpu_info_frame = QFrame(self.cpu_and_memory)
        self.cpu_info_frame.setObjectName(u"cpu_info_frame")
        self.cpu_info_frame.setFrameShape(QFrame.StyledPanel)
        self.cpu_info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.cpu_info_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.cpu_main_core = QLabel(self.cpu_info_frame)
        self.cpu_main_core.setObjectName(u"cpu_main_core")
        self.cpu_main_core.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.cpu_main_core, 2, 3, 1, 1)

        self.cpu_per = QLabel(self.cpu_info_frame)
        self.cpu_per.setObjectName(u"cpu_per")
        self.cpu_per.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.cpu_per, 3, 3, 1, 1)

        self.label_13 = QLabel(self.cpu_info_frame)
        self.label_13.setObjectName(u"label_13")
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_13, 3, 0, 1, 1)

        self.label_10 = QLabel(self.cpu_info_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)

        self.cpu_count = QLabel(self.cpu_info_frame)
        self.cpu_count.setObjectName(u"cpu_count")
        self.cpu_count.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.cpu_count, 0, 3, 1, 1)

        self.label_11 = QLabel(self.cpu_info_frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)

        self.cpu_percentage = roundProgressBar(self.cpu_info_frame)
        self.cpu_percentage.setObjectName(u"cpu_percentage")
        self.cpu_percentage.setMinimumSize(QSize(150, 150))
        self.cpu_percentage.setMaximumSize(QSize(150, 150))

        self.gridLayout_2.addWidget(self.cpu_percentage, 0, 4, 4, 1)


        self.verticalLayout_4.addWidget(self.cpu_info_frame)

        self.ram_info_frame = QFrame(self.cpu_and_memory)
        self.ram_info_frame.setObjectName(u"ram_info_frame")
        self.ram_info_frame.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.ram_info_frame.setFrameShape(QFrame.StyledPanel)
        self.ram_info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.ram_info_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.total_ram = QLabel(self.ram_info_frame)
        self.total_ram.setObjectName(u"total_ram")

        self.gridLayout_3.addWidget(self.total_ram, 0, 1, 1, 1)

        self.used_ram = QLabel(self.ram_info_frame)
        self.used_ram.setObjectName(u"used_ram")

        self.gridLayout_3.addWidget(self.used_ram, 2, 1, 1, 1)

        self.label_19 = QLabel(self.ram_info_frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font2)

        self.gridLayout_3.addWidget(self.label_19, 3, 0, 1, 1)

        self.label_18 = QLabel(self.ram_info_frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font2)

        self.gridLayout_3.addWidget(self.label_18, 2, 0, 1, 1)

        self.label_20 = QLabel(self.ram_info_frame)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font2)

        self.gridLayout_3.addWidget(self.label_20, 4, 0, 1, 1)

        self.free_ram = QLabel(self.ram_info_frame)
        self.free_ram.setObjectName(u"free_ram")

        self.gridLayout_3.addWidget(self.free_ram, 3, 1, 1, 1)

        self.available_ram = QLabel(self.ram_info_frame)
        self.available_ram.setObjectName(u"available_ram")

        self.gridLayout_3.addWidget(self.available_ram, 1, 1, 1, 1)

        self.ram_Usage = QLabel(self.ram_info_frame)
        self.ram_Usage.setObjectName(u"ram_Usage")

        self.gridLayout_3.addWidget(self.ram_Usage, 4, 1, 1, 1)

        self.label_16 = QLabel(self.ram_info_frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)

        self.gridLayout_3.addWidget(self.label_16, 0, 0, 1, 1)

        self.label_17 = QLabel(self.ram_info_frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font2)

        self.gridLayout_3.addWidget(self.label_17, 1, 0, 1, 1)

        self.ram_percantage = spiralProgressBar(self.ram_info_frame)
        self.ram_percantage.setObjectName(u"ram_percantage")
        self.ram_percantage.setMaximumSize(QSize(150, 150))

        self.gridLayout_3.addWidget(self.ram_percantage, 0, 2, 5, 1)


        self.verticalLayout_4.addWidget(self.ram_info_frame)

        self.stackedWidget.addWidget(self.cpu_and_memory)
        self.battery = QWidget()
        self.battery.setObjectName(u"battery")
        self.verticalLayout_5 = QVBoxLayout(self.battery)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_26 = QLabel(self.battery)
        self.label_26.setObjectName(u"label_26")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_26.setFont(font3)
        self.label_26.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.label_26)

        self.frame = QFrame(self.battery)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFont(font2)
        self.frame.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_27 = QLabel(self.frame)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font2)

        self.gridLayout_6.addWidget(self.label_27, 0, 0, 1, 1)

        self.battery_plugged = QLabel(self.frame)
        self.battery_plugged.setObjectName(u"battery_plugged")

        self.gridLayout_6.addWidget(self.battery_plugged, 3, 1, 1, 1)

        self.label_28 = QLabel(self.frame)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font2)

        self.gridLayout_6.addWidget(self.label_28, 1, 0, 1, 1)

        self.battery_charge = QLabel(self.frame)
        self.battery_charge.setObjectName(u"battery_charge")

        self.gridLayout_6.addWidget(self.battery_charge, 1, 1, 1, 1)

        self.label_29 = QLabel(self.frame)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font2)

        self.gridLayout_6.addWidget(self.label_29, 2, 0, 1, 1)

        self.battery_time_left = QLabel(self.frame)
        self.battery_time_left.setObjectName(u"battery_time_left")

        self.gridLayout_6.addWidget(self.battery_time_left, 2, 1, 1, 1)

        self.label_30 = QLabel(self.frame)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font2)

        self.gridLayout_6.addWidget(self.label_30, 3, 0, 1, 1)

        self.battery_status = QLabel(self.frame)
        self.battery_status.setObjectName(u"battery_status")

        self.gridLayout_6.addWidget(self.battery_status, 0, 1, 1, 1)

        self.battery_usage = roundProgressBar(self.frame)
        self.battery_usage.setObjectName(u"battery_usage")
        self.battery_usage.setMinimumSize(QSize(150, 150))
        self.battery_usage.setMaximumSize(QSize(150, 150))

        self.gridLayout_6.addWidget(self.battery_usage, 0, 2, 4, 1)


        self.verticalLayout_5.addWidget(self.frame)

        self.stackedWidget.addWidget(self.battery)
        self.system_information = QWidget()
        self.system_information.setObjectName(u"system_information")
        self.verticalLayout_6 = QVBoxLayout(self.system_information)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_2 = QFrame(self.system_information)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.system_system = QLabel(self.frame_2)
        self.system_system.setObjectName(u"system_system")
        self.system_system.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.system_system, 1, 0, 1, 1)

        self.label_45 = QLabel(self.frame_2)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font2)
        self.label_45.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.label_45, 4, 2, 1, 1)

        self.label_38 = QLabel(self.frame_2)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font2)
        self.label_38.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.label_38, 4, 0, 1, 1)

        self.system_platform = QLabel(self.frame_2)
        self.system_platform.setObjectName(u"system_platform")
        self.system_platform.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.system_platform, 2, 1, 1, 1)

        self.label_43 = QLabel(self.frame_2)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font2)
        self.label_43.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.label_43, 2, 2, 1, 1)

        self.label_39 = QLabel(self.frame_2)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font2)
        self.label_39.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.label_39, 3, 0, 1, 1)

        self.label_44 = QLabel(self.frame_2)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font2)
        self.label_44.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.label_44, 3, 2, 1, 1)

        self.label_37 = QLabel(self.frame_2)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font2)
        self.label_37.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.label_37, 2, 0, 1, 1)

        self.system_version = QLabel(self.frame_2)
        self.system_version.setObjectName(u"system_version")
        self.system_version.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.system_version, 3, 1, 1, 1)

        self.system_date = QLabel(self.frame_2)
        self.system_date.setObjectName(u"system_date")
        self.system_date.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.system_date, 4, 1, 1, 1)

        self.label_35 = QLabel(self.frame_2)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font3)
        self.label_35.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.label_35, 0, 0, 1, 1, Qt.AlignTop)

        self.system_processor = QLabel(self.frame_2)
        self.system_processor.setObjectName(u"system_processor")
        self.system_processor.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.system_processor, 2, 3, 1, 1)

        self.system_machine = QLabel(self.frame_2)
        self.system_machine.setObjectName(u"system_machine")
        self.system_machine.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.system_machine, 3, 3, 1, 1)

        self.system_time = QLabel(self.frame_2)
        self.system_time.setObjectName(u"system_time")
        self.system_time.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.system_time, 4, 3, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.system_information)
        self.activities = QWidget()
        self.activities.setObjectName(u"activities")
        self.verticalLayout_7 = QVBoxLayout(self.activities)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_3 = QFrame(self.activities)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setMinimumSize(QSize(250, 0))
        self.frame_6.setMaximumSize(QSize(400, 16777215))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.activity_search = QLineEdit(self.frame_6)
        self.activity_search.setObjectName(u"activity_search")
        self.activity_search.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 58, 85);")

        self.horizontalLayout_9.addWidget(self.activity_search)

        self.pushButton_3 = QPushButton(self.frame_6)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon11)
        self.pushButton_3.setIconSize(QSize(30, 20))

        self.horizontalLayout_9.addWidget(self.pushButton_3)


        self.gridLayout_5.addWidget(self.frame_6, 1, 1, 1, 1, Qt.AlignRight)

        self.label_49 = QLabel(self.frame_3)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font3)
        self.label_49.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.label_49, 0, 0, 1, 1)

        self.label_50 = QLabel(self.frame_3)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_5.addWidget(self.label_50, 1, 0, 1, 1)

        self.label_51 = QLabel(self.frame_3)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_5.addWidget(self.label_51, 2, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.activities)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tableWidget = QTableWidget(self.frame_4)
        if (self.tableWidget.columnCount() < 9):
            self.tableWidget.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(0, 0))
        self.tableWidget.setStyleSheet(u"background-color:\"#001f3f\";\n"
"")

        self.verticalLayout_8.addWidget(self.tableWidget, 0, Qt.AlignVCenter)


        self.verticalLayout_7.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.activities)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pushButton_4 = QPushButton(self.frame_5)
        self.pushButton_4.setObjectName(u"pushButton_4")
        font4 = QFont()
        font4.setFamily(u"MS Shell Dlg 2")
        font4.setPointSize(8)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(9)
        self.pushButton_4.setFont(font4)

        self.horizontalLayout_10.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font4)

        self.horizontalLayout_10.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_5)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_10.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frame_5)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_10.addWidget(self.pushButton_7)


        self.verticalLayout_7.addWidget(self.frame_5, 0, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.activities)
        self.storage = QWidget()
        self.storage.setObjectName(u"storage")
        self.verticalLayout_9 = QVBoxLayout(self.storage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_52 = QLabel(self.storage)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font3)
        self.label_52.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.label_52)

        self.storageTable = QTableWidget(self.storage)
        if (self.storageTable.columnCount() < 9):
            self.storageTable.setColumnCount(9)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(6, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(7, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(8, __qtablewidgetitem17)
        self.storageTable.setObjectName(u"storageTable")

        self.verticalLayout_9.addWidget(self.storageTable)

        self.stackedWidget.addWidget(self.storage)
        self.sensor = QWidget()
        self.sensor.setObjectName(u"sensor")
        self.verticalLayout_10 = QVBoxLayout(self.sensor)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_53 = QLabel(self.sensor)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font3)
        self.label_53.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_10.addWidget(self.label_53)

        self.sensorTable = QTableWidget(self.sensor)
        if (self.sensorTable.columnCount() < 6):
            self.sensorTable.setColumnCount(6)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.sensorTable.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.sensorTable.setHorizontalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.sensorTable.setHorizontalHeaderItem(2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.sensorTable.setHorizontalHeaderItem(3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.sensorTable.setHorizontalHeaderItem(4, __qtablewidgetitem22)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.Dense6Pattern)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setForeground(brush);
        self.sensorTable.setHorizontalHeaderItem(5, __qtablewidgetitem23)
        self.sensorTable.setObjectName(u"sensorTable")

        self.verticalLayout_10.addWidget(self.sensorTable)

        self.stackedWidget.addWidget(self.sensor)
        self.network = QWidget()
        self.network.setObjectName(u"network")
        self.verticalLayout_11 = QVBoxLayout(self.network)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.scrollArea = QScrollArea(self.network)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -422, 518, 772))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, -1, 0)
        self.frame_7 = QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_7)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_54 = QLabel(self.frame_7)
        self.label_54.setObjectName(u"label_54")
        font5 = QFont()
        font5.setFamily(u"MS Shell Dlg 2")
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setWeight(75)
        self.label_54.setFont(font5)
        self.label_54.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_13.addWidget(self.label_54)

        self.net_stats_table = QTableWidget(self.frame_7)
        if (self.net_stats_table.columnCount() < 5):
            self.net_stats_table.setColumnCount(5)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(3, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(4, __qtablewidgetitem28)
        self.net_stats_table.setObjectName(u"net_stats_table")
        self.net_stats_table.setMinimumSize(QSize(0, 150))

        self.verticalLayout_13.addWidget(self.net_stats_table)


        self.verticalLayout_14.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_8)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_55 = QLabel(self.frame_8)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font3)
        self.label_55.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_12.addWidget(self.label_55)

        self.net_io_table = QTableWidget(self.frame_8)
        if (self.net_io_table.columnCount() < 9):
            self.net_io_table.setColumnCount(9)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(2, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(3, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(4, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(5, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(6, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(7, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(8, __qtablewidgetitem37)
        self.net_io_table.setObjectName(u"net_io_table")
        self.net_io_table.setMinimumSize(QSize(0, 150))

        self.verticalLayout_12.addWidget(self.net_io_table)


        self.verticalLayout_14.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.scrollAreaWidgetContents)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_9)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_56 = QLabel(self.frame_9)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font3)
        self.label_56.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_15.addWidget(self.label_56)

        self.net_addresses_table = QTableWidget(self.frame_9)
        if (self.net_addresses_table.columnCount() < 6):
            self.net_addresses_table.setColumnCount(6)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(2, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(3, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(4, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(5, __qtablewidgetitem43)
        self.net_addresses_table.setObjectName(u"net_addresses_table")
        self.net_addresses_table.setMinimumSize(QSize(0, 150))

        self.verticalLayout_15.addWidget(self.net_addresses_table)


        self.verticalLayout_14.addWidget(self.frame_9)

        self.frame_11 = QFrame(self.scrollAreaWidgetContents)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_11)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_57 = QLabel(self.frame_11)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font3)
        self.label_57.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_16.addWidget(self.label_57)

        self.net_connections_table = QTableWidget(self.frame_11)
        if (self.net_connections_table.columnCount() < 8):
            self.net_connections_table.setColumnCount(8)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(0, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(1, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(2, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(3, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(4, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(5, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(6, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(7, __qtablewidgetitem51)
        self.net_connections_table.setObjectName(u"net_connections_table")
        self.net_connections_table.setMinimumSize(QSize(0, 150))
        self.net_connections_table.setStyleSheet(u"")

        self.verticalLayout_16.addWidget(self.net_connections_table)


        self.verticalLayout_14.addWidget(self.frame_11)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_11.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.network)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout_7.addWidget(self.main_body_contents_frame)


        self.verticalLayout.addWidget(self.main_body_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.NoFrame)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.footer_left_frame = QFrame(self.footer_frame)
        self.footer_left_frame.setObjectName(u"footer_left_frame")
        self.footer_left_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.footer_left_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.footer_left_frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignLeft)


        self.horizontalLayout_5.addWidget(self.footer_left_frame)

        self.footer_right_frame = QFrame(self.footer_frame)
        self.footer_right_frame.setObjectName(u"footer_right_frame")
        self.footer_right_frame.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.footer_right_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.footer_right_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_2 = QPushButton(self.footer_right_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_6.addWidget(self.pushButton_2)


        self.horizontalLayout_5.addWidget(self.footer_right_frame, 0, Qt.AlignRight)

        self.size_grip = QFrame(self.footer_frame)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.size_grip, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer_frame, 0, Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.open_close_slider_bar_button.setText(QCoreApplication.translate("MainWindow", u"  Menu", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"GRAPHENE  MANGER", None))
        self.minmize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_window_button.setText("")
        self.activity_button.setText("")
        self.system_information_button.setText("")
        self.battery_button.setText("")
        self.cpu_button.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.storage_button.setText("")
        self.sensors_button.setText("")
        self.network_button.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Battery", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"System inforamtion", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Activity", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Storage", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Sensers", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Network", None))
        self.cpu_main_core.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.cpu_per.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"CPU Per", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"CPU Count", None))
        self.cpu_count.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"CPU Main Core", None))
        self.total_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.used_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Free RAM", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Used RAM", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Ram Usage", None))
        self.free_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.available_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.ram_Usage.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Total RAM", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Avalible RAM", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Battery Information", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.battery_plugged.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Charge", None))
        self.battery_charge.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Time Left", None))
        self.battery_time_left.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Plugged In", None))
        self.battery_status.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_system.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"System Time", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"System Date", None))
        self.system_platform.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Processor", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Machine", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Platform", None))
        self.system_version.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_date.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"System Information", None))
        self.system_processor.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_machine.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_time.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.activity_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Processes", None))
        self.pushButton_3.setText("")
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Activities", None))
        self.label_50.setText("")
        self.label_51.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Process ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Process Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Process Status", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Suspend", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Started ", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Resume", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Terminate", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Kill", None));
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Suspend", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Resume", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Terminate", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Kill", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Disk Partions", None))
        ___qtablewidgetitem8 = self.storageTable.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Devices", None));
        ___qtablewidgetitem9 = self.storageTable.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"MountPoint", None));
        ___qtablewidgetitem10 = self.storageTable.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Max File", None));
        ___qtablewidgetitem11 = self.storageTable.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"FS Type", None));
        ___qtablewidgetitem12 = self.storageTable.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Used Storage", None));
        ___qtablewidgetitem13 = self.storageTable.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Opts", None));
        ___qtablewidgetitem14 = self.storageTable.horizontalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Total Storage", None));
        ___qtablewidgetitem15 = self.storageTable.horizontalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Free Storage", None));
        ___qtablewidgetitem16 = self.storageTable.horizontalHeaderItem(8)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Used Storage", None));
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Sensors", None))
        ___qtablewidgetitem17 = self.sensorTable.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Sensor", None));
        ___qtablewidgetitem18 = self.sensorTable.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Label", None));
        ___qtablewidgetitem19 = self.sensorTable.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Current", None));
        ___qtablewidgetitem20 = self.sensorTable.horizontalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Temprature", None));
        ___qtablewidgetitem21 = self.sensorTable.horizontalHeaderItem(4)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Critical", None));
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        ___qtablewidgetitem22 = self.net_stats_table.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"ISUP", None));
        ___qtablewidgetitem23 = self.net_stats_table.horizontalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Duplex", None));
        ___qtablewidgetitem24 = self.net_stats_table.horizontalHeaderItem(3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Speed", None));
        ___qtablewidgetitem25 = self.net_stats_table.horizontalHeaderItem(4)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"MTU", None));
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Network IO Counter", None))
        ___qtablewidgetitem26 = self.net_io_table.horizontalHeaderItem(1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Bytes Sent", None));
        ___qtablewidgetitem27 = self.net_io_table.horizontalHeaderItem(2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Bytes Recived", None));
        ___qtablewidgetitem28 = self.net_io_table.horizontalHeaderItem(3)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Packets Sent", None));
        ___qtablewidgetitem29 = self.net_io_table.horizontalHeaderItem(4)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Packets Recived", None));
        ___qtablewidgetitem30 = self.net_io_table.horizontalHeaderItem(5)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"ERR In", None));
        ___qtablewidgetitem31 = self.net_io_table.horizontalHeaderItem(6)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"ERR Out", None));
        ___qtablewidgetitem32 = self.net_io_table.horizontalHeaderItem(7)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Drop In", None));
        ___qtablewidgetitem33 = self.net_io_table.horizontalHeaderItem(8)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Drop Out", None));
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Network Addresses", None))
        ___qtablewidgetitem34 = self.net_addresses_table.horizontalHeaderItem(1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"FAMILY", None));
        ___qtablewidgetitem35 = self.net_addresses_table.horizontalHeaderItem(2)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"ADDRESS", None));
        ___qtablewidgetitem36 = self.net_addresses_table.horizontalHeaderItem(3)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"NETMASK", None));
        ___qtablewidgetitem37 = self.net_addresses_table.horizontalHeaderItem(4)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"ROADCAS", None));
        ___qtablewidgetitem38 = self.net_addresses_table.horizontalHeaderItem(5)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"PTP", None));
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Netwok Connection", None))
        ___qtablewidgetitem39 = self.net_connections_table.horizontalHeaderItem(1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem40 = self.net_connections_table.horizontalHeaderItem(2)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Family", None));
        ___qtablewidgetitem41 = self.net_connections_table.horizontalHeaderItem(3)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Family", None));
        ___qtablewidgetitem42 = self.net_connections_table.horizontalHeaderItem(4)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"LADDR", None));
        ___qtablewidgetitem43 = self.net_connections_table.horizontalHeaderItem(5)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"RADDR", None));
        ___qtablewidgetitem44 = self.net_connections_table.horizontalHeaderItem(6)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem45 = self.net_connections_table.horizontalHeaderItem(7)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"PID", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"Version 1.0|AbdiMK", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

