def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col - 1], -x[0]))

    s1 = [(data[row_begin - 1][j] % row_begin) for j in range(len(data[row_begin - 1]))]
    s1 = sum(s1)
    answer = s1

    if row_begin == row_end:
        return s1 ^ s1

    for i in range(row_begin, row_end):
        s2 = 0
        for j in data[i]:
            s2 += (j % (i + 1))

        answer ^= s2

    return answer


print(solution([[2, 2, 6], [1, 5, 10], [4, 2, 9], [3, 8, 3]], 2, 2, 3))
