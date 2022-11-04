from typing import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        isSameTree algo is a dfs algo, where we visit the left side of the tree and the right side of the tree,
        where the left and right must be equal. Thus we have dfs(left, right) to go down the tree and dfs(right, left) to go down the tree, where going in both opposite directions must be the same

        if we hit 2 nulls, its True
        if we hit 1 null only, that means symmetry is broken, as either left or right is null, not both null

        Time: O(n) where n is the number of nodes
        Space: O(h) height of the tree 
        """
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and (isSameTree(p.left, q.right) and isSameTree(p.right, q.left))
        return isSameTree(root.left, root.right) if root else True
        
