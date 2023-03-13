def solution(n):
    # answer = 1
    # l = [1] * n
    # i = 1
    #
    # while l.count(1) > 1:
    #     print(answer)
    #     del l[0:2]
    #     if len(l) == 0:
    #         answer += 1
    #     else:
    #         answer += n - i
    #     i += 1
    # answer %= 1234567
    # return answer
    l = [1, 2] # 피보나치 수열 이용
    for i in range(1, 2000):
        l.append(l[i] + l[i-1])

    return l[n-1] % 1234567

print(solution(4))

