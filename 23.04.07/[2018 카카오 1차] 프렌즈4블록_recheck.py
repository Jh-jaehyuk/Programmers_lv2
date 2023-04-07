def solution(m, n, board):
    answer = 0
    board = list(map(list, zip(*board)))
    m, n = n, m

    while True:
        p = [i[:] for i in board]
        tmp = answer

        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] != 'X' and board[i][j] == board[i + 1][j] \
                        == board[i][j + 1] == board[i + 1][j + 1]:
                    p[i][j] = 1
                    p[i + 1][j] = 1
                    p[i][j + 1] = 1
                    p[i + 1][j + 1] = 1

        for idx, k in enumerate(p):
            count1 = k.count(1)
            answer += count1
            board[idx] = ['X'] * count1 + [i for i in k if i != 1]

        if tmp == answer:
            break

    return answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
