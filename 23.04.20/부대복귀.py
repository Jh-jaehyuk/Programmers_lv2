# source에서 destination으로 가는 bfs 를 구하지 말고
# destination에서의 bfs 한번만 이용할 것.
# bfs를 여러번 돌리면 시간 초과 발생!
from collections import deque


def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n + 1)]

    for road in roads:
        a, b = road
        graph[a].append(b)
        graph[b].append(a)

    def bfs(node):
        queue = deque()
        queue.append(node)
        visited[node] += 1

        while queue:
            v = queue.popleft()

            for i in graph[v]:
                if visited[i] == -1:
                    visited[i] = visited[v] + 1
                    queue.append(i)

    visited = [-1] * (n + 1)
    bfs(destination)

    for source in sources:
        answer.append(visited[source])

    return answer


print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1,3,5], 5))
