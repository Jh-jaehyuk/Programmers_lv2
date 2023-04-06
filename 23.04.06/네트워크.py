def solution(n, computers):
    answer = 0
    arr = []

    def dfs(i, n, arr):
        for j in range(n):
            if computers[i][j] == 1 and j not in arr:
                arr.append(j)
                dfs(j, n, arr)

    for i in range(n):
        if i not in arr:
            arr.append(i)
            answer += 1
            dfs(i, n, arr)

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
