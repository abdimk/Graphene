import sys
import traceback
from PySide2.QtCore import QObject,Signal,QRunnable,Slot
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
    def __init__(self, fn, *args, **kwargs):
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











