def solution(arr):
    answer = [0, 0]
    n = len(arr)

    def quad(x, y, n):
        a = arr[x][y]

        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != a:
                    n //= 2
                    quad(x, y, n)
                    quad(x, y + n, n)
                    quad(x + n, y, n)
                    quad(x + n, y + n, n)
                    return
        answer[a] += 1

    quad(0, 0, n)

    return answer


print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
