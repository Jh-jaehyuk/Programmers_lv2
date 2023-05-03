import sys
sys.setrecursionlimit(10 ** 6)


def solution(a, edges):
    answer = 0
    graph = [[] for _ in range(len(a))]
    visited = [False] * len(a)

    if sum(a) != 0:
        return -1

    for edge in edges:
        x, y = edge
        graph[x].append(y)
        graph[y].append(x)

    def dfs(v):
        nonlocal answer, a
        weight = a[v]
        visited[v] = True

        for i in graph[v]:
            if not visited[i]:
                weight += dfs(i)
        answer += abs(weight)

        return weight

    dfs(0)

    return answer


print(solution([-5,0,2,1,2], [[0,1], [3,4], [2,3], [0,3]]))
print(solution([0,1,0], [[0,1], [1,2]]))
print(solution([-2, 8, -5, -5, -3, 0, 5, 2], [[0, 1], [0, 2], [1, 3], [1, 4], [1, 5], [2, 6], [2, 7]]))
