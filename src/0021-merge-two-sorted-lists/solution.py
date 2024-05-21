# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        # After the loop, if there are remaining nodes in either list1 or list2,
        # we append them to the end of the merged list.
        node.next = list1 or list2

        # Return the head of the merged list
        return dummy.next

    def mergeListRecursive(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if not list1 or not list2:
            # return the list which still has remaining nodes
            return list1 if list1 else list2
        
        # merging if condition
        if list1.val < list2.val:
            # Move the list1 pointer until its no longer small
            list1.next = self.mergeListRecursive(list1.next, list2)
            return list1
        else:
            # Move the list2 pointer until its no longer small
            list2.next = self.mergeListRecursive(list1, list2.next)
            return list2

