# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Understanding
        # if the next index is not -1 or at any point the next index is less than the current index, it means there is a cycle


        # Matching
        # two pointers

        # Planning


        # Implementing
        if not head.next:
            return False



        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


        # Reviewing


        # Evaluating
        # Time complexity: O(n)
        # Space complexity: O(1)