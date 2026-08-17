class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = 0
        # Append a 0 at the end to ensure all remaining bars in the stack are processed
        heights = heights + [0]
        
        for i, h in enumerate(heights):
            # While the stack is not empty and the current height is less than 
            # the height at the index stored at the top of the stack
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                # Calculate the width: 
                # If stack is empty, it means the popped bar is the shortest from index 0 up to i-1.
                # Otherwise, the width is the distance between the current index `i` and the new stack top index minus 1.
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
                
            stack.append(i)
            
        return max_area