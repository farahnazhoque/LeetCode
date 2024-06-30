# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Understanding
        # we will remove the index going backwards


        # Matching
        # two pointers, one slow, one fast


        # Planning
        """
        counter_slow = 0
        counter_fast = 0
        if not head.next and n == 1:
            head = None
            return head

        slow, fast = head, head
        while fast and fast.next:
            slow.next
            counter_slow += 1
            fast.nex.next
            counter_fast += 2
            if (counter_fast - counter_slow - 1) == n:
                slow.next = slow.next.next

        """


        # Implementing
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize both pointers, starting at the dummy node.
        fast = slow = dummy
        
        # Move the fast pointer n steps ahead to create the gap of n between slow and fast.
        for _ in range(n + 1):
            fast = fast.next
        
        # Move both pointers at the same pace until fast reaches the end of the list.
        while fast:
            slow = slow.next
            fast = fast.next
        
        # Now, slow is at the node before the one to be removed.
        slow.next = slow.next.next  # Remove the nth node from end.
        
        # Return the new head of the list, which might be different if the head was removed.
        return dummy.next
        

        # Reviewing: Correct


        # Evaluating
        # Time Comp: O(n)
        # Space Comp: O(1)