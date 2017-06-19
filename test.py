import sys, random, re
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPoint


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.mouse_pos = [0, 0]
        self.initUI()

    #mouse_pos = [0, 0]
    def initUI(self):

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Points')
        self.show()

        greeting_text = QLabel('Welcome', self)
        greeting_text.move(80, 50)


    def paintEvent(self, e):
        print('paint')
        #mouse_pos = self.mousePressEvent()
        #print('paintEvent: ', mouse_pos)
        qp = QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()


    def drawPoints(self, qp):
        print('drawPoints')
        qp.setPen(Qt.red)
        size = self.size()*15
        x = 140
        y = 80
        qp.drawPoint(x, y)

    # mouse click position
    def mousePressEvent(self, e):
        QWidget.mousePressEvent(self, e)

        if e.button() == Qt.LeftButton:

            slice_e_pos = re.findall("[-0-9]+", str(e.pos()))
            mouse_pos = [int(slice_e_pos[1]), int(slice_e_pos[2])]
            print('mouse_pos: ', mouse_pos)
            print('')

            #return mouse_pos
            #self.paintEvent(e, mouse_pos)
    #print(mouse_pos)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())