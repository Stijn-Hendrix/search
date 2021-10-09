from typing import ForwardRef
from matplotlib import pyplot
import matplotlib
import numpy

class SearchGrid:

    data = None
    size = 0
    cmap = None

    visited = set()

    def __init__(self, size, ) -> None:
        self.size = size
        self.data = [[1 for x in range(size)] for y in range(size)]
        self.cmap = matplotlib.colors.ListedColormap(['white', 'green', 'gray', 'red', 'black'])

        self.put(8,10,0) 
        self.put(8,9,0) 
        self.put(8,8,0) 
        self.put(8,7,0) 
        self.put(8,6,0) 
        self.put(14,10,0) 
        self.put(14,11,0) 
        self.put(14,12,0) 


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
        return self.get(x, y) != 0 and x >= 0 and y >= 0 and x < self.size - 1 and y < self.size - 1

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
            self.put(c[0], c[1], .8)

        if len(coords) >= 3:
            visited = coords[2]
            for coord in visited:
                self.put(coord[0], coord[1], .8 )


        for coord in found_path:
            self.put(coord[0], coord[1], .4 )

        self.put(start[0], start[1], .2)
        self.put(end[0], end[1], 0.2)

        self.rebuild()

    def rebuild(self):
        pyplot.figure(figsize=(5,5))
        s = range(0, self.size)
        pyplot.xticks(s)
        pyplot.yticks(s)
        pyplot.ylim(-0.5, -0.5 + self.size)
        pyplot.imshow(self.data, cmap="gray")
        pyplot.show()


  