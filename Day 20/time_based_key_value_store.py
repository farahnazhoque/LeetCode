class TimeMap:

    def __init__(self):
        self.keyDict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyDict:
            self.keyDict[key] = [] # list of [val, timestamp]
        self.keyDict[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyDict.get(key, [])
        left, right = 0, len(values) - 1

        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] <= timestamp: # if the value is equals to or less than the timestamp value, we return it
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1  # if not, then we keep on looking by changing the mid index

        return res

# Understanding
# each person will have a key and the value will be a number
# the number will be the key  for another dictionary and the value will be the value

# Matching
# ds: dictionary
# finding the binary structure 


# Planning


# Implementing


# Reviewing: Correct
"""
My initial approach was a lot more complex and would not be attained using O(lgn) time complexity
"""


# Evaluating
# Time comp: O(logn)
# Space comp: O(n)