from collections import deque


def solution(board):
    n = len(board)
    INF = int(1e9)
    answer = INF
    d = [[INF] * n for _ in range(n)]

    directions = [(-1, 0, 0), (0, 1, 1), (1, 0, 2), (0, -1, 3)]

    queue = deque([(0, 0, 0, -1)])

    while queue:
        i, j, cost, direction = queue.popleft()

        if (i, j) == (n - 1, n - 1) and answer > cost:
            answer = cost

        for dir in directions:
            next_i = i + dir[0]
            next_j = j + dir[1]
            if direction == dir[2] or direction == -1:
                next_cost = 100
            else:
                next_cost = 600

            if not (0 <= next_i < n and 0 <= next_j < n) or board[next_i][next_j] == 1:
                continue

            if d[next_i][next_j] < cost + next_cost - 400:
                continue

            d[next_i][next_j] = cost + next_cost
            queue.append((next_i, next_j, cost + next_cost, dir[2]))

    return answer


print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
