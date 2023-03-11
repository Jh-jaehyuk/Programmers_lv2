def solution(s):
    zero_count = 0
    binary_count = 0

    while s != '1':
        zero_count += s.count('0')
        s = s.replace('0', '')
        s = bin(len(s))[2:]
        binary_count += 1

    return [binary_count, zero_count]

print(solution('110010101001'))
