from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        _, max_freq = count.most_common(1)[0]
        if max_freq > (len(s) + 1) // 2:
            return ""
        
        res = [""] * len(s)
        idx = 0
        for char, freq in count.most_common():
            for _ in range(freq):
                res[idx] = char
                idx += 2
                if idx >= len(s):
                    idx = 1
                    
        return "".join(res)