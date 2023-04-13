# 마을의 개수 N(노드 개수)가 최대 50개!
# 플로이드 워셜 알고리즘 이용
# 시간복잡도가 O(N ** 3), 노드가 최대 500개 이하일 경우에 사용


def solution(N, road, K):
    INF = int(1e9)
    graph = [[INF] * (N + 1) for _ in range(N + 1)]

    for a in range(N + 1):
        graph[a][a] = 0

    for b in road:
        graph[b[0]][b[1]] = min(graph[b[0]][b[1]], b[2])
        graph[b[1]][b[0]] = min(graph[b[1]][b[0]], b[2])

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                graph[j][k] = min(graph[j][i] + graph[k][i], graph[j][k])

    answer = 0

    for x in graph[1]:
        if x <= K:
            answer += 1

    return answer


print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))
