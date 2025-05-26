class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sD = {}
        tD = {}

        for i in range(len(s)):
            sD[s[i]] = sD.get(s[i], 0) + 1
            tD[t[i]] = tD.get(t[i], 0) + 1

        return sD == tD