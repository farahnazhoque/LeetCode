from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Understanding
        # return as many lists as possible
        # has to to be 3 numbers
        # might not have a solution
        # same numbers can be used for different lists
        # indices of three numbers within the same list has to be different
        # no duplicate triplets 

        # Matching
        # 

        # Planning
        """
        def threeSum(self, nums: List[int]) -> List[List[int]]:
            1. first we create an empty list to store the result
            2. we sort the existing list so when we use the 
            two pointers, it is easy for us to shift our 
            pointers according to how small or large the value
            is compared to 0
            3. then we create a for loop for the
            first index and its value
            4. we then make sure that if the first number's
            index is greater than 0, it is not a duplicate
            of its previous number in the sequence to
            avoid duplicate lists
            5. then we initialize a left pointer which starts with i + 1
            and a right pointer which is at the end of the list
            6. we also ensure that left pointer's index is always
            less than the right pointer's (this is similar
            to the two sum problem)
            7. we check that if the addition of the three numbers is 
            less than 0, we shift the left pointer more to the right
            to increase the added value (taking advantage of the sorting)
            8. if it is too much, we shift the right pointer to the left
            to reduce the added value
            9. if it is equal to 0, we added the 3 numbers to the result list 
            and increase the left index and decrease the right index, and make
            a check to ensure that the left index is not a duplicate of the previous
            10. by the end we return the resulting list
        """

        # Implementing
        result = []
        nums.sort()

        for i, value in enumerate(nums):
            if value > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                three = value + nums[left] + nums[right]
                if three > 0:
                    right -= 1
                elif three < 0:
                    left += 1
                else:
                    result.append([value, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return result

        # Reviewing: Correct

        # Evaluating
        # Time complexity: O(n^2)
        # Space complexity: O(n)