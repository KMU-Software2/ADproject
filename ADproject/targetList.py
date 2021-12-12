import random

class TargetList():
    def __init__(self):
        self.cnt = 0
        self.targetList = []

    def setTargetList(self, size):
        self.targetList = random.sample(range(1, size + 1), size)
