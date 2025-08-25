class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1 # starting from the right
        while i > 0 and nums[i-1] >= nums[i]: # keep going till you find the drop [1, (2), 7, 4, 3, 1] 
            i -= 1

        if i == 0: # if no drop is found, means that nums is in descending order
            nums.reverse()
            return

        j = len(nums) - 1 # finding the smallest number that is bigger than the pivot because we have to find the next smallest number which is greater than the current
        while j >= i and nums[j] <= nums[i-1]: # [1, 2, 7, 4, (3), 1]
            j-=1 

        nums[i-1], nums[j] = nums[j], nums[i-1] # swapping those two [1, (3), 7, 4, 2, 1]
        nums[i:] = reversed(nums[i:]) # as the trailing numbers are still in descending order, we have to make them ascending to make it the next smallest number [1, 3, 1, 2, 4, 7]