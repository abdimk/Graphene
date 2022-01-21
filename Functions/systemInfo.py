import datetime
import platform
import psutil
from time import sleep
from PySide2.QtWidgets import QTableWidgetItem,QPushButton

class SYSTEMINFO():
    # Get System information

    def system_info(self, progress_callback):
        while True:
            try:
                #now = datetime.now()
                time = datetime.datetime.now().strftime("%H:%M:%S")
                date = datetime.datetime.now().strftime("%Y-%m-%d")
                self.ui.system_date.setText(str(date))
                self.ui.system_time.setText(str(time))

                self.ui.system_machine.setText(platform.machine())
                self.ui.system_version.setText(platform.version())
                self.ui.system_platform.setText(platform.platform())
                self.ui.system_system.setText(platform.system())
                self.ui.system_processor.setText(platform.processor())
                sleep(1)
            except:
                pass

    #a function to create a tabel widgets
    def create_table_widget(self,rowPosition, columnPosition, text, tableName):
        qtabelwidgetitem = QTableWidgetItem()

        # use getattr()
        getattr(self.ui, tableName).setItem(rowPosition, columnPosition, qtabelwidgetitem)
        qtabelwidgetitem = getattr(self.ui, tableName).item(rowPosition, columnPosition)

        qtabelwidgetitem.setText(text)
        
   