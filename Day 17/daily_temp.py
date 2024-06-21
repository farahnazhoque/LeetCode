from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Understanding
        # the index of the temprature in the output will hold the the number of days before a higher temparature is seen
        # if there are equal or no higher temparature, the value will be 0


        # Matching
        # for loop and while loop


        # Planning
        """
        res = []
        for i in range(len(tempratures)):
            count = 0
            j = i + 1
            while j < len(tempratures):
                if tempratures[j] > tempratures[i]:
                    res.append(count)
                else:
                    count += 1
                    j += 1
        return res

        Corrected:
        n = len(temperatures)
        res = [0] * n
        stack = []
        
        for i in range(n):
            while stack and temparatures[i] > temperatures[stack(-1)]:
                updating_index = stack.pop()
                res[updating_index] = i - updating_index
            stack.append(i)
            
        return res
        """


        # Implementing
        n = len(temperatures)
        # Result array initialized to zero
        res = [0] * n
        # Stack to keep track of the indices of the temperatures
        stack = []
        
        # Iterate over each day
        for i in range(n):
            # While stack is not empty and the current temperature is greater than the temperature at the index on top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # Pop the index from the stack
                index = stack.pop()
                # Calculate the number of days until a warmer temperature and update the result
                res[index] = i - index
            # Push the current index onto the stack
            stack.append(i)
        
        return res

        # Reviewing: Correct
        # My initial approach was wrong due to the fact I was not correctly handling the count and the 0s


        # Evaluating
        # Time Complexity: O(n)
        # Space Complexity: O(n)