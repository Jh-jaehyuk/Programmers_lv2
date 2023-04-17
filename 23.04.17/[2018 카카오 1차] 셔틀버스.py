def solution(n, t, m, timetable):
    answer = 0
    timetable.sort()
    crew = []

    for time in timetable:
        hour, minute = time.split(':')
        crew.append(int(hour) * 60 + int(minute))
    crew.sort()

    bus = [(540 + (t * i)) for i in range(n)]

    idx = 0

    for b in bus:
        count = 0

        while count < m and idx < len(crew) and crew[idx] <= b:
            idx += 1
            count += 1

        if count < m:
            answer = b
        else:
            answer = crew[idx - 1] - 1

    return str('%02d'%(answer // 60)) + ':' + str('%02d'%(answer % 60))


print(solution(2, 10, 3, ['09:05', '09:09', '09:13']))
