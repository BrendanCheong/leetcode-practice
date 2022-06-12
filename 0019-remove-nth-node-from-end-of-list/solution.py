# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def index(node: Optional[ListNode]):
            if not node:
                return 0
            i = index(node.next) + 1
            if i > n:
                # now we recreate the entire LL starting from the head, while we skip the correct node
                node.next.val = node.val 
            return i # this is the node infront of the one we must remove
        index(head) # start mutation of the LL
        return head.next # we skip the correct node by one place
        
