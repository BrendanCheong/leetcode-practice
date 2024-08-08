# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Post-order iteratively requires 2 stacks. One stack to know which we visited
        and one stack to know which one we went through. So postorder is left-right-middle
        """
        stack, visit = [root], [False]
        res = []
        while stack:
            curr, visited = stack.pop(), visit.pop()
            if curr:
                # because its a stack, we have to do the reverse of left-right-middle
                # we do middle-right-left, middle being we add the middle val to the res
                if visited:
                    res.append(curr.val)
                else:
                    stack.append(curr)
                    visit.append(True)
                    if curr.right:
                        stack.append(curr.right)
                        visit.append(False)
                    if curr.left:
                        stack.append(curr.left)
                        visit.append(False)
        return res
