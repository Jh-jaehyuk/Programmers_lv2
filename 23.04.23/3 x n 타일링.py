def solution(n):
    d = [0] * (n + 1)
    if n > 1:
        d[2] = 3

    for i in range(4, n + 1):
        if i % 2 == 0:
            d[i] += 3 * (d[i - 2] % 1000000007)
            for j in range(i - 4, -1, -2):
                d[i] += 2 * d[j] % 1000000007
            d[i] += 2
            d[i] %= 1000000007

    return d[n]


print(solution(4))
