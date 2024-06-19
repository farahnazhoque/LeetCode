class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

        
    # Understanding
    # Array will have a seriese of commands, we have to make sure they work


    # Matching
    # Use an array


    # Planning


    # Implementing


    # Reviewing: Corrct


    # Evaluating
    # Time complexity: O(1)
    # Space complexity: O(n)
