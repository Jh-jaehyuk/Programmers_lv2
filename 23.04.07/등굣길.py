def solution(m, n, puddles):
    graph = [[0] * m for _ in range(n)]

    if puddles:
        for i in puddles:
            x, y = i
            graph[y - 1][x - 1] = 1

    d = [[0] * m for _ in range(n)]
    for i in range(n):
        if graph[i][0] != 1:
            d[i][0] = 1
        else:
            break

    for j in range(m):
        if graph[0][j] != 1:
            d[0][j] = 1
        else:
            break

    for i in range(1, n):
        for j in range(1, m):
            if graph[i][j] != 1:
                d[i][j] = (d[i - 1][j] % 1000000007) + (d[i][j - 1] % 1000000007)

    return d[n - 1][m - 1] % 1000000007


print(solution(4, 3, [[1, 3], [3, 1]]))
