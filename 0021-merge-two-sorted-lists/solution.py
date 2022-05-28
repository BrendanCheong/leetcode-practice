# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: ListNode = None) -> None:
        self.val: int = val
        self.next: ListNode = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merging 2 sorted arrays uses the 2 pointer technique
        Have a pointer at the start of each list. If one pointer is less than the other,
        choose the less than one and increment that pointer, while the bigger pointer remains the same
        if equal, choose one or the other
        if one of the nodes are empty, choose the non-emty one, if both empty choose either
        """
        if not list1 or not list2:
            # edge case, where one is empty, we return the non-empty one
            # if both empty, return either one of the empty nodes
            return list1 or list2
        elif list1.val < list2.val:
            # if the first pointer is smaller, we advance that pointer
            # which is why list1 moves forward
            # while the other pointer remains
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            # if equal pointer we just choose one or the other, doesn't matter
            # if second pointer is smaller, we advance the second pointer
            # while the other pointer remains
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        # we return the list2/list1 to output the nodes
        
        
        
        
        
        
