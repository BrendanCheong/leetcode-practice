# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        In recursion, we return the base case
        And for every if statement we must have a return statement, as without it
        the previous connections to the nodes are ignored
        Basically the return statement is to unravel the recursion tree
        """
        # If I reached the end of the tree wheres theres no leaf nodes
        if not root:
            new_node = TreeNode(val)
            return new_node
        if val < root.val:
            # I need to go left
            root.left = self.insertIntoBST(root.left, val)
            return root
        else:
            root.right = self.insertIntoBST(root.right, val)
            return root

