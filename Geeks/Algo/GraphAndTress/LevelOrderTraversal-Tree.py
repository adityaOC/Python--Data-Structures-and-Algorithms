
from Graphs.GraphWithAdjecencyList import Graph,Vertex
from Stacks_and_Queue.Queues.MyQueue import MyQueue
from Graphs.GraphWithAdjecencyList import Color

def bfsLevel(graph,startVertex):

    q = MyQueue()
    aux = MyQueue()

    q.enqueue(startVertex)

    q.enqueue("*")

    while  not q.isEmpty():

        v = q.dequeue()
        if type(v) is str and not q.isEmpty():
            print("----")
            q.enqueue("*")
            continue

        if type(v) is str and q.isEmpty():
            break

        printKey = v.key
        if v.color == Color.White:
            print(printKey)
            g.vertices[v.key].color = Color.Grey

        for connectedVertices in v.connectedTo:
            vertexTobeadded = g.vertices[connectedVertices]
            if vertexTobeadded.color != Color.Black:
                #vertexTobeadded.color = Color.Grey
                q.enqueue(vertexTobeadded)

        g.vertices[v.key].color= Color.Black





g = Graph()
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)
g.addVertex(4)
g.addVertex(5)
g.addVertex(6)
g.addVertex(7)


g.addEdge(1,2,50)
g.addEdge(1,3,50)
g.addEdge(1,2,50)
g.addEdge(2,4,50)
g.addEdge(2,5,50)
g.addEdge(3,6,50)
g.addEdge(3,7,50)


# g.addEdge(1,2,50)
# g.addEdge(1,3,50)
# g.addEdge(2,4,50)
#
# g.addEdge(3,4,50)
# g.addEdge(3,6,50)
# g.addEdge(4,5,50)

#Square graph
"""
g.addEdge(1,2,50)
g.addEdge(1,4,50)
g.addEdge(2,3,50)
g.addEdge(3,4,50)

"""
"""
g.addEdge(1,2,50)
g.addEdge(1,3,50)
g.addEdge(2,4,50)
g.addEdge(2,5,50)
g.addEdge(3,5,50)
g.addEdge(4,5,50)
g.addEdge(4,6,50)
g.addEdge(5,6,50)
"""



#bfs(g,g.getVertex(1))

print("-----------------------")
bfsLevel(g,g.getVertex(1))