# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Understanding
        # both lists are sorted
        # if both lists have the same number, either lists' number can go ahead 

        # Matching
        # Linked list

        # Planning
        """
        1. need to have two pointers
        2. compare the value of two pointers
        3. store the value that will come next
        4. assign the curr value to the lower one
        5. curr.next will be the next one
        6. then make curr to be curr.next
        """

        # Implementing
        
        dummy = node = ListNode

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2 # if one of the lists get empty, we just point at the already sorted part of the non-empty list

        return dummy.next

        # Reviewing: Correct

        # Evaluating
        # Time comp: O(n)
        # Space comp: O(1)
        