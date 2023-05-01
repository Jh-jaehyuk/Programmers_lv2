def solution(N, number):
    d = [set() for _ in range(9)]
    # 숫자를 각각 1 ~ 8회 사용했을 때 만들 수 있는 숫자 목록
    for i in range(1, 9):
        # 일단 숫자를 1 ~ 8회 이어붙인 숫자를 목록에 추가
        d[i].add(int(str(N) * i))
        # 사용 횟수의 절반을 기준으로 앞, 뒤 나누어서 탐색할것이므로
        # 범위는 사용 횟수(i)의 절반까지
        # ex) 사용 횟수(i) = 4 라면, 범위는 2까지 탐색.
        for j in range(i // 2 + 1):
            # 앞 부분에서 만들 수 있는 숫자 목록(x)
            for x in d[j]:
                # 뒷 부분에서 만들 수 있는 숫자 목록(y)
                for y in d[i - j]:
                    # 두 부분에서 만들 수 있는 숫자들을 전부 추가
                    d[i].add(x + y)
                    d[i].add(x - y)
                    d[i].add(y - x)
                    d[i].add(x * y)
                    # 0으로 나누는 경우는 불가능하므로 제외
                    if y != 0:
                        d[i].add(x // y)
                    if x != 0:
                        d[i].add(y // x)
        # 만약에 찾는 number가 목록에 들어있다면,
        # 사용 횟수(i)를 return
        if number in d[i]:
            return i
    # 8회까지 탐색해도 없다면 -1를 return
    return -1


print(solution(2, 11))
