class Solution:
    def solveNQueens(self, n):
        res = []
        cols, diag1, diag2 = set(), set(), set()
        board = [['.'] * n for _ in range(n)]

        def dfs(r):
            if r == n:
                res.append([''.join(row) for row in board])
                return

            for c in range(n):
                if c in cols or r - c in diag1 or r + c in diag2:
                    continue

                cols.add(c)
                diag1.add(r - c)
                diag2.add(r + c)
                board[r][c] = 'Q'

                dfs(r + 1)

                cols.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)
                board[r][c] = '.'

        dfs(0)
        return res