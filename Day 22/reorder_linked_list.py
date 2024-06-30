# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Understanding
        # if you only have one character, you just returnit
        # besides the head, every other value will be replaced
        #


        # Matching
        # Linked list
        # we will have two pointers: one slow and one fast


        # Planning
        """
        1. we will have two pointers: slow and fast
        2. slow pointer will be iterating as usual
        3. fast pointer will be iterating by two nodes
        4. when the fast pointer will have come to an end, the slow pointer's next will be the second half
        5. then for the second half, we have to reverse the pointer
        6. then you alternate each pointer
        """


        # Implementing
        if not head or not head.next:
            return
        
        # split the list into two halves
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # reverse the second half
        prev, curr = None, slow.next
        slow.next = None # break the link
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        # merge the two halves
        first, second = head, prev
        while second: # since the second half is always shorter
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

        # Reviewing: Correct


        # Evaluating
        # Time comp: O(n)
        # Space comp: O(1)
        