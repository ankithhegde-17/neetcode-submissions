class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        target = total // k
        nums.sort(reverse=True)
        if nums[0] > target:
            return False
            
        memo = {}
        
        def dfs(mask, current_sum):
            if mask == (1 << len(nums)) - 1:
                return True
            if (mask, current_sum) in memo:
                return memo[(mask, current_sum)]
            
            for i in range(len(nums)):
                if not (mask & (1 << i)):
                    if current_sum + nums[i] <= target:
                        if dfs(mask | (1 << i), (current_sum + nums[i]) % target):
                            memo[(mask, current_sum)] = True
                            return True
                    elif current_sum == 0:
                        break
            
            memo[(mask, current_sum)] = False
            return False

        return dfs(0, 0)