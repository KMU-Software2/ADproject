import time

class StopTime():
    def __init__(self):
        self.stopTime = 0

    def stopTimenow(self):
        self.stopTime = time.time()