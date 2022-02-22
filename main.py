from PyQt5.QtGui import QPainter, QColor
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from random import randrange
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.is_draw = False
        self.pushButton.clicked.connect(self.re_draw)

    def re_draw(self):
        self.is_draw = True
        self.update()

    def paintEvent(self, event):
        if self.is_draw:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        self.qp.setBrush(QColor(255, 255, 0))
        a = randrange(500)
        self.qp.drawEllipse(100, 100, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
