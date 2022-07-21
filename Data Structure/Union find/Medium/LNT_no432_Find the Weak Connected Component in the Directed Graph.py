# Similar to LeetCode no323. Number of Connected Components in an Undirected Graph

from typing import (
    List,
)
from lintcode import (
    DirectedGraphNode,
)

"""
class DirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param nodes: a array of Directed graph node
    @return: a connected set of a directed graph
    """
    def connectedSet2(self, nodes: List[DirectedGraphNode]) -> List[List[int]]:
        n = len(nodes)
        parent = {}
        for node in nodes:
            if node.label not in parent:
                parent[node.label] = node.label
            for nei in node.neighbors:
                if nei.label not in parent:
                    parent[nei.label] = nei.label
                self.union(parent, node.label, nei.label)
        
        memo = collections.defaultdict(list)
        for node in nodes:
            root = self.find(parent, node.label)
            memo[root].append(node.label)
            
        res = []
        for _, nodes in memo.items():
            res.append(sorted(nodes))
        return res
    
    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]
    
    def union(self, parent, i, j):
        pi, pj = self.find(parent, i), self.find(parent, j)
        if pi != pj:
            parent[pj] = pi