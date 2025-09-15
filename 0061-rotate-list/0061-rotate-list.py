# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Handle edge cases
        if not head or not head.next or k == 0:
            return head
        
        # Find length and tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # Adjust k if it's larger than length
        k = k % length
        if k == 0:
            return head
        
        # Set both pointers to start at head
        slow = fast = head
        
        # Move fast k nodes ahead
        for _ in range(k):
            fast = fast.next
        
        # Move both pointers until fast reaches the end
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # Perform the rotation
        new_head = slow.next  # This will be our new head
        slow.next = None      # Cut the list here
        tail.next = head      # Connect the end to the ORIGINAL head
        
        return new_head