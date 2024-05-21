# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Flyod's Tortise and Hare algo, if one pointer is one position faster than the other,
        and there is a cycle, it will always collide
        tortise = slow pointer
        hare = faster pointer
        """
        tortise, hare = head, head
        while hare and hare.next:
            tortise = tortise.next
            hare = hare.next.next
            if tortise == hare:
                return True
        return False
