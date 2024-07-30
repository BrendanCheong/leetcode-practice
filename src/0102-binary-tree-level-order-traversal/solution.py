from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        res = []

        if root:
            queue.append(root)
        level = 1

        while queue:
            print(f"Current level: {level}")
            level_arr = []
            # empty the queue
            for _ in range(len(queue)):
                curr = queue.popleft()
                level_arr.append(curr.val)
                # add to queue
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level += 1
            res.append(level_arr)
        return res
