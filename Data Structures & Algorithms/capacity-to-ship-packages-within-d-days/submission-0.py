class Solution:
    def shipWithinDays(self, weights, days):
        def canShip(capacity):
            day_count = 1
            current_load = 0
            for w in weights:
                if current_load + w > capacity:
                    day_count += 1
                    current_load = 0
                current_load += w
            return day_count <= days

        low, high = max(weights), sum(weights)
        while low < high:
            mid = (low + high) // 2
            if canShip(mid):
                high = mid
            else:
                low = mid + 1
        return low
