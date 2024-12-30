from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] == val:
                if nums[r] != val:
                    # Swap the element at l with the one at r
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
                else:
                    # Decrement r if nums[r] is also val
                    r -= 1
            else:
                # Increment l if nums[l] is not val
                l += 1

        return l  # `l` now represents the count of non-val elements
