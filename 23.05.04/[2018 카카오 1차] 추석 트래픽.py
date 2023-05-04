def time_to_ms(time):
    t = list(map(float, time.split(':')))
    hour, minute, second = t[0], t[1], t[2]
    ms = (hour * 3600 + minute * 60 + second) * 1000
    return int(ms)


def solution(lines):
    answer = 0
    log_arr = []

    for line in lines:
        time, log_s = line.split(' ')[1], int(float(line.split(' ')[2][:-1]) * 1000) - 1
        ms = time_to_ms(time)
        start_time, end_time = ms - log_s, ms
        log_arr.append([start_time, end_time])

    log_arr.sort(key=lambda x: x[1])

    def check(end, logs):
        nonlocal answer
        tmp = 1
        for start in logs:
            if end + 999 < start[0]:
                continue
            tmp += 1
        if tmp > answer:
            answer = tmp

    for i in range(len(log_arr)):
        log = log_arr[i]
        check(log[1], log_arr[(i + 1):])

    return answer


print(solution([
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]))

print(solution([
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]))

print(solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))
