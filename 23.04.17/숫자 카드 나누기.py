def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def solution(arrayA, arrayB):
    if len(arrayA) == 1:
        a, b = arrayA[0], arrayB[0]
        if a < b:
            a, b = b, a
        if a % b == 0:
            return 0
        else:
            return a

    gcd_a = gcd(arrayA[0], arrayA[1])
    for i in range(2, len(arrayA)):
        gcd_a = gcd(gcd_a, arrayA[i])

    gcd_b = gcd(arrayB[0], arrayB[1])
    for j in range(2, len(arrayB)):
        gcd_b = gcd(gcd_b, arrayB[j])

    def check(x, arr):
        for i in arr:
            if i % x == 0:
                return False
        return True

    check_A = check(gcd_b, arrayA)
    check_B = check(gcd_a, arrayB)

    if check_A and not check_B:
        return gcd_b

    if not check_A and check_B:
        return gcd_a

    if check_A and check_B:
        return max(gcd_a, gcd_b)

    if not check_A and not check_B:
        return 0


print(solution([28], [14]))
