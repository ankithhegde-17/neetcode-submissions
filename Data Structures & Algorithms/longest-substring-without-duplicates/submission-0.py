class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            # If the character is already seen and is within the current window
            if s[right] in char_index_map and char_index_map[s[right]] >= left:
                left = char_index_map[s[right]] + 1
                
            # Update the latest index of the character
            char_index_map[s[right]] = right
            
            # Update the maximum length found so far
            max_len = max(max_len, right - left + 1)
            
        return max_len