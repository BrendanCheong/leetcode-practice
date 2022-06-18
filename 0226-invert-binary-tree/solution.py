# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        Recursively, run through all the subtree and invert each subtree
        """
        if not root:
            return None
        # swap the left and right
        root.left, root.right = root.right, root.left
        # continue to recurse through the rest of the sub-trees
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        
