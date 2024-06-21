from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Understanding
        # An integer is given, and we hve to make
        # as many forms of correct parenthesis
        # only add open if open < n
        # only add closed if closed < open
        # return once open == closed == n


        # Matching
        # Stacks and array


        # Planning
        """
        1. We will use recursion
        2. create a temporary stack where we will be creating the various combos
        3. create a result array where we will be appending the various combos
        4. create a backtracking function that takes in the parameters: number of open parens, number of closed parens
        5. for the first if statement, if the number of open is equals to the number of closed and that is equals to the number of target, we join all the characters in the stack as a string, and add it to the result array
        6. if, however, if the number of open parens are less than the target number, we can add it to the stack, call the backtrack function with the new updated params, and then once the recursion is done, clean it using pop function
        7. if, however, if the number of closed parens are less than the open parens, we can ad a closed paren in the stack, recursively call the backtrack with the new updated params, then clean it up
        8. outside of the function, we call the backtrack function with 0, 0 params 
        9. outside of the function, we return the resul aray
        """


        # Implementing
        stack = []
        result = []

        def backTrack(openN, closedN):
            if openN == closedN == n:
                result.append(''.join(stack))
                return
            if openN < n:
                stack.append("(")
                backTrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backTrack(openN, closedN+1)
                stack.pop()

        backTrack(0, 0)
        return result

        # Reviewing: Correct


        # Evaluating
        # Time complexity: O(4^n / sqrt(n))
        # Space complexity: O(4^n / sqrt(n))