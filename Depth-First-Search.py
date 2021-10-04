import Graph

graph = Graph.OneDirectionalGraph()

def search(start, end):
    frontier = []
    frontier.append([start])


    while len(frontier) > 0:
        currentPath = frontier.pop(-1)
        print(currentPath)
        for n in currentPath[-1].children:
            
            if n.value == end:
                currentPath.append(n)
                return "Final path: " + str(currentPath)
            elif n not in currentPath:
                a = currentPath.copy()
                a.append(n)
                frontier.append(a)

print(search(graph.root,"g"))