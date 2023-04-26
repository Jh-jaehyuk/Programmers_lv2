from itertools import product


def solution(users, emoticons):
    n, m = len(users), len(emoticons)
    cb = list(product([10, 20, 30, 40], repeat=m))
    max_member = 0
    max_money = 0

    for i in range(len(cb)):
        member = 0
        money = 0
        for user in users:
            user_money = 0
            is_member = False
            for j in range(m):
                if cb[i][j] >= user[0]:
                    user_money += (emoticons[j] * (100 - cb[i][j])) // 100
            if user_money >= user[1]:
                member += 1
                is_member = True
            if not is_member:
                money += user_money

        if member > max_member:
            max_member = member
            max_money = money

        if member == max_member and money > max_money:
            max_money = money

    return [max_member, max_money]


print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [100000]))
