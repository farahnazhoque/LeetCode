class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Pre-allocate arrays with 1s to avoid IndexError
        prefix_arr = [1] * n
        suffix_arr = [1] * n
        res = [1] * n

        # 1. Build Prefix Array
        for i in range(n):
            if i == 0:
                prefix_arr[i] = 1
            else:
                prefix_arr[i] = nums[i-1] * prefix_arr[i-1]

        # 2. Build Suffix Array
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                suffix_arr[i] = 1
            else:
                suffix_arr[i] = nums[i + 1] * suffix_arr[i + 1]

        # 3. Multiply them together
        for i in range(n):
            res[i] = prefix_arr[i] * suffix_arr[i]

        return res