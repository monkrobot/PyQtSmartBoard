import sys, random, re
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen, QImage, QBrush
from PyQt5.QtCore import Qt, QPoint


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(1000, 1000)

        self._im = QImage(300, 300, QImage.Format_ARGB32)
        self._im.fill(QColor("white"))

    def mouseMoveEvent(self, event):
        #super().mouseMoveEvent(event)


        painter = QPainter(self._im)
        painter.setPen(QPen(QColor("#234532"), 1, Qt.SolidLine, Qt.RoundCap))
        painter.setBrush(QBrush(QColor("#234532"), Qt.SolidPattern))
        painter.drawEllipse(event.pos(), 10, 10)

        # Перерисуемся
        self.update()

    def mousePressEvent(self, event):
        # super().mousePressEvent (event)


        painter = QPainter(self._im)
        painter.setPen(QPen(QColor("#234532"), 1, Qt.SolidLine, Qt.RoundCap))
        painter.setBrush(QBrush(QColor("#234532"), Qt.SolidPattern))
        painter.drawEllipse(event.pos(), 10, 10)

        # Перерисуемся
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)

        painter = QPainter(self)
        painter.drawImage(0, 0, self._im)


app = QApplication(sys.argv)

widget = Widget()
widget.setWindowTitle('simple')
widget.show()

sys.exit(app.exec_())

#mouse_pos = [0, 0]
#
##class Point(QWidget):
##    def __init__(self, point1, point2):
##        self.p1 = point1
##        self.p2 = point2
##
##    def paintEvent(self,event):
##        print('paint')
##        global mouse_pos
##        # mouse_pos = self.mousePressEvent()
##        # print('paintEvent: ', mouse_pos)
##        qp = QPainter()
##        qp.begin(self)
##        print('drawPoints')
##        qp.setPen(Qt.red)
##        size = self.size()
##        print('drawPoints', mouse_pos)
##        x = self.mouse_pos[0]
##        y = self.mouse_pos[1]
##        qp.drawPoint(x, y)
##        # self.drawPoints(qp)
##        qp.end()
#
#class Example(QWidget):
#
#    def __init__(self):
#        super().__init__()
#        self.mouse_pos = [0, 0]
#        self.initUI()
#
#    #mouse_pos = [0, 0]
#    def initUI(self):
#
#        self.setGeometry(300, 300, 280, 170)
#        self.setWindowTitle('Points')
#        self.show()
#
#        greeting_text = QLabel('Welcome', self)
#        greeting_text.move(80, 50)
#
#    def paintEvent(self, e):
#        global mouse_pos
#        print('paint')
#        #mouse_pos = self.mousePressEvent()
#        #print('paintEvent: ', mouse_pos)
#        qp = QPainter()
#        qp.begin(self)
#        print('drawPoints')
#        qp.setPen(Qt.red)
#        size = self.size()
#        print('drawPoints', mouse_pos)
#        x = mouse_pos[0]
#        y = mouse_pos[1]
#        qp.drawPoint(x, y)
#        #self.drawPoints(qp)
#        qp.end()
#
#
#    #def drawPoints(self, qp):
#    #    print('drawPoints')
#    #    qp.setPen(Qt.red)
#    #    size = self.size()*15
#    #    print('drawPoints', mouse_pos)
#    #    x = mouse_pos[0]
#    #    y = mouse_pos[1]
#    #    qp.drawPoint(x, y)
#
#    # mouse click position
#    def mousePressEvent(self, e):
#        QWidget.mousePressEvent(self, e)
#
#        if e.button() == Qt.LeftButton:
#
#            slice_e_pos = re.findall("[-0-9]+", str(e.pos()))
#            global mouse_pos
#            mouse_pos = [int(slice_e_pos[1]), int(slice_e_pos[2])]
#            print('mouse_pos: ', mouse_pos)
#            print('')
#            #newPoint = Point(QPoint(mouse_pos[0], mouse_pos[1]))
#
#            #self.paintEvent(e, mouse_pos)
#
#if __name__ == '__main__':
#
#    app = QApplication(sys.argv)
#    ex = Example()
#    sys.exit(app.exec_())
