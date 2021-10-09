import SearchGrid

grid = SearchGrid.SearchGrid(20)

def search(grid, start, end):
    frontier = []
    frontier.append([start])
    visited = set()

    while len(frontier) > 0:
        currentPath = frontier.pop(0)
        last = currentPath[-1]
        print(currentPath)
        for n in grid.neighbors(last[0], last[1]):
            if n == end:
                currentPath.append(n)
                return [currentPath, frontier, visited]
            elif n not in currentPath and n not in visited:
                a = currentPath.copy()
                a.append(n)
                visited.add(n)
                frontier.append(a)

start = (6,5) 
end = (15,11)
path = search(grid, start, end)
grid.display_path_and_frontier(path, start, end)