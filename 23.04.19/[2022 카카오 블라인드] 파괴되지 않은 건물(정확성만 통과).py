def solution(board, skill):
    answer = 0

    def destroy(x1, y1, x2, y2, degree):
        nonlocal board
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                board[i][j] -= degree

    def repair(x1, y1, x2, y2, degree):
        nonlocal board
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                board[i][j] += degree

    for i in skill:
        ty, x1, y1, x2, y2, degree = i

        if ty == 1:
            destroy(x1, y1, x2, y2, degree)
        else:
            repair(x1, y1, x2, y2, degree)

    for n in range(len(board)):
        for m in range(len(board[0])):
            if board[n][m] >= 1:
                answer += 1

    return answer


print(solution([[1,2,3],[4,5,6],[7,8,9]],
               [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))
