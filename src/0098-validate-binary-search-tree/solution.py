# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: TreeNode, left: int, right: int):
            # reached the end so just unravel the recursion
            if not node:
                return True
            # a valid BST must be between the values
            if not (left < node.val < right):
                return False
            # go left and right
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)

        return dfs(root, float("-inf"), float("inf"))
