import heapq
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Directly get the two largest numbers
        two_largest = heapq.nlargest(2, nums)
        
        # Calculate the product
        return (two_largest[0] - 1) * (two_largest[1] - 1)