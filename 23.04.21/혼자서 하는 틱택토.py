def check(player, board):
    # 행 체크
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
    # 열 체크
    for j in range(3):
        if all(board[i][j] == player for i in range(3)):
            return True
    # 대각선 체크
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def solution(board):
    count_o, count_x = sum(row.count('O') for row in board), sum(row.count('X') for row in board)
    # o, x의 개수가 같거나 o, x의 개수 차이가 1개보다 큰 경우
    if count_x - count_o > 0 or abs(count_x - count_o) > 1:
        return 0 # 불가능
    # o가 빙고 상태이고 x의 개수가 o의 개수와 1개 차이가 아닌 경우(앞의 조건)
    # x가 빙고 상태이고 x의 개수가 o의 개수와 다른 경우(뒤의 조건)
    elif (check('O', board) and count_x != count_o - 1) or (check('X', board) and count_x != count_o):
        return 0 # 불가능
    # 나머지는 전부 가능
    return 1
