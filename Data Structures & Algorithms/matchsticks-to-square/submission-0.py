class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        
        side = total // 4
        matchsticks.sort(reverse=True)
        
        if matchsticks[0] > side:
            return False
            
        sides = [0] * 4
        
        def dfs(idx):
            if idx == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3] == side
            
            for i in range(4):
                if sides[i] + matchsticks[idx] <= side:
                    sides[i] += matchsticks[idx]
                    if dfs(idx + 1):
                        return True
                    sides[i] -= matchsticks[idx]
                if sides[i] == 0:
                    break
            return False

        return dfs(0)