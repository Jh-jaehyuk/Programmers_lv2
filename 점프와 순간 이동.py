def solution(n):
    # n을 이진 변환 시키면 답이 나온다는 아이디어 필요.
    ans = 0
    n = bin(n)[2:]
    ans = n.count('1')
    return ans

print(solution(15331564))
