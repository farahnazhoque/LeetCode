class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Understanding:
        # i and j are indices, not the number themselves
        # i and j cannot be equal
        # i and j are indices within the same list
        # questions to ask: what if the target is 0
        # questions to ask: what is the time complexity constraint

        # Matching:
        # Two for loops within one another

        # Planning:
        """
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            list for output = []
            for i in nums:
                for j in nums:
                    if i + j equals to target:
                        return [i, j]
                    else:
                        continue
        """

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                else:
                    continue
        
    # Time complexity: O(n^2)
    # Space complexity: O(1)