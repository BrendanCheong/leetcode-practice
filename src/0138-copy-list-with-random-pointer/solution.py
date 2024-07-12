"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        So the first thought here is to just create a copy node of the head then
        start attaching the .next and .random nodes. However the .random nodes may
        not have been created yet, like a .random node might be pointing to the end node
        which we don't have yet.

        Solution:
        1. 1st pass is to create all the nodes
        2. 2nd pass is to do the attachment of .next and .random nodes

        We can use a hashmap to store the copy nodes
        Time: O(n)
        Space: O(n)
        """
        hashmap = { None: None }
        curr = head
        while curr:
            copy = Node(curr.val)
            # so each pointer -> copy node
            # then we can go through the nodes again and change each copy node
            hashmap[curr] = copy 
            curr = curr.next

        curr = head
        while curr:
            copy = hashmap[curr]
            # we can extract out the copy node and then change it
            copy.next = hashmap[curr.next]
            copy.random = hashmap[curr.random]
            curr = curr.next
        
        # the hashmap is pointer -> copy
        copy_head = hashmap[head]
        return copy_head
