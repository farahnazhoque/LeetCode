from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        remainder_check = {0: -1} 
        summa = 0 

        for i in range(len(nums)):
            summa += nums[i]
            remainder = summa % k

            if remainder in remainder_check:
                if i - remainder_check[remainder] > 1:  # Ensure subarray size ≥ 2
                    return True
            else:
                remainder_check[remainder] = i  
        return False
