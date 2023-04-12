from collections import deque


def solution(order):
    answer = 0
    arr = deque([i for i in range(1, len(order) + 1)])
    tmp = []

    while arr or tmp:
        if arr and arr[0] == order[answer]:
            arr.popleft()
            answer += 1

        else:
            if tmp and tmp[-1] == order[answer]:
                tmp.pop()
                answer += 1

            else:
                if not arr:
                    break
                else:
                    tmp.append(arr.popleft())

    return answer


print(solution([4, 3, 1, 2, 5]))
