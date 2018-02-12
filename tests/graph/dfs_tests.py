import unittest
import graph/dfs

# TESTDATA

adj_list = {
    'A': ['B', 'F'], 
    'B': ['C', 'E'], 
    'C': ['D'],
    'D': ['B', 'H'], 
    'E': ['D', 'G'], 
    'F': ['E', 'G'], 
    'G': ['F'], 
    'H': ['G']
}

al2 = {
    'A': ['B', 'C', 'F'], 
    'B': ['E'],
    'C': ['D'],
    'D': ['A', 'H'],
    'E': ['F', 'G', 'H'],
    'F': ['B', 'G'],
    'G': [],
    'H': ['G']
}

al3 = {
    'A': ['C'], 
    'B': ['C'],
    'C': ['D', 'E'],
    'D': ['F'],
    'E': ['F'],
    'F': ['G', 'H'],
    'G': [],
    'H': []  
}

al4 = {
    'A': ['B'], 
    'B': ['C', 'D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['B', 'F', 'G'],
    'F': ['C', 'H'],
    'G': ['H', 'J'],
    'H': ['K'],
    'I': ['G'],
    'J': ['I'],
    'K': ['L'],
    'L': ['J']
}

class DFS_Test(unittest.TestCase):
    
    def test1(self):
        dfs = DFS(al1)
        dfs.run()

