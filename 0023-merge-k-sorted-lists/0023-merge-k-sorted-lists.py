# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        new_arr = []

        # Collect values from all linked lists
        for l in lists:
            curr = l
            while curr:
                new_arr.append(curr.val)
                curr = curr.next

        # If no values, return None
        if not new_arr:
            return None

        # Sort the collected values
        new_arr.sort()

        # Build new linked list from sorted values
        head = ListNode(new_arr[0])
        curr = head
        for n in new_arr[1:]:
            curr.next = ListNode(n)
            curr = curr.next

        return head
