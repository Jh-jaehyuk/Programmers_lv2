def solution(phone_book):
    answer = True
    hash = {}

    for i in phone_book:
        hash[i] = 1

    for i in phone_book:
        tmp = ''
        for j in i:
            tmp += j
            if tmp in hash and tmp != i:
                answer = False

    return answer

print(solution(["12","123","1235","567","88"]))
