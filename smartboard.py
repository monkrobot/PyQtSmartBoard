import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.QtGui import (QIcon, QFont)

class Board(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI() #GUI developing

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Delete', self)
        btn.setToolTip('This is a Delete')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(0, 40, 1920, 1080)
        self.setWindowTitle('SmartBoard')
        self.setWindowIcon(QIcon('images/table.png')) #icon for application

        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    smartboard = Board()

    sys.exit(app.exec_())