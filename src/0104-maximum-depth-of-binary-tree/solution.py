# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Max space and time is O(n) due to a BST that can look like a single linked list
        We are using a DFS algo to find the answer
        Time: O(n)
        Space: O(n)
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))
        
        
