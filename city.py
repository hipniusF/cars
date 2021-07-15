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

        self.make_rand_roads()
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

    def make_rand_roads(self):
        n_hor = 5
        n_ver = 5

        def set_road(x, y, orient):
            if not isinstance(self.grid[y][x], Road):
                new_road = Road()
                new_road.set_orientation(orient)
                self.grid[y][x] = new_road
            else:
                old_orient = self.grid[y][x].orientation
                new_orient = (old_orient[0] + orient[0], old_orient[1] + orient[1])

                new_road = Road()
                new_road.set_orientation(new_orient)
                self.grid[y][x] = new_road

        def make_road(init_pnt, ver=False, reverse=False):
            width = len(self.grid) if ver else len(self.grid[0])

            for i in range(width):
                # if random.random() < 0.15:
                #     ver = not ver
                #     tmp = i
                #     i = init_pnt
                #     init_pnt = tmp

                if not ver:
                    orient = (-1,0) if reverse else (1, 0)
                    set_road(i, init_pnt, orient)
                else:
                    orient = (0,-1) if reverse else (0, 1)
                    set_road(init_pnt, i, orient)

        h_paths = set(range(len(self.grid[0])))
        for path in random.sample(h_paths, n_hor):
            reverse = random.randint(0, 1)
            make_road(path, reverse=reverse)

        v_paths = set(range(len(self.grid)))
        for path in random.sample(v_paths, n_ver):
            reverse = random.randint(0, 1)
            make_road(path, ver=True, reverse=reverse)

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


