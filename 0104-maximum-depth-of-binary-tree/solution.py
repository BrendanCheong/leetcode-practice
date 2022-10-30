from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        The Main solution is to give every node its own depth level, aka attaching weights
        DFS can be done, by adding a nodes to a stack, then finding the maximum depth from each node
        BFS can also be done.
        """
        """
        recursive binary trees or DFS are usually simplier and more straight-forwards
        """
        # def dfs_recursive(root: Optional[TreeNode]) -> int:
        #     if not root:
        #         return 0
        #     return 1 + max(dfs_recursive(root.left), dfs_recursive(root.right))
        # return dfs_recursive(root)
        stack = deque()
        stack.append((root, 1))
        res = -1
        # edge case, no root is depth of 0
        if not root:
            return 0
        
        while stack:
            (node, depth) = stack.popleft()
            res = max(depth, res)
            
            # edge case: sometimes we are given a null node, which means no neighbours, so don't
            # add nulls to the stack
            if node and node.left:
                stack.append((node.left, depth + 1))
            if node and node.right:
                stack.append((node.right, depth + 1))
        return res
        
