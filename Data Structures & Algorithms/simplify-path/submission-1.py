class Solution:
    def simplifyPath(self, path: str) -> str:
        s = []
        for p in path.split('/'):
            if p == '..':
                if s:
                    s.pop()
            elif p and p != '.':
                s.append(p)
        return '/' + '/'.join(s)