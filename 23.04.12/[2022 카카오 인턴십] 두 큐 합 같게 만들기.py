from collections import deque


def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    answer = 0
    s1 = sum(q1)
    s2 = sum(q2)

    while True:
        # 종결 조건에 왜 +2 를 해줘야 맞는걸까.
        if not q1 or not q2 or answer > len(queue1) + len(queue2) + 2:
            break

        if s1 == s2:
            return answer

        elif s1 > s2:
            x = q1.popleft()
            s1 -= x
            q2.append(x)
            s2 += x
            answer += 1

        else:
            x = q2.popleft()
            s2 -= x
            q1.append(x)
            s1 += x
            answer += 1

    return -1


print(solution([1, 4], [4, 8]))
