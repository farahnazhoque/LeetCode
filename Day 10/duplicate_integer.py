class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         # questions to ask: is there any time constraint?
         # questions to ask: do the numbers have to appear in consecutive manner
         # questions to ask: is there a chance that the nums list will be empty
         # questions to ask: what if there is only one number

        """
         def hashDuplicate(self, nums: List[int]) -> bool:
            hashMap = {}
            for each number in array:
                if number in hashMap keys:
                    return true
                else:
                    enter number in hashMap with a value of 1
        """

        if len(nums) == 1 or len(nums) == 0:
            return False

        hashMap = {}
        for i in range(len(nums)):
            if nums[i] in hashMap.keys():
                return True
            else:
                hashMap[nums[i]] = 1
        
        return False