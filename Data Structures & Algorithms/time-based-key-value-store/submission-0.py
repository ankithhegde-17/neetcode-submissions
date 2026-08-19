from collections import defaultdict

class TimeMap:

    def __init__(self):
        # Dictionary to map each key to a list of (timestamp, value) pairs
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Since timestamps for any given key are strictly increasing, 
        # appending keeps the list sorted automatically.
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        values = self.store[key]
        left = 0
        right = len(values) - 1
        res = ""
        
        # Binary search to find the largest timestamp <= target timestamp
        while left <= right:
            mid = left + (right - left) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]  # Found a valid candidate, store it
                left = mid + 1        # Look for a larger valid timestamp on the right
            else:
                right = mid - 1       # Timestamp is too large, look on the left
                
        return res