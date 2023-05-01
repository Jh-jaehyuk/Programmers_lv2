import sys
sys.setrecursionlimit(10 ** 8)


def solution(n, m, x, y, r, c, k):
    answer = 'z'
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    move = ['d', 'l', 'r', 'u']

    def dfs(x, y, r, c, prev_s, count, k):
        nonlocal answer

        if k < count + abs(x - r) + abs(y - c):
            return

        if x == r and y == c and count == k:
            answer = prev_s
            return

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 1 <= nx <= n and 1 <= ny <= m and prev_s < answer:
                dfs(nx, ny, r, c, prev_s + move[i], count + 1, k)

    d = abs(x - r) + abs(y - c)

    if d > k or (k - d) % 2 == 1:
        return 'impossible'

    dfs(x, y, r, c, '', 0, k)

    return answer


print(solution(3,3,1,2,3,3,4))
