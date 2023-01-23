from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseListRecursive(curr: Optional[ListNode], prev: Optional[ListNode]) -> Optional:
            if not curr:
                return prev
            next_node = curr.next
            curr.next = prev
            return reverseListRecursive(next_node, curr)
        # return reverseListRecursive(head, None)

        def reverseListIterative(head: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            curr = head

            while curr:
                next_node = curr.next
                curr.next = prev

                prev = curr
                curr = next_node
            return prev
        return reverseListIterative(head)



        

    
        
        
            
        
