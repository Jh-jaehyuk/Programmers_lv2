import math
def solution(n,a,b):
    answer = 0
    # a, b = min(a, b), max(a, b)
    while a != b:
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        answer += 1

    return answer

print(solution(8,4,5))
