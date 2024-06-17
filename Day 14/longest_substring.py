class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Understanding
        # if there are repetitions of the same character, answer will be 1
        # questions to ask: will it stop at "y" if the string looked like this "zxyz"


        # Matching
        # a hash set


        # Planning
        """
        def lengthOfLongestSubstring(self, s: str) -> int:
            hash_set = set()
            res = 0

            for i in range(len(s)):
                if s[i] in hash_set:
                    return res
                else:
                    hash_set.add(s[i])
                    res += 1
            return res

        """


        # Implementing
        hash_set = set()
        res = 0
        old = 0

        for i in range(len(s)):
            while s[i] in hash_set:
                hash_set.remove(s[old])
                old += 1
            hash_set.add(s[i])
            res = max(res, i - old + 1)
        return res


        # Reviewing: Correct


        # Evaluating
        # Time complexity: O(n)
        # Space complexity: O(n)


    
        