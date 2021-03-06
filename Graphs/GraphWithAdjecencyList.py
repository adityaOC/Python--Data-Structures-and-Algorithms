import  enum


class Color(object):
    White = 0
    Grey = 1
    Black = 2


class Vertex:

    def __init__(self,key,payload):
        self.key = key
        self.payload = payload
        self.color = Color.White
        self.connectedTo = {}#{vertex:weight}

    def addNeighbour(self,key,weight):
        self.connectedTo[key] = weight

    def getAllConectedNeighbours(self,key):
        return self.connectedTo


class Graph:

    def __init__(self):
        self.vertices = {}


    def addVertex(self,key):

        newVertex = Vertex(key,10)
        self.vertices[key] = newVertex


    def getVertex(self,key):

        return self.vertices[key]

    def addEdge(self,fromVertex,toVertex,weight):

        if fromVertex not in self.vertices:
            fromV = self.addVertex(fromVertex)
        else:
            fromV = self.vertices[fromVertex]

        if toVertex not in self.vertices:
            toV = self.addVertex(toVertex)
        else:
            toV = self.vertices[toVertex]


        fromV.addNeighbour(toVertex,weight)


"""
g = Graph()
g.addVertex(10)
g.addVertex(20)

g.addEdge(10,20,50)

"""






