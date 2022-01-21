import psutil
from multiprocessing import cpu_count
from time import sleep

class CPUANDRAM():
        #System CPU and RAM information
    def cpu_ram(self, progress_callback):
        #Live CPU and RAM Information 
        while True:
            try:
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
            except:
                pass
            
            
        
