def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)

def lcm(a, b):
    return (a * b // gcd(a, b))

def solution(arr):
    l = [lcm(arr[0], arr[1])]
    if len(arr) == 1:
        return arr[0]

    for i in range(len(arr)-1):
        n = lcm(l[0], arr[i+1])
        if n >= l[0]:
            l[0] = n

    return l[0]

print(solution([1,2,3]))
