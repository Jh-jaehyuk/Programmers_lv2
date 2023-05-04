def solution(matrix_sizes):
    n = len(matrix_sizes)
    d = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(1, n):
        for j in range(n - i):
            arr = []
            for k in range(j, i + j):
                x = d[j][k] + d[k + 1][i + j] + (matrix_sizes[j][0] * matrix_sizes[k][1] * matrix_sizes[i + j][1])
                arr.append(x)
            d[j][i + j] = min(arr)

    return d[0][-1]


print(solution([[5,3],[3,10],[10,6]]))
