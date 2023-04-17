def solution(book_time):
    answer = 0
    timetable = [[] for _ in range(len(book_time))]

    for i in range(len(book_time)):
        for j in range(2):
            hour, minute = book_time[i][j].split(':')
            timetable[i].append(int(hour) * 60 + int(minute))
            if j == 1:
                timetable[i][j] += 10
    timetable.sort(key=lambda x: x[0])

    tmp = []
    for time in timetable:
        if not tmp:
            tmp.append(time)
        else:
            tmp.sort(key=lambda x: x[1])
            for i in tmp:
                if time[0] < i[1]:
                    tmp.append(time)
                    break
                else:
                    tmp.remove(i)
                    tmp.append(time)
                    break

        answer = max(answer, len(tmp))

    return answer


print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]))
