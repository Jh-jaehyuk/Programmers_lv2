from collections import deque


def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer

    visited = [False] * len(words)
    queue = deque([(begin, 0)])
    a = len(begin)
    b = len(words)
    answer = int(1e9)

    while queue:
        x, y = queue.popleft()

        if x == target:
            answer = min(answer, y)

        for i in range(b):
            count = 0
            for j in range(a):
                if words[i][j] != x[j]:
                    count += 1

            if count == 1 and not visited[i]:
                visited[i] = True
                queue.append((words[i], y + 1))

    return answer


print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))
