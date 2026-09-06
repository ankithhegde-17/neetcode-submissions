from collections import deque

class Solution:
    def solve(self, board):
        m, n = len(board), len(board[0])
        q = deque()

        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and board[i][j] == 'O':
                    board[i][j] = '#'
                    q.append((i, j))

        while q:
            x, y = q.popleft()

            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O':
                    board[nx][ny] = '#'
                    q.append((nx, ny))

        for i in range(m):
            for j in range(n):
                board[i][j] = 'X' if board[i][j] == 'O' else 'O' if board[i][j] == '#' else 'X'