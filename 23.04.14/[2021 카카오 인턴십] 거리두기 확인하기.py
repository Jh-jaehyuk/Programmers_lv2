def solution(places):
    answer = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def check(place):
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    for move in range(4):
                        if 0 <= i + dx[move] < 5 and 0 <= j + dy[move] < 5 and place[i + dx[move]][j + dy[move]] != 'X':
                            if place[i + dx[move]][j + dy[move]] == 'O':
                                if find(place, i + dx[move], j + dy[move], i, j):
                                    return True
                            else:
                                return True
        return False

    def find(place, nx, ny, x, y):
        for move in range(4):
            if 0 <= nx + dx[move] < 5 and 0 <= ny + dy[move] < 5 and place[nx + dx[move]][ny + dy[move]] == 'P' and [nx + dx[move], ny + dy[move]] != [x, y]:
                return True
        return False

    for place in places:
        if check(place):
            answer.append(0)
        else:
            answer.append(1)

    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
