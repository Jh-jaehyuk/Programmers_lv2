# 미끄러져 이동하는 것을 구현하는 것이 핵심
# 벽이 나오거나 장애물을 만날 때까지 이동방향을 고정해야됨
from collections import deque


def solution(board):
    board = [list(i) for i in board]
    m, n = len(board), len(board[0])
    visited = [[-1] * n for _ in range(m)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    start_x, start_y = 0, 0

    for i in range(m):
        for j in range(n):
            if board[i][j] == 'R':
                start_x, start_y = i, j

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        visited[x][y] = 1

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                while 0 <= nx < m and 0 <= ny < n and board[nx][ny] != 'D':
                    nx += dx[i]
                    ny += dy[i]

                if nx < 0 or nx >= m or ny < 0 or ny >= n or board[nx][ny] == 'D':
                    nx -= dx[i]
                    ny -= dy[i]

                if visited[nx][ny] == -1:
                    if board[nx][ny] == 'G':
                        return visited[x][y]

                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

        return -1

    answer = bfs(start_x, start_y)
    return answer


print(solution([".D.R", "....", ".G..", "...D"]))
