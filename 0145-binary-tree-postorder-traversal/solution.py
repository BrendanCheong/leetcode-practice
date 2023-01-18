# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        left -> right -> root
        but using stack we do in reverse order
        """
        visited, stack = set(), []
        res = []
        stack.append(root)

        while stack:
            node = stack.pop()
            if node and node in visited:
                # we need to add out visited nodes to the answer somewhere
                res.append(node.val) 
            elif node:
                stack.append(node)
                visited.add(node)
                stack.append(node.right)
                stack.append(node.left)
        return res
