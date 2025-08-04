class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        tracking = {}

        for num in nums:
            if num in tracking:
                tracking[num] += 1
            else:
                tracking[num] = 1
        
        max_element = 0
        max_count = 0
        for key, count in tracking.items():
            if count > max_count:
                max_count = count
                max_element = key

        return max_element
