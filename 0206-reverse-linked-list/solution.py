# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        We want the current head to point to none
        then the next node point to the previous node
        do until the last node, make that the head node now
        """
        # start off with None as the prev node
        # get the current head node
#         prev = None
#         curr = head
#         while curr:
#             # here is where we do the setting of nodes
#             next_node = curr.next
#             curr.next = prev
            
#             # update the previous node to be the one we want the next node to attach to
#             # update curr to go to the next_node
#             prev = curr
#             curr = next_node
#         return prev # return the head node
        return self.reverseListRecursive(head, None)
    def reverseListRecursive(self, curr: Optional[ListNode], prev: Optional[ListNode]) -> Optional[ListNode]:
        if not curr:
            return prev
        next_node = curr.next
        curr.next = prev
        return self.reverseListRecursive(next_node, curr)
    
        
        
            
        
