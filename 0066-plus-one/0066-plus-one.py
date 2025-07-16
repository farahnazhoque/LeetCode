class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # Understanding
        # given an array of integers which is all the character within
        # a big integer, like one-hundre (100) is represented in the array
        # as [1, 0, 0], we have to return an array of what the characters
        # of +1 of the integer would have. so, in this case, [1, 0, 1].

        # Matching
        # Array + Math

        # Planning
        '''
        turn the array into a str, then into an int, plus one, then turn into str
        and then back to arr
        '''

        # Implementing
        digits_str = ''
        for n in digits:
            digits_str += str(n)

        digits_int = int(digits_str) + 1
        
        digits_str = str(digits_int)
        
        final = []
        for s in digits_str:
            final.append(int(s))

        return final

        # Reviewing