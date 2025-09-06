class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1

        while l < r:  # note: strictly less
            mid = (l + r) // 2

            if arr[mid] < arr[mid + 1]:
                l = mid + 1
            else:
                r = mid

        return l  # or r, since l == r at the peak
