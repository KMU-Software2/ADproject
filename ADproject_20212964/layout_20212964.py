import pickle
import sys
import copy
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QLabel, QComboBox, QTextEdit, QLineEdit)

class ADproject(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 시작 & 재시도 버튼
        self.startButton = QPushButton('START')
        self.againButton = QPushButton('TRY AGAIN')

        hbox_1 = QHBoxLayout()
        hbox_1.addWidget(self.startButton)
        hbox_1.addWidget(self.againButton)

        # size 선택
        self.size = QLabel('size: ')
        self.sizeCombo = QComboBox()
        self.sizeCombo.addItems(['  3  ', '  4  ', '  5  '])

        hbox_2 = QHBoxLayout()
        hbox_2.addStretch(1)
        hbox_2.addWidget(self.size)
        hbox_2.addWidget(self.sizeCombo)

        # 버튼 생성 위치
        """
        for i in range(
        """
        self.playButton = QTextEdit()

        hbox_3 = QHBoxLayout()
        hbox_3.addWidget(self.playButton)

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
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('ADproject')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ADproject()
    sys.exit(app.exec_())