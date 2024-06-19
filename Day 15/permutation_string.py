class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Understanding
        # they have to be attached together, cannot be anywhere
        # all lowercase


        # Matching
        # having a list to keep track
        # have a counter


        # Planning
        """
        def checkInclusion(self, s1: str, s2: str) -> bool:
            s1_list = list(s1)
            for i in range(len(s2)):
                if s2[i] in s1:
                    s2_list = list(s2[i:len(s1) + i])
                    if s2_list.sort() == s1_list.sort():
                        return True
            
            return False

        """


        # Implementing
        s1_list = sorted(s1)

        len_s1 = len(s1)

        for i in range(len(s2) - len_s1 + 1):
            if sorted(s2[i:i + len_s1]) == s1_list:
                return True
            
        return False


        # Reviewing: Correct


        #Evaluating
        # Time Complexity: O(n)
        # Space Complexity: O(n)