def solution(n, money):
    d = [1] + [0] * n # d[0] = 1 이라고 생각하는 것이 핵심.

    for i in money:
        for j in range(1, n + 1):
            if j >= i:
                d[j] += d[j - i]

    return d[n]


print(solution(5, [1, 2, 5]))
