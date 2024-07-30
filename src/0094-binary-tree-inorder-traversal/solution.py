# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        In order traversal is like going through a sorted array
        from LEFT to RIGHT
        so its left, root, right
        thats why its called inorder, cuz the output is the sorted BST
        """
        res = []
        def dfs(node: Optional[TreeNode]) -> None:
            if node:
                dfs(node.left)
                res.append(node.val)
                dfs(node.right)
        dfs(root)
        return res
