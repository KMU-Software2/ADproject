import random
import sys
from PyQt5.QtWidgets import (QWidget, QToolButton, QPushButton,
    QHBoxLayout,  QGridLayout, QVBoxLayout, QApplication, QLabel,QSizePolicy,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import pyqtSignal

class startWindow(QWidget):
    switchWindow = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 시작 버튼
        self.startButton = QPushButton('START')
        self.startButton.clicked.connect(self.startGame)

        hbox_1 = QHBoxLayout()
        hbox_1.addWidget(self.startButton)

        # size 선택
        self.size = QLabel('size: ')
        self.sizeCombo = QComboBox()
        self.sizeCombo.addItems(['4', '5', '6'])

        hbox_2 = QHBoxLayout()
        hbox_2.addStretch(1)
        hbox_2.addWidget(self.size)
        hbox_2.addWidget(self.sizeCombo)

        # 게임 소개
        self.gameIntro = QTextEdit()
        self.gameIntro.setReadOnly(True)

        hbox_3 = QHBoxLayout()
        hbox_3.addWidget(self.gameIntro)

        # 결과 출력 창
        self.result = QLabel('Result:')
        self.resultEdit = QLineEdit()
        self.resultEdit.setReadOnly(True)

        hbox_4 = QHBoxLayout()
        hbox_4.addWidget(self.result)
        hbox_4.addWidget(self.resultEdit)

        #최종 배치
        vbox = QVBoxLayout()
        vbox.addLayout(hbox_1)
        vbox.addLayout(hbox_2)
        vbox.addLayout(hbox_3)
        vbox.addLayout(hbox_4)

        self.setLayout(vbox)
        self.setWindowTitle('ReadyToPlay')

    def gameSize(self):
        return self.sizeCombo.currentText()

    def startGame(self):
        self.switchWindow.emit()

class mainWinodw(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.initUI()

    def getSize(self):
        self.start = startWindow()
        self.size = self.start.gameSize()
        return self.size

    def getNumOfButton(self):
        self.numOfButton = int(self.getSize()) ** 2
        return self.numOfButton

    def initUI(self):
        size = int(self.getSize())
        numOfButton = self.getNumOfButton()
        ranList = self.rand()

        r = 0
        c = 0
        layout = QGridLayout()

        for i in range(numOfButton):
            self.button = QPushButton(str(ranList[i]))
            self.button.clicked.connect(lambda: self.buttonClicked(25))
            layout.addWidget(self.button, r, c)
            c += 1
            if c == size:
                c = 0
                r += 1
        self.setLayout(layout)
        self.setWindowTitle('MainPage')

    def rand(self):
        self.start = startWindow()
        size = int(self.start.gameSize())
        numOfButton = size ** 2
        myList = [i for i in range(1, numOfButton + 1)]
        random.shuffle(myList)
        return myList

    def buttonClicked(self, number):
        numOfTarget = self.getNumOfButton()
        button = self.sender()
        key = int(button.text())
        if key == numOfTarget:
            self.button.setDisabled(True)
            numOfTarget -= 1


class Controller:
    def __init__(self):
        pass

    def startPage(self):
        self.startWindow = startWindow()
        self.startWindow.switchWindow.connect(self.mainPage)
        self.startWindow.show()

    def mainPage(self):
        self.mainWindow = mainWinodw()
        self.startWindow.close()
        self.mainWindow.show()

def main():
    app = QApplication(sys.argv)
    controller = Controller()
    controller.startPage()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
