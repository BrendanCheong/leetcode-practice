from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        We have to use BFS here to go down the tree level by level. The answer
        is to NOT just only go through the right side of the tree. We actually also need
        the left side of the tree if the right side of the tree is empty.
        Instead, we only add nodes to the result, if the node is the LAST PROCESSED
        node, or in this case the right-most node
        """
        q = deque()
        res = []
        level = 1
        if root:
            q.append(root)
        while q:
            print(f"The level is {level}")
            curr_length_of_queue = len(q)
            for i in range(len(q)):
                curr = q.popleft()
                if i == curr_length_of_queue - 1:
                    res.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            level += 1
        return res
        
