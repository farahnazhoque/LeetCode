# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        0 -> 1 -> 2 -> 0 -> 4 -> 5 -> 3 -> 0
        see 0, start adding
        see another 0, append it in a list (whic will later be turned into a listnode)
        """

        dummy = ListNode(0) # new list starter
        tail = dummy # pointing at new list
        curr = head.next # skipping 0
        running_sum = 0

        while curr:
            if curr.val != 0:
                running_sum += curr.val

            else:
                tail.next = ListNode(running_sum)
                tail = tail.next
                running_sum = 0

            curr = curr.next

        return dummy.next



            