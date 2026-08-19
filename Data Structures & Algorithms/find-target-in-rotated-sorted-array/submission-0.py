from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # If target is found, return its index
            if nums[mid] == target:
                return mid
            
            # Check if the left half is sorted
            if nums[left] <= nums[mid]:
                # Check if target lies within the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Search left
                else:
                    left = mid + 1   # Search right
            # Otherwise, the right half must be sorted
            else:
                # Check if target lies within the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Search right
                else:
                    right = mid - 1  # Search left
                    
        # Target is not present in the array
        return -1