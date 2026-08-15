from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        # Buckets index represents frequency (0 to len(nums))
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in count.items():
            buckets[freq].append(num)
            
        res = []
        # Iterate backwards from highest possible frequency
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res