from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    # 배열을 2배 늘려줌
    board = [[-1] * 102 for _ in range(102)]
    visited = [[-1] * 102 for _ in range(102)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    # 사각형의 테두리만 표현하는 것을 구현하는 것이 핵심!
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, r)
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                # 사각형의 내부일 때
                if x1 < x < x2 and y1 < y < y2:
                    board[y][x] = 0
                # 사각형의 테두리이고 내부가 아닐 때
                elif board[y][x] != 0:
                    board[y][x] = 1

    queue = deque()
    queue.append([characterY * 2, characterX * 2])
    visited[characterY * 2][characterX * 2] = 0

    while queue:
        y, x = queue.popleft()

        if [y, x] == [itemY * 2, itemX * 2]:
            answer = visited[y][x] // 2
            break

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny > 102 or nx < 0 or nx > 102 or board[ny][nx] != 1:
                continue
            if visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                queue.append([ny, nx])

    return answer


print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))
print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1))
