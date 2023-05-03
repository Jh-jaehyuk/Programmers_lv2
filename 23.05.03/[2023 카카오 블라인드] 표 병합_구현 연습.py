def solution(commands):
    answer = []
    merge_arr = [[(i, j) for j in range(51)] for i in range(51)]
    arr = [['EMPTY'] * 51 for _ in range(51)]

    for command in commands:
        c = command.split(' ')
        if c[0] == 'UPDATE':
            if len(c) == 4:
                r, c, value = int(c[1]), int(c[2]), c[3]
                x, y = merge_arr[r][c]
                arr[x][y] = value
            else:
                for i in range(51):
                    for j in range(51):
                        if arr[i][j] == c[1]:
                            arr[i][j] = c[2]

        elif c[0] == 'MERGE':
            r1, c1, r2, c2 = int(c[1]), int(c[2]), int(c[3]), int(c[4])
            x1, y1 = merge_arr[r1][c1]
            x2, y2 = merge_arr[r2][c2]

            if arr[x1][y1] == 'EMPTY':
                arr[x1][y1] = arr[x2][y2]

            for i in range(51):
                for j in range(51):
                    if merge_arr[i][j] == (x2, y2):
                        merge_arr[i][j] = (x1, y1)

        elif c[0] == 'UNMERGE':
            r, c = int(c[1]), int(c[2])
            x, y = merge_arr[r][c]
            tmp = arr[x][y]
            for i in range(51):
                for j in range(51):
                    if merge_arr[i][j] == (x, y):
                        merge_arr[i][j] = (i, j)
                        arr[i][j] = 'EMPTY'
            arr[r][c] = tmp

        elif c[0] == 'PRINT':
            r, c = int(c[1]), int(c[2])
            x, y = merge_arr[r][c]
            answer.append(arr[x][y])

    return answer


print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
