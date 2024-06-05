"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Type: LinkedList
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0) # creating a head with value 0
        tail = dummyHead # tail is pointing to head
        carry = 0 # for digit carry
        
        while l1 is not None and l2 is not None:
            # retrieving the first digit, or head values.
            digit1 = l1.val if l1 is not None else 0 
            digit2 = l2.val if l2 is not None else 0
            
            # once the digits have been retrieved, we can add them together alongside any carry we had.
            total = digit1 + digit2 + carry
            
            # we will now retrieve the carry and the value of the digit for the next value.
            carry = total // 10
            digit = total % 10
            
            # we will now create a new node with the digit value and add it to the tail.
            newNode = ListNode(digit)
            tail.next = newNode # tail is pointing to the new node
            tail = tail.next # tail is now the new node
            
            # we will now move to the next node in the linked list.
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        
        if carry > 0: # if carry is greater than 0, we will create a new node with the carry value and add it to the tail.
            tail.next = ListNode(carry)
        
        return dummyHead.next # returning the head of the linked list. 