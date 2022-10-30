# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
#         """
#         Recursively, run through all the subtree and invert each subtree
#         """
#         if not root:
#             return None
#         # swap the left and right
#         root.left, root.right = root.right, root.left
#         # continue to recurse through the rest of the sub-trees
#         self.invertTree(root.left)
#         self.invertTree(root.right)
#         return root
        """
        Iteratively, this is a BFS algorithm using a queue. 
        You can also do it using a DFS
        """
        # 1. edge case
        if not root:
            return None
        q = []
        q.append(root)
        
        while q:
            curr = q.pop()
            
            # swap the nodes
            curr.left, curr.right = curr.right, curr.left
            
            # add more nodes to the queue if there is
            if (curr.left):
                q.append(curr.left)
                
            if (curr.right):
                q.append(curr.right)
        return root
        
        
