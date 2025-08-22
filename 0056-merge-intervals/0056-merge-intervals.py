class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        1. will the lists be sorted by the start?
        '''
        intervals.sort()
        merged = []
        prev = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= prev[1]:
                prev[1] = max(prev[1], intervals[i][1])
            else:
                merged.append(prev)
                prev = intervals[i]

        merged.append(prev) # adding the last prev (either remainder)
        return merged
