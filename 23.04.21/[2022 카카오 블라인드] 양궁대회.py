from itertools import combinations_with_replacement as combi


def solution(n, info):
    answer = [-1]
    max_val = -1

    for c in combi(range(11), n):
        lion_info = [0] * 11

        for i in c:
            lion_info[10 - i] += 1

        apeach, lion = 0, 0

        for idx in range(11):
            if info[idx] == lion_info[idx] == 0:
                continue
            elif info[idx] >= lion_info[idx]:
                apeach += 10 - idx
            else:
                lion += 10 - idx

        if lion > apeach:
            val = lion - apeach

            if max_val < val:
                max_val = val
                answer = lion_info

    return answer


print(solution(2, [0,1,1,0,0,0,0,0,0,0,0]))
