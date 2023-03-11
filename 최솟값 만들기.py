def solution(A,B):
    A = list(sorted(A))
    B = list(sorted(B, reverse=True))
    answer = [A[i] * B[i] for i in range(len(A))]
    return sum(answer)

print(solution([1,4,2], [5,4,4]))
