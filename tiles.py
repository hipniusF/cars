from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class Tile(QWidget):
    def __init__(self):
        super().__init__()

    def get_angl(self):
        x, y = self.orientation

        return 90.0 * y + 180 * (x>0)

    def get_widget(self):
        label = QLabel()
        pm = QPixmap('assets/' + self.sprite)

        angl = self.get_angl()
        trans = QTransform().rotate(angl)

        pm = pm.transformed(trans)
        label.setPixmap(pm)

        return label

    def set_orientation(self, orient):
        x, y = orient
        assert x*y == 0

        self.orientation = (x,y)


class Road(Tile):
    def __init__(self):
        super().__init__()

        self.orientation = (0,1)
        self.sprite ='road.png'

    def set_orientation(self, orient):
        x, y = orient
        if x*y != 0:
            self.sprite = 'intersection.png'
        self.orientation = (x,y)

    def get_angl(self):
        x, y = self.orientation

        if x*y == 0:
            return super().get_angl()
        if x==y:
            return 180 * (x>0)
        else:
            return 90 * y


class Car(Tile):
    def __init__(self):
        super().__init__()

        self.orientation = (0,1)
        self.sprite = 'car.png'


class Grass(Tile):
    def __init__(self):
        super().__init__()
        self.orientation = (0,1)
        self.sprite = 'grass.png'


