def solution(sticker):
    if len(sticker) < 4:
        return max(sticker)
    # 첫번째 스티커를 뗀 경우
    d0 = [0] * len(sticker)
    # 첫번째 스티커를 떼지 않은 경우
    d1 = [0] * len(sticker)

    d0[0] = sticker[0]
    d0[1] = sticker[0]

    d1[0] = 0
    d1[1] = sticker[1]

    # 첫번째 스티커를 떼면 마지막 스티커를 쓰지 못함
    for i in range(2, len(sticker) - 1):
        d0[i] = max(d0[i - 1], d0[i - 2] + sticker[i])

    val0 = max(d0)

    # 첫번째 스티커를 떼지않으면 마지막 스티커까지 쓸 수 있음
    for j in range(2, len(sticker)):
        d1[j] = max(d1[j - 1], d1[j - 2] + sticker[j])

    val1 = max(d1)
    # 두가지 경우 중에 최댓값을 반환
    return max(val0, val1)


print(solution([1, 3, 2, 5, 4]))
