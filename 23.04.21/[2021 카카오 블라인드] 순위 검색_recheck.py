from itertools import combinations
from collections import defaultdict
from bisect import bisect_left


def solution(info, query):
    answer = []
    d = defaultdict(list)

    for i in info:
        i = i.split()
        condition = i[:-1]
        score = int(i[-1])

        for k in range(5):
            case = list(combinations([0, 1, 2, 3], k))
            for c in case:
                tmp = condition.copy()
                for idx in c :
                    tmp[idx] = '-'
                key = ''.join(tmp)
                d[key].append(score)

    for value in d.values():
        value.sort()

    for q in query:
        q = q.replace('and ', '')
        q = q.split()
        target_key = ''.join(q[:-1])
        target_score = int(q[-1])
        count = 0

        if target_key in d:
            target_list = d[target_key]
            idx = bisect_left(target_list, target_score)
            count = len(target_list) - idx
        answer.append(count)

    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210"],
               ["java and backend and junior and pizza 100"]))
