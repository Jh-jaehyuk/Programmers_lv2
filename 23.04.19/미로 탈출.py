from collections import deque


def solution(maps):
    arr = [list(i) for i in maps]
    m, n = len(arr[0]), len(arr)

    graph = [[0] * m for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs_to_L(x, y):
        visited = [[False] * m for _ in range(n)]
        queue = deque()
        queue.append((x, y))
        visited[x][y] = True

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and arr[nx][ny] != 'X':
                        queue.append((nx, ny))
                        visited[nx][ny] = True
                        graph[nx][ny] = graph[x][y] + 1

                    if arr[nx][ny] == 'L':
                        return nx, ny

        return None, None

    def bfs_to_E(x, y):
        visited = [[False] * m for _ in range(n)]
        queue = deque()
        queue.append((x, y))
        visited[x][y] = True

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and arr[nx][ny] != 'X':
                        queue.append((nx, ny))
                        visited[nx][ny] = True
                        graph[nx][ny] = graph[x][y] + 1

                    if arr[nx][ny] == 'E':
                        return graph[nx][ny]

        return -1

    start_x, start_y = 0, 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'S':
                start_x, start_y = i, j
                break

    lx, ly = bfs_to_L(start_x, start_y)
    if lx is None and ly is None:
        return -1

    answer = bfs_to_E(lx, ly)

    return answer


print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
