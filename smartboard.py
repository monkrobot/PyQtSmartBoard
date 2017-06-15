import sys
from PyQt5.QtWidgets import (QMainWindow, QWidget, QToolTip, QPushButton, QApplication, QTextEdit, QLineEdit,
                             QGridLayout, QMessageBox, QLabel)
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

        #Typing of text
        textEdit = QTextEdit()
        #self.setCentralWidget(textEdit)

        #greeting text with absolute position
        greeting_text = QLabel('Welcome', self)
        #greeting_text.move(980, 50)

        #popup help-text
        self.setToolTip('This is a <b>QWidget</b> widget') #Popup help text

        # Delete button
        delbtn = QPushButton('Delete', self) #Button widget
        delbtn.setToolTip('This is a Delete') # Popup help text
        delbtn.clicked.connect(self.printTest)
        delbtn.resize(delbtn.sizeHint())
        #delbtn.move(200, 50)

        #Quit button
        quitbtn = QPushButton('Quit', self)
        quitbtn.clicked.connect(QCoreApplication.instance().quit)
        quitbtn.setToolTip('This is a Quit')
        quitbtn.resize(quitbtn.sizeHint())
        #quitbtn.move(200, 100)

        titleEdit = QLineEdit()
        #titleEdit.move(100, 50)

        #LineGrid
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(greeting_text, 1, 0, 1, 1)
        grid.addWidget(titleEdit, 2, 1)

        grid.addWidget(delbtn, 3, 0)
        grid.addWidget(quitbtn, 3, 1)

        grid.addWidget(textEdit, 4, 1)

        self.setLayout(grid)

        #Window geometry
        self.setGeometry(0, 40, 500, 500)
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