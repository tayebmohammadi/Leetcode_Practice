class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        dp = {}

        def dfs(i, l, r):
            if i == len(s3) and l == len(s1) and r == len(s2):
                return True
                
            if i == len(s3):
                return False
            
            if (i, l, r) in dp:
                return dp[(i, l , r)]
            
            match_1 = (l < len(s1) and s1[l] == s3[i])
            match_2 = (r < len(s2) and s2[r] == s3[i])


            if match_1 and match_2:
                dp[(i, l , r)] = dfs(i + 1, l + 1, r)  or dfs(i + 1, l, r + 1)
            elif match_1:
                dp[(i, l , r)] = dfs(i + 1, l + 1, r)
            elif match_2:
                dp[(i, l , r)] = dfs(i + 1, l, r + 1)
            else:
                dp[(i, l , r)] = False

            return dp[(i, l , r)]
        return dfs(0, 0, 0)


            



        