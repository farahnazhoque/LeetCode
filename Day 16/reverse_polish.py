class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Understanding
        # the numbers come before the operation
        # once the operation between two numbers is completed,
        # remove the two numbers, and add the new number

        # Matching
        # using stack

        # Planning
        """
        def evalRPN(self, tokens: List[str]) -> int:
            Stack = []

            for c in tokens:
                if tokens and c == "+":
                    add = Stack.pop() + Stack.pop()
                    Stack.append = add
                elif c == "-":
                    a, b = Stack.pop(), Stack.pop()
                    Stack.append(b-a)
                elif c == "*":
                    mult = Stack.pop() * Stack.pop()
                    Stack.append(mult)
                elif c == "/":
                    a, b = Stack.pop(), Stack.pop() 
                    Stack.append(int(float(b) / a))
                else:
                    Stack.append(c)

            return Stack[0]

        """


        # Implementing
        Stack = []

        for c in tokens:
            if tokens and c == "+":
                add = int(Stack.pop()) + int(Stack.pop())
                Stack.append(add)
            elif c == "-":
                a, b = int(Stack.pop()), int(Stack.pop())
                Stack.append(b-a)
            elif c == "*":
                mult = int(Stack.pop()) * int(Stack.pop())
                Stack.append(mult)
            elif c == "/":
                a, b = int(Stack.pop()), int(Stack.pop())
                Stack.append(int(float(b) / a))
            else:
                Stack.append(c)

        return Stack[0]

        # Reviewing: Ensure to type convert

        # Evaluating: 
        # Time Complexity: O(n)
        # Space Complexity: O(n)