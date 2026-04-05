class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq_bucket = [[] for i in range(len(nums) + 1)]

        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1

        for num, cnt in count.items():
            freq_bucket[cnt].append(num)

        res = []
        for i in range(len(freq_bucket)-1, 0, -1):
            for num in freq_bucket[i]:
                res.append(num)
            if len(res) == k:
                return res

        