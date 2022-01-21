import sys
import platform
from PySide2.QtWidgets import QProgressBar
platforms = {
    'linux' : 'Linux',
    'linux1' : 'Linux',
    'linux2' : 'Linux',
    'darwin': 'OS X',
    'win32' : 'Windows' 
}


class SENSORS():
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

