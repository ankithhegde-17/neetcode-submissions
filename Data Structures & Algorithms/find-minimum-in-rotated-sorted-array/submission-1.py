from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # If the middle element is greater than the rightmost element,
            # the minimum element must be in the right half.
            if nums[mid] > nums[right]:
                left = mid + 1
            # Otherwise, the minimum element is in the left half (including mid).
            else:
                right = mid
                
        # When left == right, we have found the minimum element
        return nums[left]