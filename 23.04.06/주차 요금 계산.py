import math

def solution(fees, records):
    arr = []
    answer = []
    max_t = 60 * 23 + 59

    for i in records:
        arr.append(list(i.split()))

    for i in arr:
        h, m = i[0].split(':')
        h, m = int(h), int(m)
        i[0] = h * 60 + m

    d = dict()
    arr.sort(key=lambda x:x[1])

    for i in arr:
        d[i[1]] = 0

    for i in arr:
        if i[2] == 'IN':
            if i[1] not in d:
                d[i[1]] = -1 * i[0]

            else:
                d[i[1]] -= i[0]

        else:
            d[i[1]] += i[0]

    for i in d:
        if d[i] <= 0:
            d[i] += max_t

        if d[i] <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + (math.ceil((d[i] - fees[0]) / fees[2])) * fees[3])

    return answer


print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
