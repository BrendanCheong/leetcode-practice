from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels, height = [], 0
        if not root:
            return []
        
        right_stack = []
        left_stack = []
        right_stack.append(root)
        while right_stack or left_stack:
            levels.append([])
            while right_stack:
                node = right_stack.pop()
                print(f"right stack: {node.val}")
                levels[height].append(node.val)
                if node.left:
                    left_stack.append(node.left)
                if node.right:
                    left_stack.append(node.right)
            if height % 2 == 0 :
                levels.append([])
                height += 1
            while left_stack:
                node = left_stack.pop()
                print(f"left stack: {node.val}")
                levels[height].append(node.val)
                if node.right:
                    right_stack.append(node.right)
                if node.left:
                    right_stack.append(node.left)
            height += 1
        if len(levels[-1]) == 0:
            levels.pop()
        return levels


        
