from collections import deque

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        # BFS queue initialized with the root of the main tree
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            
            # Check if the current node's subtree matches subRoot
            if self.isSameTree(node, subRoot):
                return True
            
            # Add the left and right children to the queue to explore next
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # if we reached here means we ran out of nodes to check after searching through all nodes
        return False
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        # Check both left and right subtrees recursively
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
