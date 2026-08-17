from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        # Frequency map for characters in t
        dict_t = Counter(t)
        required = len(dict_t)
        
        # Frequency map for characters in the current window
        window_counts = {}
        
        l, r = 0, 0
        formed = 0
        
        # Tuple to store (window_length, left_index, right_index)
        ans = float("inf"), None, None
        
        while r < len(s):
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1
            
            # If the frequency of the current character matches its requirement in t, increment formed
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            
            # Try to shrink the window from the left while it remains valid
            while l <= r and formed == required:
                character = s[l]
                
                # Update our tracking of the minimum window
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                
                # The character at the left pointer is leaving the window
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                
                l += 1
            
            r += 1
            
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]