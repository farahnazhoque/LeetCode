import math
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Understanding
        # questions to ask: 
        
        # Matching
        # Hash map: dictionary of lists
        # Array
        
        # Planning
        """
        def productExceptSelf(self, nums: List[int]) -> List[int]:
            res = []

            for i in range(len(nums)):
                value = nums.pop(i)
                res.append(math.prod(nums))
                nums.insert(i, value)
            return res


        """


        # Implementing
        res = []

        for i in range(len(nums)):
            value = nums.pop(i)
            res.append(math.prod(nums))
            nums.insert(i, value)
        return res

        # Reviewing: Worked


        # Evaluation
        # Time complexity: O(n)
        # Space complexity: O(n)