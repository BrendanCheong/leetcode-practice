# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # the LCA or the closet parent node to both the given nodes, will be:
        # root > p and root < q, so iterate through the tree until we find that
        while root:
            if root.val < p.val and root.val < q.val:
                # if we're too small, go bigger
                # BST, bigger subtree is always on the right
                root = root.right
            elif root.val > p.val and root.val > q.val:
                # if we're too big, go smaller
                # BST, smaller sub tree is always on the left
                root = root.left
            else:
                return root

