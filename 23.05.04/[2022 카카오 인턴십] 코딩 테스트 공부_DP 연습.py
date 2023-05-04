def solution(alp, cop, problems):
    max_alp, max_cop = 0, 0 # 목표 alp, cop 설정

    for problem in problems:
        # 문제들 중 최댓값으로 설정
        max_alp = max(max_alp, problem[0])
        max_cop = max(max_cop, problem[1])
    # DP 테이블 설정
    # dp[alp][cop] = alp, cop를 달성하는데 필요한 최소 시간의 형태
    d = [[int(1e9)] * (max_cop + 1) for _ in range(max_alp + 1)]
    # alp, cop 가 최댓값을 넘지 않게 재설정
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    # 시작 alp, cop 달성하는데 필요한 시간은 0
    d[alp][cop] = 0
    # DP 실행
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            if i + 1 <= max_alp:
                d[i + 1][j] = min(d[i + 1][j], d[i][j] + 1)
            if j + 1 <= max_cop:
                d[i][j + 1] = min(d[i][j + 1], d[i][j] + 1)

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    new_alp = min(i + alp_rwd, max_alp)
                    new_cop = min(j + cop_rwd, max_cop)
                    d[new_alp][new_cop] = min(d[new_alp][new_cop], d[i][j] + cost)

    return d[max_alp][max_cop]


# print(solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]]))
print(solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]))
