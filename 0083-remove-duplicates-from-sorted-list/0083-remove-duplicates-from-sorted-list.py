class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                # Skip the duplicate
                curr.next = curr.next.next
            else:
                # Only move forward if there's no duplicate
                curr = curr.next

        return head
