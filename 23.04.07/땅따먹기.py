def solution(land):
    n = len(land)
    d = [[0] * 4 for _ in range(n)]
    d[0] = land[0]

    for i in range(1, n):
        d[i][0] = max(d[i - 1][1], d[i - 1][2], d[i - 1][3]) + land[i][0]
        d[i][1] = max(d[i - 1][0], d[i - 1][2], d[i - 1][3]) + land[i][1]
        d[i][2] = max(d[i - 1][0], d[i - 1][1], d[i - 1][3]) + land[i][2]
        d[i][3] = max(d[i - 1][0], d[i - 1][1], d[i - 1][2]) + land[i][3]

    return max(d[n - 1])


print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))
