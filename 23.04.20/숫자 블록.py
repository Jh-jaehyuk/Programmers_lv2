def get_divisor(n):
    divisor = []

    if n == 1:
        return 0
    else:
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                if n // i == i and i <= int(1e7):
                    divisor.append(i)
                else:
                    if i <= int(1e7):
                        divisor.append(i)
                    if n // i <= int(1e7):
                        divisor.append(n // i)
    divisor.sort()
    if len(divisor) > 1 and divisor[-1] == n:
        divisor.pop()
    return divisor[-1]


def solution(begin, end):
    answer = []

    for i in range(begin, end + 1):
        answer.append(get_divisor(i))

    return answer


print(solution(1, 10))
