class Solution:
    def encode(self, strs: list[str]) -> str:
        # Prefix each string with its length and a delimiter ('#')
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        
        while i < len(s):
            # Find the position of the delimiter starting from i
            j = s.find('#', i)
            length = int(s[i:j])
            
            # Extract the string using the length
            start = j + 1
            end = start + length
            res.append(s[start:end])
            
            # Move index past the extracted string
            i = end
            
        return res