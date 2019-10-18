class Polling(object):
    def __init__(self, mainwin, hardware):
        self.value1=88
        self.mainwin = mainwin
        self.hardware = hardware
        print(mainwin)
        self.mainwin.print("Polling")
        print("polling hardware:{}".format(self.hardware))
