from collections import Counter


def solution(a):
    answer = -1
    c = Counter(a)

    for key in c.keys():
        if c[key] <= answer:
            continue

        count = 0
        idx = 0

        while idx < len(a) - 1:
            if (a[idx] != key and a[idx + 1] != key) or (a[idx] == a[idx + 1]):
                idx += 1
                continue

            count += 1
            idx += 2

        if answer < count:
            answer = count

    return 0 if answer == -1 else answer * 2


print(solution([0]), solution([5, 2, 3, 3, 5, 3]), solution([0, 3, 3, 0, 7, 2, 0, 2, 2, 0]))
