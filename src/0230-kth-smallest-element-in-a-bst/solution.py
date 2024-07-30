# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        I wonder if theres a O(k) space solution, as this DFS in-order traversal is just
        O(n) space.

        Note: we use inorder traversal as we want a sorted list to get the kth value
        TO answer the qns, how to modify the BST if theres insert and delete operations:

        we can maintain the size of each subtree in every node, which allows us to efficiently perform order statistics. Then when we add or delete a node, update the node's
        size. Then when we search kth element, we can just do k == node.size
        """
        res = []
        def inorder(node: Optional[TreeNode], k: int):
            if not node:
                return
            inorder(node.left, k)
            res.append(node.val)
            inorder(node.right, k)
        inorder(root, k)
        return res[k - 1]
