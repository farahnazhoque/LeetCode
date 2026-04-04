class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def freq_bld(word):
            alpha_freq = [0] * 26
            for c in word:
                idx = ord(c) - ord("a")
                alpha_freq[idx] += 1

            str_bld = ""
            for i in range(len(alpha_freq)):
                alpha = chr(97 + i)
                str_bld += alpha + str(alpha_freq[i])
            return str_bld

        dict_str = {}

        for s in strs:
            str_bld = freq_bld(s)
            if str_bld in dict_str:
                dict_str[str_bld].append(s)
            else:
                dict_str[str_bld] = [s]

        return list(dict_str.values())
