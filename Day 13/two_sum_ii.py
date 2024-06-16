from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Understanding
        # questions to ask: what if the list is empty

        # Matching
        # use a for loop 

        # Planning
        """
        def twoSum(self, numbers: List[int], target: int) -> List[int]:
            for i in range(len(numbers)):
                for j in range(i+1, len(numbers)):
                    if numbers[i] + numbers[j] == target:
                        return [i, j]
           
        """

        # Implementing
        for i in range(len(numbers)):
                for j in range(i+1, len(numbers)):
                    if numbers[i] + numbers[j] == target:
                        return [i+1, j+1]

        # Review
        """
        My initial approach was correct but as I did not
        observe the example better, I was unable to grasp
        that I was to return the regular index not the 
        usual compsci index that starts at 0.
        """

        # Evaluating
        # time complexity: O(n^2)
        # space complexity: O(1)
