# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def maxDepth(node: Optional[TreeNode]):
            nonlocal diameter
            if not node:
                return 0

            maxDepthLeft = maxDepth(node.left)
            maxDepthRight = maxDepth(node.right)

            diameter = max(diameter, maxDepthLeft + maxDepthRight)

            return 1 + max(maxDepthLeft, maxDepthRight)
        
        maxDepth(root)
        return diameter

