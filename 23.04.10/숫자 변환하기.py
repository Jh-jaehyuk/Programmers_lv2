from collections import deque


def solution(x, y, n):
    d = [0] * 1000001

    if y % x != 0 and x + n > y:
        return -1

    def bfs():
        queue = deque()
        queue.append(x)

        while queue:
            v = queue.popleft()
            if v == y:
                return d[v]

            for i in [v + n, v * 2, v * 3]:
                if 0 <= i <= 1000000 and not d[i]:
                    queue.append(i)
                    d[i] = d[v] + 1

        return -1

    answer = bfs()

    return answer


print(solution(2, 5, 4))
