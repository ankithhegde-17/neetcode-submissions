from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        
        for s in strs:
            # Create a 26-element character frequency tuple (a-z)
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            # Tuples are immutable and usable as hashmap keys
            groups[tuple(count)].append(s)
            
        return list(groups.values())