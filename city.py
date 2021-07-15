import random
from time import sleep
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from tiles import Road, Car, Grass

class City(QWidget):
    height = 25
    width = 25
    grid = []

    def __init__(self):
        super().__init__()

        for i in range(self.height):
            self.grid.append([])
            for j in range(self.width):
                grass = Grass()
                self.grid[i].append(grass)

        self.layout = QGridLayout(self)
        self.layout.setHorizontalSpacing(0)
        self.layout.setVerticalSpacing(0)

        self.make_prims_maze()
        self.draw()

    def get_neighbors(self, x, y):
        neig = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i!=0 or j!=0):
                    if y+i >= 0 and y+i < len(self.grid) and \
                        x+j >= 0 and x+j < len(self.grid[0]):
                        neig.append((x+j, y+i))

        return neig

    def get_nc_neighbors(self, x, y):
        neig = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i!=0 or j!=0):
                    if y+i >= 0 and y+i < len(self.grid) and \
                       x+j >= 0 and x+j < len(self.grid[0]) and \
                       i*j == 0:
                        neig.append((x+j, y+i))

        return neig


    def make_prims_maze(self):
        walls = []
        visited = set()

        x_0, y_0 = random.randint(0, self.height-1), random.randint(0, self.width-1)
        self.grid[y_0][x_0] = Road()

        visited.add((x_0, y_0))
        init_neig = self.get_nc_neighbors(x_0, y_0)
        walls = set(init_neig)

        while len(walls) != 0:
            x, y = random.sample(walls, 1)[0]
            visited.add((x,y))
            visted_nc_neig = 0
            for j, i in self.get_nc_neighbors(x, y):
                if (j,i) in visited:
                    visted_nc_neig += 1


            if visted_nc_neig == 1:
                self.grid[y][x] = Road()
                for wall in self.get_nc_neighbors(x,y):
                    walls.add(wall)

            walls.remove((x,y))

    def draw(self):
        for i, row in enumerate(self.grid):
            for j, element in enumerate(row):
                self.layout.addWidget(element.get_widget(), i, j)

    def set_legend(self):
        road = Road()
        road.set_orientation(-1, 0)
        self.layout.addWidget(road.get_widget(), 0, 1)
        road.set_orientation(0, 1)
        self.layout.addWidget(road.get_widget(), 0, 2)
        road.set_orientation(1, 0)
        self.layout.addWidget(road.get_widget(), 0, 3)
        road.set_orientation(0, -1)
        self.layout.addWidget(road.get_widget(), 0, 4)

        road.set_orientation(-1, -1)
        self.layout.addWidget(road.get_widget(), 1, 1)
        road.set_orientation(-1, 1)
        self.layout.addWidget(road.get_widget(), 1, 2)
        road.set_orientation(1, 1)
        self.layout.addWidget(road.get_widget(), 1, 3)
        road.set_orientation(1, -1)
        self.layout.addWidget(road.get_widget(), 1, 4)

        car = Car()
        car.set_orientation(-1, 0)
        self.layout.addWidget(car.get_widget(), 2, 1)
        car.set_orientation(0, 1)
        self.layout.addWidget(car.get_widget(), 2, 2)
        car.set_orientation(1, 0)
        self.layout.addWidget(car.get_widget(), 2, 3)
        car.set_orientation(0, -1)
        self.layout.addWidget(car.get_widget(), 2, 4)


