# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_linked_list(self, head: Optional[ListNode]) -> ListNode:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        The trick comes from knowing that you only need to compare each half of the LL,
        meaning that you only need to compare 2 halfs, not compare the whole list twice
        by iterating through the list twice

        1. We can use the fast and slow pointers to find the middle of the LL
        2. Then reverse one-half of the LL
        3. Progress through each half, and if the nodes dont match, its not a palindrome 
        """
        # 1. Get the slow pointer to the middle of LL
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Now reverse the half of the LL starting from the slow pointer
        # the reverse list is the second half (right side) of the LL
        reverse_node = self.reverse_linked_list(slow)

        # 3. Go through each half, and make sure they're equal
        while reverse_node:
            if reverse_node.val != head.val:
                return False
            
            # progress the pointers
            reverse_node = reverse_node.next
            head = head.next
        return True
        
