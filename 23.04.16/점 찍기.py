import math


def solution(k, d):
    answer = 0

    def calculation(x):
        return math.sqrt(d * d - x * x)

    i = 0
    while i <= d:
        y = calculation(i)
        answer += math.floor(y / k) + 1
        i += k

    return answer


print(solution(1, 5))
