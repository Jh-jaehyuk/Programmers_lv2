from collections import deque


def solution(prices):
    count = 0
    answer = []

    queue = deque(prices)

    while queue:
        v = queue.popleft()

        if not queue:
            answer.append(0)
            break

        for i in queue:
            if i >= v:
                count += 1
            else:
                count += 1
                break

        answer.append(count)
        count = 0

    return answer


print(solution([1, 2, 3, 2, 3]))
