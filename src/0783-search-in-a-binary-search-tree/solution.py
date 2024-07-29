# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        In the BST, the left subtree is the smaller number,
        the right is the bigger number
        BST are preferred over arrays because insertion is O(log n) and searching is in 
        O(n) for the worst case (Tree looks like a Single LL)
        """
        # Means we have no trees to go through, meaning we have reached the end
        # and there are no target nodes
        if not root:
            return None
        elif root.val == val:
            return root
        elif val < root.val:
            # search left tree, we need smaller numbers, the tree is too big now
            return self.searchBST(root.left, val)
        else:
            # search right tree, we need bigger numbers, the tree is too small
            return self.searchBST(root.right, val)

