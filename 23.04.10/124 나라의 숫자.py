def solution(n):
    answer = ''

    while True:
        if n <= 0:
            break

        x = ['1', '2', '4'][(n % 3) - 1]

        if n % 3 == 0:
            n //= 3
            n -= 1

        else:
            n //= 3

        answer += x

    return answer[::-1]


print(solution(4))
