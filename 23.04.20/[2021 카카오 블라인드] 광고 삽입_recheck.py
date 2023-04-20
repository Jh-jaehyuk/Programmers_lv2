import re


def solution(play_time, adv_time, logs):
    def time_to_second(time):
        if len(time) == 8:
            s = re.findall(r"[0-9]+", time)
            s = int(s[0]) * 3600 + int(s[1]) * 60 + int(s[2])
            return s
        s, e = re.split(r"-", time)
        s = re.findall(r"[0-9]+", s)
        e = re.findall(r"[0-9]+", e)
        s = int(s[0]) * 3600 + int(s[1]) * 60 + int(s[2])
        e = int(e[0]) * 3600 + int(e[1]) * 60 + int(e[2])
        return s, e

    def time_str(time):
        h, time = divmod(time, 3600)
        m, s = divmod(time, 60)
        return f'{h:02d}:{m:02d}:{s:02d}'

    end_time = time_to_second(play_time)
    length = time_to_second(adv_time)
    d = [0] * (end_time + 1)

    for log in logs:
        s, e = time_to_second(log)
        d[s] += 1
        d[e] -= 1

    for i in range(1, end_time + 1):
        d[i] += d[i - 1]

    now = 0
    s, e = 0, -1
    result = [0, 0]

    while s <= end_time and e <= end_time:
        while e + 1 <= end_time and e + 1 - s < length:
            e += 1

            now += d[e]

            if now > result[1]:
                result[0] = s
                result[1] = now

        now -= d[s]
        s += 1

    return time_str(result[0])


print(solution("99:59:59", "25:00:00",
               ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
