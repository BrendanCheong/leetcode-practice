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
        # if not list1 or not list2:
        #     return list1 or list2
        # elif list1.val <= list2.val:
        #     list1.next = self.mergeTwoLists(list1.next, list2)
        #     return list1
        # elif list2.val <= list1.val:
        #     list2.next = self.mergeTwoLists(list1, list2.next)
        #     return list2
        def iterative(list1: Optional[ListNode], list2: Optional[ListNode]):
            prehead = ListNode(-1)
            prev = prehead
            
            while list1 and list2:
                if list1.val <= list2.val:
                    prev.next = list1
                    list1 = list1.next
                elif list2.val <= list1.val:
                    prev.next = list2
                    list2 = list2.next
                prev = prev.next
                
            prev.next = list1 if list1 is not None else list2
            
            return prehead.next
        return iterative(list1, list2)
                    
            
        
        
        
        
        
        
        
