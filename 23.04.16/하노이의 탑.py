def solution(n):
    answer = []

    def hanoi(n, f, t, s):
        if n == 1:
            answer.append([f, t])
            return
        hanoi(n - 1, f, s, t)
        answer.append([f, t])
        hanoi(n - 1, s, t, f)

    hanoi(n, 1, 3, 2)

    return answer


print(solution(2))
