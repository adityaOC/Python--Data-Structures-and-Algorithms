from Stacks_and_Queue.Stacks.MyStack import MyStack

from Graphs.GraphWithAdjecencyList import Graph,Color


def dfs(graph,startNode,stack):


    stack.push(startNode)
    print(stack.peek().key)


    while not stack.isEmpty():

        currentVertex = stack.peek()
        currentVertex.color = Color.Grey

        for key in currentVertex.connectedTo:

            childVertex = graph.vertices[key]
            if childVertex.color !=Color.Grey:
                return  dfs(graph,childVertex,stack)

        stack.pop()



def dfsRec(graph,startNode):

    currentVertex = startNode
    if currentVertex.color != Color.Grey:
        currentVertex.color = Color.Grey
        print(currentVertex.key)

        for key in currentVertex.connectedTo:
            child = graph.vertices[key]
            if child.color != Color.Grey:
              dfsRec(graph,child)
        return
    else:
        return




g = Graph()
g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addVertex("E")
g.addVertex("F")
g.addVertex("G")
g.addVertex("Z")


g.addEdge(fromVertex="A",toVertex="B",weight=50)
g.addEdge(fromVertex="A",toVertex="F",weight=50)
g.addEdge(fromVertex="B",toVertex="C",weight=50)
g.addEdge(fromVertex="B",toVertex="Z",weight=50)
g.addEdge(fromVertex="C",toVertex="D",weight=50)
g.addEdge(fromVertex="D",toVertex="E",weight=50)
g.addEdge(fromVertex="F",toVertex="G",weight=50)
g.addEdge(fromVertex="G",toVertex="H",weight=50)

stack = MyStack()
#dfs(g,g.vertices["A"],stack)

dfsRec(g,g.vertices["A"])







