import SearchGrid

grid = SearchGrid.SearchGrid(20)

def search(grid, start, end):
    frontier = []
    frontier.append([start])


    while len(frontier) > 0:
        currentPath = frontier.pop(-1)
        last = currentPath[-1]
        for n in grid.neighbors(last[0], last[1]):
            if n == end:
                currentPath.append(n)
                return (currentPath, frontier)
            elif n not in currentPath:
                a = currentPath.copy()
                a.append(n)
                frontier.append(a)

start = (5,18) 
end = (15,6)
path = search(grid, start, end)
grid.display_path_and_frontier(path, start, end)