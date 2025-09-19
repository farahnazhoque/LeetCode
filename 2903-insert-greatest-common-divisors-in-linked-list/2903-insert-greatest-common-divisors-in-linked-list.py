from math import gcd

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head   # ✅ not self.head

        itr = head

        while itr and itr.next:   # ✅ need itr.next too, otherwise AttributeError
            new_node_val = gcd(itr.val, itr.next.val)  # ✅ use self.gcd
            new_node = ListNode(new_node_val, itr.next)
            itr.next = new_node
            itr = itr.next.next

        return head   # ✅ return full list, not itr
