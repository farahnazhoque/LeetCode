from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Understanding
        # return the index of the target
        # solution has to be O(logn)


        # Matching
        # Binary tree


        # Planning
        # split and find
        """
        mid = nums[len(nums)//2]
        if mid > target:
            search(nums[:mid], target)
        elif mid < target:
            search(nums[mid+1:], target)
        elif mid == target:
            return mid
        else:
            return -1
        """


        # Implementing
        def binary_search(left, right):
            if left > right:
                return -1
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binary_search(left, mid - 1)
            else:
                return binary_search(mid + 1, right)
        
        return binary_search(0, len(nums) - 1)

        # Reviewing
        # The previous solution I had, went into infinite recursion as
        # there was no base case 


        # Evaluating
        # Time Complexity: O(logn)
        # Space Complexity: O(1)