class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        i = j = 0
        longest = l = 0

        while j < len(s):
            if s[j] not in seen:
                seen.add(s[j])
                longest = max(j - i + 1, longest)
                j += 1
            else:
                seen.remove(s[i])
                i += 1

        return longest
                

        