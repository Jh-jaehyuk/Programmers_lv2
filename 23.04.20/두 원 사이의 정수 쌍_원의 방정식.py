import math


def solution(r1, r2):
    answer = 0

    for i in range(1, r2 + 1):
        max_val = math.floor(((r2 * r2) - (i * i)) ** 0.5)
        if i > r1:
            min_val = 0
        else:
            min_val = math.ceil(((r1 * r1) - (i * i)) ** 0.5)
        answer += max_val - min_val + 1

    return answer * 4


print(solution(10, 20))
