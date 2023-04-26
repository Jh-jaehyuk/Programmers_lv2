def solution(n, weak, dist):
    repair_list = [()]
    dist.reverse()
    count = 0

    for friend in dist:
        repairs = []
        count += 1

        for idx, weak_point in enumerate(weak):
            start = weak_point
            ends = weak[idx:] + [n + w for w in weak[:idx]]
            can = [end % n for end in ends if end - start <= friend]
            repairs.append(set(can))

        cand = set()

        for r in repairs:
            for x in repair_list:
                new = r | set(x)
                if len(new) == len(weak):
                    return count
                cand.add(tuple(new))
        repair_list = cand

    return -1


print(solution(12, [1,5,6,10], [1,2,3,4]))
