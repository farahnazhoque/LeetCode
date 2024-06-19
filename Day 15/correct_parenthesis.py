class Solution:
    def isValid(self, s: str) -> bool:
        # Understanding
        # There has to be an equal number of opening and closing
        # Always even


        # Matching
        # Stacks


        # Planning
        """
        def isValid(self, s: str) -> bool:
            1. keep a map to track of the correct pairs
            2. create a stack array to store the openings and also to match the order
            3. loop through the string
            4. to check if it is closing or opening, we check if the character is in the map
            5. if is a closing, we make sure that the top of the stack containts the opening, and pop it
            6. if it is a opening, we add it to the stack
        """


        # Implementing
        Map = {")": "(", "]" : "[", "}" : "{"}
        stack = []

        for c in s:
            if c in Map:  # Check if the character is a closing parenthesis
                # If the stack is empty or the top element does not match
                if not stack or stack[-1] != Map[c]:
                    return False  # Invalid sequence
                stack.pop()  # Pop the matching opening parenthesis
            else:
                stack.append(c)  # Push the opening parenthesis to the stack
        
        # The stack should be empty if all opening have corresponding closing
        return not stack


        # Reviewing: Correct


        # Evaluating:
        # Time Complexity: O(n)
        # Space Complexity: O(n)