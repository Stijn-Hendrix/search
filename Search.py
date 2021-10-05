import SearchGrid

def search(grid, xstart, ystart, xend, yend):
    def cost(path):
        tdst = 0
        for x in path:
            tdst += grid.distance(x, (xend, yend))
        return tdst

    frontier = []
    frontier.append([(xstart, ystart)])

    while len(frontier) > 0:
        current_path = frontier.pop(0)
        current_start = current_path[-1]
        for n in grid.neighbors(current_start[0], current_start[1]): 
       
            if n == (xend, yend):
                return current_path

            if n not in current_path:
                new_path = current_path.copy()
                new_path.append(n)
                frontier.append(new_path)
        
        frontier.sort(key=cost)

grid = SearchGrid.SearchGrid(20)
grid.setcoordinates(search(grid, 0,0, 10, 10))
#grid.display_distances((10,10))

