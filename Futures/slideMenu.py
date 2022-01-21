from PySide2.QtWidgets import *
from PySide2 import QtCore
from PySide2.QtCore import QPropertyAnimation

class SlideClassMenu():
    ########################################################################
    #SLIDE LEFT MENU FUNCTION
    ########################################################################
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