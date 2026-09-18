class Solution:
    def splitArray(self, nums, k):
        def canSplit(mid):
            count, current = 1, 0
            for n in nums:
                if current + n > mid:
                    count += 1
                    current = 0
                current += n
            return count <= k

        low, high = max(nums), sum(nums)
        while low < high:
            mid = (low + high) // 2
            if canSplit(mid):
                high = mid
            else:
                low = mid + 1
        return low
