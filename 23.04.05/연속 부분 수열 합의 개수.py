def solution(elements):
    elements *= 2
    s = set()

    for i in range(len(elements) // 2):
        for j in range(len(elements) // 2):
            s.add(sum(elements[i:i + j]))

    return len(s)
