# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # prev is just to keep track of previously visited nodes to keep track of
        curr = head
        while (curr):
            next = curr.next
            curr.next = prev # make the node point to the previous node, starting from None
            prev = curr # keep track of previous node
            curr = next # move on to original next val
        return prev
            
        
