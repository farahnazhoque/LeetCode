from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Understand
        # questions to ask: will the array be sorted
        # questions to ask: what if the array is empty

        # Match:
        # Datastructure: array and hash map

        # Planning:
        """
        def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            # we will be using a bucket sort method

            hash_map = {} # it is to count the number of times a digit appears in the array
            frequency_array = [[] for i in in range(len(nums) + 1)] # we are creating an array of size as the nums

            for n in nums:
                hash_map[n] = 1 + hash_map.get(n, 0) # we will add 1 to an existing value of the key, n, and if not, the default will be 0

            for n, c in hash_map.items():
                frequency_array[c].append(n) 
                it will look like so
                nums = [1, 2, 2]
                [0, 1, 2, 3]
                [[], [1], [2], []] # each of these (n) correspond to an index (c) 

            res = []
            for i in range(len(freq) - 1, 0, -1): # we are coundting in reverse
                for n in frequency_array[i]:
                    res.append(n)
                    if len(res) == k:
                        return res

            
            
                
        """

        # Implement

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

    # Review: Passed

    # Evaluate:
    # Time complexity: O(n)
    # Space Complexity: O(n)