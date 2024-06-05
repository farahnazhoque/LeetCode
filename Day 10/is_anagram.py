class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Understanding:
        # questions to ask: what would happen if the string contained something like 'aa'
        # questions to ask: can the letters be arranged in any manner

        # Matching:
        # if the strings can be arranged in any manner: list

        # Planning: 
        # lenght of the two string have to be the same
        # if the lenght of either string does not match: false
        # if either string is 0 or 1: false
        # sort the list, and then check if they match

        """
        def isAnagram(self, s: str, t: str) -> bool:
            if len(s) != len(t) or len(s) == 0 or len(s) == 1 or len(t) == 0 or len(s) == 0:
                return False
            sort s 
            sort t 
            if s == t:
                return true
            else:
                return false
        """

        if len(s) != len(t) or len(s) == 0 or len(t) == 0:
            return False
        s = sorted(list(s))
        t = sorted(list(t))
        if s != t:
            return False
        else:
            return True

    # Time complexity: O(nlogn)
    #space complexity: O(n)