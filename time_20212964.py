import datetime

class Time():
    def __init__(self):
        self.startTime = ''
        self.stopTime = ''
        self.result = ''

    def startTime(self):
        self.startTime = datetime.datetime.now()

    def stopTime(self):
        self.stopTime = datetime.datetime.now()
        diffSec = (self.stopTime.second - self.startTime.second)
        diffMicrosec = (self.stopTime.microsecond - self.startTime.microsecond) * 0.
        self.result = str(diffSec) + '.' + str(diffMicrosec)