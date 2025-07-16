class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Understanding
        # palindtrome checking for integers
        # can have symbols, have to match those as well

        # Matching
        # Two pointers
        # mainly because we have to check outwards to inwards

        # Planning
        '''
        we turn x into a string, so it will be easier to trace.
        once turned into a string, we place the two pointers at
        two ends of the string.

        upon each iteration, we check if the two pointers have the
        same character. if not, return false immediately, if yes,
        continue to do so till the last.

        we also have to check if the length of the string is even or
        odd. based on that, we have to iterate
        '''

        # Implementing
        x_str = str(x)
        l = 0
        r = len(x_str) - 1

        while l < r:
            if x_str[l] != x_str[r]:
                return False
            l += 1
            r -= 1

        return True
        # Reviewing
        '''
        I primarily confused myself by thinking that we need to
        check for both even and odd lengths of input. However,
        due to the nature of the 'l < r', it is able to stop
        when the length is odd at the middle character.
        '''