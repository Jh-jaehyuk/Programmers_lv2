from itertools import permutations


def solution(k, dungeons):
    arr = list(permutations(dungeons, len(dungeons)))
    max_count = 0
    for i in arr:
        a = int(k)
        count = 0
        for j in range(len(i)):
            if a >= i[j][0]:
                a -= i[j][1]
                count += 1
            max_count = max(max_count, count)

    return max_count
