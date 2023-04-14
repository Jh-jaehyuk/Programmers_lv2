def solution(board):
    d = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    max_val = 0

    for i in range(1, len(board) + 1):
        for j in range(1, len(board[0]) + 1):
            if board[i - 1][j - 1] == 1:
                d[i][j] = min(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1]) + 1
                max_val = max(max_val, d[i][j])

    return max_val * max_val


print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
