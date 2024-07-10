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
        # Edge case
        if not head:
            return head

        # 1. Slow and fast pointer to find the middle, fast will iterate until we hit the end
        # slow will be the middle node
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. Reverse the second list
        # We should start reversing from the node after the middle (slow.next).
        prev, curr = None, slow.next
        # separate the first half from the second half before reversing, which could lead to cycles in the list.
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # 3. merge the 2 lists now
        # the prev pointer is head of the second list now, note that curr = None
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            # Move on to the next set of pointers
            first, second = tmp1, tmp2



            
            
        
