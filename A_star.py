from queue import PriorityQueue

class Graph:

    def __init__(self,totalNodes,directed=False):
        self.totalNodes = totalNodes
        self.adjList = [ [] for i in range(totalNodes)]
        self.directed = directed
        self.heuristic = { i: ((i*2)+2) for i in range(totalNodes)}

    def addEdge(self,u,v,weight=1):
        self.adjList[u].append((v,weight))

        if not self.directed :
            self.adjList[v].append((u,weight))

    def printAdjList(self):
        for i in range(self.totalNodes):
            print(i," -> ",self.adjList[i])

    def aStarAlgo(self,start,goal):

        print(self.heuristic)

        open_set = set()
        open_set.add(start)

        close_set = set()

        g = {}
        g[start] = 0

        parents ={}
        parents[start] = start

        while len(open_set) > 0:
            n = None

            for v in open_set :
                
                if n==None or g[v] + self.heuristic[v] < g[n] + self.heuristic[n]:
                    n = v

            if n == goal :
                path = []

                while parents[n] != n:
                    path.append(n)
                    n = parents[n]

                path.append(start)

                path.reverse()

                print("Path Found : ",path)
                return path
            else:
                print("chose" ,n," as current node")
                for  (node,weight) in self.adjList[n] :
                    if node not in open_set and node not in close_set:
                        open_set.add(node)
                        parents[node] = n
                        g[node] = g[n] + weight

                    else :
                        if g[node] > g[n] + weight:
                            g[node] = g[n]+weight
                            parents[node] = n


                            if node in close_set:
                                close_set.remove(node)
                                open_set.add(node)

            if n == None:
                print("Path Not Found")
                return None

            open_set.remove(n)
            close_set.add(n)

        print("Path Not Found")
        return None


g = Graph(6,True)
g.addEdge(0,1,2)
g.addEdge(0,4,3)
g.addEdge(1,2,1)
g.addEdge(1,5,9)
g.addEdge(4,3,6)
g.addEdge(3,5,12)


g.printAdjList()
print()
print(g.aStarAlgo(0,5))