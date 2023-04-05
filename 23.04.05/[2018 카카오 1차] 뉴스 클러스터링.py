def solution(str1, str2):
    str1 = list(str1.lower())
    str2 = list(str2.lower())

    list1 = [str1[i] + str1[i + 1] for i in range(len(str1) - 1)]
    list1 = [i for i in list1 if i.isalpha()]
    list2 = [str2[i] + str2[i + 1] for i in range(len(str2) - 1)]
    list2 = [i for i in list2 if i.isalpha()]
    if not list1 and not list2:
        return 65536

    a = list1.copy()
    union = list1.copy()

    for i in list2:
        if i not in a:
            union.append(i)
        else:
            a.remove(i)

    common = []
    for i in list2:
        if i in list1:
            list1.remove(i)
            common.append(i)

    return int(len(common) / len(union) * 65536)

print(solution('abab', 'baba'))
