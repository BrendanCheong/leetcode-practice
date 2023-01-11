from typing import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Since the diameter can start at any node, we have to find the longest left and right path of each and every node.
    """
    def __init__(self):
        self.max_diameter = 0
    def depth(self, node: Optional[TreeNode]):
        # find the depth of the left and right nodes
        left = self.depth(node.left) if node and node.left else 0
        right = self.depth(node.right) if node and node.right else 0

        # the diameter is now the longest left and right path combined
        # use it to find the max diameter
        current_diameter = left + right
        self.max_diameter = max(self.max_diameter, current_diameter)

        # calculate the depth of each side left/right
        return 1 + (left if left > right else right)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.depth(root)
        return self.max_diameter
