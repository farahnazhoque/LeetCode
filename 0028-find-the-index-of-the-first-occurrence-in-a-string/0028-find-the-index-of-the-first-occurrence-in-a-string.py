class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:  # Handle the case where needle is empty
            return 0
        
        i = 0  # Initialize i
        indexStart = -1
        j = 0
        
        while i < len(haystack):
            # Match characters and check if needle is fully matched
            if j < len(needle) and haystack[i] == needle[j]:
                if indexStart == -1:  # Set starting index on the first match
                    indexStart = i
                j += 1
                i += 1
                
                if j == len(needle):  # If needle is fully matched
                    return indexStart
            else:
                # Reset matching state if characters do not match
                if indexStart != -1:  # Only reset i if a match started
                    i = indexStart + 1
                else:
                    i += 1
                indexStart = -1
                j = 0
        
        return -1
