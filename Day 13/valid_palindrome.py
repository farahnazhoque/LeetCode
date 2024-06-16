class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Understanding
        # Case insensitive
        # no non-alphanumeric characters
        # one letter in the middle shared
        # the list can be empty and if so, it is still a palindrome


        # Matching
        # two pointer


        # Planning
        """
        remove all non-alphanumeric characters
        convert it into a list 
        then iterate from both ends
        slice into half and remove the middle character
    
        def isPalindrome(self, s: str) -> bool:
            s = ''.join(char for char in s if char.isalnum()
            s = list(s.lower())
            s.pop(len(s)//2)
            count = 0

            if (s[0] == s[len(s) - 1]):
                count += 1
                for i in range(1, len(s)-1):
                    if s[i] == s[len(s) - i]:
                        count += 1
                    else:
                        return False
                if count == len(s) //2:
                    return True
                else:
                    return False
                
            else:
                return False
            



        """


        # Implementing
        s = ''.join(char.lower() for char in s if char.isalnum())
        s = list(s)
        
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True
        
        # Reviewing
        """
        My initial approach was kind of confusing and was not 
        utilizing the two pointer method I initially
        concluded. Using while loops help a lot when it
        comes to the two pointer method.
        """

        # Evaluating
        # Time Complexity: O(n)
        # Space Complexity: O(n)