from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracking = {}

        for i, num in enumerate(nums):
            complement = target - num # the value needed to make up the target

            if complement in tracking:
                return [tracking[complement], i]

            tracking[num] = i # adding to the dictionary if not existing

        return []