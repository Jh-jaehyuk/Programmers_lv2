def solution(sequence, k):
    n = len(sequence)
    tmp = []
    end = 0
    s = 0

    for i in range(n):
        while s < k and end < n:
            s += sequence[end]
            end += 1

        if s == k:
            tmp.append([i, end - 1, end - 1 - i])

        s -= sequence[i]

    tmp.sort(key=lambda x: (x[2], x[1]))

    return [tmp[0][0], tmp[0][1]]


print(solution([1, 2, 3, 4, 5], 7))
