class Solution:
    def subsets(self, nums):
        res = [[]]
        
        for x in nums:
            res += [s + [x] for s in res]
        
        return res