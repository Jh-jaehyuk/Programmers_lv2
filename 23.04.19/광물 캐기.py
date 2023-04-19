from collections import Counter


def solution(picks, minerals):
    arr = []
    result = 0

    for i in range(0, len(minerals), 5):
        if i >= sum(picks) * 5:
            break
        arr.append(minerals[i:(i + 5)])

    arr.sort(key=lambda x: (Counter(x)["diamond"] * 25 + Counter(x)["iron"] * 5 + Counter(x)["stone"]), reverse=True)

    for i in arr:
        if picks == [0, 0, 0]:
            break
        c = Counter(i)
        if picks[0]:
            picks[0] -= 1
            result += c["diamond"] + c["iron"] + c["stone"]

        else:
            if picks[1]:
                picks[1] -= 1
                result += c["diamond"] * 5 + c["iron"] + c["stone"]

            else:
                picks[2] -= 1
                result += c["diamond"] * 25 + c["iron"] * 5 + c["stone"]

    return result


print(solution([1, 1, 0], ["iron", "iron", "diamond", "iron", "stone", "diamond", "diamond", "diamond"]))
