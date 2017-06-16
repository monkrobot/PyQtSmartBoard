import sys
from PyQt5.QtWidgets import (QMainWindow, QAction, qApp, QWidget, QToolTip, QPushButton, QApplication, QTextEdit, QLineEdit,
                             QGridLayout, QMessageBox, QLabel, QFrame, QColorDialog, QFileDialog)
from PyQt5.QtGui import (QIcon, QFont, QColor)
from PyQt5.QtCore import QCoreApplication

# Menu
class Menu(QMainWindow):
    # file
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        print('MenuFile')
        # exit
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        # save file
        saveAction = QAction(QIcon('save.png'), '&Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save as...')
        exitAction.triggered.connect(qApp.quit)

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showFiles)
        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(saveAction)

    def showFiles(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]

        f = open(fname, 'r')

        with f:
            data = f.read()
            self.textEdit.setText(data)

class Board(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI() #GUI developing

    def printTest(self):
        print('delbtn works')

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        self.c = Menu()

        #Typing of text
        textEdit = QTextEdit()
        #self.setCentralWidget(textEdit)

        #greeting text with absolute position
        greeting_text = QLabel('Welcome', self)
        #greeting_text.move(980, 50)

        #popup help-text
        self.setToolTip('This is a <b>QWidget</b> widget') #Popup help text

        # Delete button, buttons will be work without 'self'
        self.delbtn = QPushButton('Delete', self) #Button widget
        self.delbtn.setToolTip('This is a Delete') # Popup help text
        self.delbtn.clicked.connect(self.printTest)
        self.delbtn.resize(self.delbtn.sizeHint())
        #delbtn.move(200, 50)

        #Quit button
        self.quitbtn = QPushButton('Quit', self)
        self.quitbtn.clicked.connect(QCoreApplication.instance().quit)
        self.quitbtn.setToolTip('This is a Quit')
        self.quitbtn.resize(self.quitbtn.sizeHint())
        #quitbtn.move(200, 100)

        #Color Dialog. If this button will be without 'self', then col will not change color
        col = QColor(0, 0, 0)
        self.colbtn = QPushButton('Dialog', self)
        #colbtn.move(20, 20)

        self.colbtn.clicked.connect(self.showColorDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
        #frm.setGeometry(130, 22, 100, 100)

        titleEdit = QLineEdit()
        #titleEdit.move(100, 50)

        #LineGrid
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(greeting_text, 1, 0, 1, 1)
        grid.addWidget(titleEdit, 2, 1)

        grid.addWidget(self.delbtn, 3, 0)
        grid.addWidget(self.quitbtn, 3, 1)

        grid.addWidget(self.colbtn, 4, 0)
        grid.addWidget(self.frm, 4, 1)

        grid.addWidget(textEdit, 6, 1)

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

    #Color Dialog
    def showColorDialog(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                                   % col.name())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    smartboard = Board()

    sys.exit(app.exec_())