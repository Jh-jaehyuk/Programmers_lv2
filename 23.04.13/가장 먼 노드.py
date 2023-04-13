from collections import deque


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for i in edge:
        a, b = i
        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (n + 1)
    visited[1] = 1

    queue = deque([1])

    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = visited[x] + 1
                queue.append(i)

    return visited.count(max(visited))


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
