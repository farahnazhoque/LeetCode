class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        res = []
        current_sum = 0

        while l < r:
            current_sum = numbers[l] + numbers[r]

            if current_sum == target:
                res.append(l+1)
                res.append(r+1)

                return res
            elif current_sum < target:
                l += 1
            elif current_sum > target:
                r -= 1

                