from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n in range(len(nums)):
            for s in range(n+1, len(nums)):
                if nums[n] + nums[s] == target:
                    return [n, s]
                else:
                    continue