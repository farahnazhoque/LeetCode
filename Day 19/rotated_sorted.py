class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Understanding
        # we have to find the minimum value in this rotated but sorted array
        # we use the typical mid breaking of the array
        # if the mid happens to be bigger than the left most value, the mid is part of the rotated and sorted left portion, so we will explore the right
        # if the mid happens to be smaller tha the left, we put the result to be mid, and explore the left, if there is no number bigger than the current mid, we return the current mid


        # Matching
        # Binary search


        # Planning


        # Implementing
        start, end = 0, len(nums) - 1
        curr_min = float("inf")

        while start < end:
            mid = (start + end) // 2
            curr_min = min(curr_min, nums[mid])

            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid -1 

        return min(curr_min, nums[start])


        # Reviewing: Correct 
    
        # Evaluating:
        # Time Complexity: O(logn)
        # Space Complexity: O(1)