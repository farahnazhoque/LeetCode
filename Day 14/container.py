from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Understanding
        # questions to ask: what if there is one or no amount in the array
        # values can be the same
        # they actually have to create a container between two bars
        # height x distance between two bars

        # Matching
        # two pointers


        # Planning
        # 

        # Implementing
        left, right = 0, len(heights) - 1
        res = 0

        while left < right:
            res = max(res, min(heights[left], heights[right]) * (right - left))
            if heights[left] < heights[right]:
                left += 1
            elif heights[right] <= heights[left]:
                right -= 1
        return res
            


        # Reviewing: Correct


        # Evaluating
        # Time complexity: O(n)
        # Space complexity: O(1)