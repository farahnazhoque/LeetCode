class Solution:

    # Understanding:
    # questions to ask: will there be any and all characters? Yes.

    # Matching:
    # strings 
    
    # Planning:
    """
    # we will be using a count to keep track of each word in the array
    # to make it unique we will add a pound key before each word

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += len(word) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        for i in range(len(s)):
            if type(s(i)) == int and s(i+1) == "#":
                word = ""
                for j in range(i+2, i + 1 + int(s(i))):
                    word += s[j]
                res.append(word)
    
    Thhis is a wrong implementation as it is not taking into account the fact that the length of the word can be more than one digit

    """

    # Implement

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])# length of the word
            word = s[j + 1: length + j + 1] # starting of word is after the index of the pound key and the ending index is starting from the end of the pound key till the length of the word
            res.append(word)
            i = length + j + 1 # starting index of the next word
            
        return res

    # Review: Passed

    # Evaluation:
    # Time complexity: O(n)
    # Space complexity: O(1)