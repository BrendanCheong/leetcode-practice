# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        The naive solution, is in O(n) time where I am storing the past heads
        in memory or rather in a HashTable in O(1) time and to search for past
        values in O(1) time. If I encounter a visited value, then output True,
        if I have reached the end then the next val is None, output False.
        
        
        Proper solution is to use Floyd's Cycle Finding Algo using two pointers
        that runs in O(n - 1) time and O(1) memory with 2 pointers
        
        Both pointers start at the head, we move the slow pointer by 1, the fast
        by 2 every iteration. Eventually they will meet in O(n-1) time.
        """
        def cycleHashVersion(head: Optional[ListNode]) -> bool:
            mem = set()
            curr = head
            while (head not in mem): # keep checking if in memory
                if (head == None):
                    # we reached the end of the LL, its therefore no cycle
                    return False
                mem.add(head)
                head = head.next
            return True
        def cyclePointerVersion(head: Optional[ListNode]) -> bool:
            slow, fast = head, head
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return True
            return False
            
        return cyclePointerVersion(head)
        
