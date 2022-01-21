import psutil
import datetime
from PySide2.QtWidgets import QPushButton


class RunningProcess():
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
