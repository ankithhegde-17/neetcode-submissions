from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right
        
        while left <= right:
            k = left + (right - left) // 2
            
            # Calculate total hours needed at speed k
            # (pile + k - 1) // k is equivalent to math.ceil(pile / k)
            total_hours = sum((pile + k - 1) // k for pile in piles)
            
            if total_hours <= h:
                res = k
                right = k - 1  # Try a slower speed
            else:
                left = k + 1   # Need a faster speed
                
        return res