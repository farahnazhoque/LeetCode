class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        maxNum = 0
        for i in s:
            if i == "(":
                count += 1
                if maxNum < count:
                    maxNum = count
            if i == ")":
                count -= 1

        return maxNum

