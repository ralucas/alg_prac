"""
    Depth First Search
    Current implementation expects a Graph
    as a dictionary with adjacent list, e.g.
    G = {'A': ['B', 'D'], 'B': ['C'], 'C': ['D', 'A']}
"""
class DFS:
    def __init__(self, G):
        self.clock = 0
        self.PP = {}
        self.visited = []
        self.G = G
    
    def previsit(self, v):
        if v not in self.PP:
            self.PP[v] = {}
        self.clock += 1
        self.PP[v]['pre'] = self.clock

    def postvisit(self, v):
        if v not in self.PP:
            self.PP[v] = {}
        self.clock += 1
        self.PP[v]['post'] = self.clock

    def explore(self, v):
        self.visited.append(v)
        self.previsit(v)
        for E in self.G[v]:
            if E not in self.visited:
                self.explore(E)
        self.postvisit(v)

    def run(self):
        for V, E in self.G.items():
            if V not in self.visited:
                self.explore(V)
        self.printPP()
    
    def printPP(self):
        for k, v in self.PP.items():
            print "--- %s ---" % k
            print "pre : %d" % v['pre']
            print "post : %d" % v['post']
