from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0 # tracking the furthest index that can be reached
        finalIndex = len(nums) - 1

        for i in range(len(nums)):
            if i > maxReach:
                return False
            maxReach = max(maxReach, nums[i] + i)
            if maxReach >= finalIndex:
                return True
        return False