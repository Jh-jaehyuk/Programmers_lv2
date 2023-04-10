import math


def solution(n, stations, w):
    answer = 0
    idx = 1

    for i in stations:
        a, b = i - w, i + w

        if a < 1:
            a = 1

        if b > n:
            b = n

        answer += math.ceil((a - idx) / (2 * w + 1))
        idx = b + 1

    if n - idx >= 0:
        answer += math.ceil((n - idx + 1) / (2 * w + 1))

    return answer


print(solution(6, [4], 2))
