import psutil
from time import sleep
class BatteyPlugin():
    def secs2hours(self, secs):
        mm,ss = divmod(secs, 60)
        hh, mm = divmod(mm, 60)

        return "%d:%02d:%02d (H:M:S)" % (hh, mm, ss)

    def battery(self, progress_callback):
        while True:
            try:
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
                self.ui.battery_usage.rpb_setLineColor((255, 30, 99))
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
                sleep(1)
            except:
                pass
