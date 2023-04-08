from collections import deque


def solution(A, B):
    arr1 = sorted(A, reverse=True)
    arr2 = sorted(B, reverse=True)

    queue1 = deque(arr1)
    queue2 = deque(arr2)
    point = 0
    while queue1:
        x = queue1.popleft()
        y = queue2.popleft()

        while x >= y:
            if not queue1:
                return point
            x = queue1.popleft()

        point += 1

    return point


print(solution([2, 2, 2, 2], [1, 1, 1, 1]))
