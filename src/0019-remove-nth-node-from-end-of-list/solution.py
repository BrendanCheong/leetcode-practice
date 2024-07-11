# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        The idea is this, have a ruler of nth length start from the head of the list
        Now move the rule, such that the end of this ruler is at the end of the list
        Notice that the start of the ruler is now nth node from the end of the list.
        So we must delete that node

        Time: O(n)
        Space: O(1)
        """
        # Edge case: if the list is empty or has only one node
        if not head:
            return head
        if not head.next:
            return None
        
        # 1. move the ruler until we find nth node from start
        # pin is the nth node from the start of the list
        # so like a ruler, if we move the ruler to the end of the list
        # the start of the ruler would now be nth node from end of list
        pin, end, curr, count = None, None, head, 0
        while curr:
            count += 1
            if count == n:
                # pin is the end of the ruler
                pin = curr
                end = head
            curr = curr.next
        
        # Special case: if we need to remove the first node
        # Means the node to remove is the head node
        if not pin:
            return head.next
        
        # 2. We move the ruler to the end of the list, so the start of the ruler
        # is now the node we want to remove is the "end" node
        prev = None
        while pin.next:
            prev = end
            end = end.next
            pin = pin.next
        
        # 3. Remove the nth node
        # its still possible for the node to be removed to be the head node
        # basically the "ruler" is already the full width of the list
        # "end" is the node to be removed, prev is the node behind the node we want to remove
        if prev:
            prev.next = end.next
        else:
            head = head.next
        
        return head
