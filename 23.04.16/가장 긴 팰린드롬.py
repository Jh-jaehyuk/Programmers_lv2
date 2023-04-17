def solution(s):
    answer = 0

    def check(x):
        if x == x[::-1]:
            return True
        return False

    for i in range(len(s)):
        for j in range(len(s) + 1, i + 1, -1):
            x = s[i:j]
            if check(x):
                answer = max(answer, len(x))

    return answer


print(solution('abcdcba'))
