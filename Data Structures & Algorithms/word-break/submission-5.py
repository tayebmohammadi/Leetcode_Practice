class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        # def dfs(i):
        #     if i == len(s):
        #         return True

        #     for word in wordDict:
        #         if s.startswith(word, i):
        #             if dfs(i + len(word)):
        #                 return True

        #     return False

        # return dfs(0)


        dp = [False] * (len(s) + 1) #
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if len(word) <= len(s[i:]) and word == s[i: i + len(word)]:
                    dp[i] = dp[i + len(word)]
                if dp[i]: 
                    break

        return dp[0]
            



                








        # memory = {}
        # def dfs(s):
        #     if not s:
        #         return True

        #     if s in memory:
        #         return memory[s]

        #     for i in range(1,len(s) + 1): 
        #         if s[:i] in wordDict:
        #             if dfs(s[i:]):
        #                 memory[s] = True
        #                 return True

        #     memory[s] = False
        #     return False

        # return dfs(s)


        