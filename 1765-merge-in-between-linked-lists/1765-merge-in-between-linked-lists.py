# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        '''
        10 -> 1 -> 13 - 6 -> 9 - 5
                    |               |
        '''
        first_ptr = list1

        for _ in range(a-1):
            first_ptr = first_ptr.next

        second_ptr = first_ptr.next
        for _ in range(b - a + 1):
            second_ptr = second_ptr.next

        first_ptr.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = second_ptr

        return list1
