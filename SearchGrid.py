from typing import ForwardRef
from matplotlib import pyplot
import matplotlib
import numpy

class SearchGrid:

    data = None
    size = 0
    cmap = None
    blocked_code = 0

    visited = set()

    def color_code(self, index):
        return index / 6 - 0.01

    def __init__(self, size) -> None:
        self.size = size
        self.data = [[self.color_code(1) for x in range(size)] for y in range(size)]
        self.cmap = matplotlib.colors.ListedColormap(['green', 'white',  'gray', 'blue', 'black', 'red'])

        blocked = self.color_code(4)
        self.blocked_code = blocked
        self.put(8,10,blocked) 
        self.put(8,9,blocked) 
        self.put(8,8,blocked) 
        self.put(8,7,blocked) 
        self.put(8,6,blocked) 
        self.put(14,10,blocked) 
        self.put(14,11,blocked) 
        self.put(14,12,blocked) 


    def distance(self, start, end):
        return abs(start[0] - end[0]) + abs(start[1] - end[1])

    def put(self, x, y, val):
        self.data[y][x] = val
    
    def get(self, x, y):
        return self.data[y][x]

    def display_distances(self, end):
        for x in range(0, self.size):
            for y in range(0, self.size):
                self.put(x, y, -self.distance( (x, y), end)) 
        self.rebuild()

    def valid(self, x, y):
        return self.get(x, y) != self.blocked_code and x >= 0 and y >= 0 and x < self.size - 1 and y < self.size - 1

    def neighbors(self, x, y):
        n = []
        if self.valid(x, y + 1):
            n.append((x, y + 1))
        if self.valid(x + 1 , y):
            n.append((x + 1, y))
        if self.valid(x, y - 1):
            n.append((x, y - 1))
        if self.valid(x - 1, y):
            n.append((x - 1, y))
        return n

    def display_path_and_frontier(self, coords, start, end):
        found_path = coords[0]
        frontier = coords[1]


        for coord in frontier:
            c = coord[-1]
            self.put(c[0], c[1], self.color_code(2))

        if len(coords) >= 3:
            visited = coords[2]
            for coord in visited:
                self.put(coord[0], coord[1], self.color_code(2))


        for coord in found_path:
            self.put(coord[0], coord[1], self.color_code(3))

        self.put(start[0], start[1], self.color_code(0))
        self.put(end[0], end[1],  self.color_code(5))

        self.rebuild()

    def rebuild(self):
        pyplot.figure(figsize=(5,5))
        s = range(0, self.size)
        pyplot.xticks(s)
        pyplot.yticks(s)
        pyplot.ylim(-0.5, -0.5 + self.size)
        pyplot.imshow(self.data, cmap=self.cmap)
        pyplot.show()


  