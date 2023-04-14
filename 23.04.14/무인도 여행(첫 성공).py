from collections import deque


def solution(maps):
    answer = []
    arr = []
    for i in maps:
        arr.append(list(i))
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] != 'X':
                count += 1
                break

    if count == 0:
        return [-1]

    visited = [[False] * len(arr[0]) for _ in range(len(arr))]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        tmp = []
        queue = deque()
        queue.append((x, y))
        tmp.append(arr[x][y])
        visited[x][y] = True
        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                    if arr[nx][ny] != 'X' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        tmp.append(arr[nx][ny])
        return tmp

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if maps[i][j] != 'X' and not visited[i][j]:
                tmp = [int(k) for k in bfs(i, j)]
                answer.append(sum(tmp))

    return sorted(answer)


print(solution(['XXX', 'XXX', 'XXX']))
