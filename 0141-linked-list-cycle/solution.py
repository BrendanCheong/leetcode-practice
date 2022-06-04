# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        The naive solution, is in O(n) time where I am storing the past heads
        in memory or rather in a HashTable in O(1) time and to search for past
        values in O(1) time. If I encounter a visited value, then output True,
        if I have reached the end then the next val is None, output False
        """
        mem = set()
        curr = head
        while (head not in mem):
            if (head == None):
                return False
            mem.add(head)
            head = head.next
        return True
        
