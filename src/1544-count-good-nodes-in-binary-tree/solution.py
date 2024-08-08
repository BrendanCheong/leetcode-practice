# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Basically we have to use DFS to go down a path/subtree. Then for that node,
        we look at past nodes we have travelled to determine whether its the max node
        If current node is not the max node, +0, if it is, +1 to good nodes
        """
        def dfs(node: TreeNode, max_val: int, good_nodes: int):
            # Unravel the recursion tree
            if not node:
                return good_nodes
            # the Iterative condition
            if node.val >= max_val:
                good_nodes += 1
            max_val = max(node.val, max_val)
            # Go left then right
            good_nodes = dfs(node.left, max_val, good_nodes)
            good_nodes = dfs(node.right, max_val, good_nodes)

            return good_nodes
            
        return dfs(root, root.val, 0)
