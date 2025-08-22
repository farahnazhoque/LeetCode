class Solution:
    def fractionToDecimal(self, num: int, den: int) -> str:
        mapdict = {}
        a = ""

        if num == 0:
            return "0"

        if (num < 0) ^ (den < 0):
            a += "-"

        num, den = abs(num), abs(den)

        q = num // den
        a += str(q)
        r = num % den

        if r == 0:
            return a
        else:
            a += "."
            while r != 0:
                if r in mapdict:
                    indext = mapdict[r]
                    # fix: strings don't have insert, rebuild instead
                    a = a[:indext] + "(" + a[indext:] + ")"
                    break
                else:
                    mapdict[r] = len(a)   # position where this remainder first occurred
                    r *= 10
                    q = r // den
                    r = r % den
                    a += str(q)

            return a
