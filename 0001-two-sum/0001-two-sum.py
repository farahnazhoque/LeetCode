from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffd = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diffd:
                return [diffd[diff], i]
            else:
                diffd[nums[i]] = i
    