# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         def index(node: Optional[ListNode]):
#             if not node:
#                 return 0
#             i = index(node.next) + 1
#             if i > n:
#                 # now we recreate the entire LL starting from the head, while we skip the correct node
#                 node.next.val = node.val 
#             return i # this is the node infront of the one we must remove
#         index(head) # start mutation of the LL
#         return head.next # we skip the correct node by one place
        """
        2 pointer solution
        we will have one pointer on the head, and one on the head
        move the pointer on the head by n, then stop
        then, move the other head pointer by len - n, which is found by moving the first pointer until it reaches None
        """
        dummy, right = ListNode(0, head), head
        left = dummy

        # 1. progress the right pointer until it reaches then end, we want len - n
        while n > 0:
            right = right.next
            n -= 1

        #2. next, progress the left pointer and the right. When the right is null, it means we reached len - n length
        while right:
            right = right.next
            left = left.next

        #3. now that the left pointer is on the correct node, we can delete that node
        left.next = left.next.next

        return dummy.next
        
        
