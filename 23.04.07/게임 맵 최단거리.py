from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[-1] * m for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                    if visited[nx][ny] == -1:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))

        return visited[n - 1][m - 1]

    answer = bfs(0, 0)
    return answer if answer == -1 else answer + 2


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
