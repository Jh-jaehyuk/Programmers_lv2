import heapq


def solution(n, path, gates, summits):
    graph = {i: [] for i in range(1, n + 1)}

    for a, b, cost in path:
        graph[a].append((b, cost))
        graph[b].append((a, cost))

    INF = int(1e10)
    visited = [INF] * (n + 1)
    heap = []

    for gate in gates:
        visited[gate] = 0
        heap.append((0, gate))

    answer = []

    while heap:
        dist, node = heapq.heappop(heap)
        if visited[node] < dist:
            continue

        if node in summits:
            answer.append([visited[node], node])
            continue

        for next_node, next_cost in graph[node]:
            max_cost = max(visited[node], next_cost)
            if max_cost < visited[next_node]:
                visited[next_node] = max_cost
                heapq.heappush(heap, (visited[next_node], next_node))

    answer.sort(key=lambda x: (x[0], x[1]))

    return [answer[0][1], answer[0][0]]


print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1,3], [5]))
print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2,3,4]))
print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3,7], [1,5]))
print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1,2], [5]))
