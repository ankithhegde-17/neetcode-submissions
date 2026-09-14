class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = n
        for i, val in enumerate(nums):
            res ^= i ^ val
        return res