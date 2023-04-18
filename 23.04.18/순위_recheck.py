# 플로이드 워셜 알고리즘을 사용할 수 있다는 것을 생각할 것.
# 방법만 알아내면 구현은 어렵지 않음.

def solution(n, results):
    check = [[0] * (n + 1) for _ in range(n + 1)]

    for i, j, in results:
        check[i][j] = 1
        check[j][i] = -1

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                if check[j][i] == 0:
                    continue

                if check[j][i] == check[i][k]:
                    check[j][k] = check[j][i]
                    check[k][j] = -1 * check[j][i]

    answer = 0

    for i in range(1, n + 1):
        if 0 in check[i][1:i] + check[i][(i + 1):]:
            continue
        answer += 1

    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
