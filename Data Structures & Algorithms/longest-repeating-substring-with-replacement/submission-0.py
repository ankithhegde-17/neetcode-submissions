class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_len = 0
        max_freq = 0
        
        for right in range(len(s)):
            # Update frequency of the current character
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])
            
            # If the number of characters to replace exceeds k, shrink the window from the left
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
                
            # Update the maximum length found
            max_len = max(max_len, right - left + 1)
            
        return max_len