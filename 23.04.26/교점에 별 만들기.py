def solution(line):
    answer = []
    INF = int(1e16)
    min_x, max_x, min_y, max_y = INF, -INF, INF, -INF
    for i in line:
        a, b, e = i
        for j in line:
            if j != i:
                c, d, f = j
                if ((a * d) - (b * c)) != 0:
                    x = ((b * f) - (e * d)) / ((a * d) - (b * c))
                    y = ((e * c) - (a * f)) / ((a * d) - (b * c))
                    if int(x) == x and int(y) == y:
                        x, y = int(x), int(y)
                        min_x, max_x, min_y, max_y = min(min_x, x), max(max_x, x), min(min_y, y), max(max_y, y)
                        answer.append((x, y))
    arr = [['.'] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]

    for x, y in answer:
        arr[max_y - y][x - min_x] = '*'

    return [''.join(s) for s in arr]


print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
