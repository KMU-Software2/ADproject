import random
import sys
from PyQt5.QtWidgets import (QWidget, QToolButton, QPushButton,
    QHBoxLayout,  QGridLayout, QVBoxLayout, QApplication, QLabel,QSizePolicy,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import pyqtSignal, Qt
from startTime import StartTime
from stopTime import StopTime


class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class startWindow(QWidget):
    switchWindow = pyqtSignal(str)

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
        self.sizeCombo.addItems(['2', '4', '5', '6'])

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

    def startGame(self):
        self.switchWindow.emit(self.sizeCombo.currentText())


class mainWinodw(QWidget):
    switchWindow = pyqtSignal()

    def __init__(self, size):
        QWidget.__init__(self)
        self.initUI(size)
        self.startTime = 0
        self.stopTime = 0

    def getNumOfButton(self, size):
        self.numOfButton = int(size) ** 2
        return self.numOfButton

    def initUI(self, size):
        numOfButton = self.getNumOfButton(size)
        ranList = self.rand(size)

        r = 0
        c = 0
        grid = QGridLayout()

        for i in range(numOfButton):
            self.button = Button(str(ranList[i]), self.buttonClicked)
            grid.addWidget(self.button, r, c)
            c += 1
            if c == int(size):
                c = 0
                r += 1

        hbox_1 = QHBoxLayout()
        self.targetLabel = QLabel('Target Number:')
        self.line_edit = QLineEdit()
        self.line_edit.setText(str(numOfButton))
        self.line_edit.setReadOnly(True)
        self.line_edit.setAlignment(Qt.AlignCenter)
        hbox_1.addWidget(self.targetLabel)
        hbox_1.addStretch(1)
        hbox_1.addWidget(self.line_edit)

        hbox_2 = QHBoxLayout()
        self.reButton = QPushButton('Restart')
        self.reButton.clicked.connect(self.returnHome)
        hbox_2.addWidget(self.reButton)

        hbox_3 = QHBoxLayout()
        self.resultLabel = QLabel('Result:')
        self.resultLine = QLineEdit()
        self.resultLine.setText('Plese click Target Number!')
        self.resultLine.setReadOnly(True)
        self.resultLine.setAlignment(Qt.AlignCenter)
        hbox_3.addWidget(self.resultLabel)
        hbox_3.addWidget(self.resultLine)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox_1)
        vbox.addLayout(grid)
        vbox.addLayout(hbox_2)
        vbox.addLayout(hbox_3)

        self.setLayout(vbox)
        self.setWindowTitle('PlayGame')

    def rand(self, size):
        numOfButton = int(size) ** 2
        myList = [i for i in range(1, numOfButton + 1)]
        random.shuffle(myList)
        return myList

    def buttonClicked(self):
        button = self.sender()
        key = button.text()
        number = self.line_edit.text()
        BT = StartTime()
        AT = StopTime()
        if key == number:
            if key == str(self.numOfButton):
                BT.startTimenow()
                self.startTime = BT.startTime
            elif key == '1':
                AT.stopTimenow()
                self.stopTime = AT.stopTime
                timeSpent = str(round(self.stopTime - self.startTime, 3))
                self.resultLine.setText(timeSpent + ' sec')
            button.setDisabled(True)
            self.line_edit.setText(str(int(number)-1))


    def returnHome(self):
        self.switchWindow.emit()
        self.close()



class Controller:
    def __init__(self):
        pass

    def startPage(self):
        self.startWindow = startWindow()
        self.startWindow.switchWindow.connect(self.mainPage)
        self.startWindow.show()

    def mainPage(self, size):
        self.mainWindow = mainWinodw(size)
        self.mainWindow.switchWindow.connect(self.startPage)
        self.startWindow.close()
        self.mainWindow.show()

def main():
    app = QApplication(sys.argv)
    controller = Controller()
    controller.startPage()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
