# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead

        Did you notice that the solution is to first split the list into 2,
        then the first list starts at the head, while the second list starts at the tail
        to form the new Linked List?
        So [1, 2] and [3, 4, 5] is 1 - 5 - 2 - 4 - 3

        This solution is a combination of what we learned
        1. Slow and fast pointer can find the middle node
        2. Reverse the second list using reverse linked list algo, so we start at the end of the
        original list (so [3, 4, 5] is now [5, 4, 3])
        3. Swap the linked list node, then update the pointers until we reach the end

        Time: O(n)
        Space: O(1)
        """
        if not head:
            return head
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        prev, curr = None, slow

        while curr:
            curr.next, prev, curr = prev, curr, curr.next     
        first, second = head, prev

        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next


            
            
        
