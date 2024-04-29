# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        BST is false when the root is not smaller than the right
        and when the root is not bigger than the left.
        
        We traverse the BST by moving through the tree in pre-order DFS traversal
        by starting of -inf, inf, we see where the number ranges
        """
        def validTree(node, left, right):
            if not node:
                return True # empty BST is still a BST
            if not (node.val < right and node.val > left):
                return False
            # move to the left first then to the right
            # when traversing left, we know the left node and root node
            # when traversing right, we know the right node and root node
            return validTree(node.left, left, node.val) and validTree(node.right, node.val, right)
        return validTree(root, float('-inf'), float('inf'))
        
