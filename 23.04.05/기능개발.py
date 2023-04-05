from collections import deque


def solution(progresses, speeds):
    queue1 = deque(progresses)
    queue2 = deque(speeds)
    count = 0
    answer = []
    x = 0

    while queue1:
        if queue1[0] >= 100:
            x = queue1.popleft()
            y = queue2.popleft()
            count += 1

        else:
            if x != 0:
                answer.append(count)
                count = 0
                x = 0

            for i in range(len(queue1)):
                queue1[i] += queue2[i]

    answer.append(count)
    return answer


print(solution([93, 30, 55], [1, 30, 5]))
