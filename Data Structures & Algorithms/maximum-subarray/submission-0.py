class Solution:
    def maxSubArray(self, nums):
        cur = ans = nums[0]

        for x in nums[1:]:
            cur = max(x, cur + x)
            ans = max(ans, cur)

        return ans