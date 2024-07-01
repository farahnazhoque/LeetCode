
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

from typing import Optional


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Understanding


        # Matching


        # Planning
        # have a dictionary 
        # iterate once to create copy noces
        # iterate the second time to connect everything including the random


        # Implementing
        oldToNew = {None: None}

        curr = head
        while curr:
            copy = Node(curr.val)
            oldToNew[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = oldToNew[curr]
            copy.next = oldToNew[curr.next]
            copy.random = oldToNew[curr.random]
            curr = curr.next

        return oldToNew[head]
        

        # Reviewing: Correct


        # Evaluating
        # Time complexity: O(n)
        # Space complexity: O(n)
        