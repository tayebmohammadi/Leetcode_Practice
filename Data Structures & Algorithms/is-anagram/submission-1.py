class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # to make a dict and count the characters in one string
        if len(s) != len(t):
            return False
        d = {}

        for c in s:
            d[c] = d.get(c, 0) + 1

        for c in t:
            d[c] = d.get(c,0) - 1
            if d[c] == -1:
                return False
        return True
        
            
            

        

        