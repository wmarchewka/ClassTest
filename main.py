from polling import Polling
from hardware import Hardware

class MainWindow(object):
        def __init__(self):
            self.hardware = Hardware(self)
            print("mainwindow hardware:{}".format(self.hardware))
            self.polling = Polling(self, self.hardware)
            print(self.hardware.value1)
            print(self.polling.value1)


        def print(self, value):
            print("Value: {}".format(value))

MainWindow()