def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)


def solution(n, k):
    # 일렬로 줄을 세우는 경우의 수는 n!
    # 맨 처음 세워지는 수는 k // (n - 1) + 1
    # 앞에 수를 세우고 다시 줄 세우는 경우를 반복
    # n -= 1, k %= (n - 1)!
    answer = []
    arr = [i for i in range(1, n + 1)]

    while n != 0:
        num = factorial(n - 1)
        idx = int(k // num) # int() 안해주니까 효율성 4번에서 오류
        k %= num

        if k == 0:
            answer.append(arr.pop(idx - 1))
        else:
            answer.append(arr.pop(idx))

        n -= 1

    return answer


print(solution(20, 400))
