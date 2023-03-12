def solution(n):
    l = [0, 1]
    for i in range(2, n+1):
        l.append(l[i-2] + l[i-1])
    answer = l[-1] % 1234567
    return answer

print(solution(5))
