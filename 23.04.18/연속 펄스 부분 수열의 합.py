def solution(sequence):
    d1 = [0] * len(sequence)
    d2 = [0] * len(sequence)

    d1[0] = sequence[0] # 펄스 수열의 처음이 1인 경우
    d2[0] = -1 * sequence[0] # 펄스 수열의 처음이 -1인 경우

    for i in range(1, len(sequence)):
        # 펄스 수열은 1, -1이 반복되므로 인덱스가 짝수인 경우, 홀수인 경우를 따로 작성
        if i % 2 == 0:
            # 펄스 수열의 처음이 1이고 인덱스가 양수라면
            d1[i] = max(d1[i - 1] + sequence[i], sequence[i])
            # 펄스 수열의 처음이 -1이고 인덱스가 양수라면
            d2[i] = max(d2[i - 1] - sequence[i], -1 * sequence[i])
        else:
            # 펄스 수열의 처음이 1이고 인덱스가 홀수라면
            d1[i] = max(d1[i - 1] - sequence[i], -1 * sequence[i])
            # 펄스 수열의 처음이 -1이고 인덱스가 홀수라면
            d2[i] = max(d2[i - 1] + sequence[i], sequence[i])
    # 두가지 펄스 수열의 경우에서의 최댓값 비교
    return max(max(d1), max(d2))


print(solution([2, 3, -6, 1, 3, -1, 2, 4]))
