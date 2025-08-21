import math

class Solution:
    def fractionAddition(self, expression: str) -> str:
        num = 0 # we will add on to this numerator
        den = 1 # we will start and then add on to this denom

        i = 0 # we will start parsing
        n = len(expression)
        
        while i < n:
            curr_num = 0
            curr_den = 0

            is_neg = False

            if expression[i] == '-':
                is_neg = True
                i += 1
            if expression[i] == '+':
                i += 1
            
            while i < n and expression[i].isdigit():
                val = int(expression[i])
                curr_num = (curr_num * 10) + val
                i += 1

            if is_neg:
                curr_num *= -1
            
            i+= 1

            while i < n and expression[i].isdigit():
                val = int(expression[i])
                curr_den = (curr_den * 10) + val
                i+= 1

            num = num * curr_den + curr_num * den
            den = den * curr_den
        
        gcd = abs(math.gcd(num, den))

        num //= gcd
        den //= gcd

        return str(num) + "/" + str(den)

            
