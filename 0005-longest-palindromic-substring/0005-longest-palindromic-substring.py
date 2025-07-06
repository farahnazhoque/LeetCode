class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_from_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]  # last valid palindrome

        longest = ''
        for i in range(len(s)):
            # Odd-length palindrome
            odd = expand_from_center(i, i)
            # Even-length palindrome
            even = expand_from_center(i, i + 1)
            # Choose the longer one
            curr_longest = odd if len(odd) > len(even) else even
            if len(curr_longest) > len(longest):
                longest = curr_longest

        return longest
