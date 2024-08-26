# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        cache = {}
        def dfs(node):
            if node in cache:
                return cache[node]
            newNode = Node(node.val)
            cache[node] = newNode
            for n in node.neighbors:
                cache[node].neighbors.append(dfs(n))
            return newNode
        return dfs(node) if node else None

