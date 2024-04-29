from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque()
        q.append((0, root))
        max_width = 0
        while q:
            n = len(q)
            curr_idx, node = q[0] # peek
            for i in range(n):
                # for all nodes at this current level
                idx, node = q.popleft()
                if node.left:
                    q.append((2 * idx, node.left))
                if node.right:
                    q.append((2 * idx + 1, node.right))
            max_width = max(max_width, idx - curr_idx + 1)
        return max_width

