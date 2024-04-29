# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visited, stack = set(), []
        stack.append(root)
        res = []
        
        while stack:
            node = stack.pop()
            if node and node in visited:
                res.append(node.val)
            elif node:
                stack.append(node.right)
                stack.append(node.left)
                stack.append(node)
                visited.add(node)
        return res


