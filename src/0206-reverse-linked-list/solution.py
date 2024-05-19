# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: int = None):
        self.val = val
        self.next = next # By default the tail of the LL is None

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        You start with None, which is the actual head of the linked list
        Then have 2 pointers to keep track of nodes so we can reverse it
        by relinking it backwards.
        
        Time: O(n)
        Space: O(1)
        """
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            
            # Update the previous to go forward
            prev = curr
            # Update the current to go forward
            curr = temp
        return prev # the new head of the Linked List
