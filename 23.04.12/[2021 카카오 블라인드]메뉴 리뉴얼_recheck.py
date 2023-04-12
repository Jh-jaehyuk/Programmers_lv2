from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for i in course:
        tmp = []

        for order in orders:
            tmp += combinations(sorted(order), i)
        d = Counter(tmp)

        if len(d) and max(d.values()) != 1:
            answer += [''.join(k) for k in d if d[k] == max(d.values())]

    return sorted(answer)


print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
