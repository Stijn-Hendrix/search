import SearchGrid

def search(grid, xstart, ystart, xend, yend):
    def cost(path):
        return grid.distance(path[-1], (xend, yend, 2))

    frontier = []
    frontier.append([(xstart, ystart)])

    while len(frontier) > 0:
        current_path = frontier.pop(0)
        current_start = current_path[-1]
        for n in grid.neighbors(current_start[0], current_start[1]): 
            if n == (xend, yend):
                current_path.append(n)
                return (current_path, frontier)

            if n not in current_path:
                new_path = current_path.copy()
                new_path.append(n)
                frontier.append(new_path)
        
        frontier.sort(key=cost)

grid = SearchGrid.SearchGrid(20, )
grid.display_path_and_frontier(search(grid, 3,2, 15, 8), (3,2), (15,8))
#grid.display_distances((10,10))

