class Hardware(object):
    def __init__(self, mainwin):
        self.value1 = 99
        self.mainwin = mainwin
        print(mainwin)
        self.mainwin.print("Hardware")
        print("hardware in hardware:{}".format(self))
