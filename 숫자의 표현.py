def solution(n):
    s = 0
    e = 1
    l = [i for i in range(1, n+1)]
    answer = 0

    if n == 1:
        return 1
    else:
        while e <= n:
            if sum(l[s:e]) < n:
                e += 1
            elif sum(l[s:e]) > n:
                s += 1
            else:
                s += 1
                answer += 1
    return answer

# 투 포인터 알고리즘을 이용함.
print(solution(15))
