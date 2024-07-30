# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        This uses a DFS algorithm, to check through each path for each side of the
        tree until we found a solution in either the left or right sub-tree. Note we
        return the first solution we find

        Time: O(n), worst case we examine all nodes
        Space: O(1)
        """
        # We reached the a null node, so backtrack
        if not root:
            return False
        
        # if the node is the leaf node
        if not root.left and not root.right:
            # check if the leaf node is the last node needed to make the targetSum
            # if not we will backtrack
            return targetSum == root.val

        # Recursive case: here is where we go through each side of the trees
        left_sum  = self.hasPathSum(root.left, targetSum - root.val)
        right_sum = self.hasPathSum(root.right, targetSum - root.val)

        # Return True if either subtree has a path that sums to the target
        return left_sum or right_sum
        
