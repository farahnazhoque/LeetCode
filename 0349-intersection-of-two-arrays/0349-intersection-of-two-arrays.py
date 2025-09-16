class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        if len(nums1) < len(nums2) or len(nums1) == len(nums2):
            i = 0
            while i < len(nums2):
                if nums2[i] in nums1:
                    result.append(nums2[i])
                    i+= 1
                else:
                    i+= 1
            return list(set(result))

        else:
            i = 0
            while i < len(nums1):
                if nums1[i] in nums2:
                    result.append(nums1[i])
                    i+= 1
                else:
                    i+= 1
            return list(set(result))