from collections import Counter

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = []
        counter = Counter(nums)
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for num in counter:
                if counter[num] > 0:
                    counter[num] -= 1
                    path.append(num)
                    backtrack(path)
                    path.pop()
                    counter[num] += 1
        backtrack([])
        return res