# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_min_node(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # add the 'and curr.left' or else we will end up with a Null node
        while root and root.left:
            root = root.left
        return root
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Note that when you delete a node, you have to think about what if I delete the
        root node, who is the new root node then? How am I gonna rebalance the rest of the
        tree?

        Case 1: The node has 0 or 1 childs
        Case 2: The node has 2 childs - I need to keep the BST balanced, so I need
        to replace the removed node with the minimum node on the right subtree

        The time complexity of these operations is \U0001d442(\U0001d459\U0001d45c\U0001d454 \U0001d45b) if the tree is balanced. 
        However, if the tree is unbalanced, the time complexity can be \U0001d442(\U0001d45b) in the worst case.

        Space: O(n) (worst case, basically a Single Linked List structure)
        """
        # base case, node not found after full traversal
        if not root:
            return None

        if key < root.val:
            # go left for smaller nums
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            # go right for bigger nums
            root.right = self.deleteNode(root.right, key)
        else:
            # in this case we found the node to remove
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # in this case, I have 2 childs, case 2 scenario here
                # find the min node for the right sub-tree
                min_node = self.find_min_node(root.right)

                # "delete" the found key/node to delete
                root.val = min_node.val

                # rebalance the right sub-tree since I just took its
                # min node
                root.right = self.deleteNode(root.right, min_node.val)
        
        # unravel recursion tree
        return root
        
