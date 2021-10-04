class Node:
    def __init__(self, children, value) -> None:
        self.children = children
        self.value = value

    def __repr__(self) -> str:
        return self.value
            

class OneDirectionalGraph:

    root = None

    def __init__(self) -> None:
        g = Node([], "g")
        q = Node([], "q")
        a = Node([], "a")
        c = Node([a], "c")
        b = Node([a], "b")
        f = Node([c, g], "f")
        r = Node([f], "r")
        p = Node([q], "p")
        h = Node([q, p], "h")
        e = Node([r, h], "e")
        d = Node([e, c, b], "d")
        self.root = Node([p, e, d], "s")

