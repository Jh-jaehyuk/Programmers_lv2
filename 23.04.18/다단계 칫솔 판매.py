import math


def solution(enroll, referral, seller, amount):
    answer = []
    member_d = {enroll[i]: referral[i] for i in range(len(enroll))}
    d = {i: 0 for i in enroll}

    for i in range(len(seller)):
        d[seller[i]] += amount[i] * 100
        money = math.floor(amount[i] * 10)
        give_member = seller[i]
        take_member = member_d[give_member]

        while take_member != "-":
            d[take_member] += money
            d[give_member] -= money

            money *= 0.1
            money = math.floor(money)

            if money == 0:
                break

            give_member = take_member
            take_member = member_d[give_member]

        if take_member == '-':
            d[give_member] -= money

    for i in enroll:
        answer.append(d[i])

    return answer


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"],
               [12, 4, 2, 5, 10]))
