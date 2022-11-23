from random import randint
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication
)
from PyQt5.QtGui import (
    QPainter,
    QColor
)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self._should_draw = False
        self._coordinates = 0, 0
        uic.loadUi('window.ui', self)
        self._init_ui()
        self._should_draw = False

    def _init_ui(self) -> None:
        self.pushButton.clicked.connect(self._create)

    def _create(self):
        self._should_draw = True
        self.update()

    def paintEvent(self, event) -> None:
        if not self._should_draw:
            return

        qr = QPainter()
        qr.begin(self)
        self.draw_circle(qr)
        qr.end()

    def draw_circle(self, qr):
        qr.setBrush(QColor('yellow'))
        diameter = randint(70, 200)
        start = 60
        qr.drawEllipse(start, start, start + diameter, start + diameter)




app = QApplication(sys.argv)
window = MainWindow()
window.show()
exit_code = app.exec()
sys.exit(exit_code)