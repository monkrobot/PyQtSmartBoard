import sys
from PyQt5.QtWidgets import (QMainWindow, QAction, qApp, QWidget, QToolTip, QPushButton, QApplication, QTextEdit,
                             QLineEdit, QGridLayout, QMessageBox, QLabel, QFrame, QColorDialog, QFileDialog)
from PyQt5.QtGui import (QIcon, QFont, QPainter, QColor, QPen, QImage, QBrush)
from PyQt5.QtCore import (QCoreApplication, Qt, QPoint)

colourLine = "#265F00"
print(colourLine)

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



    def mouseMoveEvent(self, event):
        # super().mouseMoveEvent(event)
        global colourLine

        painter = QPainter(self._im)
        painter.setPen(QPen(QColor(str(colourLine)), 1, Qt.SolidLine, Qt.RoundCap))
        painter.setBrush(QBrush(QColor(str(colourLine)), Qt.SolidPattern))
        painter.drawEllipse(event.pos(), 10, 10)

        # Перерисуемся
        self.update()

    def mousePressEvent(self, event):
        # super().mousePressEvent (event)
        global colourLine

        painter = QPainter(self._im)
        painter.setPen(QPen(QColor(str(colourLine)), 1, Qt.SolidLine, Qt.RoundCap))
        painter.setBrush(QBrush(QColor(str(colourLine)), Qt.SolidPattern))
        painter.drawEllipse(event.pos(), 10, 10)

        # Перерисуемся
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)

        painter = QPainter(self)
        painter.drawImage(0, 0, self._im)

    def printTest(self):
        print('delbtn works')

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        self.c = Menu()
        self.c.move(100, 100)

        self._im = QImage(1700, 1080, QImage.Format_ARGB32)
        self._im.fill(QColor("white"))

        #Typing of text
        textEdit = QTextEdit()
        #self.setCentralWidget(textEdit)

        #greeting text with absolute position
        #greeting_text = QLabel('Welcome', self)
        #greeting_text.move(980, 50)

        #popup help-text
        self.setToolTip('This is a <b>QWidget</b> widget') #Popup help text

        # Delete button, buttons will be work without 'self'
        self.delbtn = QPushButton('Delete', self) #Button widget
        self.delbtn.setToolTip('This is a Delete') # Popup help text
        self.delbtn.clicked.connect(self.printTest)
        self.delbtn.resize(self.delbtn.sizeHint())
        self.delbtn.move(1750, 10)

        #Quit button
        self.quitbtn = QPushButton('Quit', self)
        self.quitbtn.clicked.connect(QCoreApplication.instance().quit)
        self.quitbtn.setToolTip('This is a Quit')
        self.quitbtn.resize(self.quitbtn.sizeHint())
        self.quitbtn.move(1750, 50)

        #Color Dialog. If this button will be without 'self', then col will not change color
        col = QColor(24, 15, 65)
        self.colbtn = QPushButton('Dialog', self)
        self.colbtn.move(1750, 90)

        self.colbtn.clicked.connect(self.showColorDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
        print(col.name())
        self.frm.setGeometry(1750, 125, 125, 30)

        #self.update()

        global colourLine
        colourLine = col.name()

        #self.update()

        #titleEdit = QLineEdit()
        #titleEdit.move(100, 50)

        ##LineGrid
        #grid = QGridLayout()
        #grid.setSpacing(10)
#
        #grid.addWidget(self.c, 1, 0, 1, 1)
        #grid.addWidget(titleEdit, 2, 1)
#
        #grid.addWidget(self.delbtn, 3, 1)
        #grid.addWidget(self.quitbtn, 4, 1)
#
        #grid.addWidget(self.colbtn, 4, 1)
        #grid.addWidget(self.frm, 5, 1)
#
        #grid.addWidget(textEdit, 6, 1)
#
        #self.setLayout(grid)

        #Window geometry
        self.setFixedSize(1920, 1080)
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
    fileSystem = Menu()

    print(colourLine)

    sys.exit(app.exec_())