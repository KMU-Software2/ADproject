import sys
from PyQt5.QtWidgets import (QWidget, QToolButton, QPushButton,
    QHBoxLayout,  QGridLayout, QVBoxLayout, QApplication, QLabel,QSizePolicy,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import pyqtSignal, Qt
from numpad import setNumpad
from checkTime import CheckTime
from manual import manual


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
        self.sizeCombo.addItems(['  4  ', '  5  ', '  6  ', '  7  ', '  8  '])

        hbox_2 = QHBoxLayout()
        hbox_2.addStretch(1)
        hbox_2.addWidget(self.size)
        hbox_2.addWidget(self.sizeCombo)

        # 게임 소개
        self.gameIntro = QTextEdit()
        self.gameIntro.setText(manual)
        self.gameIntro.setAlignment(Qt.AlignCenter)
        self.gameIntro.setReadOnly(True)

        hbox_3 = QHBoxLayout()
        hbox_3.addWidget(self.gameIntro)

        # 종료 버튼
        self.exitButton = QPushButton('Exit')
        self.exitButton.clicked.connect(self.exitGame)

        hbox_4 = QHBoxLayout()
        hbox_4.addWidget(self.exitButton)

        # 최종 배치
        vbox = QVBoxLayout()
        vbox.addLayout(hbox_1)
        vbox.addLayout(hbox_2)
        vbox.addLayout(hbox_3)
        vbox.addLayout(hbox_4)

        self.setLayout(vbox)
        self.resize(500, 260)
        self.setWindowTitle('ReadyToPlay')

    def startGame(self):
        self.switchWindow.emit(self.sizeCombo.currentText())

    def exitGame(self):
        self.close()


class mainWinodw(QWidget):
    switchWindow = pyqtSignal()

    def __init__(self, selectSize):
        QWidget.__init__(self)
        size = int(selectSize)
        self.initUI(size)
        self.startTime = CheckTime()

        self.stopTime = 0

    def initUI(self, size):
        self.numOfButton = size ** 2
        ranList = setNumpad(self.numOfButton)

        r = 0
        c = 0
        grid = QGridLayout()

        for i in range(self.numOfButton):
            self.button = Button(str(ranList[i]), self.buttonClicked)
            grid.addWidget(self.button, r, c)
            c += 1
            if c == size:
                c = 0
                r += 1

        # 타겟 넘버
        hbox_1 = QHBoxLayout()
        self.targetLabel = QLabel('Target Number:')
        self.line_edit = QLineEdit()
        self.line_edit.setText(str(self.numOfButton))
        self.line_edit.setReadOnly(True)
        self.line_edit.setAlignment(Qt.AlignCenter)
        hbox_1.addWidget(self.targetLabel)
        hbox_1.addWidget(self.line_edit)

        # 결과 출력
        hbox_2 = QHBoxLayout()
        self.resultLabel = QLabel('Result:')
        self.resultLine = QLineEdit()
        self.resultLine.setText('Please click Target Number!')
        self.resultLine.setReadOnly(True)
        self.resultLine.setAlignment(Qt.AlignCenter)
        hbox_2.addWidget(self.resultLabel)
        hbox_2.addWidget(self.resultLine)

        # 재시작&종료 버튼
        hbox_3 = QHBoxLayout()
        self.reButton = QPushButton('Restart')
        self.reButton.clicked.connect(self.returnHome)
        self.exitButton = QPushButton('Exit')
        self.exitButton.clicked.connect(self.buttonClicked)
        hbox_3.addWidget(self.reButton)
        hbox_3.addWidget(self.exitButton)

        # 최종 배치
        vbox = QVBoxLayout()
        vbox.addLayout(hbox_1)
        vbox.addLayout(grid)
        vbox.addLayout(hbox_2)
        vbox.addLayout(hbox_3)

        self.setLayout(vbox)
        self.setWindowTitle('PlayGame')

    # 버튼 클릭 시, 기능 구현
    def buttonClicked(self):
        button = self.sender()
        key = button.text()
        number = int(self.line_edit.text())
        if key == str(number):
            self.resultLine.setText('Please click Target Number!')
            if key == str(self.numOfButton):
                self.line_edit.setText(str(number - 1))
            elif key == '1':
                self.line_edit.setText('SUCCESS!')
                self.stopTime = CheckTime()
                timeSpent = str(round(self.stopTime - self.startTime, 3))
                self.resultLine.setText(timeSpent + ' sec')
            else:
                self.line_edit.setText(str(number-1))
            button.setDisabled(True)
        else:
            try:
                int(key)
                self.resultLine.setText("You push the wrong button!")
            except:
                self.close()

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
