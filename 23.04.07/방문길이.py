def solution(dirs):
    x, y = 5, 5
    answer = set()

    for i in dirs:
        if i == 'U':
            nx, ny = x - 1, y
        elif i == 'D':
            nx, ny = x + 1, y
        elif i == 'R':
            nx, ny = x, y + 1
        else:
            nx, ny = x, y - 1
        # 선을 지나간 기록을 점이 아닌 선으로 할 것.
        if 0 <= nx <= 10 and 0 <= ny <= 10:
            answer.add((x, y, nx, ny)) # 실제 이동한 길
            answer.add((nx, ny, x, y)) # 실제 이동한 길과 출발점 도착점이 반대인 경우
            x, y = nx, ny

    return len(answer) // 2


print(solution("LULLLLLLU"))
