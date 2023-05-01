def solution(cap, n, deliveries, pickups):
    answer = 0
    # 배달, 회수 값을 기본 0으로 설정
    d, p = 0, 0
    # 배달, 회수목록을 맨 뒤에서부터 지나오면
    for i in range(n - 1, -1, -1):
        count = 0
        # 배달, 회수 해야되는 값을 0에서 빼줌
        d -= deliveries[i]
        p -= pickups[i]
        # 둘 중 하나라도 음수인 경우,
        while d < 0 or p < 0:
            # 둘 다 양수가 될 때까지 cap을 더해줌
            # cap을 더해준다는 것은 그만큼 왕복으로 이동했다는 뜻.
            d += cap
            p += cap
            # 왕복한만큼 카운트 증가
            count += 1
        # 이동거리는 항상 (i + 1) * 2 인데
        # 왕복한 경우에는 count만큼 곱해주어야 함.
        # 단, 둘 다 0인 경우. 따라서 d, p가 둘 다 0 이상인 경우엔
        # 방문 할 필요가 없으므로 count 가 0 이 되어서 answer에 변화 없음.
        answer += (i + 1) * 2 * count

    return answer


print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
