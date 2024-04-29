# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        left -> root -> right
        but with stack its in reverse order
        """
        visited, stack = set(), []
        res = []
        stack.append(root)

        while stack:
            node = stack.pop()
            if node and node in visited:
                res.append(node.val)
            elif node:
                stack.append(node.right)
                stack.append(node)
                visited.add(node)
                stack.append(node.left)
        return res
