class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        word_set = set(wordDict)
        memo = {}
        
        def dfs(sub):
            if sub in memo:
                return memo[sub]
            if not sub:
                return [""]
            
            res = []
            for i in range(1, len(sub) + 1):
                prefix = sub[:i]
                if prefix in word_set:
                    for suffix in dfs(sub[i:]):
                        res.append(prefix + ((" " + suffix) if suffix else ""))
            
            memo[sub] = res
            return res

        return dfs(s)