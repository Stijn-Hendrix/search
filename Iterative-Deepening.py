import Graph

graph = Graph.OneDirectionalGraph()

def search(start, end, depth):
    frontier = []
    frontier.append([start])

    k = 0
    while len(frontier) > 0:
        currentPath = frontier.pop(0)
        k += 1
        print(currentPath)
        if k < depth:
            for n in currentPath[-1].children:
                if n.value == end:
                    currentPath.append(n)
                    return "Final path: " + str(currentPath)
                elif n not in currentPath:
                    a = currentPath.copy()
                    a.append(n)
                    frontier.insert(0, a)

depth = 1
goal = None
while goal == None:
    goal = search(graph.root, "g", depth)
    depth += 1

print (goal)