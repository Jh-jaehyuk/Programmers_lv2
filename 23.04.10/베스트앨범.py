def solution(genres, plays):
    answer = []
    idx_list = [i for i in range(len(genres))]
    arr = list(zip(genres, plays, idx_list))
    d = dict()

    for i in range(len(genres)):
        if genres[i] not in d:
            d[genres[i]] = plays[i]
        else:
            d[genres[i]] += plays[i]

    l = sorted(list(d.items()), key=lambda x: x[1])

    while l:
        v = l.pop()
        tmp = []
        for j in arr:
            if v[0] == j[0]:
                tmp.append(j)
        tmp.sort(key=lambda x: (x[1], -x[2]))
        count = 0
        while tmp:
            if count == 2:
                break
            answer.append(tmp.pop()[2])
            count += 1

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
