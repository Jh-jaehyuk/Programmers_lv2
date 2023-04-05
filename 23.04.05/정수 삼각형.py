def solution(triangle):
    d = [[0] * i for i in range(1, len(triangle) + 1)]
    d[0][0] = triangle[0][0]
    d[1][0] = d[0][0] + triangle[1][0]
    d[1][1] = d[0][0] + triangle[1][1]

    for i in range(2, len(d)):
        d[i][0] = d[i - 1][0] + triangle[i][0]
        d[i][-1] = d[i - 1][-1] + triangle[i][-1]
        for j in range(1, i):
            d[i][j] = max(d[i - 1][j - 1], d[i - 1][j]) + triangle[i][j]

    return max(d[len(triangle) - 1])
