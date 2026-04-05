class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False

        d1 = {}
        for c in s1:
            d1[c] = d1.get(c, 0) + 1

        d2 = {}
        i = j = 0
        
        while j < n:  

            d2[s2[j]] = d2.get(s2[j], 0) + 1
            j += 1

            if j - i > m:
                d2[s2[i]] -= 1
                if d2[s2[i]] == 0:
                    del d2[s2[i]]
                i += 1
            
            if j - i == m and d1 == d2:
                return True

        return False
