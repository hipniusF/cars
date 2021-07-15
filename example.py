import sys
import random
from time import sleep
from PySide2 import QtWidgets, QtCore, QtGui

class GenericWidget(QtWidgets.QWidget):
    def __init__(self, title, content):
        super().__init__()

        self.box = QtWidgets.QGroupBox(title)
        box_layout = QtWidgets.QHBoxLayout()
        box_layout.addWidget(content)

        self.box.setLayout(box_layout)

        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.addWidget(self.box)


class CounterWidget(QtWidgets.QWidget):
    counter = 0

    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton('Click')
        self.text = QtWidgets.QLabel(str(self.counter), alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.handle_click)

        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update)
        self.timer.start()

    @QtCore.Slot()
    def handle_click(self):
        self.counter += 1
        self.text.setText(str(self.counter))

    @QtCore.Slot()
    def update(self):
        self.counter += 0.1
        self.text.setText(str(self.counter))


app = QtWidgets.QApplication([])

counter = CounterWidget()
widget = GenericWidget('This is my counter', counter)

widget.resize(800, 600)
widget.show()

print('a')
app.exec_()
print('a')

sys.exit()
