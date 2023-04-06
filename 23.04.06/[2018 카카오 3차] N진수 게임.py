def solution(n, t, m, p):
    num = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
    answer = '0'

    for i in range(1, t * m):
        tmp = ''
        while i > 0:
            tmp = num[i % n] + tmp
            i //= n
        answer += tmp
    return answer[(p - 1):(t * m):m]

print(solution(2, 4, 2, 1))
