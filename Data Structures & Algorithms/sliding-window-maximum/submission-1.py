from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        d = deque()
        output = []
        
        for i, n in enumerate(nums):
            # Remove indices that are out of the current sliding window
            if d and d[0] < i - k + 1:
                d.popleft()
            
            # Remove smaller elements from the back of the deque as they are useless
            while d and nums[d[-1]] < n:
                d.pop()
            
            # Add the current element's index to the deque
            d.append(i)
            
            # Once the window reaches size k, record the maximum (at the front of the deque)
            if i >= k - 1:
                output.append(nums[d[0]])
                
        return output