class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)  # Fix edge case
        
        nums = sorted(list(set(nums)))
        
        max_length = 1
        current_length = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                current_length += 1
            else:
                max_length = max(max_length, current_length)
                current_length = 1  # Reset for new sequence
        
        # Don't forget the final sequence!
        max_length = max(max_length, current_length)
        
        return max_length
