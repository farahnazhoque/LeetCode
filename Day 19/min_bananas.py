import math
from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Understanding
        # the number of hours always will be larger than the number of piles or else we will not be able to finish
        # k is the rate at which the bananas are being eaten per hour
        # each pile can be eaten after the next hour
        # we have to find the minimum rate to eat the bananas in all the piles within the given hour


        # Matching
        # binary search


        # Planning
        """
        def minEatingSpeed(self, piles: List[int], h: int) -> int:
            l, r = 1, max(piles) # setting up the pointers for the raters
            res = r

            while l < r:
                k = (l + r) // 2

                totalTime = 0
                for p in piles:
                    totalTime += math.ceil(float(p) / k) # we are trying to get the total hours it takes to complete a single pile of bananas
                if totalTime <=h: # if the total time is less than or equal to the allocated hour, we can try and keep on finding the minimum, but just in case there are none, we set the res to k
                    res = k
                    r = k - 1
                else: # if the totalTime is more than the allocated hour, we shift the left pointer to the right, hence increasing the value of k
                    l = k + 1
            return res

        """


        # Implementing
        left, right = 1, max(piles)
        res = right

        while left <= right:
            k = (left + right) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                right = k - 1
            else:
                left = k + 1
        return res



        # Reviewing: Correct


        # Evaluating: 
        # Time Complexity: O(nlogn)
        # Space Complexity: O(1)
