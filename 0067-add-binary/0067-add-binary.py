class Solution:
    def addBinary(self, a: str, b: str) -> str:

        # Understanding
        '''
        two binary strings are provided, we have to find their sum.
        1 + 1 = 0, carry: 1
        1 + 0 = 1
        0 + 0 = 0

        we have to read from right to left
        '''

        # Matching

        # Planning
        '''
        carry
        curr1
        curr2
        str
        
        '''

        # Implementing
        carry = 0
        curr1 = len(a) - 1
        curr2 = len(b) - 1
        res = []
        
        while curr1 >= 0 or curr2 >= 0 or carry == 1:
            if curr1 >= 0:
                carry += int(a[curr1])
                curr1 -= 1
            if curr2 >= 0:
                carry += int(b[curr2])
                curr2 -= 1

            res.append(str(carry % 2))
            carry = carry // 2

        return "".join(res[::-1])

        # Reviewing
        