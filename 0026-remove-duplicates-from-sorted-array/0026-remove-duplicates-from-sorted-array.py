class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        j = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]: # when the elements are different, swap one of the duplicate elements with this new different element and increment j, where the next swap will take place early on
                nums[j] = nums[i]
                j += 1
        return j
