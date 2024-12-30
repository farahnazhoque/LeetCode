from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # `j` points to the position of the next unique element
        j = 1  # Start at index 1 since the first element is always unique
        
        for i in range(1, len(nums)):  # `i` iterates through the array
            if nums[i] != nums[j - 1]:  # Compare with the last unique element
                nums[j] = nums[i]  # Swap the unique element to `j`
                j += 1  # Move the swap pointer
            
        return j
