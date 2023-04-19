# 1차원 누적합의 개념을 확장하여 2차원으로 누적합을 구현함.
# 정확성만 통과한 코드는 O(M * N * K)의 시간복잡도를 갖지만
# 누적합을 이용하면 O(K + MN)의 시간복잡도를 가지게 됨.
def solution(board, skill):
    answer = 0

    arr = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]

    for i in skill:
        ty, x1, y1, x2, y2, degree = i

        if ty == 1:
            arr[x1][y1] -= degree
            arr[x1][y2 + 1] += degree
            arr[x2 + 1][y1] += degree
            arr[x2 + 1][y2 + 1] -= degree
        else:
            arr[x1][y1] += degree
            arr[x1][y2 + 1] -= degree
            arr[x2 + 1][y1] -= degree
            arr[x2 + 1][y2 + 1] += degree

    for i in range(len(arr) - 1):
        for j in range(len(arr[0]) - 1):
            arr[i][j + 1] += arr[i][j]

    for j in range(len(arr[0]) - 1):
        for i in range(len(arr) - 1):
            arr[i + 1][j] += arr[i][j]

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += arr[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer
