class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]: # left sorted
                if nums[l] <= target and target <= nums[mid]:
                    r = mid-1
                else:
                    l = mid + 1
            else: # right sorted
                if nums[mid] <= target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1

                
        