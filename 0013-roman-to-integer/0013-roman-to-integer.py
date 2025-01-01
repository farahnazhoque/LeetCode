class Solution:
    def romanToInt(self, s: str) -> int:
        romToInt = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        total = 0
        n = len(s)

        for i in range(n):
            # if the current character is smaller than the next character like I is for V in IV, subtract I from V
            if i < n-1 and romToInt[s[i]] < romToInt[s[i + 1]]:
                total -= romToInt[s[i]]
            else:
                total += romToInt[s[i]]

        return total
