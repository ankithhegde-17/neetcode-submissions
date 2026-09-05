class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        res = [[]]

        for i, x in enumerate(nums):
            start = 0 if i == 0 or x != nums[i - 1] else prev
            prev = len(res)
            for j in range(start, prev):
                res.append(res[j] + [x])

        return res