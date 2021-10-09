import SearchGrid

def search(grid, start, end):
    def cost(path):
        return grid.distance(path[-1], end)

    frontier = []
    frontier.append([start])

    while len(frontier) > 0:
        current_path = frontier.pop(0)
        last = current_path[-1]
        for n in grid.neighbors(last[0], last[1]): 
            if n == end:
                current_path.append(n)
                return (current_path, frontier)
            if n not in current_path:
                new_path = current_path.copy()
                new_path.append(n)
                frontier.append(new_path)
        frontier.sort(key=cost)

grid = SearchGrid.SearchGrid(20)
start = (3,2)
end = (15,8)
path = search(grid, start, end)
grid.display_path_and_frontier(path, start, end)
#grid.display_distances((10,10))

