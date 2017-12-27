

from Graphs.GraphWithAdjecencyList import Graph
from  Stacks_and_Queue.Stacks.MyStack import MyStack



def topoSort(graph):

    stack = MyStack()
    visited = set()

    for vKey in graph.vertices:

        vertex = graph.vertices[vKey]



        if vertex in visited:
            continue
        else:
            topUtil(vertex=vertex,visited=visited,stack=stack,graph=graph)

    return stack


def topUtil(vertex,visited,stack,graph):

    visited.add(vertex)

    for childVertexKey in vertex.connectedTo:
        childVertex = graph.vertices[childVertexKey]

        if childVertex in visited:
            continue
        topUtil(vertex=childVertex,visited=visited,stack=stack,graph=graph)

    stack.push(vertex)










g = Graph()
g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addVertex("E")
g.addVertex("F")
g.addVertex("G")


g.addEdge(fromVertex="A",toVertex="C",weight=50)
g.addEdge(fromVertex="B",toVertex="C",weight=50)
g.addEdge(fromVertex="C",toVertex="D",weight=50)
g.addEdge(fromVertex="B",toVertex="E",weight=50)
g.addEdge(fromVertex="D",toVertex="F",weight=50)
g.addEdge(fromVertex="E",toVertex="F",weight=50)
g.addEdge(fromVertex="F",toVertex="G",weight=50)

stack = topoSort(g)
while not stack.isEmpty():
    vertex = stack.peek()
    stack.pop()
    print(vertex.key)





