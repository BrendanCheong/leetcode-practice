# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_linked_list(self, head, k):
        previous, current, next_node = None, head, None
        for _ in range(k):
            # temporarily store the next node
            next_node = current.next
            # reverse the current node
            current.next = previous
            # before we move to the next node, point previous to the
            # current node
            previous = current
            # move to the next node 
            current = next_node
        return previous, current

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # edge case, k = 1 means no change
        if k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        ptr = dummy
    
        while(ptr != None):
            tracker = ptr

            for i in range(k):
                if tracker == None:
                    break
                tracker = tracker.next

            if tracker == None:
                break
        
            previous, current = self.reverse_linked_list(ptr.next, k)
            last_node_of_reversed_group = ptr.next
            last_node_of_reversed_group.next = current
            ptr.next = previous
            ptr = last_node_of_reversed_group

        return dummy.next
        
