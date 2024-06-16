from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Understanding
        # the numbers are not necessarily in order
        # there can be empty lists
        # there can be consecutive numbers but as different sets

        # Matching
        # using a sorted array


        # Planning
        """
        def longestConsecutive(self, nums: List[int]) -> int:
            nums = sort(nums)
            count = 0

            for i in range(1, len(nums)):
                if (nums[i] - 1) == nums[i]):
                    count += 1
            
            return count

        """

        # Implementing
        if len(nums) == 0:
            return 0
        nums = set(nums)
        max_count = 0
        count = 1
        for num in nums:
            if num in nums and num-1 not in nums:
                while num + 1 in nums:
                    count += 1
                    num += 1
                max_count = max(max_count, count)
                count = 1
        # Reviewing: Worked


        # Evaluating
        # Time complexity: O(n)
        # Space complexity: O(n)