class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Understanding
        # a sorted int array is given, we have to return the target
        # int's index if found

        # Matching
        # Binary Search as sorted

        # Planning
        '''
        we have to split the list, check the mid value.
        if the mid value is smaller than the target value, 
        we assign the beginning of the new array to 
        '''

        # Implementing
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
                
        return l

        # Reviewing
        