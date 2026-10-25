class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ""

        def palindrome(i, j):

            while i >= 0 and j < len(s):
                if s[i] == s[j]:
                    i -= 1
                    j += 1
                else:
                    break
            return s[i+1:j]
            
        for i in range(len(s)):
            s1 = palindrome(i, i)
            s2 = palindrome(i, i + 1)
            curr = s1 if len(s1) >= len(s2) else s2
            if len(curr) > len(res):
                res = curr

        return res









































        # res = ""
        # resLen = 0

        # for i in range(len(s)):

        #     l , r = i , i 
        #     # for odd palindrome
        #     while l >= 0 and r < len(s) and s[l] == s[r]:

        #         if (r - l + 1) > resLen:
        #             res = s[l:r + 1]
        #             resLen = r - l + 1 
        #         r += 1
        #         l -= 1

        #     l , r = i , i + 1
        #     # for even palindrome
        #     while l >= 0 and r < len(s) and s[l] == s[r]:

        #         if (r - l + 1) > resLen:
        #             res = s[l:r + 1]
        #             resLen = r - l + 1 
        #         r += 1
        #         l -= 1


        # return res

            


        