from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def helper(left, right):
            if left == right:
                return left  # single element is a peak
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                # peak is on the left including mid
                return helper(left, mid)
            else:
                # peak is on the right excluding mid
                return helper(mid + 1, right)

        return helper(0, len(nums) - 1)
