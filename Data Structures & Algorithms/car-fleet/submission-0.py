class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Pair up position and speed, then sort by position in descending order 
        # (processing cars from closest to the target to farthest)
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        
        for p, s in cars:
            # Calculate time needed to reach the target
            time = (target - p) / s
            
            # If the stack is empty or the current car takes more time than 
            # the car/fleet ahead of it, it cannot catch up and forms a new fleet
            if not stack or time > stack[-1]:
                stack.append(time)
            # Otherwise, it catches up and merges into the fleet ahead (do nothing)
            
        return len(stack)