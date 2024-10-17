"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone = {}

        def dfs(node):
            if node in clone:
                return clone[node]
            clone[node] = Node(node.val)
            for nei in node.neighbors:
                clone[node].neighbors.append(dfs(nei))
            return clone[node]

        return dfs(node) if node else None

# Create clone empty hashmap. Do DFS and traverse through each node and its neighbours. If its already in clone, return that, else create empty node with val copied over and add to clone hashmap.

# Optimized solution >> Time : O(v+e). Space : O(v+e)