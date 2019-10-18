from polling import Polling
from hardware import Hardware
from PyQt5 import QtCore, uic, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import PyQt5

import sys

class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.hardware = Hardware(self)
            print("mainwindow hardware:{}".format(self.hardware))
            self.polling = Polling(self, self.hardware)
            print(self.hardware.value1)
            print(self.polling.value1)
            # load screen
            uic.loadUi("MainWindow.ui", self)
            self.hardware.pollobject()

        def print(self, value):
            print("Value: {}".format(value))

if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(['PORTABLE TESTER'])
    start_window = MainWindow()
    start_window.show()  # show the window
    sys.exit(app.exec())  # app.exit(app.exec_())