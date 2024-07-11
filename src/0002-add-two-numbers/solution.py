# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        There are 2 edge cases here:
        1. The lists are of different length, so if we have no number to add, jsut assume the number
        to add is a 0
        2. The lists are of length 1 each, so like 8 + 7 is 15, but we must remember to create 2 nodes

        Time: O(n)
        Space: O(n)
        """
        dummy = ListNode()
        curr = dummy

        carry_number = 0

        # Edge case 2: what if we had 2 single digits? like 8 + 7?
        # If there is still a carry left over, we want to continue the loop and add the carry number
        # to the remaining list!
        while l1 or l2 or carry_number:
            # Edge case 1: default to 0 if theres no value, 
            # as this scenario accounts for unequal length of the 2 lists
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0
            
            # 1. do the addition
            sum_result = value1 + value2 + carry_number
            # 2. get the carry number from the result
            carry_number = sum_result // 10
            # 3. get the digit that will be our new node, which is the first digit of the sum
            val = sum_result % 10
            new_node = ListNode(val)
            # 4. Attach the new node
            curr.next = new_node


            # Move the pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

