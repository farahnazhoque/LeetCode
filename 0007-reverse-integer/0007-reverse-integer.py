class Solution:
    def reverse(self, x: int) -> int:
        
        # Understanding
        '''
        if given an integer, we basically reverse it
        if the first char/int is 0, we remove it
        if the integer is negative, we keep it negative
        '''

        # Matching
        '''
        we use for loop
        '''

        # Planning
        '''
        convert int -> str
        go through each string and reverse it, if 0, remove
        if negative sign, keep it at front
        '''

        # Implementing
        is_negative = x < 0
        x_str = str(abs(x))

        # Reverse the string
        reversed_str = x_str[::-1]
        reversed_int = int(reversed_str)

        # Restore the sign
        if is_negative:
            reversed_int = -reversed_int

        # Check for 32-bit integer overflow
        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0

        return reversed_int

        # Reviewing
        