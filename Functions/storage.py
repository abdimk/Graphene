import sys
import psutil
import shutil
from PySide2.QtWidgets import QProgressBar
import platform
platforms = {
    'linux' : 'Linux',
    'linux1' : 'Linux',
    'linux2' : 'Linux',
    'darwin': 'OS X',
    'win32' : 'Windows' 
}

class STORAGE():
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
 