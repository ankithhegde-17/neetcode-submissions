class Solution:

  def findTargetSumWays(self, nums: list[int], target: int) -> int:
    total_sum = sum(nums)
    if (total_sum + target) % 2 != 0 or total_sum < abs(target):
      return 0

    s = (total_sum + target) // 2
    dp = [0] * (s + 1)
    dp[0] = 1

    for num in nums:
      for i in range(s, num - 1, -1):
        dp[i] += dp[i - num]

    return dp[s]