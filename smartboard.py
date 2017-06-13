import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QMessageBox)
from PyQt5.QtGui import (QIcon, QFont)
from PyQt5.QtCore import QCoreApplication

class Board(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI() #GUI developing

    def printTest(self):
        print('delbtn works')

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget') #Popup help text
        # Delete button
        delbtn = QPushButton('Delete', self) #Button widget
        delbtn.setToolTip('This is a Delete') # Popup help text
        delbtn.clicked.connect(self.printTest)
        delbtn.resize(delbtn.sizeHint())
        delbtn.move(50, 50)
        #Quit button
        quitbtn = QPushButton('Quit', self)
        quitbtn.clicked.connect(QCoreApplication.instance().quit)
        quitbtn.setToolTip('This is a Quit')
        quitbtn.resize(quitbtn.sizeHint())
        quitbtn.move(50, 100)

        self.setGeometry(0, 40, 1920, 1020)
        self.setWindowTitle('SmartBoard')
        self.setWindowIcon(QIcon('images/table.png')) #icon for application

        self.show()
    # Popup message about closing (saving) the file
    def closeEvent (self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?', QMessageBox.Save | QMessageBox.No,
                                     QMessageBox.No)

        if reple == QMessageBox.Save:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    smartboard = Board()

    sys.exit(app.exec_())