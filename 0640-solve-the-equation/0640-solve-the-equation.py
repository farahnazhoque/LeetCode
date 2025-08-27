class Solution:
    def solveEquation(self, equation: str) -> str:
        '''
        x = 5
        '''
        def parse(expr):
            expr = expr.replace('-', '+-') # make every term explicit with +
            tokens = expr.split('+')

            x_coef = 0
            const = 0

            for token in tokens:
                if not token:
                    continue
                if 'x' in token:
                    if token == "x":
                        x_coef += 1

                    elif token == "-x":
                        x_coef -= 1

                    else:
                        x_coef += int(token.replace('x', ''))

                else:
                    const += int(token)
            return x_coef, const

        left, right = equation.split("=")
        left_x, left_c = parse(left)
        right_x, right_c = parse(right)

        total_x = left_x - right_x
        total_c = right_c - left_c

        if total_x == 0:
            if total_c == 0:
                return "Infinite solutions"
            else:
                return "No solution"

        else:
            x_val = total_c // total_x
            return f"x={x_val}"

                    