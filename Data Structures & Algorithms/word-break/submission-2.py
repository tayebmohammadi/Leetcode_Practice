class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memory = {}
        def dfs(s):
            if not s:
                return True

            if s in memory:
                return memory[s]

            for i in range(1,len(s) + 1): 
                if s[:i] in wordDict:
                    if dfs(s[i:]):
                        memory[s] = True
                        return True

            memory[s] = False
            return False

        return dfs(s)


        