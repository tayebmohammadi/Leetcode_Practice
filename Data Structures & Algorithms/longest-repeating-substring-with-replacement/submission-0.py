class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        i = j = 0
        W_size = 0
        freq = 0
        d = {}
        longest = 0
        for j in range(len(s)):
            char_right = s[j]
            w_size = j - i + 1
            d[char_right] = d.get(char_right, 0) + 1
            freq = max(freq, d[char_right]) 

            if w_size - freq <= k:
                longest = max(longest, w_size)
            else:
                d[s[i]] -= 1
                i += 1
        
        return longest
                


            






        