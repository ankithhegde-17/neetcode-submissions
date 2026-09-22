class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        timeline = [0] * 1001
        for num, start, end in trips:
            timeline[start] += num
            timeline[end] -= num
            
        current_passengers = 0
        for p in timeline:
            current_passengers += p
            if current_passengers > capacity:
                return False
                
        return True