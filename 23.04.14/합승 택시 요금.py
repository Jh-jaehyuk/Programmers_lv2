# 노드의 개수가 200개로 500개보다 작으므로 플로이드 워셜 알고리즘 이용
def solution(n, s, a, b, fares):
    answer = int(1e9)
    INF = int(1e9)
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        graph[i][i] = 0

    for i in fares:
        x, y, z = i
        graph[x][y] = z
        graph[y][x] = z

    for k in range(1, n + 1):
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

    for i in range(1, n + 1):
        if graph[s][i] != INF:
            answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])

    return answer


print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
