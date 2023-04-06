def solution(record):
    answer = []
    d = dict()
    arr = []

    for i in record:
        arr.append(list(i.split()))

    for i in arr:
        if i[0] == 'Enter' or i[0] == 'Change':
            d[i[1]] = i[2]

    for i in arr:
        if i[0] == 'Enter':
            answer.append(f'{d[i[1]]}님이 들어왔습니다.')

        elif i[0] == 'Leave':
            answer.append(f'{d[i[1]]}님이 나갔습니다.')

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
