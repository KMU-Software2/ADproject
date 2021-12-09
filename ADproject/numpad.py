import random

def setNumpad(size):
    numpad = random.sample(range(1, size + 1), size)
    return numpad