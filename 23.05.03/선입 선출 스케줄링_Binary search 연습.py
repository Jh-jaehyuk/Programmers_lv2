def solution(n, cores):
    n -= len(cores)
    if n <= 0:
        return n
    # 이분 탐색 구현을 위해서 양 끝값을 설정
    left, right = 1, max(cores) * n
    # 탐색 진행
    while left < right:
        mid = (left + right) // 2
        # 진행 완료된 일을 0으로 설정
        tmp = 0

        for core in cores:
            # 어떤 시간 mid 만큼 지났을 때 각 core가 처리한 일을 모두 더해줌
            tmp += mid // core
        # 만약에 그 값이 총 처리해야되는 일 n보다 크거나 같다면,
        # 그 값들 중에 가장 작은 값을 찾아야하므로 right를 mid로 변경
        if tmp >= n:
            right = mid
        # 그렇지 않다면 left를 mid + 1로 변경
        else:
            left = mid + 1
    # 총 처리해야되는 일 n에서 (right - 1) 시간만큼 지났을 때
    # 각 코어에서 처리한 일만큼 빼줌
    n -= sum(map(lambda x: (right - 1) // x, cores))
    # 빼고 남은만큼의 일은 core를 하나씩 탐색하면서 확인
    for i in range(len(cores)):
        if right % cores[i] == 0:
            n -= 1
            # 가장 마지막에 들어간 core의 index 반환
            if n == 0:
                return i + 1


print(solution(6, [1,2,3]))
