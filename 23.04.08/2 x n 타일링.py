def solution(n):
    d = [0] * 60001
    d[1] = 1
    d[2] = 2

    for i in range(3, n + 1):
        d[i] = (d[i - 1] % 1000000007 + d[i - 2] % 1000000007) % 1000000007

    return d[n]


print(solution(4))
