# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Understanding
        # revresed a linked list using its head


        # Matching
        # Linked List


        # Planning
        """
        prev, curr = none, head

        while curr:
            temp = curr.next # we will temporary store the real next value 
            curr.next = prev # we will then change the next pointer to reverse and point to prev
            prev = curr # we will shift prev to the left now
            curr = temp # we will shift the curr to to the next pointer now

        return prev



        """


        # Implementing


        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


        # Reviewing: Correct


        # Evaluating: 
        # Time complexity: O(n)
        # Space complexity: O(1)