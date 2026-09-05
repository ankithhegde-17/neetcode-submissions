class Solution:
    def exist(self, board, word):
        m, n = len(board), len(board[0])

        def dfs(i, j, k):
            if k == len(word):
                return True
            if i < 0 or j < 0 or i == m or j == n or board[i][j] != word[k]:
                return False

            c = board[i][j]
            board[i][j] = '#'

            found = any(dfs(i + x, j + y, k + 1) for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)))

            board[i][j] = c
            return found

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False