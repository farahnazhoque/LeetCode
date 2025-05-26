class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ###
        if len(s) != len(t):
            return False

        sL = list(s)
        tL = list(t)

        return sorted(sL) == sorted(tL)
        
