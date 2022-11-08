from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        What are some assumptions? the LL are not of equal length all the time, the LL will at least be length 1.
        What is the naive solution? Well we could try to form the number by iterating through each LL, first number is x1 * 1, x2 * 10, x3 * 100 and so on. Then we can add those numbers. Then given those 2 added numbers, add them together to get the answer, which must be converted into a LL.

        What about an actual solution? we have 2 pointers at the start of each LL, for each node, we add them together. If the answer is > 9, we create another node at the end with val = 1. The next time we add the another pair of nodes, check to see if there is 1 at the end.

        Time: O(L + 1), L being longer LL
        Space: O(L + 1), L being longer LL
        """
        dummy = ListNode()
        curr = dummy
        carry = 0
        #! IMPORTANT: need or carry, or else if we get [7], [8], we forget to add "1" to the end
        while l1 or l2 or carry:
            #1. make sure if either LL is longer than the other, the shorter one defaults to 0
            node1 = l1.val if l1 else 0
            node2 = l2.val if l2 else 0
            added = node1 + node2 + carry # remember to add the carry over...

            #2. we can only be above 10, since the range is 0 <= x <= 9
            if added >= 10: 
                carry = 1 # carry is always 1
                added %= 10
                curr.next = ListNode(added)
            else:
                curr.next = ListNode(added)
                carry = 0 # if carry is not used, then reset it

            # move the pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

