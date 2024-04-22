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
        if not head: # if head is None or the linked list is empty
            return None
        old_new = {} # creating a hash map to keep track of node, the next node and the random node

        curr = head # pointing to the head
        while curr:
            old_new[curr] = Node(curr.val) # creating a deep copy
            curr = curr.next
        
        curr = head
        while curr:
            old_new[curr].next = old_new.get(curr.next) # we do not use curr.next because it will link the cloned node's next to the orignal list's node so we find the corresponding node in the hash map (clone)
            old_new[curr].random = old_new.get(curr.random)
            curr = curr.next
        return old_new[head]
        