import time

class StartTime():
    def __init__(self):
        self.startTime = 0

    def startTimenow(self):
        self.startTime = time.time()
